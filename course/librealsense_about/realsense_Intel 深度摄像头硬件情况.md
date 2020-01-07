





## 概述

- Intel的体感摄像机是具有深度图像采集能力的摄像机，目前已经出到了400系列。与kinect 2，ZED，leap motion比较，属于比较中庸。
- 手势识别方面不如leap motion，leap motion的视角是120度，精度和速度都比intel高，缺点是leap motion不给深度图，只给最后的骨骼跟踪结果，也就是只能做手势识别应用，不能干别的。
- kinect 2采用了TOF稳定性相对较好、细节更多；被其他环境光源（红外线）影响的概率也更低。与散斑技术相比、画面很干净。视角变为70×60度。kinect 2后端的分析模块也比较给力，如可以侦测6 位使用者（含骨架）、25 个关节点（关节点与上一代相比多5个，现在在手掌这部分现在有三个关节点，所以可以在一定程度上侦测手的开合状态）；可以根据脸部彩色影像的细微变化侦测心跳。开发资源较丰富。确点是需要PC支持，体积大等等
- librealsense 是结构光方案.

## **real sense 的设备型号**

### **real sense200系列**

**F200**为前置摄像头，支持室内近距离。F200的硬件组成包括，一个IR camera，一个HD1080p camera，一个IR Laser projector。F200的3D扫描范围为25-54cm。点追踪范围30-85cm，速度1.5米/秒。

![](https://img-blog.csdn.net/20180414152427925)

**R200**为后置摄像头，摄像头一般背对用户，旨在对周围环境的感知。有 3 个摄像头和惯性传感器。可提供 RGB（彩色）和立体红外图像，以生成深度。借助激光投影仪，该摄像头可进行三维扫描，获取场景感知和增强的摄影。 内部范围约 0.5-3.5 米，外部范围可达 10 米。R200集成了IMU数据，可以跟踪/定位：使用深度、RGB 和 IMU 数据，实时预估摄像头的位置和方位。只有 R200 支持场景感知、增强摄影和 3D 捕捉整个头部和身体。
R200的型号分为一代和二代。R200一代右边是“INTEL”标志，R200二代右边是“CREATIVE”标志。一代型号编号为946432，二代型号编号为VF0830。

![](https://img-blog.csdn.net/20180414152454901)



![](https://img-blog.csdn.net/20180414152504997)



![](https://img-blog.csdn.net/20180414152512284)



### **300系列**

300系列的发布时间是2016年2月

#### SR300 

是F200的升级版本， 与 F200 摄像头型号相似，SR300 使用编码光深技术，在更小范围内创建高质量的 3D 深度视频流。 SR300 摄像头的组件包括红外激光投影系统、高速 VGA 红外摄像头和具备集成 ISP 的 200 万像素彩色摄像头。 SR300 使用高速 VGA 深度模式替代了 F200 使用的本机 VGA 深度模式。 此新型深度模式降低了曝光时间，并且可以捕捉到高达 2 米/秒的动态动作。 该摄像头可向客户端提供同步颜色、深度和 IR 视频流数据，能够支持实现全新的平台使用方式。 摄像头深度解决方案的有效范围为室内 0.2 米至 1.2 米。3D扫描范围为25-70cm。点追踪范围20-150cm，速度2米/秒。景深/红外：每秒60帧时，分辨率640X480，RGB（红绿蓝）；每秒30帧时，1080P要求USB3.0。



###  前置摄像头 SR300 和 F200 的比较



| **产品亮点** | **SR300**                    | **F200**                               |
| ------------ | ---------------------------- | -------------------------------------- |
| 方向         | 前置                         | 前置                                   |
| 技术         | 编码光；高速 VGA 60 帧       | 编码光；本机 VGA 60 帧                 |
| 彩色摄像头   | 多至 1080p 30 帧、720p 60 帧 | 多至 1080p 30 帧                       |
| SDK          | SDK 2015 R5 或更新版本       | SDK R2 或更新版本                      |
| DCM 版本     | DCM 3.0.24.51819*            | DCM 1.4.27.41994*                      |
| 操作系统     | Windows 10 64 位 RTM         | Windows 10 64 位 RTM、 Windows 8 64 位 |
| 范围         | 室内：20 – 120 厘米          | 室内：20 – 120 厘米                    |



#### **zr300\***

是R300的升级版本，为后置摄像头。包含了惯性测量单元。貌似是创新公司产品，Intel很少提到，并不支持。VGA, 480x360, QVGA 分辨率。深度相机有效范围 0.55m to 2.8m。1080p 彩色相机输出。



#### SR305

2019年7月发布

SR305最大的特点就是通过优化内部结构和零部件，使得价格降低至79美元

RealSense SR305定位就是入门级深度传感器。据悉，其采用结构光投射方案，仅内置一颗RGB相机，即可输出60帧/深度分辨率为640×480的图像。 


RealSense SR305还支持Intel开源的RealSense SDK 2.0，简化开发成本和上手难度。 

应用场景方面，RealSense SR305可用于近距离物品识别、手势追踪、人脸识别、AR、3D扫描、背景分割和3D摄影，工作范围在0.2米-1.5米之间。 



### **400系列（**发布时间2018年1月）

#### **D415**

的硬件包含了两个深度相机，一个RGB相机和一个结构光红外投影仪。深度卷帘相机（逐行扫描），红外结构光深度测距。



| Use Environment                                              | Indoor and Outdoor                                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Depth Technology                                             | Active IR stereo                                             |
| Main Intel® RealSense™ component                             | Intel® RealSense™ Vision Processor D4Intel® RealSense™ module D410 |
| Depth Field of View (FOV)—(Horizontal × Vertical × Diagonal) | 69.4° x 42.5° x 77° (+/- 3°)                                 |
| Depth Stream Output Resolution                               | Up to 1280 x 720                                             |
| Depth Stream Output Frame Rate                               | Up to 90 fps                                                 |
| Minimum Depth Distance (Min-Z)                               | 0.3m                                                         |
| Maximum Range                                                | Approx. 10 meters; Varies depending on calibration, scene, and lighting condition |
| RGB Sensor Resolution and Frame Rate                         | 1920 x 1080 at 30 fps                                        |
| RGB Sensor FOV (Horizontal x Vertical x Diagonal)            | 69.4° x 42.5° x 77° (+/- 3°)                                 |
| Camera Dimension (Length x Depth x Height)                   | 99 mm x 20 mm x 23 mm                                        |
| Connectors                                                   | USB 3.0 Type - C                                             |
| Mounting Mechanism                                           | One 1/4-20 UNC thread mounting pointTwo M3 thread mounting points |

#### **D435** 

特点是采用了全局相机。

| Use Environment                                              | Indoor/Outdoor                                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Depth Technology                                             | Active IR Stereo (Global Shutter)                            |
| Main Intel® RealSense™ component                             | Intel® RealSense™ Vision Processor D4Intel® RealSense™ module D430 |
| Depth Field of View (FOV)—(Horizontal × Vertical × Diagonal) | 91.2 x 65.5 x 100.6 (+/- 3°)                                 |
| Depth Stream Output Resolution                               | Up to 1280 x 720                                             |
| Depth Stream Output Frame Rate                               | Up to 90 fps                                                 |
| Minimum Depth Distance (Min-Z)                               | 0.2m                                                         |
| Sensor Shutter Type                                          | Global shutter                                               |
| Maximum Range                                                | Approx.10 meters; Varies depending on calibration, scene, and lighting condition |
| RGB Sensor Resolution and Frame Rate                         | 1920 x 1080 at 30 fps                                        |
| RGB Sensor FOV (Horizontal x Vertical x Diagonal)            | 69.4° x 42.5° x 77° (+/- 3°)                                 |
| Camera Dimension (Length x Depth x Height)                   | 90 mm x 25 mm x 25 mm                                        |
| Connectors                                                   | USB 3.0 Type - C                                             |
| Mounting Mechanism                                           | One 1/4-20 UNC thread mounting pointTwo M3 thread mounting points |



3.2.openCV 2.4 support
https://docs.opencv.org/2.4/doc/user_guide/ug_intelperc.html

    n.ImShow-最小OpenCV应用程序用于可视化深度数据
    n.GrabCuts-使用基于GrabCut算法的简单背景删除
    潜伏期工具-利用计算机视觉进行基本时延估计
    DNN-用于实时目标检测的英特尔RealSense相机




## 参考链接

1. [英特尔推出全新RealSense深度相机模组SR305，兼容RealSense 2.0 SDK,79美元](https://www.xianjichina.com/special/detail_411044.html)
2. [体感摄像头 realsense 系列硬件资料](https://blog.csdn.net/jepco1/article/details/79940577)
3. [卷帘快门(Rolling shutter)与全局快门(global shutter)的区别](https://blog.csdn.net/danmeng8068/article/details/80726514)