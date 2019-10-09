





##### 五、使用ffmpeg推RTMP直播流

1.安装nignx环境
 弄个WINDOWS版本的Nginx吧，参照[Linux&Windows搭建基于nginx的视频点播服务器](https://link.jianshu.com/?t=http://blog.csdn.net/akeron/article/details/54974034)，使用了[nginx-rtmp-win32](https://link.jianshu.com/?t=https://github.com/illuspas/nginx-rtmp-win32)做了本地点播测试。具体步骤参照原文，为了节约时间，最好去[CSDN下载作者那个DEMO](https://link.jianshu.com/?t=http://download.csdn.net/detail/akeron/9752215)

2.参考[手把手教你搭建Nginx-rtmp流媒体服务器+使用ffmpeg推流](https://www.jianshu.com/p/06c2025edcd3)
 在上述下载的demo中，看一下conf/nginx.conf配置文件：

```csharp
rtmp {
    server {
        listen 1935;

        application live {
            live on;
        }
        
        application vod {
            play video;
        }
        
        application hls {
            live on;
            hls on;  
            hls_path temp/hls;  
            hls_fragment 8s;  
        }
    }
}
```

其中rtmp就是rtmp服务器模块，端口是1935，application我理解为一个路径。可以通过访问`rtmp://localhost/live`来访问live这个资源。live  on  表示这是实时的传输，这不同于点播，点播就好比我在某视频网站上想看一个视频，无论我什么时候去点击，它会从头开始播放。而实时传输（直播），就是好比看电视，我在19:20去打开电视（打开直播路），视频不会从头开始播放，而是从当前(19:20)的视频数据开始播放。

然后在nginx.exe路径下命令行运行nginx -s reload重新加载配置。

3.使用ffmpeg推流
 参考[使用FFmpeg在B站直播的姿势](https://zhuanlan.zhihu.com/p/23951969)
 `ffmpeg -re -i 1.mp4 -vcodec copy -f flv rtmp://localhost/live`
 或者

```go
ffmpeg -re -i 1.mp4 -vcodec copy -acodec copy
 -b:v 800k -b:a 32k -f flv rtmp://localhost/live
```

-re : **表示使用文件的原始帧率进行读取，因为ffmpeg读取视频帧的速度很快，如果不使用这个参数，ffmpeg可以在很短时间就把video.mp4中的视频帧全部读取完并进行推流，这样就无法体现出视频播放的效果了。**官方文档中对这个参数的解释是：

> -re (input)
>  Read input at native frame rate. Mainly used to simulate a grab device,  or live input stream (e.g. when reading from a file). Should not be used  with actual grab devices or live input streams (where it can cause  packet loss). By default ffmpeg attempts to read the input(s) as fast as  possible. This option will slow down the reading of the input(s) to the  native frame rate of the input(s). It is useful for real-time output  (e.g. live streaming).

-vcodec copy : -vcodec表示使用的视频编解码器 ，前缀v表示video。后面紧跟的copy 表示复制使用源文件的视频编解码器，比如原文件的编解码器(codec)是h264，则这里就使用h264。

-acodec copy : -acodec表示使用的音频编解码器，前缀a表示audio。后面的copy 表示使用源文件的音频编解码器。

-b:v 800k : -b:v表示视频的比特率(bitrate) ，为800k。

-b:a 32k : 表示音频的比特率为32k。

-f flv : -f表示format ，就是强制输出格式为flv，这一步其实也叫封装(mux)，封装要做的事就是把视频和音频混合在一起，进行同步。紧跟在后面的`rtmp://localhost/live` 表示输出的"文件名"，这个文件名可以是一个本地的文件，也可以指定为rtmp流媒体地址。指定为rtmp流媒体地址后，则ffmpeg就可以进行推流。

4.可以使用VLC或ffplay进行播放了

## 参考链接

https://www.jianshu.com/p/ddafe46827b7