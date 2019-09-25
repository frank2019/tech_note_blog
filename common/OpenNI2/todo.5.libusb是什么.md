

## 1，Overview

**libusb** is a C library that provides generic access to USB  devices. It is intended to be used by developers to facilitate the  production of applications that communicate with USB hardware.

It is **portable**: Using a single cross-platform API, it provides access to USB devices on Linux, OS X, Windows, Android, OpenBSD, etc.

It is **user-mode**: No special privilege or elevation is required for the application to communicate with a device.

It is **version-agnostic**: All versions of the USB protocol, from 1.0 to 3.1 (latest), are supported.

### What platforms are supported?

Linux, OS X, Windows, Windows CE, Android, OpenBSD/NetBSD, Haiku.



## 2，How do I get started?

If you are using Linux, chances are your distribution already  includes libusb, so you probably just need to reference the libusb  header in your source.

For other platforms, or if you want to use the very latest, you  are encouraged to recompile from source. Please check the Downloads  menu.

If you prefer, you can also access the source directly from [github](https://github.com/libusb/libusb).

Once you have secured your access to the library and its header, please check the [libusb API](http://libusb.sourceforge.net/api-1.0/) or the [libusb samples](https://github.com/libusb/libusb/tree/master/examples).     







## 3，libusb、winusb、libusbK、libusb-win32联系和区别

### libusb 

说明：libusb是一个跨平台的usb驱动框架。libusb原始项目在2010年后基本没有更新，曾有libusbx项目2012年从libusb分出来，2014年1月26日又合并回libusb了。当时的libusbx-1.0.18和libusb-1.0.18其实完全一样，相当于libusbx替换了libusb的代码！后续的版本其实都是基于libusbx的代码了！
包含两个主要分支1.x和0.1.x。
1.x和0.1.x并不兼容，可以同时存在，如果要在1.x基础上兼容0.1.x需要libusb-compat转换层。所以0.1.x和libusb-compat不能同时装上！
内核：目前1.x分支的驱动只有用户态，linux下支持usbfs，windows下支持WinUSB.sys。
也可以支持libusbK和libusb-win32（通过libusbK支持）。
工具：通过Zadig支持生成基于libusb0、libusbK、WinUSB的inf文件。
https://github.com/pbatard/libwdi/wiki/Zadig

### libusb-win32

说明：libusb-win32是从libusb-0.1.x分支衍生的，
主要是针对Windows做优化，所以接口风格和libusb-0.1.x一致。
内核：WDM框架的libusb0.sys驱动。
工具：自带inf-wizard.exe生成基于libusb0.sys的inf文件。
注意：目前建议是新的项目尽可能使用libusb，而不是这个libusb-win32了。我在这个上面花了很多时间，一直报错，坑爹了，要注意libusb-win32已经废弃，目前使用的是libusb+Zadig的组合。

### libusbK

说明：libusbK主要是想做一个WinUSB接口风格的开源usb库，
支持基于KMDF的libusbK.sys和系统自带的WinUSB.sys。参考libusb-win32做的开发，部分工具是从libusb-win32整合而来的。因为源代码里也包含了libusb0.dll的加载功能和转换层，所以也可以支持WDM框架的libusb0.sys（libusb-win32）。
内核：基于KMDF框架的libusbK.sys、WDM的libusb0.sys、系统的WinUSB.sys
工具：自带libusbK-inf-wizard.exe（基于libusb-win32的工具改的）
生成基于libusb0、libusbK、WinUSB的inf文件。

### 结论

简单说，就是不要去管libusb-win32和libusbK项目，目前不管是windows还是Linux都是使用libusb项目，主页是libusb.info。
在Windows上使用libusb时是调用微软的WinUSB接口，在Linux上是usbfs。用Zadig工具统一安装驱动，不用理什么inf-wizard.exe。

来源：http://bbs.21ic.com/icview-2630430-1-2.html





## 4，参考链接

1. [Linux USB开发：libusb开发指南](https://blog.csdn.net/u012247418/article/details/82960889)
2. 官网：http://libusb.info/
3. API：http://libusb.sourceforge.net/api-1.0
4. download：https://github.com/libusb/libusb
5. mailing list：http://mailing-list.libusb.info
   libusb test demo：https://github.com/crazybaoli/libusb-test
