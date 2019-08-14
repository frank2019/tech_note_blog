



## c++/c 调试宏



```c++
#ifdef WIN32
#define TrimFilePath(x) strrchr(x,'\\')?strrchr(x,'\\')+1:x
#else //*nix
#define TrimFilePath(x) strrchr(x,'/')?strrchr(x,'/')+1:x
#endif

#define D(fmt, ...)   \
	printf("[DEBUG] [%s(%d)]\t: " fmt"\n",TrimFilePath(__FILE__),__LINE__,##__VA_ARGS__)

#define LOG_DEBUG(fmt, ...)		write_log(S_DEBUG, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
```



### ANSI C标准中几个预定义宏

```c++
__DATE__：编译日期
__TIME__：编译时间；
__FILE__：当前源文件路径及文件名；
__LINE__：当前源代码行号；
__FUNCTION__
__STDC__：当要求程序严格遵循ANSI C标准时该标识被赋值为1；
__cplusplus：当编写C++程序时该标识符被定义。

```



## 简单宏函数



```c++
#define  tests(t)    (printf("[DEBUG] [%s-%s]",(__FILE__),__FUNCTION__),t )
```

