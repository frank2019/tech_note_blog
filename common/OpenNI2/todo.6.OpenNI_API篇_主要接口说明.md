

# Openni API 接口编程说明



## 高级API的四个主要类：

-  **openni::OpenNI** – 提供一个单一静态的API入口点。同时提供访问设备的途径，设备相关的事件，版本及错误信息。被用来建立与Device的连接。
-  **openni::Device** – 提供连接到系统的单一传感器设备的接口。 在被创建前要求OpenNI先进行初始化。 Devices提供访问Streams的途径。
- **openni::VideoStream** – 抽象化一个单一视频流。从一个特定的Device中获取。用来获取VideoFrameRefs
- **openni::VideoFrameRef** – 抽象化一个单一视频元数据（meta-data）并和其相关。从一个特定的Stream获取。

 

##  支援类：

 **Recorder**：用来把OpenNI视频流储存到文件
 **Listener Classes**（多个）：监听OpenNI和Stream产生的事件。

 

 

##  OpenNI 类

### 设备(Device)基本访问：

 OpenNI类提供到API的静态入口点——**OpenNI::initialize()**：这个函数初始化所有可用的传感器驱动，并扫描系统寻找可用设备。任何使用OpenNI的应用程序都应在最初调用此函数。一旦执行过初始化函数，就可以创建Device对象了，并用它们和真实的传感器硬件进行通信。

 **OpenNI::enumerateDevices()**：返回一个所有连接系统的可用设备的列表。

 **OpenNI::shutdown()**：当应用程序准备退出时，这个函数应被调用关闭所有驱动并作适当清理。

 

###  *到视频流（**Video Streams**）的基本访问：

 访问（视频）流的轮询（polling）系统可通过**OpenNI::waitForAnyStream()**实现：该函数用一个流列表作为传入参数之一。当被调用时，它进行阻塞直到列表中的任一流有新的可用数据。然后它会返回一个状态码并说明是哪个流有可用数据。这个函数可用来实现一个关于新的可用数据的轮询循环。

 

###  *到设备（**Device**）的事件驱动的访问：

 OpenNI类提供一个以事件驱动方式访问设备的框架。它定义了三种事件：

 **onDeviceConnected**：当一个新的设备通过OpenNI接入且可用是产生
 **onDeviceDisconnected**：从系统中移除某一设备时产生
 **onDeviceStateChanged**：当设备的设置放生变动时产生

 

 监听类可通过以下方法被添加到事件句柄列表或被移除：

```bash
OpenNI::addDeviceDisconnectedListener() OpenNI::addDeviceDisconnectedListener() OpenNI::addDeviceStateChangedListener() OpenNI::removeDeviceConnectedListener() OpenNI::removeDeviceDisconnectedListener() OpenNI::removeDeviceStateChangedListener()
```



 以上三种事件均提供一个指向**openNI::DeviceInfo**对象的指针。这个对象可用来获取事件相关设备的的细节并对设备进行鉴别。另外，**onDeviceStateChanged**事件还提供一个指向**DeviceState**对象的指针，可用来查看设备的新状态。

 

###  *错误信息：

 当错误发生时，类型**Status**会包含一段可记录进日志或显示给用户查看的代码。

 **OpenNI::getExtendedError()**：返回一段额外的，人为可读的错误信息。

 

###  *版本信息：

 通过**OpenNI::getVersion()**返回。

 

 

##  **Device** **类**

 可通过驱动提供单一物理硬件设备的接口，也可通过从物理设备录制的ONI文件提供模拟硬件设备的接口。主要目的是提供Streams。

###  *接入设备的先决条件：

 硬件设备必须物理地接入PC且驱动已安装；如果是用ONI文件，只需ONI记录在运行应用程序的系统上可用，且这个应用程序有可以访问读取该文件。

 接入任何设备前需调用**OpenNI::waitForAnyStream()**。

 

###  *基本操作：

 构建函数：不需要传参，也不连接设备。单纯创建一个对象。

 **Device:open()**：实际负责连接硬件设备的函数，传入一个参数——设备的URI。返回指示操作成功或所发生错误的状态码。

 最简单的用法是传入**openni::ANY_DEVICE**作为URI。使用这个参数会让系统连接任何激活中的硬件设备。当系统上恰好仅有一个激活硬件设备时最为实用。

 如果系统上有多个传感器，则需要先调用**OpenNI::enumerateDevices()**获得所有激活设备的列表。找到想要的设备，用**DeviceInfo:getUri()**获得它的URI。将这个函数的输出作为**Device:open()**的参数打开具体的设备。

 如果是要打开文件则需要传入.ONI文件的路径。

 

 **Device:close()**：关闭硬件设备，作为良好的习惯所有打开的设备最后都应关闭。

 

 **Device:isValid()**：用来判断当前是否存在一个激活设备连接这个Device对象。

 

###  *从Device获取信息：

 可获取信息包括name、 vendor string、 uri、和USB VID/PID。**openni::DeviceInfo**类包含以上所有信息，通过待用**Device:getDeviceInfo()**获得。

 一个设备可能含有N个传感器。比如PrimeSense设备含一个IR传感器，颜色传感器和深度传感器。Streams可在任何一个既存的传感器上打开。

 

 **Device:hasSensor()**：用来查询设备是否提供某种传感器，包括：

 **SENSOR_IR**

**SENSOR_COLOR  SENSOR_DEPTH**

 

 **Device:getSensorInfo()**：用来获取想要的传感器信息，封装在一个**SensorInfo**对象里。可获取传感器类型，和一个包含所有可用视屏模式（video modes）的数组。每个视屏模式被封装在**VideoMode**类里。

 

###  *具体设备能力

 **注册：

 同时提供深度和色彩图像流的设备，一般会使用两个不同的物理相机，它们往往存在于空间中两个分离的点，而其中一张图像中的物体会明显有别于另一张中的同一物体。需要用数学变换的方式让其中一张看起来和另一张拥有相同的拍摄点。这样就可实现将两张图像进行重叠，好比从彩色图像中提取每个像素的RGB信息放入深度图像。这个过程即所谓的**注册（Registration）**。

 有些设备的硬件既有能力进行计算，连同所需的校正参数一起。若有这方面能力，则硬件上会有一个flag来开启或关闭它。

 Device对象提供**isImageRegistrationSupported()**来测试接入设备是否支持注册。支持的话，

 **getImageRegistrationMode()**：查询这个特性的当前状态
 **setImageRegistrationMode()**：设置为特定值

 可传值由枚举类型**openni::ImageRegistrationMode**给出：

 IMAGE_REGISTRATION_OFF – 停用注册特性
 IMAGE_REGISTRATION_DEPTH_TO_IMAGE – 使深度图像变换为何RGB图像具有相同视角

 

 注意两个传感器的视野范围存在不重叠部分，启用以上特性则深度图有一侧不会被显示在最后结果上。除此之外，在深度几何中突然出现的边（sudden edges）也会在深度图上显示成“影子”或“洞”（This is caused by the fact that objects are “shifted” by a different amount depending on their distance from the camera. This may result in a faraway object being moved more than an adjacent nearby object, leaving a space between them where no depth information is available）。

 

###  **帧同步：

 两个设备视屏流产生的帧很可能不同步，反映在帧率上有轻微差异，或帧到达时间存在较小的相位差。有些硬件有能力使两帧保持同步，利用**setDepthColorSyncEnabled()**来启用或停用这一特性。

 

###  **其他能力：

 除了以上两种特性外，可通过**setProperty()**和**getProperty()**来激活硬件设备所具有的其他特性。传参对应属性的数字ID即可。

 

###  *文件设备

 设备上所有流输出均可记录在一种.oni文件中。使用ONI文件和使用物理传感器没有明显区别。文件输入非常适用于算法调试，测试等。

 **PlaybackControl**类是用来访问文件设备的各种**文件限定功能**的，使用前用**Device::isFile()**来确定当前Device是否是由文件创建。

 

##  **PlaybackControl** **类**

 封装了一些仅能对文件设备使用的**文件限定功能**：

###  *初始化：

 先要从文件创建一个Device实例并初始化，之后就可利用**Device::getPlaybackControl()**获取它内部的**PlaybackControl**对象。

 

###  *查找：

 **PlaybackControl::seek()**：传入一个**VideoStream**指针和一个frameID。设置从指定帧处为记录回放（playback）。如果记录中有多个流，所有的流都会被设置到和指定流一样的时间点——输入流仅用来提供frameID的内容。

 **PlaybackControl::getNumberOfFrames()**：用来获得记录长度。主要用来获得查找函数的有效目标。传参一个流指针，返回记录中指定流的帧数。注意一个记录中的不同流是可以拥有不同的帧数的，因为它们的帧并不总保持同步。

 

###  *回放速度：

 记录的回放速度是可变的。在使用大量数据测试算法时很实用，因为可以更快地获取结果。

 **PlaybackControl::setSpeed()**：传入一个浮点型，代表想要回放速度的倍数（For example, if a recording was of a 30fps stream, and a value of 2.0 was passed to setSpeed(), then the stream would play back at 60fps. If a value of 0.5 was passed, the stream would play back at 15fps）。

 当设置速度为0.0时则会以主系统力所能及的最快速度运行；设为-1则允许手动读取流——即向应用程序读入一帧，流就暂停一次。设为手动模式并采用紧凑循环的方式读取会获得和设为0.0类似的效果。设为0.0主要用于事件驱动的数据读取。

 **PlaybackControl::getSpeed()**：返回最近设置（激活）的速度

 

###  *回放循环：

 用来应对记录中仅有有限帧，无法模拟持续提供数据的物理传感器的问题。

 **PlaybackControl::setRepeatEnabled()**：开启或关闭循环

 **PlaybackControl::getRepeatEnabled()**：用来查询当前循环状态

 

 

##  **VideoStream 类**

 封装Device类创建的所有数据流。允许请求让特定的数据流开始，停止或进行设置。还允许对流（与Device相反）级别上存在的参数进行设置。

 *基本功能

 **创建和初始化

 调用缺省构造函数可创建一个空的，未初始化的VideoStream对象，在使用前必须用**VideoStream::create()**进行初始化，该函数要求一个有效的初始化过的设备。创建后需用**VideoStream::start()**来开始数据流。而**VideoStream::stop()**则用于停止数据流。

 

 **基于轮询的数据读取：

 **VideoStream::readFrame()**：直接读取数据。如果有新的可用数据，则可访问最近VideoStream产生的VideoFrameRef。当新帧还未准备好时，此函数阻塞。注意对于未开启循环的文件设备，这个函数在读完最后一帧后永久阻塞。

 

 **基于事件的数据读取：

 需要用**VideoStream::Listener**类扩展出一个新类，这个类应实现一个叫做**onNewFrame()**的函数。创建并实例化这个类后，把它传给**VideoStream::addListener()**。当有新的可用帧时，**onNewFrame()**就会被调用。仍需要调用**readFrame()**。

 

 *获取VideoStream的信息

 **VideoMode类**：封装了帧率，分辨率和VideoStream的像素格式

 **SensorInfo类**：包含产生VideoStream的传感器类型，并包含一个VideoMode对象列表——每个都含有流的有效参数组。通过对这些对象进行迭代，可确定产生所给VideoStream的传感器的所有模式。

 

 **视野域（FOV）：

 **getHorizontalFieldOfView() getVerticalFieldOfView()**

 单位是弧度

 

 **最小/最大像素值：

 **getMinPixelValue() getMaxPixelValue()**

 

 *设置VideoStream

 **视屏模式

 **setVideoMode()**：可设置帧率，分辨率和所给流的像素格式。使用前需先获得SensorInfo以选取有效的VideoMode。

 

 **裁剪（Cropping）

 **VideoStream::isCroppingSupported()**：获取传感器是否支持裁剪，当支持时：

 **setCropping()**：启用裁剪并进行想要的设置

 **resetCropping()**：重置裁剪

 **getCropping()**：获取当前裁剪设置

 

 **镜像（Mirroring）

 使图像像素全体垂直翻折。

 setMirroringEnabled()：镜像设置，TRUE启用，FALSE停用
 getMirroringEnabled()：获取当前镜像设置

 

 **其他属性

 在固件（firmware）层级，多数传感器的设置被存为【地址/值】的形式。可直接通过**setProperty**和 **getProperty**进行操作。

 

 --**VideoFrameRef 类**

 封装了从VideoStream中读取的单一帧的所有相关数据。是VideoStream用来返回新帧的基本类。提供访问含有帧数据的底层数组（underlying array）的途径，同时还有操作帧所需的元数据。通过调用**VideoStream::readFrame()**返回VideoFrameRef对象。

 **getSensorType()**：获取产生当前帧的传感器类型

 

 *访问帧数据：

 VideoFrameRef::getData()：返回一个直接指向底层帧数据的指针（void类型），需要用各个像素的数据类型进行强制转换来建立合适的索引。

 

 *元数据：

 每一帧都提供元数据的几个项目来促进对数据的操作。

 

 *裁剪数据：

 可确定裁剪窗口的原点，裁剪窗口的大小，还有产生当前帧时裁剪是否被启用：

 **getCropOriginX()**

 **getCropOriginY()**

 **getCroppingEnabled()**

 当裁剪启用时，裁剪窗口的大小等于帧大小（分辨率）

 

 *时间戳（TimeStamp）：

 每一帧数据都具有一个时间戳，此值以微妙为单位从一些假定零点开始记录。同流中两帧的时间戳的差即为两帧之间的时间差。同一设备中的所有流可保证使用同一零点，所以不同流间的帧也可通过事件戳对比。（OpenNI 2.0的实现中以流的第一帧作为时间零点）

 

 *帧索引：

 用来确定帧的序列，也可用来获知两帧之间间隔了多少帧。如果两个流已用**Device::setColorDepthSync()**进行过同步，则可确保用帧索引关联的两帧互相匹配。反之则不能保证，这时最后用时间戳来确定帧之间的关系。

 

 *视屏模式：

 **VideoFrameRef::getVideoMode()**：用来获取当前帧被创建时的视屏模式设置。包括图像的像素格式，分辨率及相机拍下图像时的帧率。

 

 *数据大小：

 **getDataSize()**：获取图像数组中所含全部数据的大小

 **VideoMode::getPixelFormat()**：获取单一数组元素的大小

 

 *图像分辨率：

 可同过以下方式获得

 **getHeight()**

 **getWidth()**

 或

 **VideoFrameRef::getVideoMode().getResolutionX()**

 **VideoFrameRef::getVideoMode().getResolutionY()**

 注意后者略显冗余且不效率

 

 *数据有效性：

 **The VideoFrameRef::isValid()**

 如果在初始构造VideoFrameRef和从真实的VideoStream载入第一个时间数据之间调用这个函数会返回false。

 

 *传感器类型：

 **getSensorType()**：返回用来产生帧的传感器类型，可为：

**SENSOR_IR**

**SENSOR_COLOR SENSOR_DEPTH**

 

 *数组跨距（Stride）：

 数组的跨距含有可由**getStrideInBytes()**获取的帧。提供了以bytes为单位的数据数组每行的大小。主要用于对图像数据进行二维索引。

 

##  **Recorder 类**

 用来将VideoStream数据转录入ONI文件。ONI文件可包含一个或多个流信息，也包含用来创建这些信息的设备设置

 

 *设置recorder

 1.调用缺省构造函数进行实例化

 2.调用**Recorder::create()**并提供一个转录用的文件名。任何创建和写入错误均会作为状态码由

 **create**函数返回

 3.利用**Recorder::attach()**提供要转录的数据流。如果要记录多个流，则多次调用**attach**函数即可

 

 *转录

 **Recorder::start()**：调用后所有流产生的帧均会被写入ONI文件
 **Recorder::stop()**：完成转录
 **Recorder::destroy()**：释放recorder的内存并保证文件被适当地写入到了硬盘

 

 

--支援**类**

 *传感器设置类：

 **DeviceInfo**：记录设备名称，URI，USB VID/PID描述子和供应商名称

 
 **SensorInfo**：存储适用于给定传感器的设置。传感器可以是IR相机，RGB相机，或深度相机
 
 **VideoMode**：存储一帧的分辨率，帧率和像素格式
 
 **CameraSettings**：存储RGB相机的设置。允许启用/停用自动白平衡和自动曝光

 

*数据存储类/结构体

 **Version**：存储软体版本

 **RGB888Pixel**：存储一个单色像素值

 **Array**：由原始数组扩展来存储图像数据

 **Coordinate Conversion**：用来转换真是世界和深度坐标



## 参考链接

1. [OpenNI Programmer's Guide](http://com.occipital.openni.s3.amazonaws.com/OpenNI_Programmers_Guide.pdf)