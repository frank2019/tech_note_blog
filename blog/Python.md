

# ToDO



单元测试PyUnit 



### LATEX数学公式基本语法

#### 上标与下标

上标命令是 ^{角标}，下标命令是 _{角标}



1. [CSDN-markdown语法之怎样使用LaTeX语法编写数学公式](http://www.cnblogs.com/lcchuguo/p/5061692.html)



-----------------------------------------------

# python   

python网络数据采集



wordpress   提交文章接口

https://blog.csdn.net/su_tianbiao/article/details/50622682



1. [Python爬虫工程师告诉你爬虫应该怎么学，太详细了！](http://baijiahao.baidu.com/s?id=1578594478424685451&wfr=spider&for=pc)
2. 





RESTful架构与传统的RPC、SOAP等方式 



### 0x05 python 是request 发送post 请求

安装模块

```
pip install requests
```





#### 参考链接

1.[快速上手](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)



### T0x05 Python 项目目录结构规范

1. 良好的项目结构和良好的编码风格 对于项目质量十分重要





#### 目录结构约定

```
Foo/
|-- bin/
|   |-- foo
|
|-- foo/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |
|   |-- __init__.py
|   |-- main.py
|
|-- docs/
|   |-- conf.py
|   |-- abc.rst
|
|-- setup.py
|-- requirements.txt
|-- README
```



1. `bin/`: 存放项目的一些可执行文件，文件名可自定义。
2. `foo/`: 项目的所有源代码。(1) 源代码中的所有模块、包都应该放在此目录。不要置于顶层目录。(2) 其子目录`tests/`存放单元测试代码； (3) 程序的入口最好命名为`main.py`。
3. `docs/`: 存放一些文档。
4. `setup.py`: 安装、部署、打包的脚本。
5. `requirements.txt`: 存放软件依赖的外部Python包列表。
6. `README`: 项目说明文件。

#### Readme.md内容说明

每个项目都应该有的一个文件，简要描述该项目的信息。

主要说明以下几个事项:

1. 软件定位，软件的基本功能。
2. 运行代码的方法: 安装环境、启动命令等。
3. 简要的使用说明。
4. 代码目录结构说明，更详细点可以说明软件的基本原理。
5. 常见问题说明。



可以参考Redis源码中[Readme](https://github.com/antirez/redis#what-is-redis)的写法，这里面简洁但是清晰的描述了Redis功能和源码结构。



#### setup.py



1. `setup.py`来管理代码的打包、安装、部署问题。
2. 业界标准的写法是用Python流行的打包工具[setuptools](https://pythonhosted.org/setuptools/setuptools.html#developer-s-guide)来管理这些事情。这种方式普遍应用于开源项目中
3. 一个项目一定要有一个安装部署工具，能快速便捷的在一台新机器上将环境装好、代码部署好和将程序运行起来。
4. setup.py可以将这些事情自动化起来，提高效率、减少出错的概率。"复杂的东西自动化，能自动化的东西一定要自动化。"是一个非常好的习惯。



可以参考   flask是如何写的: [setup.py](https://github.com/mitsuhiko/flask/blob/master/setup.py)



#### requirements.txt

这个文件存在的目的是:

1. 方便开发者维护软件的包依赖。将开发过程中新增的包添加进这个列表中，避免在`setup.py`安装依赖时漏掉软件包。
2. 方便读者明确项目使用了哪些Python包。

这个文件的格式是每一行包含一个包依赖的说明，通常是`flask>=0.10`这种格式，要求是这个格式能被`pip`识别，这样就可以简单的通过 `pip install -r requirements.txt`来把所有Python包依赖都装好了。具体格式说明： [点这里](https://pip.readthedocs.org/en/1.1/requirements.html)。

 

#### 关于配置文件的使用方法

注意，在上面的目录结构中，没有将`conf.py`放在源码目录下，而是放在`docs/`目录下。

很多项目对配置文件的使用做法是:

1. 配置文件写在一个或多个python文件中，比如此处的conf.py。
2. 项目中哪个模块用到这个配置文件就直接通过`import conf`这种形式来在代码中使用配置。

这种做法我不太赞同:

1. 这让单元测试变得困难（因为模块内部依赖了外部配置）
2. 另一方面配置文件作为用户控制程序的接口，应当可以由用户自由指定该文件的路径。
3. 程序组件可复用性太差，因为这种贯穿所有模块的代码硬编码方式，使得大部分模块都依赖`conf.py`这个文件。

所以，我认为配置的使用，更好的方式是，

1. 模块的配置都是可以灵活配置的，不受外部配置文件的影响。
2. 程序的配置也是可以灵活控制的。

能够佐证这个思想的是，用过nginx和mysql的同学都知道，nginx、mysql这些程序都可以自由的指定用户配置。

所以，不应当在代码中直接`import conf`来使用配置文件。上面目录结构中的`conf.py`，是给出的一个配置样例，不是在写死在程序中直接引用的配置文件。可以通过给`main.py`启动参数指定配置路径的方式来让程序读取配置内容。当然，这里的`conf.py`你可以换个类似的名字，比如`settings.py`。或者你也可以使用其他格式的内容来编写配置文件，比如`settings.yaml`之类的。



#### “_init__.py” 文件的使用



1."__ init __.py"的在文件夹中，可以使文件夹变为一个python模块，python的每个模块对应的包中都有一个__init__.py文件的存在

2.通常__init__.py文件为空，但是我们还可以为它增加其他的功能，我们在导入一个模块时候（也叫包），实际上导入的是这个模块的__init__.py文件。我们可以在__init__.py导入我们需要的模块，不需要一个个导入

3._init__.py 中还有一个重要的变量，叫做 __all__。我们有时会使出一招“全部导入”，也就是这样：from PackageName import **，这时 import 就会把注册在包 __init__.py 文件中 __all__ 列表中的子模块和子包导入到当前作用域中来。比如：*

*#文件 __init__.py*

```
__all__ = ["Module1", "Module2", "subPackage1", "subPackage2"]
```





#### 参考链接

1. [Python学习-软件目录结构规范](https://www.cnblogs.com/Ian-learning/p/8366634.html)
2. [Open Sourcing a Python Project the Right Way](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way)





### 0x04  python2  和python3 的主要区别



1. python的 print 声明已经被 `print()` 函数 

2. python3将raw_input和input进行了整合，只有input

3. python3 中的  X/Y 整数与整数的除法，结果是一个浮点数   ，这一点与python2  不同

4. python3   中打印不带回车      print("nei long",end='')

   python2 中  print("neirong"),     以，结尾



### 0x03 BeautifulSoup  HTML/XML的解析器 



Beautiful Soup 是用Python写的一个HTML/XML的解析器，它可以很好的处理不规范标记并生成剖析树(parse tree)。 它提供简单又常用的导航（navigating），搜索以及修改剖析树的操作。它可以大大节省你的编程时间。



```
pip install beautifulsoup4
```



```python
from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"html5lib")
print(bsObj.h1)
```





```


    '''
    r = requests.get(url='http://www.itwhy.org')    # 最基本的GET请求
    print(r.status_code)    # 获取返回状态
    r = requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})   #带参数的GET请求
    print(r.url)
    print(r.text)   #打印解码后的返回数据
    '''
```



### 0x02 python json


本文实例讲述了Python简单读取json文件功能。分享给大家供大家参考，具体如下：

config.json:

```
{
    "aid": [
        "40",
        "44"
    ],
    "rule": {
        "namespace": "strategy",
        "name": "test_exp_1496234234223400",
        "version": 0,
        "last_modify_time": 1434234236819000,
        "log_rate": 1023300,
        "schema_version": "hello_world!"
    }
}
```

read_json.py:

```python
    # -*- coding:utf-8 -*-
	import json
    basedir = os.path.abspath(os.path.dirname(__file__))
    config=basedir+'/config.json'

    if not os.path.exists(config):
        print 'config not exist!'
        return None
    
    
    with open(config, 'r') as f:
        temp = json.loads(f.read())
        print(temp)
        print(temp['rule'])
        print(temp['rule']['namespace'])
        print(temp['aid'])
      
```

运行结果：



-----



1. [python中sqlite3对数据库的增删改查](https://blog.csdn.net/liuyanlin610/article/details/76021959)
2. [BaseHTTPServer构建基本服务器](https://blog.csdn.net/adream307/article/details/47403365)
3. [Python类对象的JSON序列化处理](https://blog.csdn.net/jerry_1126/article/details/76409042)





### 0x01 python 守护进程的实现

守护进程最重要的特性是后台运行；它必须与其运行前的环境隔离开来，这些环境包括未关闭的文件描述符、控制终端、会话和进程组、工作目录以及文件创建掩码等；它可以在系统启动时从启动脚本/etc/rc.d中启动，可以由inetd守护进程启动，也可以有作业规划进程crond启动，还可以由用户终端（通常是shell）执行。



#### 参考链接

1. [Python实例浅谈之五Python守护进程和脚本单例运行](http://blog.csdn.net/taiyang1987912/article/details/44850999)





---------------------









#### Flask-

使用Flask-SQLAlchemy操作MySQL数据库

使用

1. [一个初学者的辛酸路程-python操作SQLAlchemy-13](http://www.cnblogs.com/jixuege-1/p/6272888.html)

2. [Flask使用Flask-SQLAlchemy操作MySQL数据库](http://www.cnblogs.com/xiaoxi-3-/p/8026504.html)

3. http://flask-sqlalchemy.pocoo.org/2.3/config/

4. https://www.cnblogs.com/xiaoxi-3-/p/8026504.html

   ​





#### 参考链接

1. [Python获取并输出当前日期时间](http://www.cnblogs.com/kerwinC/p/5760811.html)



创建所有表

```
#db.create_all()
```




https://www.zhihu.com/question/42186243

#### Flask-Login

Flask-Login 为 Flask 提供了用户会话管理。它处理了日常的登入，登出并且长时间记住用户的会话。

它会:

- 在会话中存储当前活跃的用户 ID，让你能够自由地登入和登出。
- 让你限制登入(或者登出)用户可以访问的视图。
- 处理让人棘手的 “记住我” 功能。
- 帮助你保护用户会话免遭 cookie 被盗的牵连。
- 可以与以后可能使用的 Flask-Principal 或其它认证扩展集成。

但是，它不会:

- 限制你使用特定的数据库或其它存储方法。如何加载用户完全由你决定。
- 限制你使用用户名和密码，OpenIDs，或者其它的认证方法。
- 处理超越 “登入或者登出” 之外的权限。
- 处理用户注册或者账号恢复。






#### Flask Web  

1.  python中两个下划线包裹的变量 含义




[flask_script的几个具体用法](http://blog.csdn.net/u010445540/article/details/52957420)



#### Flask-Bootstrap



参考链接

http://flask-bootstrap-zh.readthedocs.io/zh/latest/basic-usage.html

http://docs.jinkan.org/docs/flask/

https://github.com/miguelgrinberg/flasky





参考链接

1. [Flask中Jinja2模板引擎详解](http://www.bjhee.com/jinja2-block-macro.html)
2. [Flask-SQLAlchemy 文档](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html)






#### 参考链接

1. [Creating Flask RESTful API Using Python & MySQL](https://codehandbook.org/flask-restful-api-using-python-mysql/)
2. [Flask：一个使用Python编写的轻量级Web应用框架](http://hao.jobbole.com/flask/)
3. [哪些 Python 库让你相见恨晚？](https://www.zhihu.com/question/24590883)
4. [python实现RESTful服务（基于flask）](https://www.jianshu.com/p/6ac1cab17929)






### centos安装pip

yum -y install epel-release

yum install python-pip



解决Python.h No such file or directory

1.可以先查看一下含python-devel的包

​    yum search python | grep python-devel

2.64位安装python-devel.x86_64，32位安装python-devel.i686，我这里安装:

​    sudo yum install python-devel.x86_64

1. 进入/usr/include/python2.7看一下现在有没有Python.h，版本不同目录名不同，我这里是2.7版本。其实也可以看到很多.h文件，python需要库或头文件都在这个地方。

如果是其他Linux发行版，也可以用相应的方法。suse用YaST，deb系用apt-get。





### No module named MYSQLdb 问题解决

​			[No module named MYSQLdb 问题解决](http://www.cnblogs.com/guohaojintian/p/6030818.html)		

#### 问题描述：

报错：ImportError: No module named MySQLdb

#### 对于不同的系统和程序有如下的解决方法：

1. easy_install mysql-python (mix os)
2. pip install mysql-python (mix os)
3. apt-get install python-mysqldb (Linux Ubuntu)
4. cd/usr/ports/databases/py-MySQLdb && make install clean (FreeBSD)
5. yum install MySQL-python (linux Fedora, CentOS)
6. pip install mysqlclient (Windows)

更多内容请参考下面的这两个链接：

<http://stackoverflow.com/questions/454854/no-module-named-mysqldb>

<http://stackoverflow.com/questions/21440230/install-mysql-python-windows>

 

当你遇到问题无法解决而抓狂的时候，可以看看网友的抱怨，原来还有另外的人跟你一样的抓狂~~~

:)



# CSS

## CSS 概述

- CSS 指层叠样式表 (*C*ascading *S*tyle *S*heets)
- 样式定义*如何显示* HTML 元素
- 样式通常存储在*样式表*中
- 把样式添加到 HTML 4.0 中，是为了*解决内容与表现分离的问题*
- *外部样式表*可以极大提高工作效率
- 外部样式表通常存储在 *CSS 文件*中
- 多个样式定义可*层叠*为一



## 样式表极大地提高了工作效率

样式表定义如何显示 HTML 元素，就像 HTML 3.2 的字体标签和颜色属性所起的作用那样。样式通常保存在外部的 .css 文件中。通过仅仅编辑一个简单的 CSS 文档，外部样式表使你有能力同时改变站点中所有页面的布局和外观。

由于允许同时控制多重页面的样式和布局，CSS 可以称得上 WEB 设计领域的一个突破。作为网站开发者，你能够为每个 HTML 元素定义样式，并将之应用于你希望的任意多的页面中。如需进行全局的更新，只需简单地改变样式，然后网站中的所有元素均会自动地更新。



## 多重样式将层叠为一个

样式表允许以多种方式规定样式信息。样式可以规定在单个的 HTML 元素中，在 HTML 页的头元素中，或在一个外部的 CSS 文件中。甚至可以在同一个 HTML 文档内部引用多个外部样式表。

### 层叠次序优先级

**当同一个 HTML 元素被不止一个样式定义时，会使用哪个样式呢？**

一般而言，所有的样式会根据下面的规则层叠于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。

1. 浏览器缺省设置
2. 外部样式表
3. 内部样式表（位于 <head> 标签内部）
4. 内联样式（在 HTML 元素内部）

因此，内联样式（在 HTML 元素内部）拥有最高的优先权，这意味着它将优先于以下的样式声明：<head> 标签中的样式声明，外部样式表中的样式声明，或者浏览器中的样式声明（缺省值）。





http://www.w3school.com.cn/css/css_syntax_class_selector.asp





# Android



### 0x01 android app的实现架构



参考链接

1.  [App架构经验总结](http://www.iteye.com/news/31472)
2. [一个互联网app的开发设计（技术选型和架构）](https://blog.csdn.net/brycegao321/article/details/51830525)
3.  [Android MVP Pattern](https://www.cnblogs.com/changyiqiang/p/6044618.html)
















# Go 语言

## Q&A

1. go语言中 对redis的操作



## go语言中 对redis的操作

可选择的库有好几个，这里选择了redigo

下载

`go get github.com/garyburd/redigo/redis`





### messagepack的使用





### 参考链接

1. [redis开启远程访问](http://www.cnblogs.com/liusxg/p/5712493.html)
2. [阿里云Redis公网连接的解决办法](http://www.cnblogs.com/doseoer/p/6681202.html)
3. [几种Go序列化库的性能比较](http://colobu.com/2015/09/28/Golang-Serializer-Benchmark-Comparison/)      
4. [messagepac](https://msgpack.org/)
5. [golang msgp](https://www.jianshu.com/p/34f71a86108b)
6. [GoLang redis 连接池](https://studygolang.com/articles/3029)
7. [Redis Auth 命令](http://www.redis.net.cn/order/3649.html)



[golang--- Redis 操作](http://www.cnblogs.com/mafeng/p/6322957.html)







### rinted的使用

### unity3D note

### 参考链接

1. [新手学Unity3d的一些网站及相应学习路线](http://www.cnblogs.com/zhangbaochong/p/4774684.html)
2. [Unity 开发入门指南（学习感悟）](https://www.jianshu.com/p/7f05b90f411e)





## 开发工具

### vscode for  python

下载链接：https://code.visualstudio.com/docs/?dv=win