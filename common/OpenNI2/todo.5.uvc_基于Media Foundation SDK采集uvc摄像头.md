

## 目标

本文描述基于Media Foundation SDK 实现对uvc摄像头的采集和控制

## 下载SDK

在MSDN官网上去查找 media fundation SDK samples > > video Capture >> MFCaptureToFile>>Downloading the Sample >> windows SDK

链接： [Media Foundation SDK Samples](https://docs.microsoft.com/zh-cn/windows/win32/medfound/media-foundation-sdk-samples)

github地址： https://github.com/microsoft/Windows-classic-samples



Media Foundation SDK   的开发环境     vs2015    windows7 SDK

vs2017  windows10



## Media Foundation  Unit

### Sink Writer

The sink writer is a component for encoding audio or video files.

The following diagram shows, at a high level, how an application uses the sink writer to encode and audio/video file.

![a diagram that shows the sink writer.](https://docs.microsoft.com/zh-cn/windows/win32/medfound/images/encoding09.png)

The sink writer hosts a media sink and optionally one or more  encoders. The encoders convert uncompressed audio or video data to  encoded bitstreams. The media sink outputs the bitstreams to a file. The  sink writer performs the following tasks:

- Loads the media sink.
- Finds and loads the encoders.
- Manages the data flow to the encoders and the media sink.

The application passes audio/video data to the sink writer as input.  It does not matter how the application obtains or generates the input  data. One option is to use the [Source Reader](https://docs.microsoft.com/zh-cn/windows/win32/medfound/source-reader),  as shown in the following diagram. However, the sink writer does not  require the use of the source reader. These two components are  independent.

![a diagram that shows the source reader and sink writer.](https://docs.microsoft.com/zh-cn/windows/win32/medfound/images/encoding02.png)

**In this section**

- [Using the Sink Writer](https://docs.microsoft.com/zh-cn/windows/win32/medfound/using-the-sink-writer)
- [Tutorial: Using the Sink Writer to Encode Video](https://docs.microsoft.com/zh-cn/windows/win32/medfound/tutorial--using-the-sink-writer-to-encode-video)



## Media Foundation SDK API





### MFCreateAttributes

Creates an empty attribute store.

```
HRESULT MFCreateAttributes(
  IMFAttributes **ppMFAttributes,
  UINT32        cInitialSize
);
```

 一个Attribute就是一个“键”-“值”对，其中“键”是一个GUID，“值”是一个PROPVARIANT。在Media Foundation中，Attributes被广泛地用于配置对象、描述媒体格式、查询对象属性和其他目的。

 “值”只能是这7种类型：UINT32、UINT64、64-bits浮点数、GUID、null结尾的宽字符串、字节数组和IUnknown指针，

### MFEnumDeviceSources

用来枚举 符合条件的音频和视频设备

```
HRESULT MFEnumDeviceSources(
  IMFAttributes *pAttributes,
  IMFActivate   ***pppSourceActivate,
  UINT32        *pcSourceActivate
);
```



- pAttributes 指向包含搜索条件的属性存储的指针。若要创建属性存储，请调用MFCreateAttributes。在属性存储上设置一个或多个属性：



### MFCreateSinkWriterFromURL

```c++
HRESULT MFCreateSinkWriterFromURL(
  LPCWSTR       pwszOutputURL,
  IMFByteStream *pByteStream,
  IMFAttributes *pAttributes,
  IMFSinkWriter **ppSinkWriter
);
```

#### Parameters

```
pwszOutputURL
```

A null-terminated string that contains the URL of the output file. This parameter can be **NULL**.

```
pByteStream
```

Pointer to the [IMFByteStream](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream) interface of a byte stream. This parameter can be **NULL**.

If this parameter is a valid pointer, the sink writer writes to the  provided byte stream. (The byte stream must be writable.) Otherwise, if *pByteStream* is **NULL**, the sink writer creates a new file named *pwszOutputURL*.

```
pAttributes
```

Pointer to the [IMFAttributes](https://docs.microsoft.com/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface. You can use this parameter to configure the sink writer. For more information, see [Sink Writer Attributes](https://docs.microsoft.com/windows/desktop/medfound/sink-writer-attributes). This parameter can be **NULL**.

```
ppSinkWriter
```

Receives a pointer to the [IMFSinkWriter](https://docs.microsoft.com/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriter) interface. The caller must release the interface.

#### Return Value

This function can return one of these values.

| Return code        | Description |
| ------------------ | ----------- |
| **S_OK**           | Success.    |
| **MF_E_NOT_FOUND** |             |



### IMFSourceReader::ReadSample method

```cpp
HRESULT ReadSample(
  DWORD     dwStreamIndex,
  DWORD     dwControlFlags,
  DWORD     *pdwActualStreamIndex,
  DWORD     *pdwStreamFlags,
  LONGLONG  *pllTimestamp,
  IMFSample **ppSample
);
```





## 遇到的问题

### LNK2019	无法解析的外部符号 _QISearch

```ini
错误	LNK2019	无法解析的外部符号 _QISearch@16，该符号在函数 "public: virtual long __stdcall CCapture::QueryInterface(struct _GUID const &,void * *)" (?QueryInterface@CCapture@@UAGJABU_GUID@@PAPAX@Z) 中被引用	mf_camera_video	D:\MoreBetter\ffmpeg_with_opencv\demos\FFmpegTest\buildx86\mf_camera_video.obj	1	

```

解决办法

链接时 增加库：

```
Shlwapi.lib
```

### IMFActivate :: ActivateObject返回错误代码“CoInitialize尚未调用。”

在线程中增加 

```
CoInitialize(NULL);
```



https://stackoverrun.com/cn/q/8396042



## 参考链接

1. [media-foundation-programming-guide](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming-guide)
2. [一个清华学子写的关于directshow的学习心得](https://blog.csdn.net/qq_25408423/article/details/81613241)
3. [官方API使用说明](https://docs.microsoft.com/en-us/windows/win32/medfound/processing-media-data-with-the-source-reader)
4. [How to capture raw format image using media foundation?](https://social.msdn.microsoft.com/Forums/vstudio/en-US/c34dd4b0-b677-4223-98f4-69234c7d2968/how-to-capture-raw-format-image-using-media-foundation)
5. [Microsoft Media Foundation官方文档翻译（21）《Media Buffers》](https://www.cnblogs.com/zhangchaosd/p/10680426.html)