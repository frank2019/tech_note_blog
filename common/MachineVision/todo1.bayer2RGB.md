

bayer2RGB  转换的实现







## 原理篇

### 一，bayerg格式简介

 	bayer格式图片是伊士曼·柯达公司科学家Bryce Bayer发明的，Bryce Bayer所发明的拜耳阵列被广泛运用数字图像。

 	对于彩色图像，需要采集多种最基本的颜色，如rgb三种颜色，最简单的方法就是用滤镜的方法，红色的滤镜透过红色的波长，绿色的滤镜透过绿色的波长，蓝色的滤镜透过蓝色的波长。如果要采集rgb三个基本色，则需要三块滤镜，这样价格昂贵，且不好制造，因为三块滤镜都必须保证每一个像素点都对齐。当用bayer格式的时候，很好的解决了这个问题。bayer   格式图片在一块滤镜上设置的不同的颜色，通过分析人眼对颜色的感知发现，人眼对绿色比较敏感，所以一般bayer格式的图片绿色格式的像素是是r和b像素的和。

​      另外，Bayer格式是相机内部的原始图片, 一般后缀名为.raw。很多软件都可以查看, 比如PS。我们相机拍照下来存储在存储卡上的.jpeg或其它格式的图片, 都是从.raw格式转化过来的。如下图，为bayer色彩滤波阵列，由一半的G，1/4的R，1/4的B组成。



<p align="center"><img src="img/bayer_color_filter_matrix.png" width="400" height="200" /></p>



Bayer数据，其一般格式为：
 奇数扫描行输出 RGRG……
 偶数扫描行输出 GBGB…… 

　　根据人眼对彩色的响应带宽不高的大面积着色特点，每个像素没有必要同时输出3种颜色。因此，数据采样时，

奇数扫描行的第1，2，3，4，…象素分别采样和输出R，G，R，G，…数据；

偶数扫描行的第1，2，3，4，…象素分别采样和输出G，B，G，B，…数据。

在实际处理时，每个象素的R，G，B信号由象素本身输出的某一种颜色信号和相邻象素输出的其他颜色信号构成。这种采样方式在基本不降低图像质量的同时，可以将采样频率降低60％以上。



拜耳色彩滤波阵列（Bayer Color Filter Array，CFA）是非常有名的彩色图片的数字采集格式。色彩滤波器的模式如上图所示，由一半的G，1/4的R，1/4的B组成。

拜耳色彩滤波器的模式、序列、滤波器有很多种，但最常见的模式是由Kodak提出的2*2模式。

[![wps_clip_image-29239](http://files.chinaaet.com/images/blog/2013/04/15/4447152485327.png)](http://files.chinaaet.com/images/blog/2013/04/15/4447147488187.png)





# 　　

### 二， bayer格式图像传感器硬件

　　图像传感器的结构如下所示，每一个感光像素之间都有金属隔离层，光纤通过显微镜头，在色彩滤波器过滤之后，投射到相应的漏洞式硅的感光元件上。  

　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230327210-1156084365.png) 

　　当Image Sensor往外逐行输出数据时，像素的序列为GRGRGR.../BGBGBG...（顺序RGB）。这样阵列的Sensor设计，使得RGB传感器减少到了全色传感器的1/3，如下所示。

　　　　　　　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230428413-1301823553.png)

### 三， bayer格式插值红蓝算法实现

　　每一个像素仅仅包括了光谱的一部分，必须通过插值来实现每个像素的RGB值。为了从Bayer格式得到每个像素的RGB格式，我们需要通过插值填补缺失的2个色彩。插值的方法有很多（包括领域、线性、3*3等），速度与质量权衡，最好的线性插值补偿算法。其中算法如下： 

　　R和B通过线性领域插值，但这有四种不同的分布，如下图所示： 

 　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230501554-1232262581.png)

​                       　　　　　　　　　　　　　　　　(a)                                   (b)

 　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230544663-1346580093.png)

　　　　　　　　　　　　　　　　　　　　　　　　 (c)                                   (d)

　　在（a）与（b）中，R和B分别取邻域的平均值。

　　在（c）与（d）中，取领域的4个B或R的均值作为中间像素的B值。 

### 四， bayer格式插值绿算法实现

 　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230635991-2089764601.png)

​      　　　　　　　　　　　　　　　　　　  (c)                                                        (d)

　　由于人眼对绿光反应最敏感，对紫光和红光则反应较弱，因此为了达到更好的画质，需要对G特殊照顾。在上述（c）与（d）中，扩展开来就是上图的（e）与（f）中间像素G的取值，者也有一定的算法要求，不同的算法效果上会有差异。经过相关的研究，

　　（e）中间像素G值的算法如下： 

 　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230723647-380711004.png)

　　（f）中间像素G值的算法如下：

 　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230748194-1081239687.png)　　　　　　

　　CMOS摄像头这部分转换是在内部用ADC或者ISP完成的，生产商为了降低成本必然会使得图像失真。当然用外部处理器来实现转换，如果处理器的速度足够NB，能够胜任像素的操作，用上面的算法来进行转换，皆大欢喜。不过上述算法将直接成倍提高了算法的复杂度，速度上将会有所限制。因此为了速度的提成，可以直接通过来4领域G取均值来中间像素的G值，将会降低一倍的速率，而在性能上差之甚微，算法如下： 

 　　　　　　　　　　　　　　　　　　![img](https://images2015.cnblogs.com/blog/893951/201603/893951-20160311230816788-692690023.png)

　　如果能够通过损失图像的额质量，来达到更快的速度，还可以取G1、G2的均值来实现，但是这样的做法会导致边沿以及跳变部分的失真。 



### 五，编码实现



目前常用的bayer的格式有那些？

1. bayer每个像素的值是8位的. 但是有的相机的bayer格式却有10位, 12位以及14位, 16位的；

2. 12位的转化为 8位的 可以使用log映射 ： f(in) = 2 ^ ( log(in) * 8 / 12 )

   

## 实现篇







 case DC1394_COLOR_FILTER_           :
        filters = 0x16161616;
        break;
    case DC1394_COLOR_FILTER_GRBG:
        filters = 0x61616161;
        break;
    case DC1394_COLOR_FILTER_RGGB:
        filters = 0x94949494;
        break;
    case DC1394_COLOR_FILTER_GBRG:





### 参考链接

1. [OpenCV中Bayer转BGR](https://blog.csdn.net/j_d_c/article/details/54019582)
2. [Bayer RGB和RGB Raw](https://www.cnblogs.com/biglucky/p/4128566.html)
3. [Libdc1394 Library Support for IEEE 1394 Cameras HOWTO](http://www.tldp.org/HOWTO/libdc1394-HOWTO/concepts.html)
4. http://www.siliconimaging.com/Specifications/AN3%20-%20Bayer%20Color%20Processing.PDF



5. [Bayer8转RGB并用OpenCV显示](https://blog.csdn.net/weixinhum/article/details/81945479)
6. https://github.com/jdthomas/bayer2rgb
7. https://stackoverflow.com/questions/10403841/convert-12-bit-bayer-image-to-8-bit-rgb-using-opencv
8. [What algorithm does OpenCV's Bayer conversion use?](https://stackoverflow.com/questions/11890955/what-algorithm-does-opencvs-bayer-conversion-use)
9. https://vovkos.github.io/doxyrest-showcase/opencv/sphinx_rtd_theme/page_imgproc_color_conversions.html?highlight=bayer
10. https://blog.csdn.net/vincentlipan/article/details/36480619?utm_source=blogxgwz2
11. [libdc1394 Homepage](https://damien.douxchamps.net/ieee1394/libdc1394/)
12. [Bayer Pattern](https://blog.csdn.net/wgx571859177/article/details/79772626)
13. [Bayer filter  wiki](https://en.wikipedia.org/wiki/Bayer_filter)



https://review.lineageos.org/c/LineageOS/android_device_oppo_r7plus/+/32385