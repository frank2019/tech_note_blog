



# What's New for Media Foundation

- 05/31/2018
- 4 minutes to read

Microsoft Media Foundation 在 Windows Vista 时代作为 DirectShow  的替代品出现。当然，在 Windows 7 中仍然支持DirectShow，但是建议开发者在开发新的数字媒体应用程序时使用 Media  Foundation。

Media Foundation 的改进可归纳如下：

- 更好的格式支持，包括 MPEG-4
- 支持捕捉设备和硬件编解码器
- 编程模型简单
- 平台的改进（？）

## 更好的格式支持

Media Foundation 的音视频管线在 Windows Vista  中就已经实现，但那时候仅仅支持有限的一些编码格式和文件封装格式，这就意味着有些程序还需要用回像 DirectShow 这种旧的技术。在  Windows 7 中，Media Foundation 包括了以下这些新的codecs， media sources，和 media  sinks:

- AAC decoder
- AAC encoder
- AVI/WAVE file source
- DV video decoder
- H.264 video decoder
- H.264 video encoder
- MJPEG decoder
- MP3 file sink*
- MP4/3GP file source
- MP4/3GP file sink

 注意

MP3 file sink 不包括 MP3 audio 编码器.

 

更多相关信息， [Supported Media Formats in Media Foundation](https://docs.microsoft.com/en-us/windows/desktop/medfound/supported-media-formats-in-media-foundation).

## 硬件设备支持

Media Foundation 现在 audio/video pipeline 在中支持以下几种硬件设备：

- UVC 1.1 视频捕捉设备，例如摄像头
- 音频捕捉设备
- 硬件编码器和解码器
- 其他视频图像处理硬件， 例如 color-space converters

硬件编解码器可以非常快地进行视频转码。例如，（后面废话不翻了）

硬件设备在 Media Foundation 被包装成 proxy object，然后在 pipeline 中使用时就像使用其他普通组件一样。

## Simplified Programming Model

在 Windows Vista 时，Media Foundation  暴露了一些比较底层的API。虽然这些API很灵活，但对于一些简单的任务来说还是太过复杂了。Windows 7 中增加了一些新的封装好的  API，这使得用C++开发媒体应用程序简单了很多。这些新的 API 包括以下：

| API                                                          | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Source Reader](https://docs.microsoft.com/en-us/windows/desktop/medfound/source-reader) | source reader 从媒体文件中获取原始数据或者解码后的数据。例如，你可以从一个视频文件获取 bitmaps 缩略图，或者分析一个音频文件的 waveform 数据。也可以从一个音/视频捕捉设备实时获取数据。 |
| [Sink Writer](https://docs.microsoft.com/en-us/windows/desktop/medfound/sink-writer) | sink writer 可以把传过来的未压缩的数据或者编码后的数据写成媒体文件。例如，你可以用来重新编码一个视频文件，或者把摄像头传过来的实时数据写入文件。 |
| [Transcode API](https://docs.microsoft.com/en-us/windows/desktop/medfound/transcode-api) | 包括了最常见音/视频编码场景。                                |

如果需要对整个流程进行更多控制，则可以继续使用那些底层 API 。

## Platform Improvements

Windows 7 包含了许多对 Media Foundation 底层 API 的增强。这些提升包括：

- 降低了功耗和 video memory 的使用。
- [DXVA-HD](https://docs.microsoft.com/en-us/windows/desktop/medfound/dxva-hd):  Microsoft DirectX Video Acceleration High Definition (DXVA-HD)  是一个新的支持硬件加速的视频处理 API。 DXVA-HD 比之前的 DXVA   API 提供了更灵活的处理方式，而且更适合处理高清视频格式。
- 一种新的机制，用于枚举 sources 和 decoders，包括了权重值和优先/阻止列表，更多信息参考以下主题： 	
  - [**MFTEnumEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfapi/nf-mfapi-mftenumex)
  - [**IMFPluginControl**](https://docs.microsoft.com/en-us/windows/desktop/api/mfobjects/nn-mfobjects-imfplugincontrol)
  - [Codec Merit](https://docs.microsoft.com/en-us/windows/desktop/medfound/codec-merit)

## SDK Changes

- 一些新的头文件和 lib 文件： [Media Foundation Headers and Libraries](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-headers-and-libraries)

- DLL 和 .lib 更改： [Library Changes in Windows 7](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-headers-and-libraries)

- 新的 SDK 示例： 	

  - [Audio Clip Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/audio-clip-sample)
  - [DXVA-HD Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/dxva-hd-sample)
  - [MFCaptureD3D Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/mfcaptured3d-sample)
  - [MFCaptureToFile Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/mfcapturetofile-sample)
  - [Transcode Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/transcode-sample)
  - [VideoThumbnail Sample](https://docs.microsoft.com/en-us/windows/desktop/medfound/videothumbnail-sample)

- TopoEdit

   的改进： 	

  - 支持转码。 See Building a [Transcode Topology with TopoEdit](https://docs.microsoft.com/en-us/windows/desktop/medfound/building-a-transcode-topology-with-topoedit).
  - 支持音/视频捕获。 See [Topology Menu](https://docs.microsoft.com/en-us/windows/desktop/medfound/topology-menu).

## New in Windows 8

Some of the new updates to Media Foundation with Windows 8 are:

- [**IMFCaptureEngine**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengine) 可以控制多个捕捉设备。 在 [Capture Engine Attributes](https://docs.microsoft.com/en-us/windows/desktop/medfound/capture-engine-attributes) 查看属性列表。另外几个新的捕捉设备的接口有 [**IMFCapturePhotoSink**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturephotosink), [**IMFCapturePreviewSink**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturepreviewsink), [**IMFCaptureRecordSink**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturerecordsink), [**IMFCaptureSink**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesink), 和 [**IMFCaptureSource**](https://docs.microsoft.com/en-us/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesource).
- The following Media Foundation class extensions are new for Windows 8: 	
  - [**IMFMediaEngineEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineex)
  - [**IMFMediaSourceEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfidl/nn-mfidl-imfmediasourceex)
  - [**IMFRealTimeClientEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclientex)
  - [**IMFSinkWriterEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterex)
  - [**IMFSourceReaderEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereaderex)
  - [**IMFVideoSampleAllocatorEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorex)
  - [**IMFWorkQueueServicesEx**](https://docs.microsoft.com/en-us/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservicesex)
- [Direct3D 11 Video API](https://docs.microsoft.com/en-us/windows/desktop/medfound/direct3d-11-video-apis) 是 Windows 8 中新加入的。Windows 8 桌面程序仍然可以使用 [Direct3D 9 Video API](https://docs.microsoft.com/en-us/windows/desktop/medfound/direct3d-video-apis)，但是  Windows Store apps 必须使用新的 Direct3D 11 Video API。更多关于 Microsoft Direct3D 11 Video 的信息请查看 [Supporting Direct3D 11 Video Decoding in Media Foundation](https://docs.microsoft.com/en-us/windows/desktop/medfound/supporting-direct3d-11-video-decoding-in-media-foundation).
- Media Foundation 的 work queues 也有一些更新， [Work Queue and Threading Improvements](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-work-queue-and-threading-improvements) for more info.
- [H.264 UVC 1.5 camera encoders](https://docs.microsoft.com/en-us/windows/desktop/medfound/camera-encoder-h264-uvc-1-5).
- 关于 Media Foundation API 列表，可以查看这个 Windows Store apps [Win32 and COM for Windows Store apps (multimedia)](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-headers-and-libraries).
- Windows 8 的 N 和 KN 版本中没有包含 Media Foundation。相关信息 [Microsoft Windows Media Feature Pack for N and KN Versions of all Windows 8 Editions](https://support.microsoft.com/kb/2703761).

## Related topics

[About Media Foundation](https://docs.microsoft.com/en-us/windows/desktop/medfound/about-the-media-foundation-sdk)

[Microsoft Media Foundation](https://docs.microsoft.com/en-us/windows/desktop/medfound/microsoft-media-foundation-sdk)



## 参考链接

1. [(Microsoft Media Foundation官方文档翻译（二）《What's New for Media Foundation》](https://blog.csdn.net/rzdyzx/article/details/86695048)
2. [](https://blog.csdn.net/chenchong_219/article/details/44262905)