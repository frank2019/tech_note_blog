# About Media Foundation

- ‎05‎/‎31‎/‎2018
- 2 minutes to read

Microsoft Media Foundation is the next generation multimedia  platform for Windows that enables developers, consumers, and content  providers to embrace the new wave of premium content with enhanced  robustness, unparalleled quality, and seamless interoperability（废话）.

Media Foundation 要求 Windows Vista 或者更新版本的 Windows。 Media Foundation  使用 C/C++ 的 COM 组件。 Microsoft 没有提供 managed API for Media Foundation.

Media Foundation APIs 包含在 [Windows SDK](https://go.microsoft.com/fwlink/p/?linkid=129787) 里。为了开发 Media Foundation 应用，请安装最新版本的Windows SDK。

## Audio and Video Quality

Media Foundation has been designed to meet the challenges posed by  high-definition content. Audio and video quality enhancements made  throughout the platform now make it possible to deliver a great  experience for next generation high-definition content.（废话）

- DirectX Video Acceleration (DXVA) 2.0 比 DXVA 1.0 相比提供了更高效的视频加速,  具有更强大、更精简的视频解码功能, 并在视频处理中扩展了硬件的使用。使用 dxva  2.0，Windows可以处理一些要求最苛刻的高清内容，具有高质量和更高的故障恢复能力。
- 在整个 video pipeline 中保留色彩空间信息。用户可以欣赏到高质量的视频内容。颜色信息和隔行扫描图像现在被传递到硬件进行单次传递合成。保留色彩空间信息还可以减少不必要的色彩空间转换，从而缩短图像处理时间。
- The enhanced video renderer (EVR) 提供了更好的 timing 支持，增强的视频处理和更高的故障恢复能力。全屏播放支持得到了增强，在窗口模式下的视频撕裂已被最小化。
- Media Foundation 使用 Multimedia Class Scheduler Service (MMCSS)，这是  Windows Vista 中一种新的系统服务。MMCSS使多媒体应用程序能够确保其时间敏感的处理获得对 cpu 资源的优先访问。

## Content Access

随着数字娱乐进入高清时代，内容变得更加便携和无处不在，内容保护将成为数字媒体产品不可或缺的一部分。Media Foundation 的可扩展性确保它能够支持这些趋势。

此外，媒体基础的可扩展性使不同的内容保护系统能够一起运行。

## About Media Foundation

本节包含有关媒体基础 api 的一般信息。详细的编程信息可在媒体基础编程指南中找到。

| Section                                                      | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [What's New for Media Foundation](https://docs.microsoft.com/en-us/windows/desktop/medfound/whats-new-for-media-foundation) | Describes new features in Media Foundation.                  |
| [Media Foundation Headers and Libraries](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-headers-and-libraries) | Lists the header and library files that define the Media Foundation APIs. |
| [Media Foundation Tools](https://docs.microsoft.com/en-us/windows/desktop/medfound/media-foundation-tools) | Describes the development tools that are available for Media Foundation. |

 

Media Foundation is not included with the N and KN editions of Windows 8. For more information, see [Microsoft Windows Media Feature Pack for N and KN Versions of all Windows 8 Editions](https://support.microsoft.com/kb/2703761).