```

```

#### 二值化（Thresholding）

图像二值化（ Image Binarization）就是将图像上的[像素](https://baike.baidu.com/item/像素/95084)点的[灰度值](https://baike.baidu.com/item/灰度值/10259111)设置为0或255，也就是将整个图像呈现出明显的黑白效果的过程。

在数字图像处理中，二值图像占有非常重要的地位，图像的二值化使图像中数据量大为减少，从而能凸显出目标的轮廓。



- 彩色图像：三个通道0-255，0-255，0-255，所以可以有2^24位空间


- 灰度图像：一个通道0-255,所以有256种颜色


- 二值图像：只有两种颜色，黑和白，1白色，0黑色

#### 给定值进行二值化

直接将阈值设置为128来进行二值化：

```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Grayscale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# Binarization
th = 128
out[out < th] = 0
out[out >= th] = 255

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### 大津二值化算法（Otsu's Method）

大津算法，也被称作最大类间方差法，是一种可以自动确定二值化中阈值的算法，从类内[方差](https://ja.wikipedia.org/wiki/%E5%88%86%E6%95%A3_(%E7%A2%BA%E7%8E%87%E8%AB%96))和类间方差的比值计算得来：

- 小于阈值 t 的类记作 0，大于阈值 t 的类记作 1；
- w0 和 w1 是被阈值 t 分开的两个类中的像素数占总像素数的比率（满足 w0+w1=1）；
- S0^2, S1^2 是这两个类中像素值的方差；
- M0, M1 是这两个类的像素值的平均值；

也就是说：

```
类内方差：Sw^2 = w0 * S0^2 + w1 * S1^2
类间方差：Sb^2 = w0 * (M0 - Mt)^2 + w1 * (M1 - Mt)^2 = w0 * w1 * (M0 - M1) ^2
图像所有像素的方差：St^2 = Sw^2 + Sb^2 = (const)
根据以上的式子，我们用以下的式子计算分离度：  
分离度 X = Sb^2 / Sw^2 = Sb^2 / (St^2 - Sb^2)
```

也就是

```
argmax_{t} X = argmax_{t} Sb^2
```

换言之，如果使 Sb^2 =  w0 * w1 * (M0 - M1) ^2 最大，就可以得到最好的二值化阈值 t。



```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)

H, W, C = img.shape

# Grayscale
out = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
out = out.astype(np.uint8)

# Determine threshold of Otsu's binarization
max_sigma = 0
max_t = 0

for _t in range(1, 255):
    v0 = out[np.where(out < _t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0.
    w1 = len(v1) / (H * W)
    sigma = w0 * w1 * ((m0 - m1) ** 2)
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = _t

# Binarization
print("threshold >>", max_t)
th = max_t
out[out < th] = 0
out[out >= th] = 255

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
```