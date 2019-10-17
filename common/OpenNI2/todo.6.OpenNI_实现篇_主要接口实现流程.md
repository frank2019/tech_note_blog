

## 目标

本文主要描述 主要接口得调用流程。



## OpenNI::initialize()

- 用于初始化openni库
- 用于加载所有存在得驱动，同时查看哪一个设备存在。
- 禁止在调用此函数之前调用库得其他函数。



### 流程

- OpenNI::initialize()

- oniInitialize(ONI_API_VERSION)

- g_Context.initialize();
  - Context::resolvePathToOpenNI()   获取当前程序得运行目录存在在m_pathToOpenNI
  - rc = configure();    通过配置文件ini获取配置： m_driversList，日志情况
  - loadLibraries()；   依次遍历加载驱动库，加入到驱动链表 m_deviceDrivers。每个驱动注册回调事件(设备连接 断开  状态变化)
  - oniDriverInitialize()





该函数主要的一个主要功能是枚举 usb 设备，在 windows 下是通过注册表中读取每个
usb 设备的信息和 我们保存 PID， VID 的设备 List 进行比较，对设备进行枚举，枚举到的
设备保存在 Hash 链表 ms_devices。 



## device.open(ANY_DEVICE)

打开设备

```c++
	Device device;
	rc = device.open(ANY_DEVICE);
	if (rc != STATUS_OK)
	{
		printf("Couldn't open device\n%s\n", OpenNI::getExtendedError());
		return 2;
	}
```



- device.open(ANY_DEVICE)
- Status Device::open(const char* uri)
- OniStatus oniDeviceOpen(const char* uri, OniDeviceHandle* pDevice)
- OniStatus oniDeviceOpenEx(const char* uri, const char* mode, OniDeviceHandle* pDevice)
- g_Context.deviceOpen(uri, mode, pDevice);
  - 如果m_overrideDevice不为空，则使用m_overrideDevice
  - 如果  deviceURI为null，则使用设备列表中得第一个设备，否则根据url 遍历获得设备。
  - pMyDevice->open(mode)  -->  回调到设备驱动函数： (*funcs.oniDriverDeviceOpen)(uri, mode);



## device.getSensorInfo(SENSOR_DEPTH)

通过SensorType   获取指定sensor info 信息，null代表不存在。



- SensorInfo* getSensorInfo(SensorType sensorType)
- 遍历获取。



## depth.create(device, SENSOR_DEPTH)

在指定设备上创建指定type得流



- Status VideoStream::create(const Device& device, SensorType sensorType)
- OniStatus oniDeviceCreateStream(OniDeviceHandle device, OniSensorType sensorType, OniStreamHandle* pStream)
  - g_Context.createStream(device, sensorType, pStream)
  - 1. VideoStream* pMyStream = pDevice->createStream(sensorType); 
    2. pMyStream->setNewFrameCallback(newFrameCallback, this); 注册新帧回调事件
  3. pMyStream->setFrameHolder(pFrameHolder);   为pMyStream  分配一个pFrameHolder
    4. 添加pMyStream到列表
  
- m_pCameraSettings = new CameraSettings(this);  如果支持STREAM_PROPERTY_AUTO_EXPOSURE 和STREAM_PROPERTY_AUTO_WHITE_BALANCE 则创建 m_pCameraSettings 



## depth.start();



- Status VideoStream::start()
- OniStatus oniStreamStart(OniStreamHandle stream)
- stream->pStream->start();
- OniStatus VideoStream::start()
  1. 根据标志位m_started 配段是否已经启动过
  2. 清除m_pFrameHolder中得数据帧
  3. OniStatus rc = m_driverHandler.streamStart(m_pSensor->streamHandle());  打开驱动中注册得streamStart方法。
  4. void Device::refreshDepthColorSyncState()





## waitForAnyStream()

等待直到给定得流中有数据帧到来。

- VideoStream** pStreams  跟定得数据流数组
- int streamCount 数据流得个数
-  int* pReadyStreamIndex   输出 第几个数据流有数据了
- int timeout = TIMEOUT_FOREVER  超时时间。



```c++
static Status waitForAnyStream(VideoStream* pStreams, int streamCount, int pReadyStreamIndex, int timeout = TIMEOUT_FOREVER)
```



- OniStatus oniWaitForAnyStream(OniStreamHandle* pStreams, int streamCount, int* pStreamIndex, int timeout)
- g_Context.waitForStreams(pStreams, streamCount, pStreamIndex, timeout);
  - 如果设置了自动录制还没启动，则启动自动录制
  - 遍历直到有事件发生。



## depth.readFrame(&frame)

```c++
Status readFrame(VideoFrameRef* pFrame)
```



- OniStatus oniStreamReadFrame(OniStreamHandle stream, OniFrame** pFrame)

- g_Context.readFrame(stream, pFrame);

  - OniStatus rc = waitForStreams(&stream, 1, &streamIndex, ONI_TIMEOUT_FOREVER);

  - pStream->pStream->readFrame(pFrame);

    

## frame.getVideoMode().getPixelFormat()

```
if (frame.getVideoMode().getPixelFormat() != PIXEL_FORMAT_DEPTH_1_MM && frame.getVideoMode().getPixelFormat() != PIXEL_FORMAT_DEPTH_100_UM){
...
}
```

获取帧得数据格式





## 释放资源

```c++
	depth.stop();
	depth.destroy();
	device.close();
	OpenNI::shutdown();
```

