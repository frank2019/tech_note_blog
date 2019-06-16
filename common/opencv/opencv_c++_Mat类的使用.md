```
路遥知马力
```

本节主要描述 opencv中的cv::Mat类的基本介绍，和常用使用。

在当前的OpenCV开发中，Mat可以说是最常见的数据单元，深入了解Mat类对于OpenCV深入开发有着重大意义。

#### 常用构造函数

##### 默认构造函数

```c++
cv::Mat::Mat()
```

**默认构造函数**，生成一个矩阵并由OpenCV提供的函数(一般是Mat::create() 和 cv::imread() )来分配储存空间

Mat类可以分为两个部分：矩阵头和指向像素数据的矩阵指针

矩阵头 包括数字图像的矩阵尺寸、存储方法、存储地址和引用次数等，矩阵头的大小是一个常数，不会随着图像的大小而改变，但是保存图像像素数据的矩阵则会随着图像的大小而改变，通常数据量会很大，比矩阵头大几个数量级。这样，在图像复制和传递过程中，主要的开销是由存放图像像素的矩阵而引起的。因此，OpenCV使用了引用次数，当进行图像复制和传递时，不再复制整个Mat数据，而只是复制矩阵头和指向像素矩阵的指针。

```c++
cv::Mat a ; //默认构造函数，创建矩阵头
a = cv::imread("test.jpg");//读入图像，矩阵指针指向该像素数据
cv::Mat b = a ;//浅拷贝
cv::Mat c = a.clone();  //深拷贝
```



##### Mat(int rows,int cols,int type)

```c++
cv::Mat::Mat(int rows,int cols,int type)
cv::Mat::Mat(Size size,int type )   
```

重载的构造函数，这也是常用构造函数之一，在创建对象同时，提供矩阵的大小（rows，行数；cols ，列数），以及存储类型（type） 该类型表示矩阵中每一个元素在计算机内存的存储类型，如CV_8UC3，具体含义为“3通道8位无符号数”。

| 类型                       | 定义                                 | 描述 |
| -------------------------- | ------------------------------------ | ---- |
| CV_8U                      | 无符号单字节像素                     |      |
| CV_8S                      | 有符号单字节像素                     |      |
| CV_8UC3                    | CV_8UC3（3通道每个通道是无符号单字节 |      |
| CV_16SC3                   | 3通道，每个通道是16位有符号          |      |
| CV_32F                     | 单通道，32位浮点数                   |      |
|                            |                                      |      |
| ####Mat 支持的存储类型定义 |                                      |      |



##### Mat 支持的存储类型定义  

```
CV_<bit_depth>(S|U|F)C<number_of_channels>
```

- --bit_depth---比特数---代表8bite,16bites,32bites,64bites---举个例子吧--比如说,如
          如果你现在创建了一个存储--灰度图片的Mat对象,这个图像的大小为宽100,高100,那么,现在这张
          灰度图片中有10000个像素点，它每一个像素点在内存空间所占的空间大小是8bite,8位--所以它对应的就是CV_8
- --S|U|F--S--代表---signed int---有符号整形
                 U--代表--unsigned int--无符号整形
                 F--代表--float---------单精度浮点型
- C<number_of_channels>----代表---一张图片的通道数,比如:
           1--灰度图片--grayImg---是--单通道图像
           2--RGB彩色图像---------是--3通道图像
           3--带Alph通道的RGB图像--是--4通道图像





Size类等效于一个成对数据，size::Size(cols,rows)，**特别注意 cols和rows的位置**



###### 示例

```c++
Mat src1(3, 4, CV_32FC3); 
Mat src2(Size(3, 4), CV_32FC3); 

```



#### Mat(int ndims,const int *  sizes,int type,const Scalar& s) 

```
cv::Mat::Mat(int ndims,const int *  sizes,int type,const Scalar& s) 
cv::Mat::Mat(const Mat & m)
```

该构造函数与使用了Scalar参数，作用是能够通过Scalar数据类来初始化元素值，例如，我们要生成一张白色背景的图片

```c++
Mat src1(300, 400, CV_8UC3,Scalar(255,255,255));
imshow("test", src1);
```

#### 成员函数

##### at函数

at函数的功能是访问矩阵元素，根据不同的使用场景，有多个重载函数可供选择。 

示例

```c++
//获取jpg图像的(0，0) 元素
Mat src = imread("test.jpg");
int elem = src.at<int>(0,0);  
```

##### **convertTo函数**

```
void cv::Mat::convertTo(OutputArray m,int rtype,double alpha = 1,double beta = 0)   const
```

转换矩阵存储类型，具体计算公式如下：

```
m(x,y)=saturate_cast<rType>(α(∗this)(x,y)+β)
```

m是输入矩阵，rtype是目标类型，alpha是放缩系数，beta是增减标量

这个函数也**至关重要**，因为在数字图像处理中，矩阵是最基本的运算单位，而**矩阵的数据类型转换全靠该函数来实现**，比如说，从八位无符号数到32位浮点型的转换

```
Mat image = imread("test.png",IMREAD_COLOR);
image.convertTo(CV_32FC3)；
```



##### 常用基本函数



```c++

    int cv::Mat::channels   ()  const   //获取通道数
    Mat cv::Mat::clone()    const		//深拷贝
    void cv::Mat::copyTo(OutputArray    m)  const  //复制数据
    int cv::Mat::depth()    const   //返回图像深度
    Mat cv::Mat::diag(int   d = 0)  const  //提取矩阵的对交元素
    
    MatExpr cv::Mat::mul(InputArray m,double scale = 1 )    const  //矩阵乘法
    MatExpr cv::Mat::inv(int    method = DECOMP_LU) const //逆矩阵
    MatExpr cv::Mat::t() const//返回转置矩阵
    size_t cv::Mat::total() const  //返回矩阵的元素总个数，如30*40的图像，存在1200个像素点
    
    int cv::Mat::cols; //返回矩阵的列数 
	int cv::Mat::rows // 返回矩阵行数 
    uchar* cv::Mat::data // 指向矩阵的数据单元的指针 
    int cv::Mat::dims // 返回矩阵维度，该维度≥2 MatSize 
    cv::Mat::size // 返回矩阵大小

```



#### 参考资料

1. [cv::Mat Class Reference](https://docs.opencv.org/master/d3/d63/classcv_1_1Mat.html)



