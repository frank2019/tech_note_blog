



# Openni SDK  API  主要接口类



## OpenNI是什么



- OpenNI中文译为开放自然语言交互，用官方的表述来讲就是a standard framework for 3D sensing，用于3D感知的开发接口；
- OpenNI2是第二代版本，相对于第一代更加专注于对3D设备的支持和数据的获取，移除了手势识别等中间件的方式，代码更加的精简，简而言之OpenNI2就是一个RGBD相机的用户态驱动，对上提供统一的接口，方便用户获取RGBD的图像数据，对下提供统一的标准类，方便RGBD厂商进行适配；
- 目前OpenNI2支持的设备包括PS1080、PSLink、orbbec、Kinect等设备，由于其清晰的代码结构，很容易对第三方设备进行适配；
- OpenNI2的源码地址为https://github.com/OpenNI/OpenNI2
  



OpenNI2相当于rgbd设备的用户态驱动，主要提供了一套获取rgbd设备的深度数据和color图片的API函数；手势识别等算法应用是建立在OpenNI2 API之上的；
OpenNI2的两大特点：

1. 对外提供统一的接口用以获取rgbd设备的数据，屏蔽应用层对不同设备的操作的差异；
2. OpenNI2 提供了两种方式来获取数据：轮询和事件方式；



## 整体框图



![](resource/1.png)



- 最上层为关于OpenNI2的应用如NITE手势识别，身体运动检测等
- 接下来是OpenNI2的对外提供的统一接口，这些接口对应的头文件为OpenNI.h
- OpenNI Core为OpenNI2的核心部分，OpenNI.h中的结构实现都在这部分；对Driver层提供统一的API，用于Driver的开发扩展，这部分API对应的头文件为OniDriverAPI.h
- 最底层为硬件驱动、或者第三方库，如PS1080通信用的libusb，以及kinect的Nui API
  

## OpenNI2 API 

```c++
namespace openni {
    class VideoMode；
    class SensorInfo;
    class VideoFrameRef;
    class VideoStream;
    class Device;
    class OpenNI;
    class CameraSettings;
    class PlaybackControl;
}
```



OpenNI2 的类都放在命名空间openni中，主要有OpenNI、Device、VideoStream、VideoFrameRef这些类

- openni::Device 	顾名思义是rgbd设备的封装
- openni::VideoStream     是各个视频流的封装，类型有depth，IR、color等
- openni::VideoFrameRef 是图片信息的封装
- openni::OpenNI              用于管理上述各个封装



### openni::OpenNI      

- OpenNI类是库的静态入口点。
- 每个OpenNI 2.0应用程序都使用它来初始化SDK和驱动程序，以便创建有效的设备对象。
- 它还定义了一个侦听器类和事件，这些类和事件允许事件驱动通知*设备连接、设备断开和设备配置更改。*
- 提供了对SDK版本信息的访问，
- 并提供了一个函数，允许您可以等待数据在任何一个流列表上可用(而不是等待一个具有视频流类提供的功能的特定流上的数据)

### openni::VideoMode

- 封装视频流的一组设置。
- 存储的设置包括：帧率、分辨率和像素格式(pixel format)
- 该类别被用作用于设置或获取视频流的设置的输入
- 推荐的做法是使用SensorInfo::getSupportedVideoModes() 函数 获取有效视频模式的列表，然后使用该列表中的项目来进行设置。



### openni::SensorInfo

- sensorInfo类将与特定传感器相关的所有信息封装在特定中设备。
- 设备对象为其包含的每个传感器保存SensorInfo。
- VideoStream 对象保存一个SensorInfo，描述用于生成该数据流的传感器。
- 给定的SensorInfo对象将包含传感器的类型（Depth, IR or Color），以及传感器可以支持的所有VideoStream的列表。
- 每个可用的VideoStream都将有一个单一的视频模式可以查询的视频模式对象获取该模式的详细信息。
- sensorInfo对象应该是绝大多数的VideoStream对象的唯一来源应用程序。
- 应用程序不会直接实例化类型sensorInfo的对象。事实上，不提供公共构造函数。应当从设备或VideoStream中获得sensorInfo对象,并且反过来可用于为该传感器提供可用的VideoStream。



### openni::VideoFrameRef



- VideoFrameRef类封装了单个视频帧-- VideoStream 特点时间得一个输出。
- 这个视频帧可以是  color, IR, or depth帧及其原数据。
- VideoFrameRef 不真实保存数据，只是保存一个引用。
- 引用可以通过销毁VideoFrameRef 对象，或通过调用   VideoFrameRef  得release()方法来释放引用。当真实得数据得所有引用被释放后，实际数据才会自动释放。
- 获得VideoFrameRef  对象的常用方法是通过调用VideoFrameRef :ReadFrame()。
- 将VideoFrameRef  的所有数据引用存储为像素阵列。每个像素将根据已配置的像素格式键入的类型（请参见VideoMode  ）。





### openni::VideoStream

- VideoStream对象封装来自设备的单个视频流。创建后，将其用于启动数据流并读取各个帧的数据。
- 这是用于在OpenNi中获取数据的中心类。它提供在轮询循环中手动读取数据的能力，以及提供可被用于实现事件驱动的数据采集。
- 除了视频数据帧本身之外，类提供了用于获得关于VideoStream信息的多个函数。
- @REF视频流。可以全部获得视场、可用视频模式和最小和最大有效像素值。除获取数据外，@ref视频流对象用于设置应用于特定的所有配置属性流(而不是整个设备)。特别是，它用于控制裁剪、镜像和视频模式。指向提供所需的流类型的有效的、已初始化的设备的指针需要创建流。可以创建若干视频流来从相同的传感器流数据。如果应用程序的多个组件需要单独读取帧。而一些设备可能允许不同的流,从相同的传感器到具有不同的配置,大多数设备将具有用于传感器的单一配置,由所有流共享。*//



### openni::Device

- 该设备对象抽象特定的设备；或者是单个硬件设备，或者是从硬件设备中保存记录的文件设备。
- 它提供了连接到设备的能力，并获得有关其配置和它可以提供的数据流的信息。
- 它提供了查询和更改应用于整个设备的所有配置参数的方法。这包括启用深度/彩色图像配准和帧同步。
- 设备在创建和初始化VideoStream “VideoStreams”时使用-您需要一个指向设备的有效指针才能使用VideoStream.create()函数。这与配置一起，是应用程序开发人员对该类的主要使用。
- 在创建设备之前，必须运行OpenNI：initialization()才能使系统上的设备驱动程序对API可用。

### openni::CameraSettings

### openni::PlaybackControl

- PlaybackControl类提供对一系列特定于播放录制文件的访问。
- 当播放从记录返回的流，而不是从现场设备播放时，*可以改变播放速度，更改当前时间位置(即：快进/倒带/查找)，指定是否应在记录的末尾*重复播放，并查询记录的总大小。
- 由于这些功能在物理设备的上下文中都没有意义，所以它们被分割成单独的播放控制类。
- 要使用，只需创建文件设备，创建PlaybackControl，然后将PlaybackControl附加到文件设备。



### openni::CoordinateConverter

用于在不同坐标系之间转换。



## API示例



```c++
#include <stdio.h>
#include <OpenNI.h>

#include "OniSampleUtilities.h"

#define SAMPLE_READ_WAIT_TIMEOUT 2000 //2000ms

using namespace openni;

int main(){
    // OpenNI 的初始化， 该方法必须调用，在此之后才能使用Videostream、 Device等
    Status rc = OpenNI::initialize();
    if (rc != STATUS_OK){
        printf("Initialize failed\n%s\n", OpenNI::getExtendedError());
        return 1;
    }

    // 打开一个设备，这里的ANY_DEVICE为打开系统中连接的第一个设备
    Device device;
    rc = device.open(ANY_DEVICE);
    if (rc != STATUS_OK){
        printf("Couldn't open device\n%s\n", OpenNI::getExtendedError());
        return 2;
    }

    VideoStream depth;
    // 打开设备后，获取传感器信息，然后根据传感器信息创建视频流
    if (device.getSensorInfo(SENSOR_DEPTH) != NULL){
        // 创建一个深度视频流
        rc = depth.create(device, SENSOR_DEPTH);
        if (rc != STATUS_OK){
            printf("Couldn't create depth stream\n%s\n", OpenNI::getExtendedError());
            return 3;
        }
    }

    // 调用start方法开始采集深度信息
    rc = depth.start();
    if (rc != STATUS_OK){
        printf("Couldn't start the depth stream\n%s\n", OpenNI::getExtendedError());
        return 4;
    }

    VideoFrameRef frame;

    while (!wasKeyboardHit()){
        int changedStreamDummy;
        VideoStream* pStream = &depth;

        // 采用轮询方式获取码流信息
        rc = OpenNI::waitForAnyStream(&pStream, 1, &changedStreamDummy, SAMPLE_READ_WAIT_TIMEOUT);
        if (rc != STATUS_OK) {
            printf("Wait failed! (timeout is %d ms)\n%s\n", SAMPLE_READ_WAIT_TIMEOUT, OpenNI::getExtendedError());
            continue;
        }

        // 读取一帧数据
        rc = depth.readFrame(&frame);
        if (rc != STATUS_OK) {
            printf("Read failed!\n%s\n", OpenNI::getExtendedError());
            continue;
        }

        if (frame.getVideoMode().getPixelFormat() != PIXEL_FORMAT_DEPTH_1_MM && frame.getVideoMode().getPixelFormat() != PIXEL_FORMAT_DEPTH_100_UM){
            printf("Unexpected frame format\n");
            continue;
        }

        // 获取深度图像中心点的深度值
        DepthPixel* pDepth = (DepthPixel*)frame.getData();
                float x,y,z;
                CoordinateConverter coorvert; 

        int middleIndex = (frame.getHeight()+1)*frame.getWidth()/2;

                coorvert.convertDepthToWorld(depth, frame.getWidth()/4, frame.getHeight()/4, pDepth[middleIndex], &x, &y, &z);

        printf("[%08llu] %8d %f %f %f\n", (long long)frame.getTimestamp(), pDepth[middleIndex], x, y, z);
    }

    // 停止视频采集后关闭相关设备
    depth.stop();
    depth.destroy();
    device.close();
    OpenNI::shutdown();

    return 0;
}
```





## 参考类

1. [OpenNI2编程说明 ](https://blog.csdn.net/weixin_43496525/article/details/84728415)