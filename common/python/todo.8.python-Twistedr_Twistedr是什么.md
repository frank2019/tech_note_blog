

# 简介

Twisted是基于事件驱动的网络引擎框架，支持Python2.7和3.3+。它包括很多不同的模块，如：

- twisted.web：HTTP客户和服务端，HTML模板，和一个WSGI服务器
- twisted.conch:基于SSHv2和Telnet协议的的客户端，服务器和终端模拟器
- twisted.words:基于IRC，XMPP和其他IM协议的客户端和服务器
- twisted.mail：基于IMAPv4，POP3，SMTP的客户端和服务器
- twisted.positioning:和NMEA（国际海上电子协会）兼容的GPS接收者通信的工具
- twisted.names:DNS客户端和工具可用于构建自己的DNS服务器
- twisted.trial:和基于Twisted的代码高度整合的单元测试框架

twisted支持所有主流的事件轮询机制：select（所有平台）、poll（大部分POSIX平台）、epoll（Linux）、kqueue（FreeBSD,OSX）、OCP（Windows)和各种GUI事件轮询机制（GTK+2/3、QT、wxWidgets）。第三方的reactors也可以加入到twisted中来支持额外的事件轮询机制。

# 示例

## 安装

```bash
pip install twisted
```

## echo server

回显服务器，将收到的内容返回给客户端。



https://twistedmatrix.com/trac/

# 参考链接

1. [Twisted：一个基于事件驱动的网络引擎](http://hao.jobbole.com/twisted/)
2. 官方网站：<http://twistedmatrix.com/trac/>
3. 开源地址：<https://github.com/twisted/twisted>