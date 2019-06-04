```

```





## 高斯滤波（Gaussian Filter）

使用高斯滤波器（3x3 大小，标准差 s=1.3​）来对`imori_noise.jpg`进行降噪处理吧！

高斯滤波器是一种可以使图像平滑的滤波器，用于去除噪声。可用于去除噪声的滤波器还有中值滤波器（参见问题10），平滑滤波器（参见问题11）、LoG 滤波器（参见问题19）。

高斯滤波器将中心像素周围的像素按照高斯分布加权平均进行平滑化。这样的（二维）权值通常被称为卷积核或者滤波器。

但是，由于图像的长宽可能不是滤波器大小的整数倍，因此我们需要在图像的边缘补0。这种方法称作 Zero Padding。并且权值（卷积核）要进行[归一化操作](https://blog.csdn.net/lz0499/article/details/54015150)(sum g = 1)。



```
权值 g(x,y,s) = 1/ (s*sqrt(2 * pi)) * exp( - (x^2 + y^2) / (2*s^2))
标准差 s = 1.3 的 8 近邻 高斯滤波器如下：
            1 2 1
K =  1/16 [ 2 4 2 ]
            1 2 1
```



```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape


# Gaussian Filter
K_size = 3
sigma = 1.3

## Zero padding
pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

## Kernel
K = np.zeros((K_size, K_size), dtype=np.float)
for x in range(-pad, -pad+K_size):
    
    for y in range(-pad, -pad+K_size):
        K[y+pad, x+pad] = np.exp( -(x**2 + y**2) / (2* (sigma**2)))
K /= (sigma * np.sqrt(2 * np.pi))
K /= K.sum()

tmp = out.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            out[pad+y, pad+x, c] = np.sum(K * tmp[y:y+K_size, x:x+K_size, c])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

