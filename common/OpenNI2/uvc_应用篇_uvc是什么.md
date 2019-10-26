



## UVC(USB Video Class)

**UVC全称为USB Video Class，即：USB视频类，是一种为USB视频捕获设备定义的协议标准。**是Microsoft与另外几家设备厂商联合推出的为USB视频捕获设备定义的协议标准，目前已成为USB org标准之一。

- uvc是一种硬件的框架结构，符合此标准的设计即可实现免驱。

- V4L2 是专门为 linux 设备设计的一套视频框架，其主体框架在 linux 内核，可以理解为是整个 linux 系统上面的视频源捕获驱动框架。其广泛应用在嵌入式设备以及移动端、个人电脑设备上面，市面上的编码产品类如：SDV、手机、IPC、行车记录仪都会用到这个框架来进行视频采集。
  



## 概述

如今的主流操作系统都已提供UVC设备驱动，因此符合UVC规格的硬件设备在不需要安装任何的驱动程序下即可在主机中正常使用。使用UVC技术的包括摄像头、数码相机、类比影像转换器、电视棒及静态影像相机等设备。

最新的UVC版本为UVC 1.5，由USB Implementers Forum定义包括基本协议及负载格式。

网络摄像头是第一个支持UVC而且也是数量最多的UVC设备，目前，操作系统只要是 Windows XP SP2 之后的版本都可以支持 UVC，当然 Vista 就更不用说了。Linux系统自2.4以后的内核都支持了大量的设备驱动，并可以支持UVC设备。

使用 UVC 的好处 USB 在 Video这块也成为一项标准了之后，硬件在各个程序之间彼此运行会更加顺利，而且也省略了驱动程序安装这一环节。

UVC相机最适合作为工业网络相机在视频会议、站亭系统、小型设备生产、物流业等应用中使用

## UVC功能

UVC设备都是多Interface设备，这点同普通的u盘不同。UVC设备最起码有两个Interface，VideoControl（VC）Interface和VideoStream(VS)  Interface； 这也是最常见的UVC设备。 Spec明确要求一个具有可用的，具有实际UVC功能的设备要有一个VC  Interface，一个或多个VS Interface。

VCInterface用于进行配置，操控，设置UVC设备进入不同的功能状态，而VSInterface则负责视频数据流的传输；完整的UVC功能需依赖VS，VC Interfaces的配合才能实现



## UVC VS MSC

UVC同MSC（大容量存储设备）一样，系USB框架下的功能类协议，但却与MSC有着较大差异。MSC功能采用Control+Bulk传输完成，其枚举流程，描述符配置较为清晰，控制传输阶段简单，定义的类功能控制命令较少。而BULK传输阶段则较为复杂繁琐，出错机制，续传机制等要求较为严格。

而UVC则刚好相反，它采用Control+ISO传输机制实现（BULK和INTR机制为可选特性），其枚举流程，描述符配置较为复杂，繁琐，定义了诸多的类控制命令，Entity等；而具体的数据传输阶段即ISO传输较为简单。





## 解析uvc 使用那个SDK？

### libuvc 

a cross-platform library for USB video devices https://ken.tossell.net/libuvc/

项目地址： https://github.com/libuvc/libuvc

参考链接

1. [libuvc on Windows](https://github.com/libuvc/libuvc/issues/12)

### UVCCamera

安卓USB   uvc摄像头类库

### Media Foundation SDK

MicrosoftMediaFoundation允许开发用于在WindowsVista及更高版本上使用数字媒体的应用程序和组件。Media Foundation是Windows的下一代多媒体平台，它使开发人员、消费者和内容提供商能够以更强的健壮性、无与伦比的质量和无缝的互操作性接受新一轮的优质内容。

Media Foundation 是[DirectShow](https://baike.baidu.com/item/DirectShow)为主的旧式多媒体[应用程序接口](https://baike.baidu.com/item/应用程序接口)的替代者与继承者，在微软的计划下将逐步汰换[DirectShow](https://baike.baidu.com/item/DirectShow)技术。Media Foundation要求Windows Vista或更高版本，不支持较早期的Windows版本，特别是Windows XP。

Media Foundation 长于高质量的音频和视频播放，高清内容（如[HDTV](https://baike.baidu.com/item/HDTV), 高清电视）和数字版权管理（DRM）访问控制。Media Foundation在不同的Windows版本上能力不同，如Windows 7上就添加了H264编码支持。Windows 8上则提供数种更高质量的设置。



开源项目Azure-Kinect-Sensor-SDK  在windows下使用的即是此接口SDK，在linux下使用的是libuvc。

而开源项目librealsense 在win7 使用自定义的实现基于winusb.h。 在其他版本 使用的是Media Foundation SDK。 在linux使用libuvc。

### 参考链接

1. [Media Foundation Headers and Libraries](https://docs.microsoft.com/zh-cn/windows/win32/medfound/media-foundation-headers-and-libraries?redirectedfrom=MSDN)
2. [Microsoft Media Foundation官方文档翻译（一）《Microsoft Media Foundation》](https://blog.csdn.net/rzdyzx/article/details/86684365)



### 初步结论

在不同平台 选择不同的库，

- 在windows 使用 Media Foundation SDK

- 在linux平台使用 libuvc
- android 平台



## 参考链接

1. [libuvc 官网](https://ken.tossell.net/libuvc/doc/)

2. [维基百科中的描述]( https://en.wikipedia.org/wiki/USB_video_device_class)

3. uvc协议下载：
    https://www.usb.org/documents
    https://www.usb.org/document-library/video-class-v15-document-set
    https://www.usb.org/document-library/video-class-v11-document-set
    https://www.usb.org/document-library/audi

4.[USB官网下载UVC官方文档](https://www.usb.org/document-library/video-class-v15-document-set)

