



```bash
pip install turtle 
```



https://files.pythonhosted.org/packages/ff/f0/21a42e9e424d24bdd0e509d5ed3c7dfb8f47d962d9c044dba903b0b4a26f/turtle-0.0.2.tar.gz
  按照网址下载安装包，进行源码安装！

在setup.py里面进行修改：

修改第40行代码如下（其实就是增加了括号，python2的语法格式是没有括号的，但是python3没有括号就会报错，就像print函数）  

   except (ValueError, ve):



```python
# Most of the following code is from Divmod Epsilon, (C) 2008 Divmod, Inc.
# under MIT license, see http://divmod.org/trac/wiki/DivmodEpsilon
# since I only need this to install turtle correctly with Twisted
# Plugins I'd rather copy this few lines than actually add another
# dependency. Also this version uses the setuptools setup() function.

def pluginModules(moduleNames):
    from twisted.python.reflect import namedAny
    for moduleName in moduleNames:
        try:
            yield namedAny(moduleName)
        except ImportError:
            pass
        except (ValueError, ve):
            if ve.args[0] != 'Empty module name':
                traceback.print_exc()
        except:
            traceback.print_exc()
```



然后进入cmd命令窗口进行：再用pip安装，此处 pip install 后面接的是你修改好的turtle文件夹所在位置

pip install   C:\Users\XXX\Desktop\turtle-0.0.2



## 参考链接

1. https://blog.csdn.net/weixin_42429173/article/details/90034524