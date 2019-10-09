

# FFmpeg命令简单使用



## 1，概述

FFmpeg 号称多媒体开发的“瑞士军刀”，提供了丰富的功能。



## 2，基本功能一览

```ini
ffmpeg.exe -h
ffmpeg version 3.4 Copyright (c) 2000-2017 the FFmpeg developers
  built with gcc 7.2.0 (GCC)
  configuration: --enable-gpl --enable-version3 --enable-sdl2 --enable-bzlib --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvorbis --enable-cuda --enable-cuvid --enable-d3d11va --enable-nvenc --enable-dxva2 --enable-avisynth --enable-libmfx
  libavutil      55. 78.100 / 55. 78.100
  libavcodec     57.107.100 / 57.107.100
  libavformat    57. 83.100 / 57. 83.100
  libavdevice    57. 10.100 / 57. 10.100
  libavfilter     6.107.100 /  6.107.100
  libswscale      4.  8.100 /  4.  8.100
  libswresample   2.  9.100 /  2.  9.100
  libpostproc    54.  7.100 / 54.  7.100
Hyper fast Audio and Video encoder
usage: ffmpeg [options] [[infile options] -i infile]... {[outfile options] outfile}...

Getting help:
    -h      -- print basic options
    -h long -- print more options
    -h full -- print all options (including all format and codec specific options, very long)
    -h type=name -- print all options for the named decoder/encoder/demuxer/muxer/filter
    See man ffmpeg for detailed description of the options.

Print help / information / capabilities:
-L                  show license
-h topic            show help
-? topic            show help
-help topic         show help
--help topic        show help
-version            show version
-buildconf          show build configuration
-formats            show available formats
-muxers             show available muxers
-demuxers           show available demuxers
-devices            show available devices
-codecs             show available codecs
-decoders           show available decoders
-encoders           show available encoders
-bsfs               show available bit stream filters
-protocols          show available protocols
-filters            show available filters
-pix_fmts           show available pixel formats
-layouts            show standard channel layouts
-sample_fmts        show available audio sample formats
-colors             show available color names
-sources device     list sources of the input device
-sinks device       list sinks of the output device
-hwaccels           show available HW acceleration methods

Global options (affect whole program instead of just one file:
-loglevel loglevel  set logging level
-v loglevel         set logging level
-report             generate a report
-max_alloc bytes    set maximum size of a single allocated block
-y                  overwrite output files
-n                  never overwrite output files
-ignore_unknown     Ignore unknown stream types
-filter_threads     number of non-complex filter threads
-filter_complex_threads  number of threads for -filter_complex
-stats              print progress report during encoding
-max_error_rate ratio of errors (0.0: no errors, 1.0: 100% error  maximum error rate
-bits_per_raw_sample number  set the number of bits per raw sample
-vol volume         change audio volume (256=normal)

Per-file main options:
-f fmt              force format
-c codec            codec name
-codec codec        codec name
-pre preset         preset name
-map_metadata outfile[,metadata]:infile[,metadata]  set metadata information of outfile from infile
-t duration         record or transcode "duration" seconds of audio/video
-to time_stop       record or transcode stop time
-fs limit_size      set the limit file size in bytes
-ss time_off        set the start time offset
-sseof time_off     set the start time offset relative to EOF
-seek_timestamp     enable/disable seeking by timestamp with -ss
-timestamp time     set the recording timestamp ('now' to set the current time)
-metadata string=string  add metadata
-program title=string:st=number...  add program with specified streams
-target type        specify target file type ("vcd", "svcd", "dvd", "dv" or "dv50" with optional prefixes "pal-", "ntsc-" or "film-")
-apad               audio pad
-frames number      set the number of frames to output
-filter filter_graph  set stream filtergraph
-filter_script filename  read stream filtergraph description from a file
-reinit_filter      reinit filtergraph on input parameter changes
-discard            discard
-disposition        disposition

Video options:
-vframes number     set the number of video frames to output
-r rate             set frame rate (Hz value, fraction or abbreviation)
-s size             set frame size (WxH or abbreviation)
-aspect aspect      set aspect ratio (4:3, 16:9 or 1.3333, 1.7777)
-bits_per_raw_sample number  set the number of bits per raw sample
-vn                 disable video
-vcodec codec       force video codec ('copy' to copy stream)
-timecode hh:mm:ss[:;.]ff  set initial TimeCode value.
-pass n             select the pass number (1 to 3)
-vf filter_graph    set video filters
-ab bitrate         audio bitrate (please use -b:a)
-b bitrate          video bitrate (please use -b:v)
-dn                 disable data

Audio options:
-aframes number     set the number of audio frames to output
-aq quality         set audio quality (codec-specific)
-ar rate            set audio sampling rate (in Hz)
-ac channels        set number of audio channels
-an                 disable audio
-acodec codec       force audio codec ('copy' to copy stream)
-vol volume         change audio volume (256=normal)
-af filter_graph    set audio filters

Subtitle options:
-s size             set frame size (WxH or abbreviation)
-sn                 disable subtitle
-scodec codec       force subtitle codec ('copy' to copy stream)
-stag fourcc/tag    force subtitle tag/fourcc
-fix_sub_duration   fix subtitles duration
-canvas_size size   set canvas size (WxH or abbreviation)
-spre preset        set the subtitle options to the indicated preset

```



### 从mp4中提取音频数据

```bash
ffmpeg  -i OneNoteFRE_Welcome.mp4  -acodec copy -vn o.aac
```



## 3，常用命令

主要参数：

```undefined
-i 设定输入流 
-f 设定输出格式 
-ss 开始时间 
```

视频参数：

```undefined
-b 设定视频流量(码率)，默认为200Kbit/s 
-r 设定帧速率，默认为25 
-s 设定画面的宽与高 
-aspect 设定画面的比例 
-vn 不处理视频 
-vcodec 设定视频编解码器，未设定时则使用与输入流相同的编解码器 
```

音频参数：

```undefined
-ar 设定采样率 
-ac 设定声音的Channel数 
-acodec 设定声音编解码器，未设定时则使用与输入流相同的编解码器 
-an 不处理音频
```



### 3.1视频容器格式转换

比如一个avi文件，想转为mp4，或者一个mp4想转为ts。

```
ffmpeg -i input.avi output.mp4
ffmpeg -i input.mp4 output.ts
```



### 3.2. 提取音频

从mp4中提取音频数据

```bash
ffmpeg  -i OneNoteFRE_Welcome.mp4  -acodec copy -vn o.aac
```

默认mp4的audio codec是aac，如果不是会出错，咱可以暴力一点，不管什么音频，都转为最常见的aac。

```bash
ffmpeg  -i OneNoteFRE_Welcome.mp4  -acodec aac -vn o.aac
```

-vn 不处理视频 

### 3.3. 提取视频

从mp4中提取一个纯视频文件

```
ffmpeg -i input.mp4 -vcodec copy -an output.mp4
```

-an 不处理音频

### 3.4. 视频剪切

```
ffmpeg -ss 00:00:15 -t 00:00:05 -i input.mp4 -vcodec copy -acodec copy output.mp4
```

-ss表示开始切割的时间，-t表示要切多少。上面就是从开始，切5秒钟出来。

> 注意一个问题，ffmpeg 在切割视频的时候无法做到时间绝对准确，因为视频编码中关键帧（I帧）和跟随它的B帧、P帧是无法分割开的，否则就需要进行重新帧内编码，会让视频体积增大。所以，如果切割的位置刚好在两个关键帧中间，那么 ffmpeg 会向前/向后切割，所以最后切割出的 chunk 长度总是会大于等于应有的长度。

### 3.5. 码率控制

#### 什么是码率

码率控制对于在线视频比较重要。因为在线视频需要考虑其能提供的带宽。

那么，什么是码率？很简单： `bitrate = file size / duration`

比如一个文件20.8M，时长1分钟，那么，码率就是：
 `biterate = 20.8M bit/60s = 20.8*1024*1024*8 bit/60s= 2831Kbps`
 一般音频的码率只有固定几种，比如是128Kbps， 那么，video的就是
 `video biterate = 2831Kbps -128Kbps = 2703Kbps。`

#### ffmpeg如何控制码率。

 ffmpg控制码率有3种选择，`-minrate -b:v -maxrate`

- -b:v主要是控制平均码率。 比如一个视频源的码率太高了，有10Mbps，文件太大，想把文件弄小一点，但是又不破坏分辨率。 `ffmpeg -i input.mp4 -b:v 2000k output.mp4`上面把码率从原码率转成2Mbps码率，这样其实也间接让文件变小了。目测接近一半。
- 不过，ffmpeg官方wiki比较建议，设置b:v时，同时加上 -bufsize
   -bufsize 用于设置码率控制缓冲器的大小，设置的好处是，让整体的码率更趋近于希望的值，减少波动。（简单来说，比如1 2的平均值是1.5， 1.49 1.51 也是1.5, 当然是第二种比较好） `ffmpeg -i input.mp4 -b:v 2000k -bufsize 2000k output.mp4`
- -minrate -maxrate就简单了，在线视频有时候，希望码率波动，不要超过一个阈值，可以设置maxrate。
   `ffmpeg -i input.mp4 -b:v 2000k -bufsize 2000k -maxrate 2500k output.mp4`



### 3.6. 视频编码格式转换

MPEG4  H264 相互转化

```
ffmpeg -i input.mp4 -vcodec h264 output.mp4
```

```
ffmpeg -i input.mp4 -vcodec mpeg4 output.mp4
```

使用第三方库

```
ffmpeg -i input.mp4 -c:v libx265 output.mp4
ffmpeg -i input.mp4 -c:v libx264 output.mp4
```

### 3.7只提取视频ES数据

这个可能做开发的人会用到，顺便提一下吧。
 `ffmpeg –i input.mp4 –vcodec copy –an –f m4v output.h264`

### 3.8.过滤器的使用

#### 8.1 将输入的1920x1080缩小到960x540输出:

`ffmpeg -i input.mp4 -vf scale=960:540 output.mp4`
 //ps: 如果540不写，写成-1，即scale=960:-1, 那也是可以的，ffmpeg会通知缩放滤镜在输出时保持原始的宽高比。

#### 8.2 为视频添加logo

想要贴到一个视频上，那可以用如下命令：
`./ffmpeg -i input.mp4 -i iQIYI_logo.png -filter_complex overlay output.mp4`

### 3.9. 抓取视频的一些帧，存为jpeg图片

比如，一个视频，我想提取一些帧，存为图片，咋办？
 `ffmpeg -i input.mp4 -r 1 -q:v 2 -f image2 pic-%03d.jpeg`

> -r 表示每一秒几帧
>  -q:v表示存储jpeg的图像质量，一般2是高质量。

如此，ffmpeg会把input.mp4，每隔一秒，存一张图片下来。假设有60s，那会有60张。60张？什么？这么多？不要不要。。。。。不要咋办？？ 可以设置开始的时间，和你想要截取的时间呀。
 `ffmpeg -i input.mp4 -ss 00:00:20 -t 10 -r 1 -q:v 2 -f image2 pic-%03d.jpeg`

> -ss 表示开始时间
>  -t表示共要多少时间。

如此，ffmpeg会从input.mp4的第20s时间开始，往下10s，即20~30s这10秒钟之间，每隔1s就抓一帧，总共会抓10帧。

### 3.10.输出YUV420原始数据

提取视频的YUV原始数据

```
ffmpeg -i input.mp4 output.yuv
```

播放yuv 可以试试RawPlayer

那如果我只想要抽取某一帧YUV呢？ 简单，你先用上面的方法，先抽出jpeg图片，然后把jpeg转为YUV。 比如： 你先抽取10帧图片。 `ffmpeg -i input.mp4 -ss 00:00:20 -t 10 -r 1 -q:v 2 -f image2 pic-%03d.jpeg`
 结果：

```css
-rw-rw-r-- 1 chenxf chenxf    296254  7月 20 16:08 pic-001.jpeg
-rw-rw-r-- 1 chenxf chenxf    300975  7月 20 16:08 pic-002.jpeg
-rw-rw-r-- 1 chenxf chenxf    310130  7月 20 16:08 pic-003.jpeg
-rw-rw-r-- 1 chenxf chenxf    268694  7月 20 16:08 pic-004.jpeg
-rw-rw-r-- 1 chenxf chenxf    301056  7月 20 16:08 pic-005.jpeg
-rw-rw-r-- 1 chenxf chenxf    293927  7月 20 16:08 pic-006.jpeg
-rw-rw-r-- 1 chenxf chenxf    340295  7月 20 16:08 pic-007.jpeg
-rw-rw-r-- 1 chenxf chenxf    430787  7月 20 16:08 pic-008.jpeg
-rw-rw-r-- 1 chenxf chenxf    404552  7月 20 16:08 pic-009.jpeg
-rw-rw-r-- 1 chenxf chenxf    412691  7月 20 16:08 pic-010.jpeg
```

然后，你就随便挑一张，转为YUV: `ffmpeg -i pic-001.jpeg -s 1440x1440 -pix_fmt yuv420p xxx3.yuv`如果-s参数不写，则输出大小与输入一样。当然了，YUV还有yuv422p啥的，你在-pix_fmt 换成yuv422p就行啦！

### 3.11.H264编码profile & level控制

举3个例子吧

```css
ffmpeg -i input.mp4 -profile:v baseline -level 3.0 output.mp4
ffmpeg -i input.mp4 -profile:v main -level 4.2 output.mp4
ffmpeg -i input.mp4 -profile:v high -level 5.1 output.mp4
```

如果ffmpeg编译时加了external的libx264，那就这么写：
 `ffmpeg -i input.mp4 -c:v libx264 -x264-params "profile=high:level=3.0" output.mp4`
 从压缩比例来说，baseline< main <  high，对于带宽比较局限的在线视频，可能会选择high，但有些时候，做个小视频，希望所有的设备基本都能解码（有些低端设备或早期的设备只能解码baseline），那就牺牲文件大小吧，用baseline。自己取舍吧！







