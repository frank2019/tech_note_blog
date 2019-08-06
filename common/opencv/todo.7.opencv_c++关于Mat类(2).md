```

```



```
Mat mat1；
```

1， Mat 变量使用默认构造函数初始化，当使用的时候会自动分配空间吗

```
Mat mat_amp_data(width, height, CV_16UC1, ampData);
```

是的，会进行自动分配，包括在进行convertTo的时候也会自动根据类型进行重新分配空间以适合。

convertTo转换时使用的方法：

```
m(x,y)=saturate_cast<rType>(α(∗this)(x,y)+β)
```



### 3,  cv::Mat 与内存的相互访问



#### 3.1 使用缓存区构造 Mat

```c++
Mat (int rows, int cols, int type, void *data, size_t step=AUTO_STEP)
```

使用此构造函数，可使用缓存区构造Mat，Mat不再分配缓存区，直接使用给定的缓存区。

那么理论上

> 1. 是不是对缓存区的修改即是对Mat的修改
> 2. 反之对修改Mat  即会影响缓存区

#### 3.2 疑问

如果使用此对此Mat 调用 ConvertTo 函数，Mat重新分配空间的话，是怎么处理之歌缓存区的呢

#### 3.3 访问Mat中的缓存区

```
 cv::Mat depthin = cv::imread("Depth_0.png", CV_LOAD_IMAGE_UNCHANGED);
 uint16_t *imgdata = depthin.ptr<uint16_t>(0);
 
```

imgdata是指向image第一行第一个元素的指针。



Mat  

rows   代表行数  也就是 height  

cols 代码列数 也就是width





### 参考链接

1. [opencv 3.1.0 Mat ](https://docs.opencv.org/3.1.0/d3/d63/classcv_1_1Mat.html)

