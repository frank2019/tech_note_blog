



## UVC

**UVC全称为USB Video Class，即：USB视频类，是一种为USB视频捕获设备定义的协议标准。**是Microsoft与另外几家设备厂商联合推出的为USB视频捕获设备定义的协议标准，目前已成为USB org标准之一。



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

UVC同MSC一样，系USB框架下的功能类协议，但却与MSC有着较大差异。MSC功能采用Control+Bulk传输完成，其枚举流程，描述符配置较为清晰，控制传输阶段简单，定义的类功能控制命令较少。而BULK传输阶段则较为复杂繁琐，出错机制，续传机制等要求较为严格。

而UVC则刚好相反，它采用Control+ISO传输机制实现（BULK和INTR机制为可选特性），其枚举流程，描述符配置较为复杂，繁琐，定义了诸多的类控制命令，Entity等；而具体的数据传输阶段即ISO传输较为简单。

## 准备材料



1. [USB官网下载UVC官方文档](https://www.usb.org/document-library/video-class-v15-document-set)