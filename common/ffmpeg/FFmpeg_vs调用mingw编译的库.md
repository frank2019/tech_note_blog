## vs  调用mingw 库



### 是否可以调用

1. 如果dll 中导出了C++的类，那么就不要折腾了。不同的编译器编译出来的C++代码是不保证通用的。
2. 如果dll中只是一些C 函数，那么是可以互相调用的。

## 调用方法

Mingw 生成dll时即使生成了 .a 文件也是不能用到VC 上的（至少我用的VC2010版本是不行了，表现为生成的程序 Debug模式下可以运行，但是Release 模式下却无法运行）。

如果生成dll 没有生成def文件，需要先生成def文件。

###  def文件的生成

如果连def文件也没有，那么先要生成def文件，可以从网上下载一个小工具叫做[pexports](https://sourceforge.net/projects/mingw/files/MinGW/Extension/pexports/)。

 运行命令生成def文件

```bash
pexports.exe test.dll > test.def
```

### 使用lib命令生成lib文件

lib.exe 位于vs安装目录下(比如："D:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\lib.exe")

生成lib文件。

```dos
λ "D:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\lib.exe"  /DEF:avcodec.def /MACHINE:IX86


Microsoft (R) Library Manager Version 12.00.30501.0
Copyright (C) Microsoft Corporation.  All rights reserved.

   正在创建库 avcodec.lib 和对象 avcodec.exp
```



## 参考链接

1. [VC 调用 MinGW 生成的dll](https://blog.csdn.net/liyuanbhu/article/details/44650641)
2. [VC/VS调用mingw32编译出的dll文件](https://blog.csdn.net/zhuobixin/article/details/79540417)