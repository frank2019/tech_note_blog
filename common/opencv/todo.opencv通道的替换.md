通道的交换



```

```

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

