```

```



# tornado 简介

Tornado 是一个开源的网络服务器框架，该平台基于社交聚合网站 FriendFeed  的实时信息服务开发而来。2007年，4名谷歌前软件工程师一起创办了 FriendFeed，旨在使用户能方便地跟踪好友在 Facebook 和  Twitter 等多个社交网站上的活动。结果两年后，Facebook 宣布收购  FriendFeed，这一交易的价格约为5000万美元。而此时，FriendFeed 只有12名员工。据说这帮人后来又到了  Google，搞出了现在的Google App Engine …… 

[Tornado](http://www.nowamagic.net/academy/tag/Tornado)  是 FriendFeed 使用的可扩展的非阻塞式 web 服务器及其相关工具的开源版本。这个 Web 框架看起来有些像 web.py 或者  Google 的 webapp，不过为了能有效利用非阻塞式服务器环境，这个 Web 框架还包含了一些相关的有用工具和优化。

Tornado 和现在的主流 Web 服务器框架（包括大多数 Python  的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。得利于其非阻塞的方式和对 epoll 的运用，Tornado  每秒可以处理数以千计的连接，这意味着对于实时 Web 服务来说，Tornado 是一个理想的 Web 框架。



## 特点

- tornado 是一个异步网络通讯框架
- Http 服务框架
- 支持Websockets



## Tornado VS Django

### Django：

重量级web框架，功能大而全，注重高效开发

- 内置管理后台
- 内置封装完善的ORM操作
-  session功能
- 后台管理
- 缺陷：高耦合
  

###  Tornado：

轻量级web框架，功能少而精，注重性能优越

- HTTP服务器
- 异步编程
- WebSocket
- 缺陷：入门门槛较高



# tornado 组成

Tornado 是个轻量级框架，它的[模块](http://www.nowamagic.net/academy/tag/模块)不多，最重要的一个模块是[web](http://github.com/facebook/tornado/blob/master/tornado/web.py)， 它就是包含了 Tornado 的大部分主要功能的 Web 框架。其它的模块都是工具性质的， 以便让 web 模块更加有用 后面的 Tornado 攻略 详细讲解了 web 模块的使用方法。

## 主要模块

- [web](http://github.com/facebook/tornado/blob/master/tornado/web.py) - FriendFeed 使用的基础 Web 框架，包含了 Tornado 的大多数重要的功能
- [escape](http://github.com/facebook/tornado/blob/master/tornado/escape.py) - XHTML, JSON, URL 的编码/解码方法
- [database](http://github.com/facebook/tornado/blob/master/tornado/database.py) - 对 MySQLdb 的简单封装，使其更容易使用
- [template](http://github.com/facebook/tornado/blob/master/tornado/template.py) - 基于 Python 的 web 模板系统
- [httpclient](http://github.com/facebook/tornado/blob/master/tornado/httpclient.py) - 非阻塞式 HTTP 客户端，它被设计用来和 web 及 httpserver 协同工作
- [auth](http://github.com/facebook/tornado/blob/master/tornado/auth.py) - 第三方认证的实现（包括 Google OpenID/OAuth、Facebook Platform、Yahoo BBAuth、FriendFeed OpenID/OAuth、Twitter OAuth）
- [locale](http://github.com/facebook/tornado/blob/master/tornado/locale.py) - 针对本地化和翻译的支持
- [options](http://github.com/facebook/tornado/blob/master/tornado/options.py) - 命令行和配置文件解析工具，针对服务器环境做了优化

## 底层模块

- [httpserver](http://github.com/facebook/tornado/blob/master/tornado/httpserver.py) - 服务于 web 模块的一个非常简单的 HTTP 服务器的实现
- [iostream](http://github.com/facebook/tornado/blob/master/tornado/iostream.py) - 对非阻塞式的 socket 的简单封装，以方便常用读写操作
- [ioloop](http://github.com/facebook/tornado/blob/master/tornado/ioloop.py) - 核心的 I/O 循环

# 简单示例

## 安装

```

```

## hello server

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```

### 代码运行：

1. 这是官方提供了Hello, World实例，
2. 执行`python hello.py`，启动服务
3. 打开浏览器访问<http://localhost:8888/>
4. 看到网页显示 `Hello, world`

### 代码解释

一个普通的tornado web服务器通常由四大组件组成。

1. ioloop实例，它是全局的tornado事件循环，是服务器的引擎核心，示例中`tornado.ioloop.IOLoop.current()`就是默认的tornado ioloop实例。
2. app实例，它代表着一个完成的后端app，它会挂接一个服务端套接字端口对外提供服务。一个ioloop实例里面可以有多个app实例，示例中只有1个，实际上可以允许多个，不过一般几乎不会使用多个。
3. handler类，它代表着业务逻辑，我们进行服务端开发时就是编写一堆一堆的handler用来服务客户端请求。
4. 路由表，它将指定的url规则和handler挂接起来，形成一个路由映射表。当请求到来时，根据请求的访问url查询路由映射表来找到相应的业务handler。

这四大组件的关系是，一个ioloop包含多个app(管理多个服务端口)，一个app包含一个路由表，一个路由表包含多个handler。ioloop是服务的引擎核心，它是发动机，负责接收和响应客户端请求，负责驱动业务handler的运行，负责服务器内部定时任务的执行。

当一个请求到来时，ioloop读取这个请求解包成一个http请求对象，找到该套接字上对应app的路由表，通过请求对象的url查询路由表中挂接的handler，然后执行handler。handler方法执行后一般会返回一个对象，ioloop负责将对象包装成http响应对象序列化发送给客户端。

# 参考链接

1. [tornado官方文档](http://www.tornadoweb.org/en/stable/)
2. [Tornado编程实践建议](http://www.nowamagic.net/academy/detail/1332177)
3. Set-ExecutionPolicy RemoteSigned