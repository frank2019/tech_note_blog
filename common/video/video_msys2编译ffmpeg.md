

# windows下 MSYS2编译FFMPEG



## 安装依赖的包

运行c:\msys64\msys2_shell.bat，在弹出的shell窗口中执行

```bash
pacman -S make yasm diffutils pkg-config
```



## 安装gcc

使用 pacman -Sl | grep “gcc” 可查看安装了哪些gcc。

安装

```bash
pacman -S mingw-w64-i686-gcc 
pacman -S mingw-w64-x86_64-gcc 
```



## 编译

### 4.1 编译32位库

１、通过cmd进入msys2的安装目录即msys64， 执行

```bash
msys2_shell.cmd -mingw32
```

在启动的shell中，执行

```bash
./configure --enable-shared --disable-everything --enable-decoder=h264 --enable-parser=h264 --arch=x86_32
```

２、编译
　　按顺序执行

```bash
make 
make install
```

备注：生成的库在C:\msys64\usr\local\bin

### 4.2 编译64位库

１、通过cmd进入msys2的安装目录即msys64， 执行

```bash
msys2_shell.cmd -mingw64
```

在启动的shell中，执行

```bash
./configure --enable-shared --disable-everything --enable-decoder=h264 --enable-parser=h264 --arch=x86_64
```

２、编译
　按顺序执行

    make 
    make install

备注：生成的库在C:\msys64\usr\local\bin
　

特别说明：用Msys2生成的库有依赖，依赖于C:\msys64\mingw32\bin 或 C:\msys64\mingw64\bin 下的某些dll库。



若需要ffmpeg支持其他视频音频编解码器，只需下载相应源代码，按照以下步骤安装：

**配置(./configure)—>编译(make)—>安装(make install)—>导入环境变量(export)。**

另外，在编译ffmpeg时，开启相应编解码器的配置即可。



## 遇到的问题

### ffmpeg 源码编译找不到 libpostproc 库

给 ./configure   加参数
 --enable-shared : 编译动态库
 --enable-postproc
 --enable-gpl

即 使用 ./configure --enable-shared --enable-postproc --enable-gpl









## 参考链接

1. https://ffmpeg.zeranoe.com/forum/viewtopic.php?f=5&t=3688
2. [win10 msys2 vs2015 ffmpeg3.2.2 编译](https://blog.csdn.net/longji/article/details/54891236)


