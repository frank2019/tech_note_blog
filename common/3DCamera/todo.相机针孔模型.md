针孔相机模型详解



数码相机图像拍摄的过程实际上是一个光学成像的过程。相机的成像过程涉及到四个坐标系：世界坐标系、相机坐标系、图像坐标系、像素坐标系以及这四个坐标系的转换。

### 理想透视模型——针孔成像模型

相机模型是光学成像模型的简化，目前有线性模型和非线性模型两种。实际的成像系统是透镜成像的非线性模型。最基本的透镜成像原理如图所示：

![]()

透镜成像原理示意图



其中 u 为物距， f 为焦距，v 为相距。三者满足关系式：
$$
\frac{1}{f}=\frac{1}{u}+\frac{1}{v}
$$
相机的镜头是一组透镜，当平行于主光轴的光线穿过透镜时，会聚到一点上，这个点叫做焦点，焦点到透镜中心的距离叫做焦距 f。数码相机的镜头相当于一个凸透镜，感光元件就处在这个凸透镜的焦点附近，将焦距近似为凸透镜中心到感光元件的距离时就成为[小孔成像](https://www.baidu.com/s?wd=%E5%B0%8F%E5%AD%94%E6%88%90%E5%83%8F&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)模型。小孔成像模型如图所示。



小孔成像模型

小孔成像模型是相机成像采用最多的模型。在此模型下，物体的空间坐标和图像坐标之间是线性的关系，因而对相机参数的求解就归结到求解线性方程组上。四个坐标系的关系图如下图所示，其中 M 为三维空间点，m 为 M 在图像平面投影成的像点。



四个坐标系的关系图

- **世界坐标系：**是客观三维世界的绝对坐标系，也称客观坐标系。因为数码相机安放在三维空间中，我们需要世界坐标系这个基准坐标系来描述数码相机的位置，并且用它来描述安放在此三维环境中的其它任何物体的位置，用（Xw, Yw, Zw）表示其坐标值。
- **相机坐标系（光心坐标系）：**以相机的光心为坐标原点，X 轴和Y 轴分别平行于图像坐标系的 X 轴和Y 轴，相机的光轴为Z 轴，用（Xc, Yc, Zc）表示其坐标值。
- **图像坐标系：**以CCD 图像平面的中心为坐标原点，X轴和Y 轴分别平行于图像平面的两条垂直边，用( x , y )表示其坐标值。图像坐标系是用物理单位（例如毫米）表示像素在图像中的位置。
- **像素坐标系：**以 CCD 图像平面的左上角顶点为原点，X 轴和Y 轴分别平行于图像坐标系的 X 轴和Y 
  轴，用(u , v )表示其坐标值。数码相机采集的图像首先是形成标准电信号的形式，然后再通过模数转换变换为数字图像。每幅图像的存储形式是M × 
  N的数组，M 行 N 列的图像中的每一个元素的数值代表的是图像点的灰度。这样的每个元素叫像素，像素坐标系就是以像素为单位的图像坐标系。



像素坐标系与图像坐标系的关系如图。



他们之间的转换关系为：
$$
u=\frac{x}{dx}+u_0
$$

$$
v=\frac{y}{dy}+v_0
$$




### 参考链接

1. [相机针孔模型详解](https://blog.csdn.net/x_r_su/article/details/52682318)
2. [SLAM入门之视觉里程计(2)：相机模型（内参数，外参数）](https://www.cnblogs.com/wangguchangqing/p/8126333.html)