



libusb 源码位于： https://github.com/libusb/libusb



## libusb 目录分析

### tests/

关于libusb的四个压力测试，不涉USB打开操作及具体的数据传输。

### android/

用于生成Android版本的libusb库、test和examples。进入android/jni/，执行ndk_build即可。在android/README中有以下描述：

> To build libusb for Android do the following:
>
>  1. Download the latest NDK from:
>     http://developer.android.com/tools/sdk/ndk/index.html
>
>  2. Extract the NDK.
>
>  3. Open a shell and make sure there exist an NDK global variable
>     set to the directory where you extracted the NDK.
>
>  4. Change directory to libusb's "android/jni"
>
>  5. Run "$NDK/ndk-build".
>
> The libusb library, examples and tests can then be found in:
>     "android/libs/$ARCH"



### doc/

用于生成软件接口文档。编译完工程后，打开doc/doxygen.cfg，将PROJECT_LOGO = libusb.png修改为PROJECT_LOGO = ，否则产生文档时会提示 libusb.png不存在，修改完成后在doc/目录下执行：doxygen doxygen.cfg即可生成html格式文档，或者执行make docs。
注：Ubuntu需要提前安装doxygen。

### libusb/

libusb的核心代码。
1）os/目录是是平台相关的代码，支持：darwin、haiku、linux、windows、sunos、netbsd、openbsd等七种平台，即Linux, OS X, Windows, Windows CE, Android, OpenBSD/NetBSD, Haiku。
2）libusb-1.0.def DLL中导出函数的声明的一种方式：采用模块定义(.def) 文件声明，.def文件为链接器提供了有关被链接程序的导出、属性及其他方面的信息。
3）libusb-1.0.rc 用于windows，产生 .res文件。

### msvc/

微软VC编译环境，目录下均是windows平台环境相关文件。

### m4/

linux编译相关。m4 是一种宏处理器，它扫描用户输入的文本并将其输出，期间如果遇到宏就将其展开后输出。

### Xcode/

apple平台相关文件。Xcode是苹果的集成开发环境（IDE），开发者可用其构建适用于苹果iPad、iPhone以及Mac设备的应用程序。在应用程序的创建、测试、优化以及提交至App Store的过程中，Xcode为开发者提供了用以管理整个开发工作流的工具。

### examples/

libusb的测试demo，进入目录后执行make即可生成可执行文件进行测试。

#### 1）getopt/

getopt现在已经是C函数库的一部分，没有编译使用，删除此目录不会有影响。

#### 2）hotplugtest.c

热插拔测试demo

#### 3）listdevs.c

获取系统当前的usb设备列表，并打印出VID、PID、bus和device编号

#### 4）testlibusb.c

打印usb设备列表的详细信息：包括设备描述符、配置、接口、端点描述符

#### 5）dpfp.c

一款指纹识别器的应用程序：URU4000B fingerprint scanner 应用程序，将采集到的指纹图像保存为文件。系统采用异步传输的方式，使用了control、interrupt、bulk三种传输方式。不仅使用了libusb_control_transfer等同步接口传输，也使用了libusb_submit_transfer的异步传输方式。

#### 6）dpfp_threaded.c

与dpfp.c功能一致，代码也大部分相同，唯一不同在于dpfp.c将libusb_handle_events 放在 main loop中，而dpfp_threaded.c 将libusb_handle_events 放在一个线程当中。

#### 7）sam3u_benchmark.c

Atmel SAM3U isochronous（等时传输）性能测试。程序不断接收来自SAM3U iso端点的数据，当按下CTRL-C时，计算花费时间和传输的总数据量。

#### 8）xusb.c

一个综合的USB测试程序，包括：HID设备（xbox、PS3和Joystick）、Mass Storage，涉及中断、批量和控制传输。其中Mass Storage可以使用普通的U盘进行测试，只需修改VID和PID即可，可以实现的功能有：读取描述符、查询U盘信息、读取U盘容量、读取U盘数据（因为没有使用文件系统，读取出来的数据是原始二进制数据）。
关于Mass Storage中涉及的SCSI命令，参考： USB Mass Stroage - SCSI指令格式详解。

#### 9）fxload.c和ezusb.c

EZ-USB的固件下载程序，可实现下载固件（image）到Cypress EZ-USB microcontrollers，ezusb系列芯片使用端点0和厂商特定命令将数据写到片上SRAM，并且也支持写数据到CPUCS register或者eeprom。
程序使用控制传输方式进行指令和数据的传输，libusb_control_transfer()的形参bmRequestType使用LIBUSB_REQUEST_TYPE_VENDOR（厂商自定义请求）。程序支持五种下载类型（Target type）： an21, fx, fx2, fx2lp, fx3，支持四种固件(image)类型：“Intel HEX”, “Cypress 8051 IIC”, “Cypress 8051 BIX”, “Cypress IMG format”。

#### 注：

Atmel SAM3U：基于ARM Cortex M3内核的MCU，支持usb high speed。
关于ezusb的介绍：
http://www.linux-usb.org/ezusb/
http://www.cypress.com/
EZ-USB FX是CYPRESS公司出品的一种带有USB功能的8051兼容系列，封装采用PQFP。这一系列芯片的最大不同之处在于使用不同的方式存储固件，EZ-USB FX可以在一个串行EEPROM中存储固件，也可以在主机上存储固件。当设备连接主机后，这些固件通过USB总线传输到芯片中。这样做最大的好处就是固件容易升级，不需要替换芯片或使用特殊的程序，只要在主机上更新固件即可。
CY7C61083A是一款FX2LP芯片，支持full/high speed，应用：MP3、读卡器、照相机等等

### other

- ChangeLog：代码修改日志。2008-05-25: v0.9.0 release，目前最新版2016-10-01: v1.0.21
- INSTALL：编译、安装方法。编译器选项，如： ./configure CC=c99 CFLAGS=-g LIBS=-lposix
- PORTING：移植libusb到其他未支持平台的方法。



## 参考链接

1. [Linux USB开发：libusb开发指南](https://blog.csdn.net/u012247418/article/details/82960889)