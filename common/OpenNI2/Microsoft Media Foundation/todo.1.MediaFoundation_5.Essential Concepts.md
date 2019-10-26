## Media Foundation: Essential Concepts

如果您是数字媒体的新手，本主题将介绍一些您在编写媒体基础应用程序之前需要理解的概念。

- [Streams](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts#streams)
- [Compression](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts#compression)
- [Media Containers](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts#media-containers)
- [Formats](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts#formats)
- [Related topics](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming--essential-concepts#related-topics)

## Streams 流

流是具有统一类型的媒体数据序列。最常见的类型是音频和视频，但流几乎可以包含任何类型的数据，包括文本、脚本命令和静态图像。本文档中的术语流并不意味着通过网络传递。用于本地播放的媒体文件也包含流。

通常，媒体文件包含单个音频流，或者恰好包含一个视频流和一个音频流。但是，媒体文件可能包含多个相同类型的流。例如，视频文件可能包含几种不同语言的音频流。在运行时，应用程序将选择使用哪个流。

## Compression 压缩

*Compression* refers to any process that reduces the size of a  data stream by removing redundant information(冗余信息). Compression algorithms  fall into two broad categories:

- *Lossless* compression(无损压缩). Using a lossless algorithm, the reconstructed data is identical to the original(重构后的数据跟原始数据一致).
- *Lossy* compression. Using a lossy algorithm, the reconstructed data is an approximation of the original, but is not an exact match.

In most other domains, lossy compression is not acceptable. (Imagine  getting back an "approximation" of a spreadsheet! 想象一下，得到一个“近似”的电子表格！) But lossy compression  schemes are well-suited to audio and video, for a couple of reasons.

The first reason has to do with the physics of human perception. When  we listen to a complex sound, like a music recording, some of the  information contained in that sound is not perceptible to the ear. With  the help of signal processing theory, it is possible to analyze and  separate the frequencies that cannot be perceived. These frequencies can  be removed with no perceptual effect. Although the reconstructed audio  will not match the original exactly, it will *sound* the same to the listener. Similar principles apply to video.

Second, some degradation in sound or image quality may be acceptable,  depending on the intended purpose. In telephony, for example, audio is  often highly compressed. The result is good enough for a phone  conversation—but you wouldn't want to listen to a symphony orchestra  over a telephone.

Compression is also called *encoding*, and a device that encodes is called an *encoder*. The reverse process is *decoding*, and the device is a naturally called a *decoder*. The general term for both encoders and decoders is *codec*. Codecs can be implemented in hardware or software.

Compression technology has changed rapidly since the advent of  digital media(自从数字媒体的出现), and a large number of compression schemes are in use  today. This fact is one of the main challenges for digital media  programming.

## Media Containers

It is rare to store a raw audio or video stream as a computer file,  or to send one directly over the network. For one thing, it would be  impossible to decode such a stream, without knowing in advance which  codec to use. Therefore, media files usually contain at least some of  the following elements:

- File headers that describe the number of streams, the format of each stream, and so on.
- An index that enables random access to the content.
- Metadata that describes the content (for example, the artist or title).
- Packet headers, to enable network transmission or random access.

This documentation uses the term *container* to describe the entire package of streams, headers, indexes, metadata, and so forth. The reason for using the term *container* rather than *file*  is that some container formats are designed for live broadcast. An  application could generate the container in real time, never storing it  to a file.

An early example of a media container is the AVI file format. Other  examples include MP4 and Advanced Systems Format (ASF). Containers can  be identified by file name extension (for example, .mp4) or by MIME  type.

The following diagram shows a typical structure for a media  container. The diagram does not represent any specific format; the  details of each format vary widely.

![diagram showing a typical media container](https://docs.microsoft.com/en-us/windows/win32/medfound/images/concepts01.png)

Notice that the structure shown in the diagram is hierarchical, with  header information appearing at the start of the container. This  structure is typical of many (but not all) container formats. Also  notice that the data section contains interleaved audio and video  packets. This type of interleaving is common in media containers.

The term *multiplexing* refers to the process of packetizing  the audio and video streams and interleaving the packets into the  container. The reverse process, reassembling the streams from the  packetized data, is called *demultiplexing*.

## Formats

In digital media, the term *format* is ambiguous. A format can refer to the type of *encoding*, such as H.264 video, or the *container*,  such as MP4. This distinction is often confusing for ordinary users.  The names given to media formats do not always help. For example, *MP3* refers both to an encoding format (MPEG-1 Audio Layer 3) and a file format.

The distinction is important, however, because reading a media file actually involves two stages:

1. First, the container must be parsed. In most cases, the number of  streams and the format of each stream cannot be known until this step is  complete.
2. Next, if the streams are compressed, they must be decoded using the appropriate decoders.

This fact leads quite naturally to a software design where separate  components are used to parse containers and decode streams. Further,  this approach lends itself to a plug-in model, so that third parties can  provide their own parsers and codecs. On Windows, the Component Object  Model (COM) provides a standard way to separate an API from its  implementation, which is a requirement for any plug-in model. For this  reason (among others), Media Foundation uses COM interfaces.

The following diagram shows the components used to read a media file:

![diagram showing the components to read a media file](https://docs.microsoft.com/en-us/windows/win32/medfound/images/concepts02.png)

Writing a media file also requires two steps:

1. Encoding the uncompressed audio/video data.
2. Putting the compressed data into a particular container format.

The following diagram shows the components used to write a media file:

![diagram showing the components to write a media file.](https://docs.microsoft.com/en-us/windows/win32/medfound/images/concepts03.png)

## Related topics

-  [Media Foundation Programming Guide](https://docs.microsoft.com/en-us/windows/win32/medfound/media-foundation-programming-guide) 