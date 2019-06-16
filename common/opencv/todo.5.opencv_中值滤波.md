

## 中值滤波（Median filter）

使用中值滤波器（3x 3大小）来对`imori_noise.jpg`进行降噪处理吧！

中值滤波器是一种可以使图像平滑的滤波器。这种滤波器用滤波器范围内（在这里是3x3）像素点的中值进行滤波，在这里也采用 Zero Padding。





```python
import cv2
import numpy as np

# Read image
img = cv2.imread("imori_noise.jpg")
H, W, C = img.shape


# Median Filter
K_size = 3

## Zero padding
pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

tmp = out.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

