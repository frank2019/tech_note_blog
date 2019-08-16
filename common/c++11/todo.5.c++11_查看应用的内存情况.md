## 进程的内存 Vss Rss Pss Uss

adb shell procrank | grep com.package > appmem
[![screenshot](http://img2.tbcdn.cn/L1/461/1/8fea3ee054b6398a1c1b588b4b4fe3084415ed83)](http://img2.tbcdn.cn/L1/461/1/8fea3ee054b6398a1c1b588b4b4fe3084415ed83)
说明：五个参数分别为PID Vss Rss Pss Uss

VSS - Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）
RSS - Resident Set Size 实际使用物理内存（包含共享库占用的内存）
PSS - Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存）
USS - Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）

一般来说内存占用大小有如下规律：VSS >= RSS >= PSS >= USS

1. VSS - Virtual Set Size （用处不大）
    虚拟耗用内存（包含共享库占用的全部内存，以及分配但未使用内存）。其大小还包括了可能不在RAM中的内存（比如虽然malloc分配了空间，但尚未写入）。VSS 很少被用于判断一个进程的真实内存使用量。

   

   ![img](https:////upload-images.jianshu.io/upload_images/2828107-946368da958a6504.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/360)

   

2. RSS - Resident Set Size （用处不大）
    实际使用物理内存（包含共享库占用的全部内存）。但是RSS还是可能会造成误导，因为它仅仅表示该进程所使用的所有共享库的大小，它不管有多少个进程使用该共享库，该共享库仅被加载到内存一次。所以RSS并不能准确反映单进程的内存占用情况

   

   ![img](https:////upload-images.jianshu.io/upload_images/2828107-219e9bf1b34efbdb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/397)

   

3. PSS - Proportional Set Size （仅供参考）
    实际使用的物理内存（比例分配共享库占用的内存，按照进程数等比例划分）。例如：如果有三个进程都使用了一个共享库，共占用了30页内存。那么PSS将认为每个进程分别占用该共享库10页的大小。 PSS是非常有用的数据，因为系统中所有进程的PSS都相加的话，就刚好反映了系统中的   总共占用的内存。 而当一个进程被销毁之后， 其占用的共享库那部分比例的PSS，将会再次按比例分配给余下使用该库的进程。这样PSS可能会造成一点的误导，因为当一个进程被销毁后， PSS不能准确地表示返回给全局系统的内存。

   

   ![img](https:////upload-images.jianshu.io/upload_images/2828107-bf9353a80d3829b4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/384)

   

4. USS - Unique Set Size （非常有用）
    进程独自占用的物理内存（不包含共享库占用的内存）。USS是非常非常有用的数据，因为它反映了运行一个特定进程真实的边际成本（增量成本）。当一个进程被销毁后，USS是真实返回给系统的内存。当进程中存在一个可疑的内存泄露时，USS是最佳观察数据。

   

## 查看应用本身内存使用情况的接口



```c++
/*
* Author:  David Robert Nadeau
* Site:    http://NadeauSoftware.com/
* License: Creative Commons Attribution 3.0 Unported License
*          http://creativecommons.org/licenses/by/3.0/deed.en_US
*/

#if defined(_WIN32)
#include <windows.h>
#include <psapi.h>

#elif defined(__unix__) || defined(__unix) || defined(unix) || (defined(__APPLE__) && defined(__MACH__))
#include <unistd.h>
#include <sys/resource.h>

#if defined(__APPLE__) && defined(__MACH__)
#include <mach/mach.h>

#elif (defined(_AIX) || defined(__TOS__AIX__)) || (defined(__sun__) || defined(__sun) || defined(sun) && (defined(__SVR4) || defined(__svr4__)))
#include <fcntl.h>
#include <procfs.h>

#elif defined(__linux__) || defined(__linux) || defined(linux) || defined(__gnu_linux__)
#include <stdio.h>

#endif

#else
#error "Cannot define getPeakRSS( ) or getCurrentRSS( ) for an unknown OS."
#endif





/**
* Returns the peak (maximum so far) resident set size (physical
* memory use) measured in bytes, or zero if the value cannot be
* determined on this OS.
*/
size_t getPeakRSS()
{
#if defined(_WIN32)
	/* Windows -------------------------------------------------- */
	PROCESS_MEMORY_COUNTERS info;
	GetProcessMemoryInfo(GetCurrentProcess(), &info, sizeof(info));
	return (size_t)info.PeakWorkingSetSize;

#elif (defined(_AIX) || defined(__TOS__AIX__)) || (defined(__sun__) || defined(__sun) || defined(sun) && (defined(__SVR4) || defined(__svr4__)))
	/* AIX and Solaris ------------------------------------------ */
	struct psinfo psinfo;
	int fd = -1;
	if ((fd = open("/proc/self/psinfo", O_RDONLY)) == -1)
		return (size_t)0L;      /* Can't open? */
	if (read(fd, &psinfo, sizeof(psinfo)) != sizeof(psinfo))
	{
		close(fd);
		return (size_t)0L;      /* Can't read? */
	}
	close(fd);
	return (size_t)(psinfo.pr_rssize * 1024L);

#elif defined(__unix__) || defined(__unix) || defined(unix) || (defined(__APPLE__) && defined(__MACH__))
	/* BSD, Linux, and OSX -------------------------------------- */
	struct rusage rusage;
	getrusage(RUSAGE_SELF, &rusage);
#if defined(__APPLE__) && defined(__MACH__)
	return (size_t)rusage.ru_maxrss;
#else
	return (size_t)(rusage.ru_maxrss * 1024L);
#endif

#else
	/* Unknown OS ----------------------------------------------- */
	return (size_t)0L;          /* Unsupported. */
#endif
}





/**
* Returns the current resident set size (physical memory use) measured
* in bytes, or zero if the value cannot be determined on this OS.
*/
size_t getCurrentRSS()
{
#if defined(_WIN32)
	/* Windows -------------------------------------------------- */
	PROCESS_MEMORY_COUNTERS info;
	GetProcessMemoryInfo(GetCurrentProcess(), &info, sizeof(info));
	return (size_t)info.WorkingSetSize;

#elif defined(__APPLE__) && defined(__MACH__)
	/* OSX ------------------------------------------------------ */
	struct mach_task_basic_info info;
	mach_msg_type_number_t infoCount = MACH_TASK_BASIC_INFO_COUNT;
	if (task_info(mach_task_self(), MACH_TASK_BASIC_INFO,
		(task_info_t)&info, &infoCount) != KERN_SUCCESS)
		return (size_t)0L;      /* Can't access? */
	return (size_t)info.resident_size;

#elif defined(__linux__) || defined(__linux) || defined(linux) || defined(__gnu_linux__)
	/* Linux ---------------------------------------------------- */
	long rss = 0L;
	FILE* fp = NULL;
	if ((fp = fopen("/proc/self/statm", "r")) == NULL)
		return (size_t)0L;      /* Can't open? */
	if (fscanf(fp, "%*s%ld", &rss) != 1)
	{
		fclose(fp);
		return (size_t)0L;      /* Can't read? */
	}
	fclose(fp);
	return (size_t)rss * (size_t)sysconf(_SC_PAGESIZE);

#else
	/* AIX, BSD, Solaris, and Unknown OS ------------------------ */
	return (size_t)0L;          /* Unsupported. */
#endif
}
```





## windows下的工具ProcessExplorer

下载：https://gsf-fl.softonic.com/2ce/c65/e536dec8cf60b2a83fd4d87c159c616bde/ProcessExplorer.zip?Expires=1565961910&Signature=8279ca98224c36d9dfd899e42bb1368d85da54bc&SD_used=&channel=WEB&fdh=no&id_file=be263f4e-96d2-11e6-b288-00163ec9f5fa&instance=softonic_en&type=PROGRAM&url=https://process-explorer.en.softonic.com&Filename=ProcessExplorer.zip