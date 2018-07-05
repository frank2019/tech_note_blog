



## TODO
1. [入门 | 机器学习新手必看10大算法](http://www.sohu.com/a/220248494_129720)
2. [如何简单形象又有趣地讲解神经网络是什么？](https://www.zhihu.com/question/22553761)
3. [10 种机器学习算法的要点（附 Python 和 R 代码）](http://blog.jobbole.com/92021/)
4. https://www.cnblogs.com/nkwy2012/p/7875897.html
5. https://www.cnblogs.com/fangbei/p/python-time.html



单元测试PyUnit 



### LATEX数学公式基本语法

#### 上标与下标

上标命令是 ^{角标}，下标命令是 _{角标}



1. [CSDN-markdown语法之怎样使用LaTeX语法编写数学公式](http://www.cnblogs.com/lcchuguo/p/5061692.html)






### 0x02 独立同分布

独立同分布independent and identically distributed (i.i.d.)

在概率统计理论中，指随机过程中，任何时刻的取值都为随机变量，如果这些随机变量服从同一[分布](https://baike.baidu.com/item/%E5%88%86%E5%B8%83)，并且互相独立，那么这些随机变量是独立同分布。如果随机变量X1和X2独立，是指X1的取值不影响X2的取值，X2的取值也不影响X1的取值且随机变量X1和X2服从同一分布，这意味着X1和X2具有相同的分布形状和相同的分布参数，对离随机变量具有相同的分布律，对连续随机变量具有相同的[概率密度函数](https://baike.baidu.com/item/%E6%A6%82%E7%8E%87%E5%AF%86%E5%BA%A6%E5%87%BD%E6%95%B0)，有着相同的[分布函数](https://baike.baidu.com/item/%E5%88%86%E5%B8%83%E5%87%BD%E6%95%B0)，相同的期望、方差。如实验条件保持不变，一系列的抛硬币的正反面结果是独立同分布




### 0x01 线性回归

监督学习指的是有目标变量或预测目标的机器学习方法。回归与分类的不同，就在于其目标变量是否是连续数值型



#### 什么是回归

回归分析是在一系列的已知或能通过获取的自变量与因变量之间的相关关系的基础上，建立变量之间的回归方程，把回归方程作为算法模型，通过其来实现对新自变量得出因变量的关系。因此回归分析是实用的预测模型或分类模型。

凡事皆有因果关系，解读“回归”二字，其实就是由因回溯果的过程，最终得到的因与果的关系，就称为回归。

回归方法是一种对数值型连续随机变量进行预测和建模的监督学习算法。使用案例一般包括房价预测、股票走势或测试成绩等连续变化的案例。

  回归任务的特点是标注的数据集具有数值型的目标变量。也就是说，每一个观察样本都有一个数值型的标注真值以监督算法。

#### 什么是线性回归

线性回归是处理回归任务最常用的算法之一。该算法的形式十分简单，它期望使用一个超平面拟合数据集（只有两个变量的时候就是一条直线）。如果数据集中的变量存在线性关系，那么其就能拟合地非常好。

在实践中，简单的线性回归通常被使用正则化的回归方法（LASSO、Ridge 和 Elastic-Net）所代替。正则化其实就是一种对过多回归系数采取惩罚以减少过拟合风险的技术。当然，我们还得确定惩罚强度以让模型在欠拟合和过拟合之间达到平衡。

- 优点：线性回归的理解与解释都十分直观，并且还能通过正则化来降低过拟合的风险。另外，线性模型很容易使用随机梯度下降和新数据更新模型权重。
- 缺点：线性回归在变量是非线性关系的时候表现很差。并且其也不够灵活以捕捉更复杂的模式，添加正确的交互项或使用多项式很困难并需要大量时间。


- [Python](http://lib.csdn.net/base/python) 实现：http://scikit-learn.org/stable/modules/linear_model.html 
- R 实现：https://cran.r-project.org/web/packages/glmnet/index.html 



3种学习方式-监督、非监督和强化学习

基于最佳拟合线的自变量与因变量之间的线性回归模型

3 Learning styles - supervised, unsupervised & reinforcement learning

Linear Regression models relationship between independent & dependent variables via line of best fit




$$
h_θ(x)=  ∑^n_{i=0} θ_ix_i =θ^Tx
$$


Thanks  to siraj raval

**根据动物的大脑重量来预测对应体重**



```bash
pip install pandas matplotlib scikit-learn
pip  install  scipy
```



```python
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
```





参考链接

1. [深度学习笔记 - 102 - 回归模型](https://www.jianshu.com/p/be9834f3c3fe)
2. https://github.com/llSourcell/linear_regression_demo/blob/master/brain_body.txt
3. https://www.jianshu.com/p/cd5a929bec33






1. [城市公交聚合支付一体收费终端](http://www.slzrsz.com/show-22-303.html)
2. https://wenku.baidu.com/view/afcdb9783a3567ec102de2bd960590c69ec3d8fa.html
3. https://wenku.baidu.com/view/ce1fbbfb04a1b0717fd5ddfc.html?rec_flag=default&mark_pay_doc=0&mark_rec_page=1&mark_rec_position=5&mark_rec=view_r_1&clear_uda_param=1





-----------------------------------------------

# python   

python网络数据采集



wordpress   提交文章接口



https://blog.csdn.net/su_tianbiao/article/details/50622682





RESTful架构与传统的RPC、SOAP等方式 



### 0x05 python 是request 发送post 请求

安装模块

```
pip install requests
```





#### 参考链接

1.[快速上手](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

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