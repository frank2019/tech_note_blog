

深度转点云



```

```



#### 原理

##### 世界坐标点M(Xw,Yw,Zw)映射到图像点m(u,v)的过程



![](D:\MoreBetter\tech_note_blog\common\MachineVision\img\2.jpg)



针孔成像原理
$$
Z_c \begin{bmatrix} u  \\ v  \\ 1 \end{bmatrix}=\begin{bmatrix} f/d_x & 0 & u_0 \\ 0 & f/d_y & v_0 \\ 0 & 0 & 1 \end{bmatrix}[R T]\begin{bmatrix} x_w  \\ y_w  \\ z_w \\1 \end{bmatrix}
$$


其中（u，v）为图像坐标系下的任意坐标点，对应的世界坐标系点位`(xw,yw,zw)`,

`zc`:  相机坐标的z轴值

`R,T` 分别为外参矩阵的3x3旋转矩阵和3x1平移矩阵。

dx，dy：  表示一个像素的长和高。

f：表示焦距







#### 参考

2. https://blog.csdn.net/bflong/article/details/79320516
3. http://www.cnblogs.com/wangguchangqing/p/8126333.html
3. https://blog.csdn.net/baishuo8/article/details/81005993