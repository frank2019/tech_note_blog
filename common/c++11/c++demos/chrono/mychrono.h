#ifndef MYMATH_H_
#define MYMATH_H_

#ifdef WIN32
#define TrimFilePath(x) strrchr(x, '\\')?strrchr(x, '\\')+1:x
#else  // *nix
#define TrimFilePath(x) strrchr(x,'/')?strrchr(x,'/')+1:x
#endif

#ifndef  D
#define D(fmt, ...)   \
    printf("[DEBUG] [%s(%d)] : \t" fmt"\n",TrimFilePath(__FILE__),__LINE__,##__VA_ARGS__)
#endif

#ifdef __cplusplus
extern "C" {
#endif

    int FibonacciSequence(int index);

#ifdef __cplusplus
}
#endif


#endif