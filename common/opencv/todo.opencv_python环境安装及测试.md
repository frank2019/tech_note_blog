

`NumPy`是`Python`的一个包,擅长进行矩阵运算，Python中的opencv基于NumPy。`

#### 环境设定

在[这里](https://conda.io/miniconda.html)下载安装 `Miniconda`，官网下载有时候很慢，可以从这里下载：

```
链接：https://pan.baidu.com/s/1YYn1ex5Raykx19pqjTewtw 
提取码：sy7p 
```

配置环境变量到Path

```
D:\Program Files (x86)\anaconda3\condabin
D:\Program Files (x86)\anaconda3\Scripts
D:\Program Files (x86)\anaconda3
```

如果已经安装 `Miniconda`，打开终端，使用以下命令创建 `conda` 虚拟环境：

```
$ conda create python=3.7 -n  mycv
```

激活虚拟环境：

```
$ conda  activate mycv
```

### 2. 安装模块

使用以下的指令安装模块：

```
pip install numpy matplotlib opencv-python
```

或者可以用主目录下的 `requirements.txt` 来完成安装：

```bash
$ pip install -r requirements.txt
```

#### 3,环境测试

```python
import cv2

img = cv2.imread("assets/imori.jpg")
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```



```
$ python sample.py
```

加载指定图片，并显示。按任意键退出。





#### 参考链接

1. [图像处理100问](https://github.com/gzr2017/ImageProcessing100Wen)
2. https://www.anaconda.com/distribution/#download-section

