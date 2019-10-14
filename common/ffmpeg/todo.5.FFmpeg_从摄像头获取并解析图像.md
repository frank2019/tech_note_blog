





本文主要描述使用ffmpeg 访问摄像头，获取并解析图像



使用ffplay命令显示摄像头

```bash
ffplay -f dshow -i   "video=Logitech HD Webcam C270"
```



### 用命令行枚举采集设备和采集数据

FFmpeg支持通过DShow获取采集设备（摄像头、麦克风）的数据



#### 查看音视频设备列表

```
ffmpeg -list_devices true -f dshow -i dummy  
```



#### 查看分辨率帧率 像素格式

```
ffmpeg -list_options true -f dshow -i video="Logitech HD Webcam C270"
```

  这个命令行的作用是获取指定视频采集设备支持的分辨率、帧率和像素格式等属性，返回的是一个列表，



```
ffmpeg -f dshow -i video="Logitech HD Webcam C270" -f dshow -i audio="HD Webcam C270" -vcodec libx264 -acodec aac -strict -2 mycamera.mkv
```



```
ffmpeg -f dshow -i video="Logitech HD Webcam C270" -framerate 15  -rtbufsize 702000k  -vcodec libx264 -acodec aac -strict -2 mycamera.mkv

```

 命令运行之后，控制台打印FFmpeg的运行日志，按“Q”键则中止命令。



## 问题

###  real-time buffer ... [video input] too full or near too full 

```
[dshow @ 000000001cf86580] real-time buffer ... [video input] too full or near too full (90% of size: 3041280 [rtbufsize parameter])! frame dropped!
```

原因：内存不够大

解决方法：av_dict_set_int(&options, "rtbufsize", 3041280 * 100, 0);//默认大小3041280

可能导致的问题：当电脑性能不够时会出现延迟问题。





## 参考链接

1. [如何用FFmpeg API采集摄像头视频和麦克风音频，并实现录制文件的功能](https://www.cnblogs.com/lidabo/p/8662955.html)
2. http://www.pianshen.com/article/1517300903/
3. [](http://www.360doc.com/content/17/0224/18/474846_631726230.shtml)
4. [使用FFmpeg库读取USB摄像头并解码](https://blog.csdn.net/iamqianrenzhan/article/details/84830277)

