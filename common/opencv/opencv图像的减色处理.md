

```
知之为知之
```

图像的减色处理跟二值化类似，只不过二值化是将图像转化为0，1 两种值，而减色处理则是，将彩色图每个通道的对应像素转换为给定的几个枚举值。

示例：

这里我们将图像的值由256^3压缩至4^3，即将 RGB 的值只取 {32, 96, 160, 224}。这被称作色彩量化。色彩的值按照下面的方式定义：



```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori.jpg")

# Dicrease color
out = img.copy()

#" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法
out = out // 64 * 64 + 32     

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

