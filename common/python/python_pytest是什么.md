

>  安徐正静



## pytest 特点

pytest是一个非常成熟的全功能的Python测试框架，主要有以下几个特点：

- 简单灵活，容易上手
- 支持参数化
- 能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）
- `pytest`具有丰富第三方插件，良好的自定义扩展
- 测试用例的skip和xfail处理
- 可以很好的和jenkins集成
- report框架----allure 也支持了pytest

## 支持插件


完整的插件list，可以到下面这三个站点看看：

1. https://docs.pytest.org/en/latest/plugins.html

2. https://pypi.python.org

3. https://github.com/pytest-dev

下面是一些出名的插件list:

- pytest-repeat: 可以多次运行测试用例，用来提高发现那些偶然错误的几率
- pytest-xdist: 可以利用机器的多核，提升测试的速度
- pytest-timeout: 可以为测试加入超时
- pytest-instatfail: 在错误发生的时候，立即报告它
- pytest-sugar: 整合了pytest-instatfail以及代码高亮，颜色字体...
- pytest-emoji: 为测试报告加入了一些有趣的东西
- pytest-html: 在测试完成后，会生成一份html报告文件
- pytest-pycodestyle, pytest-pep8, pytest-flake8: 进行代码规范检查
- pytest-rerunfailures（失败case重复执行）
- pytest-selenium
- pytest-django
- pytest-flask    



## 安装

```bash
pip install -U pytest
```

验证安装的版本：

```bash
pytest --version
```

### 例子

```python
import pytest

# content of test_sample.py
def func(x):
    return x + 1
def test_answer():
    assert func(3) == 5

```

命令行切换到文件所在目录，执行测试（也可以直接在IDE中运行）

```
pytest  xxx.py
```

当需要编写多个测试样例的时候，我们可以将其放到一个测试类当中，如

```python
class TestClass:  
    def test_one(self):  
        x = "this"  
        assert 'h' in x  
  
    def test_two(self):  
        x = "hello"  
        assert hasattr(x, 'check') 
```



## **如何编写pytest测试样例**

规则：

- 测试文件以test_开头（以_test结尾也可以）
- 测试类以Test开头，并且不能带有 **init** 方法
- 测试函数以test_开头
- 断言使用基本的assert即可



## 运行模式

   Pytest的多种运行模式，让测试和调试变得更加得心应手，下面介绍5种常用的模式。在介绍之前需要提醒一句，运行pytest时会找当前目录及其子目录中的所有test_*.py 或 *_test.py格式的文件以及以test开头的方法或者class，不然就会提示找不到可以运行的case了。

**1.运行后生成测试报告（htmlReport）**

安装pytest-html：

```bash
pip install -U pytest-html
```

运行模式：

```
pytest --html=report.html
```

报告效果：



![img](https:////upload-images.jianshu.io/upload_images/6536777-15708c4ed724a509.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)





在以上报告中可以清晰的看到测试结果和错误原因，定位问题很容易。

**2.运行指定的case**

  当我们写了较多的cases时，如果每次都要全部运行一遍，无疑是很浪费时间的，通过指定case来运行就很方便了。

例子代码：

```
class TestClassOne(object):
    def test_one(self):
        x = "this"
        assert 't'in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


class TestClassTwo(object):
    def test_one(self):
        x = "iphone"
        assert 'p'in x

    def test_two(self):
        x = "apple"
        assert hasattr(x, 'check')
```

运行模式：

模式1：直接运行test_se.py文件中的所有cases:

```
pytest test_se.py
```

模式2：运行test_se.py文件中的TestClassOne这个class下的两个cases:

```
pytest test_se.py::TestClassOne
```

模式3：运行test_se.py文件中的TestClassTwo这个class下的test_one:

```
pytest test_se.py::TestClassTwo::test_one
```

> 注意：定义class时，需要以T开头，不然pytest是不会去运行该class的。

**3.多进程运行cases**

  当cases量很多时，运行时间也会变的很长，如果想缩短脚本运行的时长，就可以用多进程来运行。

安装pytest-xdist：

```
pip install -U pytest-xdist
```

运行模式：

```
pytest test_se.py -n NUM
```

其中NUM填写并发的进程数。

**4.重试运行cases**

  在做接口测试时，有事会遇到503或短时的网络波动，导致case运行失败，而这并非是我们期望的结果，此时可以就可以通过重试运行cases的方式来解决。

安装pytest-rerunfailures：

```
pip install -U pytest-rerunfailures
```

运行模式：

```
pytest test_se.py --reruns NUM
```

NUM填写重试的次数。

**5.显示print内容**

  在运行测试脚本时，为了调试或打印一些内容，我们会在代码中加一些print内容，但是在运行pytest时，这些内容不会显示出来。如果带上-s，就可以显示了。

运行模式：

```
pytest test_se.py -s
```

  另外，pytest的多种运行模式是可以叠加执行的，比如说，你想同时运行4个进程，又想打印出print的内容。可以用：

```
pytest test_se.py -s -n 4
```

## 参考链接

1. [unittest和pytest对比](https://www.cnblogs.com/xiaohuhu/p/9804527.html)

2. [全功能Python测试框架：pytest](https://www.jianshu.com/p/932a4d9f78f8)

3. [Full pytest documentation](https://docs.pytest.org/en/latest/contents.html)

4.  [Pytest学习笔记](https://www.cnblogs.com/sparkling-ly/category/851617.html)

5.  [pytest单元测试框架](https://blog.csdn.net/liuchunming033/article/category/3193659)

   