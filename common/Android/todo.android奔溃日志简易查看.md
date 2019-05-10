





```

```





编写调试c/c++代码时经常会遇到奔溃：

```
--------- beginning of crash
03-21 11:23:59.354  6031  6093 F libc    : Fatal signal 11 (SIGSEGV), code 2, fault addr 0x75cf8fb000 in tid 6093 (depth-camera), pid 6031 (rbbec.demo)
03-21 11:23:59.407  6102  6102 I crash_dump64: obtaining output fd from tombstoned, type: kDebuggerdTombstone
03-21 11:23:59.408  1376  1376 I /system/bin/tombstoned: received crash request for pid 6031
03-21 11:23:59.409  6102  6102 I crash_dump64: performing dump of process 6031 (target tid = 6093)
03-21 11:23:59.409  6102  6102 F DEBUG   : *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
03-21 11:23:59.409  6102  6102 F DEBUG   : Build fingerprint: 'OPPO/R11s/R11s:8.1.0/OPM1.171019.026/1545230981:user/release-keys'
03-21 11:23:59.409  6102  6102 F DEBUG   : Revision: '0'
03-21 11:23:59.409  6102  6102 F DEBUG   : ABI: 'arm64'
03-21 11:23:59.409  6102  6102 F DEBUG   : pid: 6031, tid: 6093, name: depth-camera  >>> com.o3w.demo <<<
03-21 11:23:59.409  6102  6102 F DEBUG   : signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x75cf8fb000
03-21 11:23:59.409  6102  6102 F DEBUG   :     x0   0000000000000000  x1   0000000000000000  x2   00000076740c32d0  x3   00000000000003c0
03-21 11:23:59.409  6102  6102 F DEBUG   :     x4   0000000000000010  x5   00000000000001e0  x6   00000076740c2000  x7   0000000000907044
03-21 11:23:59.409  6102  6102 F DEBUG   :     x8   0000000000000500  x9   00000000000003c0  x10  0000000000001400  x11  0000000000000500
03-21 11:23:59.409  6102  6102 F DEBUG   :     x12  00000075cf8fa602  x13  00000000000003bf  x14  00000075cfe95b08  x15  00000000000004f8
03-21 11:23:59.409  6102  6102 F DEBUG   :     x16  00000075cf8faff2  x17  00000000000004f9  x18  00000000000004f8  x19  0000000000000500
03-21 11:23:59.409  6102  6102 F DEBUG   :     x20  00000075cf6a3000  x21  00000075cfe00008  x22  00000000000001e0  x23  00000000000003c0
03-21 11:23:59.409  6102  6102 F DEBUG   :     x24  0000000000000280  x25  00000000000001e0  x26  0000000000000500  x27  0000000000000010
03-21 11:23:59.409  6102  6102 F DEBUG   :     x28  00000075cfe96008  x29  00000075cf9fd3e0  x30  00000075d3741f70
03-21 11:23:59.409  6102  6102 F DEBUG   :     sp   00000075cf9fd340  pc   00000075d3741fa8  pstate 0000000080000000
03-21 11:23:59.411  6102  6102 F DEBUG   : 
03-21 11:23:59.411  6102  6102 F DEBUG   : backtrace:
03-21 11:23:59.411  6102  6102 F DEBUG   :     #00 pc 0000000000000fa8  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/lib/arm64/libpostfilter.so (softFilterOptDwUp+184)
03-21 11:23:59.411  6102  6102 F DEBUG   :     #01 pc 00000000000055e4  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/lib/arm64/libdemo.so (softfilter_showtime+512)
03-21 11:23:59.411  6102  6102 F DEBUG   :     #02 pc 0000000000005880  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/lib/arm64/libdemo.so (obc_unpackdata_2_depth+544)
03-21 11:23:59.411  6102  6102 F DEBUG   :     #03 pc 0000000000005f74  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/lib/arm64/libdemo.so (obc_raw_2_depth+416)
03-21 11:23:59.411  6102  6102 F DEBUG   :     #04 pc 0000000000001b90  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/lib/arm64/libdemo_jni.so (com_o3w_obdepth_disparity_to_depth(_JNIEnv*, _jclass*, _jobject*, _jobject*, int, int)+120)
03-21 11:23:59.411  6102  6102 F DEBUG   :     #05 pc 0000000000037fd4  /data/app/com.o3w.demo-fYcvHrACzGVr87viBMX_8Q==/oat/arm64/base.odex (offset 0x1b000)

```





#### 含义解析

这个日志大概透漏了那些信息



```
signal 11 (SIGSEGV), code 2 (SEGV_ACCERR), fault addr 0x75cf8fb000
```



信号

1. SIGBUS(Bus error)意味着指针所对应的地址是有效地址，但总线不能正常使用该指针。通常是未对齐的数据访问所致。

2. SIGSEGV(Segment fault)意味着指针所对应的地址是无效地址，没有物理内存对应该地址。

3. SEGV_MAPERR, 地址没有映射到对象，可能的原因是dangling pointer或者overflow，

比如

1. 访问得内存已经被释放，或者访问得空间越界

SEGV_ACCERR, 对映射的对象没有权限



#### 奔溃具体在哪一行

使用工具addr2line

addr2line 工具（它是标准的 GNU Binutils 中的一部分）是一个可以将指令的地址和可执行映像转换成文件名、函数名和源代码行数的工具。

使用此工具可以判断出函数名、源文件 以及它在源文件中的行号

命令

```
addr2line  -C -f  -e  libpoxx.so   0x0000000000000fa8
E:\build\arm64-v8a/../../source/soxxx.c:200
```



```
whereis  addr2line 
addr2line: /usr/bin/addr2line /usr/share/man/man1/addr2line.1.gz
```





#### 参考链接

1. [](https://www.cnblogs.com/zl1991/p/5893554.html)

