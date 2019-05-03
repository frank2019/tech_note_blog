

```

```



#### NumPy 是什么？

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的多维数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

NumPy 的前身 Numeric 最早是由 Jim Hugunin 与其它协作者共同开发，2005 年，Travis Oliphant 在  Numeric 中结合了另一个同性质的程序库 Numarray 的特色，并加入了其它扩展而开发了 NumPy。NumPy  为开放源代码并且由许多协作者共同维护开发。

是python科学计算库的基础库，许多其他著名的科学计算库如Pandas，Scikit-learn等都要用到Numpy库的一些功能。

#### NumPy能做什么？

NumPy 是一个运行速度非常快的数学库，主要用于数组计算，包含：

这类数值计算广泛用于以下任务：

- **机器学习模型**：在编写机器学习算法时，需要对矩阵进行各种数值计算。例如矩阵乘法、换位、加法等。NumPy提供了一个非常好的库，用于简单(在编写代码方面)和快速(在速度方面)计算。NumPy数组用于存储训练数据和机器学习模型的参数。
- **图像处理和计算机图形学**：计算机中的图像表示为多维数字数组。NumPy成为同样情况下最自然的选择。实际上，NumPy提供了一些优秀的库函数来快速处理图像。例如，镜像图像、按特定角度旋转图像等。
- **数学任务**：NumPy对于执行各种数学任务非常有用，如数值积分、微分、内插、外推等。因此，当涉及到数学任务时，它形成了一种基于Python的MATLAB的快速替代。



如果有以上需求，可以使用NumPy。



#### Hello NumPy



```python
import numpy as np

#创建一维数组
a = np.array([1,2,3,4,5])  
print(a)
print(a.shape)

a[0] = -1
#创建一维数组 值全为0
b = np.zeros(5)

#创建一维数组 值为0-1 之间的随即值
c = np.random.random(5)

#创建一维数组 值为1 
c = np.ones(5)

#创建二维数组
d2 = np.zeros((2,3))


e1 = np.array([[1,3],[3,4]])
e2 = np.array([[2,3],[4,5]])

#矩阵按相应位的加减乘除运算
sum = e1 + e2
di = e1 - e2
product = e1 * e2
quotient = e1 /e2

print("sum= %r\n" %(sum))
print("di= %r\n" %(di))
print("product = %r\n" %(product))
print("quotient= %r\n" %(quotient))


#矩阵的乘法

f = e1.dot(e2)
print("f= %r\n" %(f))

```



#### 参考链接

1. [NumPy 中文文档](https://www.numpy.org.cn/article/basics/index.html)
2. [NumPy 教程 ](https://www.runoob.com/numpy/numpy-tutorial.html)
3. https://cloud.tencent.com/info/1de1d4b5cb1b3147d07262cec8f58f2e.html

