## 概述

## 相机

Android 的相机硬件抽象层 (HAL) 可将 Camera 2 中较高级别的相机框架 API 连接到底层的相机驱动程序和硬件。相机子系统包括相机管道组件的实现，而相机 HAL 则可提供用于实现您的这些组件版本的接口。

- 注意：如果您要在搭载 Android 8.0 或更高版本的设备上实现相机 HAL，则必须使用 HIDL 接口。要了解旧版组件，请参阅旧版 HAL 组件。



## 架构

------

下列图表和列表说明了 HAL 组件：

![](res/1.png)





### **应用框架**

应用代码位于应用框架级别，它使用 Camera 2 API 与相机硬件进行交互。在内部，这些代码会调用相应的 Binder 接口，以访问与相机互动的原生代码。

### **AIDL**

 与 CameraService 关联的 Binder 接口可在  frameworks/av/camera/aidl/android/hardware 中找到。  生成的代码会调用较低级别的原生代码以获取对实体相机的访问权限，并返回用于在框架级别创建 CameraDevice 并最终创建  CameraCaptureSession 对象的数据。

### **原生框架**

 此框架位于 frameworks/av/ 中，并提供相当于 CameraDevice 和 CameraCaptureSession 类的原生类。另请参阅 NDK camera2 参考。

### **Binder IPC 接口**

 IPC binder 接口用于实现跨越进程边界的通信。调用相机服务的若干个相机 Binder 类位于  frameworks/av/camera/camera/aidl/android/hardware 目录中。 ICameraService  是相机服务的接口；ICameraDeviceUser 是已打开的特定相机设备的接口；ICameraServiceListener 和  ICameraDeviceCallbacks 分别是对应用框架的 CameraService 和 CameraDevice 回调。

### **相机服务**

 位于 frameworks/av/services/camera/libcameraservice/CameraService.cpp 下的相机服务是与 HAL 进行互动的实际代码。

### **HAL**

 硬件抽象层定义了由相机服务调用、且您必须实现以确保相机硬件正常运行的标准接口。



## **实现 HAL**

------

HAL 位于相机驱动程序和更高级别的 Android 框架之间，它定义您必须实现的接口，以便应用可以正确地操作相机硬件。从  Android 8.0 开始，相机 HAL 接口是 Project Treble 的一部分，相应的 HIDL 接口在  hardware/interfaces/camera 中定义。

典型的绑定式 HAL 必须实现以下 HIDL 接口：

- ICameraProvider：用于枚举单个设备并管理其状态。
- ICameraDevice：相机设备接口。
- ICameraDeviceSession：活跃的相机设备会话接口。

参考 HIDL 实现适用于 CameraProvider.cpp、CameraDevice.cpp 和  CameraDeviceSession.cpp。该实现封装了仍在使用旧版 API 的旧 HAL。从 Android 8.0 开始，相机 HAL  实现必须使用 HIDL API；不支持使用旧版接口。

要详细了解 Treble 和 HAL 开发，请参阅 Treble 资源。



## 参考链接

1. [Android [Camera 源码] 概述(overview) Google官方文档](https://blog.csdn.net/kiazhu/article/details/84671593)
2. [Google源码网地址链接：https://source.android.com/devices/camera](https://source.android.com/devices/camera)