```
滴水石穿
```



> 本文主要描述：
>
> 1. Twisted是基于事件驱动的网络引擎框架
> 2. python 另一个性能优异的异步网络框架是tornado。
> 3. Twisted的简单使用

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

# twisted vs tornado



| 项目     | twisted | tornado |
| -------- | ------- | ------- |
| 依赖包   | 是      | 否      |
| I/O性能  | 低      | 高      |
| CPU占用  | 低      | 高      |
| 抽象级别 | 高      | 低      |
| 易用性   | 低      | 高      |
| 扩展功能 | 多      | 少      |
| Epoll    | 支持    | 支持    |

ornado 和 twisted，作为异步框架，是大同小异的。相对来讲 tornado 轻量级一些。  互有长短。I/O性能差不多，对计算资源的占用相差较多！  
如果追求整体性能的话，推荐使用twisted。

# 示例

## 安装

```bash
pip install twisted
```

## echo server

回显服务器，将收到的内容返回给客户端。

#### 服务端代码示例



```python
from twisted.internet import protocol, reactor, endpoints
 
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
 
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
 
endpoints.serverFromString(reactor, "tcp:8000").listen(EchoFactory())
reactor.run()
```



#### 客户端测试代码：

```python
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
An example client. Run simpleserv.py first before running this.
"""
from __future__ import print_function

from twisted.internet import reactor, protocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        self.transport.write(b"hello, world!")
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("Server said:", data)
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()

```



#### 官网示例地址

https://twistedmatrix.com/documents/current/core/examples/





# 参考链接

1. [Twisted：一个基于事件驱动的网络引擎](http://hao.jobbole.com/twisted/)
2. 官方网站：<http://twistedmatrix.com/trac/>
3. 开源地址：<https://github.com/twisted/twisted>
4. https://twistedmatrix.com/trac/