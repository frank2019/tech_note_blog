

## Context

上下文，

oni::implementation::Context g_Context;

中心管家，大部分得操作都是通过它来实现

```c++
class Context
{
public:
	Context();
	~Context();
	//初始化，主要进行加载驱动操作
	OniStatus initialize();
	//反初始化
	void shutdown();
	//注册/反注册 回调事件  设备连接断开 状态改变
	OniStatus registerDeviceConnectedCallback(OniDeviceInfoCallback handler, void* pCookie, OniCallbackHandle& handle);
	void unregisterDeviceConnectedCallback(OniCallbackHandle handle);
	OniStatus registerDeviceDisconnectedCallback(OniDeviceInfoCallback handler, void* pCookie, OniCallbackHandle& handle);
	void unregisterDeviceDisconnectedCallback(OniCallbackHandle handle);
	OniStatus registerDeviceStateChangedCallback(OniDeviceStateCallback handler, void* pCookie, OniCallbackHandle& handle);
	void unregisterDeviceStateChangedCallback(OniCallbackHandle handle);

    //获取设备列表
	OniStatus getDeviceList(OniDeviceInfo** pDevices, int* pDeviceCount);
    //释放设备列表
	OniStatus releaseDeviceList(OniDeviceInfo* pDevices);

    //打开设备  关闭设备
	OniStatus deviceOpen(const char* uri, const char* mode, OniDeviceHandle* pDevice);
	OniStatus deviceClose(OniDeviceHandle device);
	//从指定设备上获取sensor info
	const OniSensorInfo* getSensorInfo(OniDeviceHandle device, OniSensorType sensorType);

	OniStatus createStream(OniDeviceHandle device, OniSensorType sensorType, OniStreamHandle* pStream);
	OniStatus streamDestroy(OniStreamHandle stream);

	const OniSensorInfo* getSensorInfo(OniStreamHandle stream);

	OniStatus readFrame(OniStreamHandle stream, OniFrame** pFrame);

	void frameRelease(OniFrame* pFrame);
	void frameAddRef(OniFrame* pFrame);

	OniStatus waitForStreams(OniStreamHandle* pStreams, int streamCount, int* pStreamIndex, int timeout);

	OniStatus enableFrameSync(OniStreamHandle* pStreams, int numStreams, OniFrameSyncHandle* pFrameSyncHandle);
	OniStatus enableFrameSyncEx(VideoStream** pStreams, int numStreams, DeviceDriver* pDriver, OniFrameSyncHandle* pFrameSyncHandle);
	void disableFrameSync(OniFrameSyncHandle frameSyncHandle);

	void clearErrorLogger();
	const char* getExtendedError();

	void addToLogger(const XnChar* cpFormat, ...);

    OniStatus recorderOpen(const char* fileName, OniRecorderHandle* pRecorder);
    OniStatus recorderClose(OniRecorderHandle* pRecorder);
    OniStatus recorderClose(Recorder* pRecorder);

	static OniBool s_valid;
protected:
	OniStatus streamDestroy(VideoStream* pStream);
	static void ONI_CALLBACK_TYPE deviceDriver_DeviceConnected(Device* pDevice, void* pCookie);
	static void ONI_CALLBACK_TYPE deviceDriver_DeviceDisconnected(Device* pDevice, void* pCookie);
	static void ONI_CALLBACK_TYPE deviceDriver_DeviceStateChanged(Device* pDevice, OniDeviceState deviceState, void* pCookie);

private:
	Context(const Context& other);
	Context& operator=(const Context&other);

	XnStatus resolvePathToOpenNI();
	XnStatus configure();
	XnStatus resolveConfigurationFile(char* strConfigurationFile);
	XnStatus loadLibraries();
	void onNewFrame();
	XN_EVENT_HANDLE getThreadEvent();
	static void XN_CALLBACK_TYPE newFrameCallback(void* pCookie);

	FrameManager m_frameManager;

	xnl::ErrorLogger& m_errorLogger;

	xnl::Event1Arg<const OniDeviceInfo*> m_deviceConnectedEvent;
	xnl::Event1Arg<const OniDeviceInfo*> m_deviceDisconnectedEvent;
	xnl::Event2Args<const OniDeviceInfo*, OniDeviceState> m_deviceStateChangedEvent;

	xnl::List<oni::implementation::DeviceDriver*> m_deviceDrivers;
	xnl::List<oni::implementation::Device*> m_devices;
	xnl::List<oni::implementation::VideoStream*> m_streams;
    xnl::List<oni::implementation::Recorder*> m_recorders;

	xnl::Lockable<xnl::List<OniStreamHandle> > m_streamsToAutoRecord;
	XnBool m_autoRecording;
	XnBool m_autoRecordingStarted;
	OniRecorderHandle m_autoRecorder;

	xnl::Hash<XN_THREAD_ID, XN_EVENT_HANDLE> m_waitingThreads;

	xnl::CriticalSection m_cs;

	char m_pathToOpenNI[XN_FILE_MAX_PATH];
	char m_overrideDevice[XN_FILE_MAX_PATH];
	char m_driverRepo[XN_FILE_MAX_PATH];
	xnl::Array<xnl::FileName> m_driversList;

	int m_initializationCounter;
	XnUInt64 m_lastFPSPrint;

};
```







## StreamFrameHolder

```c++
class StreamFrameHolder : public FrameHolder
{
public:

	// Constructor.
	StreamFrameHolder(FrameManager& frameManager, VideoStream* pStream);

	// Destructor.
	virtual ~StreamFrameHolder();

	// Get the next frame belonging to a stream.
	virtual OniStatus readFrame(VideoStream* pStream, OniFrame** pFrame);

	// Process a newly received frame.
	virtual OniStatus processNewFrame(VideoStream* pStream, OniFrame* pFrame);
	
	// Peek at next frame.
	virtual OniFrame* peekFrame(VideoStream* pStream);

	// Clear all the frame in the holder.
	virtual void clear();

	// Return list of streams which are members of the stream group.
	virtual void getStreams(VideoStream** ppStreams, int* pNumStreams);

	// Return number of streams which are members of the stream group.
	virtual int getNumStreams();

	//
	virtual void setStreamEnabled(VideoStream* /*pStream*/, OniBool /*enabled*/);

private:

	VideoStream* m_pStream;

	OniFrame* m_pLastFrame;
};
```



## Device