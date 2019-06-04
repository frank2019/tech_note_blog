通道的交换



```
千里之行始于足下
```

#### 通道的交换

题目：

读取图像，然后将RGB通道替换成BGR通道。



```python
import cv2

# Read image
img = cv2.imread("imori.jpg")  #BGR格式
b = img[:, :, 0].copy()  #切片取第0维
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB > BGR
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# Save result
cv2.imwrite("out.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

#### 灰度化（Grayscale）

将图像灰度化吧！灰度是一种图像亮度的表示方法，通过下式计算：

```
Y = 0.2126 R + 0.7152 G + 0.0722 B
```

```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray scale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

参考链接

https://github.com/KuKuXia/Image_Processing_100_Questions