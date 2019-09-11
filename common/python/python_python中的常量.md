https://blog.csdn.net/GentleCP/article/details/88625595





一个好的python程序员除了能够把功能、逻辑实现以外，还应该让你的代码可读性更强、拓展性更高。遵循良好的编码风格

本文主要介绍python编程中经常用到的固定变量应该如何进行编写。

在我们编写程序的时候有的变量一旦在设定之后就不会再进行变动，对于这些变量，称之为const变量。python中没有自带const变量，不过我们可以自定义一个。



定义const.py文件

```python
# -*- coding: utf-8 -*-
# python 3.x
# Filename:const.py
# 定义一个常量类实现常量的功能
# 
# 该类定义了一个方法__setattr()__,和一个异常ConstError, ConstError类继承 
# 自类TypeError. 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典 
# 中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。 
# 最后两行代码的作用是把const类注册到sys.modules这个全局字典中。
class _const:
    class ConstError(TypeError):pass
    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" %name)
        self.__dict__[name]=value
        
import sys
sys.modules[__name__]=_const()

```



使用

```python
import const

const.kMattoDBName = 'matto.db'
print(const.kMattoDBName)
```

