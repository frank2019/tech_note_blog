```

```



平均池化（Average Pooling）

#### 定义

将图片按照固定大小网格分割，网格内的像素值取网格内所有像素的平均值。我们将这种把图片使用均等大小网格分割，并求网格内代表值的操作称为池化（Pooling）。

池化操作是卷积神经网络（Convolutional Neural Network）中重要的图像处理方式。

平均池化按照下式定义：

```
v = 1/|R| * Sum_{i in R} v_i
```

#### 作用

pooling的结果是使得**特征减少，参数减少**，但pooling的目的并不仅在于此。

pooling目的是为了**保持某种不变性（旋转、平移、伸缩等）**



#### 分类

常用的有mean-pooling，max-pooling和Stochastic-pooling三种。

mean-pooling，即对邻域内特征点只求平均，

max-pooling，即对邻域内特征点取最大

#### 平均池化（Average Pooling）实现

请把大小为 128x128 的`jpg`使用 8x8 的网格做平均池化。

```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Average Pooling
out = img.copy()

H, W, C = img.shape
G = 8
Nh = int(H / G)
Nw = int(W / G)

for y in range(Nh):
    for x in range(Nw):
        for c in range(C):
            out[G*y:G*(y+1), G*x:G*(x+1), c] = np.mean(out[G*y:G*(y+1), G*x:G*(x+1), c]).astype(np.int)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```



#### 最大池化（Max Pooling）

网格内的值不取平均值，而是取网格内的最大值进行池化操作



```
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Max Pooling
out = img.copy()

H, W, C = img.shape
G = 8
Nh = int(H / G)
Nw = int(W / G)

for y in range(Nh):
    for x in range(Nw):
        for c in range(C):
            out[G*y:G*(y+1), G*x:G*(x+1), c] = np.max(out[G*y:G*(y+1), G*x:G*(x+1), c])

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

