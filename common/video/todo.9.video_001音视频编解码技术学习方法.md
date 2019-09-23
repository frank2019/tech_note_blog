

# 读书笔记：音视频编解码技术学习方法



## **0.     生活中的视音频技术**

### 封装格式与视音频编码标准

电影文件有不同的格式，用不同的后缀表示：avi，rmvb，mp4，flv，mkv.些格式代表的是**封装格式**。何为封装格式？就是把视频数据和音频数据打包成一个文件的规范.

有些封装格式支持的视音频编码标准十分广泛，，比如MKV；而有些封装格式支持的视音频编码标准很少，比如RMVB。

### 查看媒体信息的工具：MediaInfo

MediaInfo是一个专门查看视音频格式的工具，软件的详细使用可参考：

[MediaInfo使用简介（新版本支持HEVC）](http://blog.csdn.net/leixiaohua1020/article/details/11903507)

源代码分析可参考：

[MediaInfo源代码分析 1：整体结构系列文章](http://blog.csdn.net/leixiaohua1020/article/details/12016231)



## 1，视频播放器原理

视音频技术主要包含以下几点：

- 封装技术，
- 视频压缩编码技术以及音频压缩编码技术。
- 如果考虑到网络传输的话，还包括流媒体协议技术。

视频播放器的源代码详细解析（Media Player Classic - HC，Mplayer，FFplay，XBMC）可以参考系列文章：

- [Media Player Classic：Media Player Classic - HC源代码分析 1：整体结构[系列文章]](https://blog.csdn.net/leixiaohua1020/article/details/13280659)

- [Mplayer：MPlayer源代码分析](https://blog.csdn.net/leixiaohua1020/article/details/11885509)

- [FFplay： FFplay源代码分析：整体流程图](https://blog.csdn.net/leixiaohua1020/article/details/11980843)

- [XBMC： XBMC源代码分析 1：整体结构以及编译方法[系列文章]](https://blog.csdn.net/leixiaohua1020/article/details/17454977)


### 视频播放器的原理。

视频播放器播放一个互联网上的视频文件，需要经过以下几个步骤：解协议，解封装，解码视音频，视音频同步。如果播放本地文件则不需要解协议，为以下几个步骤：解封装，解码视音频，视音频同步。他们的过程如图所示。

![](001/1.jpg)



#### 解协议的作用

就是将流媒体协议的数据，解析为标准的相应的封装格式数据。视音频在网络上传播的时候，常常采用各种流媒体协议，例如HTTP，RTMP，或是MMS等等。这些协议在传输视音频数据的同时，也会传输一些信令数据。这些信令数据包括对播放的控制（播放，暂停，停止），或者对网络状态的描述等。解协议的过程中会去除掉信令数据而只保留视音频数据。例如，采用RTMP协议传输的数据，经过解协议操作后，输出FLV格式的数据。

#### 解封装的作用

就是将输入的封装格式的数据，分离成为音频流压缩编码数据和视频流压缩编码数据。封装格式种类很多，例如MP4，MKV，RMVB，TS，FLV，AVI等等，它的作用就是将已经压缩编码的视频数据和音频数据按照一定的格式放到一起。例如，FLV格式的数据，经过解封装操作后，输出H.264编码的视频码流和AAC编码的音频码流。

#### 解码的作用

就是将视频/音频压缩编码数据，解码成为非压缩的视频/音频原始数据。音频的压缩编码标准包含AAC，MP3，AC-3等等，视频的压缩编码标准则包含H.264，MPEG2，VC-1等等。解码是整个系统中最重要也是最复杂的一个环节。通过解码，压缩编码的视频数据输出成为非压缩的颜色数据，例如YUV420P，RGB等等；压缩编码的音频数据输出成为非压缩的音频抽样数据，例如PCM数据。

#### 视音频同步的作用

就是根据解封装模块处理过程中获取到的参数信息，同步解码出来的视频和音频数据，并将视频音频数据送至系统的显卡和声卡播放出来。


接下来的几节我们将会列出主要的流媒体协议，封装格式，以及视音频编码标准。更详细的比较可以参考：

[视频参数（流媒体系统，封装格式，视频编码，音频编码，播放器）对比](http://blog.csdn.net/leixiaohua1020/article/details/11842919)

有关本文中涉及到的协议数据、封装格式数据、视频编码数据、音频编码数据、视频像素数据、音频采样数据的分析可以参考下面系列文章：

[视音频数据处理入门：RGB、YUV像素数据处理](http://blog.csdn.net/leixiaohua1020/article/details/50534150)

[视音频数据处理入门：PCM音频采样数据处理](http://blog.csdn.net/leixiaohua1020/article/details/50534316)

[视音频数据处理入门：H.264视频码流解析](http://blog.csdn.net/leixiaohua1020/article/details/50534369)

[视音频数据处理入门：AAC音频码流解析](http://blog.csdn.net/leixiaohua1020/article/details/50535042)

[视音频数据处理入门：FLV封装格式解析](http://blog.csdn.net/leixiaohua1020/article/details/50535082)

[视音频数据处理入门：UDP-RTP协议解析](http://blog.csdn.net/leixiaohua1020/article/details/50535230)



## **2.     流媒体协议**

流媒体协议是服务器与客户端之间通信遵循的规定。当前网络上主要的流媒体协议如表所示。

主要流媒体协议一览

| 名称     | 推出机构       | 传输层协议 | 客户端   | 目前使用领域    |
| -------- | -------------- | ---------- | -------- | --------------- |
| RTSP+RTP | IETF           | TCP+UDP    | VLC, WMP | IPTV            |
| RTMP     | Adobe Inc.     | TCP        | Flash    | 互联网直播      |
| RTMFP    | Adobe Inc.     | UDP        | Flash    | 互联网直播      |
| MMS      | Microsoft Inc. | TCP/UDP    | WMP      | 互联网直播+点播 |
| HTTP     | WWW+IETF       | TCP        | Flash    | 互联网点播      |



- RTSP+RTP经常用于IPTV领域。因为其采用UDP传输视音频，支持组播，效率较高。但其缺点是网络不好的情况下可能会丢包，影响视频观看质量。因而围绕IPTV的视频质量的研究还是挺多的。
- RTSP规范可参考：[RTSP协议学习笔记](http://blog.csdn.net/leixiaohua1020/article/details/11955341)

- RTSP+RTP系统中衡量服务质量可参考：[网络视频传输的服务质量（QoS）](http://blog.csdn.net/leixiaohua1020/article/details/11883393)

- 上海IPTV码流分析结果可参考：[IPTV视频码流分析](http://blog.csdn.net/leixiaohua1020/article/details/11846761)

因为互联网网络环境的不稳定性，RTSP+RTP较少用于互联网视音频传输。互联网视频服务通常采用TCP作为其流媒体的传输层协议，因而像RTMP，MMS，HTTP这类的协议广泛用于互联网视音频服务之中。这类协议不会发生丢包，因而保证了视频的质量，但是传输的效率会相对低一些。

此外RTMFP是一种比较新的流媒体协议，特点是支持P2P。

RTMP我做的研究相对多一些：比如[RTMP规范简单分析](http://blog.csdn.net/leixiaohua1020/article/details/11694129)，或者[RTMP流媒体播放过程](http://blog.csdn.net/leixiaohua1020/article/details/11704355)

相关工具的源代码分析：[RTMPdump源代码分析 1： main()函数[系列文章\]](http://blog.csdn.net/leixiaohua1020/article/details/12952977)

RTMP协议学习：[RTMP流媒体技术零基础学习方法](http://blog.csdn.net/leixiaohua1020/article/details/15814587)









## 参考链接

1. [总结]视音频编解码技术零基础学习方法](https://blog.csdn.net/leixiaohua1020/article/details/18893769)