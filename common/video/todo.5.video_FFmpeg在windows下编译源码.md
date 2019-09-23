

# FFmpeg在windows下编译源码

由于FFmpeg是基于Linux开发的开源项目，源代码和Windows下最常见的Visual  Studio提供的C/C++编译器不兼容，因此它不能使用MSVC++编译，需要在Windows下配置一个类似Linux的编译环境。本文主要记录Windows下FFmpeg编译的过程。

## **1.资源准备**

准备编译过程所需的软件工具和源代码。

(1). MinGW-MSYS Bundle http://sourceforge.net/projects/mingwbundle/

(2). Yasm http://yasm.tortall.net/Download.html

(3). SDL http://www.libsdl.org/download-1.2.php

(4). X264 http://www.videolan.org/developers/x264.html

(5). FFmpeg http://www.ffmpeg.org/download.html



https://sourceforge.net/projects/mingwbundle/files/GCC%206.3.0/

http://www.msys2.org/



安装minGW  

下载：https://mirrors.xtom.com.hk/osdn//mingw/68260/mingw-get-setup.exe



mingw版本差异

[mingw-w64](http://mingw-w64.org/doku.php/start)

http://www.msys2.org/



## 2.软件安装**

### (1).MinGW+Msys编译环境安装

一种方法是先安装mingw，再通过网络下载的方法来安装mingw和msys软件。安装好之后，再通过烦琐的配置，来搭建编译环境。另一种直接安装配置好的MinGW+Msys系统。为了降低安装过程的烦琐程度，选择第二种方法，安装MinGW+Msys编译环境。下载MinGW-MSYS
Bundle软件后，直接安装程序，配置安装路径，按照软件默认的安装向导，即可把软件安装好。













## 1、搭建 MinGW 的编译环境

下载yasm，地址：http://yasm.tortall.net/Download.html

改名为yasm.exe放到C:\WINDOWS\system32 或者 C:\MinGW\msys\1.0\bin文件夹下。

下载 mingw-get-inst-20101030.exe , 点击这里下载 http://sourceforge.net/projects/mingw/files/ 。

安装时选择如下 



https://nchc.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe







## 参考链接



1. [图文介绍windows下实现编译ffmpeg工程的详细步骤](https://www.cnblogs.com/eachan/p/4711840.html)
2. https://github.com/msys2/msys2/wiki/MSYS2-installation
3. [cygwin](https://cygwin.com/install.html)
4. [Windows下FFmpeg编译](http://ffmpeg.me/archives/12.html)

