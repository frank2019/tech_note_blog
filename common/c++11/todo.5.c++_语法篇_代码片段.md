

## 使用XN_NEW 创建对象

```c++
#if XN_PLATFORM_VAARGS_TYPE == XN_PLATFORM_USE_WIN32_VAARGS_STYLE
	#define XN_NEW(type, ...)		new type(__VA_ARGS__)
#elif XN_PLATFORM_VAARGS_TYPE == XN_PLATFORM_USE_GCC_VAARGS_STYLE
	#define XN_NEW(type, ...)		new type(__VA_ARGS__)
#elif XN_PLATFORM_VAARGS_TYPE == XN_PLATFORM_USE_ARC_VAARGS_STYLE
	#define XN_NEW(type, arg...)	new type(arg)
#else
	#define XN_NEW(type, arg)		new type(arg)
#endif

#define XN_NEW_ARR(type, count)		new type[count]
#define XN_DELETE(p)				delete (p)
#define XN_DELETE_ARR(p)			delete[] (p)
```

```c++
DeviceDriver* pDeviceDriver = XN_NEW(DeviceDriver, m_driversList[i].getData(), m_frameManager, m_errorLogger)
```

通过指定type及参数，创建对象。