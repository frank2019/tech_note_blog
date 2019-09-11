

# Python import其他文件夹的文件          



## 相同目录下

一般情况下，import的文件和被import的文件在同一个路径下面，import也比较方便。

```
form A  import *
```



## 不同目录

如果这两个文件不在一个路径下面，import就比较麻烦了，需要在被import的文件路径下面新建一个`__init__.py`文件，可以是一个没有代码的空文件。

比如被import的文件路径是../A/B/b.py下面，那么在在文件夹A、B下面分别新建一个`__init__.py`文件，然后按照下面的语句引用：

```
import A.B.b
```