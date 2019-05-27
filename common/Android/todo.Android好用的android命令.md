

#### pranck

```
adb shell procrank | grep "com.android.gallery"
```





#### 截屏命令

```bash
127|R11s:/ # screencap   -h
usage: screencap [-hp] [-d display-id] [FILENAME]
   -h: this message
   -p: save the file as a png.
   -d: specify the display id to capture, default 0.
If FILENAME ends with .png it will be saved as a png.
If FILENAME is not given, the results will be printed to stdout.
```



#### 启动指定app的指定类

```bash
adb  shell  am start -n   com.oppo.engineermode/com.oppo.engineermode.camera.mx6300camera2.MainActivity
```



制定参数

```
--ei pid 10 --es str "hello, world"
```







参考链接

1. https://blog.csdn.net/qq_32274413/article/details/55096343
2. [内存分析命令](https://blog.csdn.net/berber78/article/details/47819139)
3. [Android内存监控与分析（三）：内存分析及原理](https://blog.csdn.net/Allan_shore_ma/article/details/78353737)

