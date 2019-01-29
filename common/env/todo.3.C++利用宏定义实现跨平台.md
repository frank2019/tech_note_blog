C++编写跨平台程序的关键，C/C++中的内置宏定义
分两部分：

#### 操作系统判定：

Windows:   WIN32

Linux:   linux

Solaris:   __sun

#### 编译器判定：

VC:  _MSC_VER

GCC/G++:   __GNUC__

SunCC:   __SUNPRO_C和__SUNPRO_CC





```
 //#define OSX // to compile with cc on Macintosh OSX

//#define OSX_TIGER // use with OSX if OSX Tiger is being used

//#define OSX_INTEL // compile with cc on Macintosh OSX on Intel-style processors

//#define GCC // to compile with gcc (or g++) on LINUX

//#define MSVC // to compile with Microsoft Studio

//#define X_P3 // when this is defined, the proteotypic peptide version of X! Tandem, X! P3 is built
```

