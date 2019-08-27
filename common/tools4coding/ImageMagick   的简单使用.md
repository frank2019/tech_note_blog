## ImageMagick   的简单使用



## 1，简介

ImageMagick (TM) 是一个免费的创建、编辑、合成图片的软件。它可以读取、转换、写入多种格式的图片。图片切割、颜色替换、各种效果的应用，图片的旋转、组合，文本，直线，多边形，椭圆，曲线，附加到图片伸展旋转。

ImageMagick是免费软件：全部源码开放，可以自由使用，复制，修改，发布。它遵守GPL许可协议。它可以运行于大多数的操作系统。

ImageMagick的大多数功能的使用都来源于命令行工具。也就是说使用命令行即可调用大多数功能。通常来说，它可以支持以下程序语言：Perl, C, C++, Python, PHP, Ruby, Java；现成的ImageMagick接口(PerlMagick,  Magick++, PythonMagick, MagickWand for PHP, RubyMagick, and 
JMagick)是可利用的。这使得自动的动态的修改创建图片变为可能。ImageMagick支持至少90种图片格式。

## 2，ImageMagick支持的命令行工具



###         convert

　　转换图像格式和大小，模糊，裁剪，驱除污点，抖动，临近，图片上画图片，加入新图片，生成缩略图等。

### 　　identify

　　描述一个或较多图像文件的格式和特性。

### 　　mogrify

　　按规定尺寸制作一个图像，模糊，裁剪，抖动等。Mogrify改写最初的图像文件然后写到一个不同的图像文件。

### 　　composite

　　根据一个图片或多个图片组合生成图片。

### 　　montage

　　创建一些分开的要素图像。在含有要素图像任意的装饰图片，如边框、结构、图片名称等。

### 　　compare

　　在算术上和视觉上评估不同的图片及其它的改造图片。

### 　　display

　　如果你拥有一个X server的系统，它可以按次序的显示图片

### 　　animate

　　利用X server显示动画图片

### 　　import

　　在X server或任何可见的窗口上输出图片文件。 你可以捕获单一窗口，整个的荧屏或任何荧屏的矩形部分。

### 　　conjure

　　解释执行 MSL (Magick Scripting Language) 写的脚本。



## 3，安装



[下载链接](http://www.imagemagick.org/script/download.php)

### Mac OS X

```bash
sudo port install ImageMagick
```



### Windows Binary 

下载地址： https://imagemagick.org/download/binaries/ImageMagick-7.0.8-62-Q16-x64-dll.exe

 跟常见windows安装程序一样，点下一步即可。



## 4，命令示例

### 文件格式转换

magick 支持常见90多种图片格式，可以轻易的在各种文件格式之间转换。

基本格式如下示例 根据后缀判断文件格式

```bash
#将png格式的文件in.png 转换为jpg格式文件 out.jpg
magick   in.png   out.jpg
```



bash终端

将当前目录下的png文件，转换为bmp，放在当前目录，同名文件后缀改位bmp

```
for %f in (*.png) do magick  "%f"  "%~nf.bmp"
```

将当前目录下的png文件，转换为bmp，放在指定目录out，同名文件后缀改位bmp

```
for %f in (*.png) do magick  "%f"  "out/%~nf.bmp"
```



windows终端

```
for /f %%i in ('dir /b *.png') do (echo "1/%%~ni.bmp")
```



将当前目录下的png图像，转换未bmp文件存放在out目录下，文件名与原文件名一致

```bash
for /f %%i in ('dir /b *.png') do (magick   %%i  "out/%%~ni.bmp")
```



## 实例 递归转换png文件为bmp

>1.可以支持多种分辨率png转bmp
>2.遍历多级目录输出结果，输出的图片保存在原始路径下且名称和原始图片名称保持一致
>3.可以批量处理



### 实现

```bash
@echo off
rem  传参的第一个参数，也可以直接在这里设定
set mydir=%1

for /R %mydir% %%s in (*.png)do (magick   %%s  %%~ds%%~ps%%~ns.bmp)

rem for /R %mydir%  %%s in (*.png)do (echo %%~ds%%~ps%%~ns.bmp)

```



其他功能示例

```bash
#对图片加边框
magick convert -raise 10x10 in.png   out.png
magick convert -bordercolor red -border 5×5 input.jpg output.jpg 

#调整分辨率为1280 960
magick convert -resize 1280x960 in.jpg out.jpg
#你也可以用百分比，这样显的更为直观：会自动地考虑在缩放图像大小时图像的高宽的比例
magick convert -resize 50%x50% in.jpg out.jpg

#模糊高斯模糊:  -blur 代表Sigma值
magick convert -blur 80 foo.jpg foo.png

#翻转上下翻转：
magick　　convert -flip foo.png bar.png

#左右翻转：
magick convert -flop foo.png bar.png

#反色形成底片的样子：
convert -negate foo.png bar.png

#单色把图片变为黑白颜色：
convert -monochrome foo.png bar.png

#加噪声
convert -noise 3 foo.png bar.png

#油画效果我们可用这个功能，把一张普通的图片，变成一张油画，效果非常的逼真
convert -paint 4 foo.png bar.png

#旋转把一张图片，旋转一定的角度：
convert -rotate 30 foo.png bar.png
#上面的30，表示向右旋转30度，如果要向左旋转，度数就是负数。

　　
#炭笔效果
magick convert -charcoal 2 foo.png bar.png形成炭笔或者说是铅笔画的效果。

#散射毛玻璃效果：
convert -spread 30 foo.png bar.png

#漩涡以图片的中心作为参照，把图片扭转，形成漩涡的效果：
convert -swirl 67 foo.png bar.png
　　
　　
#凸起效果用-raise来创建凸边：
convert -raise 5x5 foo.png bar.png

#执行后，你会看到，照片的四周会一个5×5的边，如果你要一个凹下去的边，把-raise改为+raise就可以了。其实凸边和凹边看起来区别并不是很大
@magick identify   1.png
1.png PNG 640x480 640x480+0+0 16-bit Grayscale Gray 387973B 0.000u 0:00.000
```



## 参考链接

1. [imagemagick官网](https://imagemagick.org/index.php)

   

