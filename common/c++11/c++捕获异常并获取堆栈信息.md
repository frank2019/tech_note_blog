



# c++捕获异常并获取堆栈信息



```c++
#if defined(WIN32)
#include <io.h>
#include <direct.h>
#include <Windows.h>
#include <DbgHelp.h>
#pragma comment(lib, "Dbghelp.lib") 
#elif defined(linux)
#include <unistd.h>
#include <pthread.h>
#include <sys/stat.h>
#include <execinfo.h>
#endif


static HANDLE _get_curr_proc_handle()
{
#if defined(WIN32)
    HANDLE curr_proc = GetCurrentProcess();
    if (NULL == curr_proc) {
        return NULL;
    }
    if (SymInitialize(curr_proc, NULL, TRUE) != TRUE) {
        return NULL;
    }
#elif defined(linux)
    curr_proc = NULL;
#endif
    return curr_proc;
}

#if 0
#define INNER_DEEP         (2)
#define MAX_DEEP           (24)
#define MAX_ST_INFO        (256)
#define MAX_ST_LINE        (512)
#endif


static void printf_stacktrace() {

#define INNER_DEEP         (0)
#define MAX_DEEP           (100)
#define MAX_ST_INFO        (256)
#define MAX_ST_LINE        (512)

    unsigned int i = 0;
    unsigned short frames = 0;
    void *stack[MAX_DEEP] = { 0 };
    char st_line[MAX_ST_LINE] = { 0 };

    HANDLE   process = _get_curr_proc_handle();

#if defined(WIN32)
    SYMBOL_INFO *symbol = NULL;

    frames = CaptureStackBackTrace(INNER_DEEP, MAX_DEEP, stack, NULL);
    symbol = (SYMBOL_INFO *)calloc(sizeof(SYMBOL_INFO) + sizeof(char) * MAX_ST_INFO, 1);
    symbol->MaxNameLen = MAX_ST_INFO - 1;
    symbol->SizeOfStruct = sizeof(SYMBOL_INFO);
    for (i = 0; i < frames; ++i) {
        SymFromAddr(process, (DWORD64)(stack[i]), 0, symbol);
        snprintf(st_line, sizeof(st_line) - 1, "    %d: %s [0x%X]\n", frames - i - 1, symbol->Name, symbol->Address);
        printf("%s", st_line);

    }
#elif defined(linux)
    char **st_arr = NULL;

    frames = backtrace(stack, MAX_DEEP);
    st_arr = backtrace_symbols(stack, frames);
    for (i = 0; i < frames; ++i) {
        snprintf(st_line, sizeof(st_line) - 1, "    %d: %s\n", frames - i - 1, st_arr[i]);
        fwrite(st_line, sizeof(char), strlen(st_line), g_logger_cfg.log_file);
    }
    free(st_arr);
#endif
}




int test_print_strace() {
    try {
        throw  -1;
    }catch (const std::exception& e) {
        std::cout << e.what() << std::endl;
    }
    catch (int m) {
        printf_stacktrace();
    }
    return  0;
}

```



libcsdbg 

## 参考链接

1. https://blog.csdn.net/zqp2013/article/details/51140236
2. https://blog.csdn.net/weixin_33725722/article/details/85819408
3. [BugTrap：程序崩溃快照、bug跟踪之利器](https://blog.csdn.net/zqp2013/article/details/51140236)