## TODO



1. [ConcurrentLinkedQueue使用和方法介绍](https://www.cnblogs.com/yangzhenlong/p/8359875.html)
2. [一线互联网常见的14个Java面试题，你颤抖了吗程序员  ](http://group.jobbole.com/33336/?utm_source=python.jobbole.com&utm_medium=article-related-group-topic)         
3. [java基础思维导图，让java不再难懂](https://www.jianshu.com/p/6a589ffbf34c)







# java语言

**"=="操作符的作用**

1、用于基本数据类型的比较

2、判断引用是否指向堆内存的同一块地址。





1、java中线程池和网络   

2、自己实现c++智能指针  

3、android多进程通信方式   

4、进程被杀后怎样能自启动

5、编程题  fibonacci数列

6、共享内存优势
7、一般通信优势
8、C代码如何回掉Java
9、网络运营商欠费，缴费之后，为什么上不了网






1、熟悉android应用开发
2、熟悉JAVA，c/c++，JAVA Script。
3、熟悉linux系统框架，具有基于linux操作系统的开发经验。
4、熟悉主流操作系统框架android framework，qt。
5、熟悉 yocto /open openembedded 系统构建工具。
6、具有android framework开发经验、linux 系统移植经验、bsp 开发经验、node js开发经验优先。
7、熟悉 linux debug 方法，熟练使用相关开发及debug工具。
8、团队合作精神强，任劳任怨，勇于创新。



### 反射机制及应用场景

#### 什么是java反射机制

 JAVA反射机制是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意一个方法；这种动态获取的以及动态调用对象的方法的功能称为Java的反射机制。 



#### 反射机制的应用场景：

- 逆向代码 ，例如反编译
- 与注解相结合的框架 例如Retrofit
- 单纯的反射机制应用框架 例如EventBus 2.x
- 动态生成类框架 例如Gson

#### 反射机制的优缺点：

 **优点：**

​    运行期类型的判断，动态类加载，动态代理使用反射。

 **缺点：**

​    性能是一个问题，反射相当于一系列解释操作，通知jvm要做的事情，性能比直接的java代码要慢很多。



参考地址

1. [反射机制及应用场景](https://www.cnblogs.com/whoislcj/p/6038511.html)

### T java基础 Java中的String，StringBuilder，StringBuffer的区别

#### 执行速度的快慢

**StringBuilder > StringBuffer > String** 

#### 线程安全角度

**StringBuilder是线程不安全的，而StringBuffer是线程安全的** 

实现的区别

1. String为字符串常量，即String对象一旦创建之后该对象是不可更改的，如果对这个对象做修改，本质上是创建新的对象，然后老的对象被系统自动回收。
2. 而StringBuilder和StringBuffer均为字符串变量，是可以更改的

[Java中的String，StringBuilder，StringBuffer三者的区别](https://www.cnblogs.com/su-feng/p/6659064.html)



#### 源码分析







----



# Spring MVC



### mybatis   Mapper 的配置

Mybatis中定义Mapper信息有两种方式，一种是利用xml写一个对应的包含Mapper信息的配置文件；另一种就是定义一个Mapper接口，然后定义一些相应的操作方法，再辅以相应的操作注解。





1. [深入浅出Mybatis系列（一）---Mybatis入门](https://www.cnblogs.com/dongying/p/4031382.html) 
2. 



### java 中rsa的使用





参考链接

1. [RSA加密算法的java实现](https://blog.csdn.net/cz0217/article/details/78426733)
2. [SHA1算法原理](https://www.cnblogs.com/scu-cjx/p/6878853.html)







## Q&A

1. es  框架是什么

2. spring mvc 框架初探

3. ```
   @Resource
   private ChannelInvokeService channelInvokeService;
   ```


channelInvokeService  是怎么实例化的？、



1. 依赖注入（dependency injection， DI） 
2. 面向切面编程（aspect-oriented programming， AOP）  
3. [Spring MVC 入门示例讲解](http://www.importnew.com/15141.html)
4. ​








### 0x01 项目打包



![](https://images2015.cnblogs.com/blog/803570/201705/803570-20170508103910160-1706732853.png)



重点 选择上一项

参考链接

1. [IntelliJ IDEA java项目导入jar包，打jar包](http://www.cnblogs.com/yulia/p/6824058.html)









###  Log4j 配置



参考链接

1. [Lookups](http://logging.apache.org/log4j/2.x/manual/lookups.html)






## 0x01 @Resource 在spring是如何使用

参考链接

1. [以@Resource为例，透析注解的本质，spring中是如何使用注解的  ](http://blog.csdn.net/qq_27093465/article/details/52702463)           
2. [Spring 注解 @Resource和@Autowired](https://my.oschina.net/u/216467/blog/205951)
   ​                    


## 0x02  SpringMVC使用RedirectView进行POST重定向

SpringMVC提供一个优雅的后台重定向方式：RedirectView在需要封装数据，并进行重定向的场景使用它在适合不过了;

```
   /**  
     * 请求进行重定向  
     */  
    @RequestMapping(value = "postPayAmount", method = RequestMethod.GET)   
    public RedirectView postPayAmount(HttpSession session,ModelMap map) {   
        return new RedirectView(WsUrlConf.URI_PAY,true,false,false);//最后的参数为false代表以post方式提交请求   
    }  
```



而ModelAndView又可以封装RedirectView进行使用，用起来酸爽得很~~

常见用法：

```
return new ModelAndView(new RedirectView("xxx.do"), map);  
```

重定向到百度

```
return  new ModelAndView(new RedirectView("https://www.baidu.com/"));
```



最后，附上一下SpringMVC执行流程图：

## 0x03 spring mvc maven 项目目录结构



```
├─src
│  └─main
│      ├─java
│      │  └─com
│      │      └─mx
│      │          └─adplatform
│      │              ├─common
│      │              │  ├─cache
│      │              │  ├─core
│      │              │  ├─exceptionlogs
│      │              │  ├─exceptions
│      │              │  ├─http
│      │              │  ├─ip
│      │              │  ├─ipseeker
│      │              │  └─utils
│      │              ├─controller
│      │              ├─dao
│      │              ├─listener
│      │              ├─main
│      │              ├─mapper
│      │              ├─po
│      │              ├─service
│      │              │  ├─DianGuan
│      │              │  └─fmobi
│      │              ├─serviceImpl
│      │              │  ├─DianGuan
│      │              │  └─fmobi
│      │              ├─utils
│      │              └─vo
│      │                  ├─AdRequest
│      │                  ├─AdResponse
│      │                  ├─dianguan
│      │                  │  ├─AdRequest
│      │                  │  └─AdResponse
│      │                  └─fmobi
│      │                      ├─AdRequest
│      │                      └─AdResponse
│      ├─resources
│      └─webapp
│          └─WEB-INF
└─Adplatform.iml
└─pom.xml  

```



### pom.xml

1. [Maven之（七）pom.xml配置文件详解]()

### web.xml



[Spring MVC的web.xml配置详解(转)](http://www.cnblogs.com/wkrbky/p/5929943.html)



### applicationContext.xml





## 0x03 mybatis 



//todo



MyBatis应用程序根据XML配置文件创建SqlSessionFactory，SqlSessionFactory在根据配置，配置来源于两个地方，一处是配置文件，一处是Java代码的注解，获取一个SqlSession。SqlSession包含了执行sql所需要的所有方法，可以通过SqlSession实例直接运行映射的sql语句，完成对数据的增删改查和事务提交等，用完之后关闭SqlSession。



- 一类用于指定数据源、事务属性以及其他一些参数配置信息（通常是一个独立的文件，可以称之为全局配置文件）；


- 另一类则用于 指定数据库表和程序之间的映射信息（可能不止一个文件，我们称之为映射文件）







![img](http://img.mukewang.com/55b1dbbd00016b6407090390.png)



参考链接

1. [【持久化框架】Mybatis简介与原理](http://blog.csdn.net/jiuqiyuliang/article/details/45286191)
2. [SpringMVC+Spring4+Mybatis3集成，开发简单Web项目](http://blog.csdn.net/jiuqiyuliang/article/details/45132493)
3. [mybatis 文档](http://www.mybatis.org/mybatis-3/zh/configuration.html#settings)
4. ​



## 0x04 日志框架 slf4j

todo





## 0x05  java spring  tomcat项目部署 

参考文件

1. [在Linux安装配置Tomcat 并部署web应用 ( 三种方式 )](http://www.cnblogs.com/magicalSam/p/magicalSam.html)




## 0x06  java spring 使用测试框架





1. [SpringBoot开发详解（十一） -- Redis在SpringBoot中的整合](http://blog.csdn.net/qq_31001665/article/details/74080154)
2. ​

-------


# 一.概述



### 1.1 目前java平台主流的框架有哪些

1. 精通J2EE架构，熟悉SpringMVC，mybatis，Spring开发框架；
2. 熟悉Tomcat应用服务器的使用以及mysql数据库；
3. 熟练Struts*、SpringMVC、Mybatis、easyUI（或JQuery）等常用框架；
4. 理解ESB架构原理，熟悉http、socket等常用通讯协议；
5. 有代码重构、性能调优






```

```



1. ](https://www.jianshu.com/p/7bf5dc61ca06)



### 3.2  spring中的常用注解

传统的Spring做法是使用.xml文件来对bean进行注入或者是配置aop、事物，这么做有两个缺点：

1. 如果所有的内容都配置在.xml文件中，那么.xml文件将会十分庞大；如果按需求分开.xml文件，那么.xml文件又会非常多。总之这将导致配置文件的可读性与可维护性变得很低。
2. 在开发中在.java文件和.xml文件之间不断切换，是一件麻烦的事，同时这种思维上的不连贯也会降低开发的效率。

为了解决这两个问题，Spring引入了注解，通过"@XXX"的方式，让注解与Java Bean紧密结合，既大大减少了配置文件的体积，又增加了Java Bean的可读性与内聚性。



Spring里面的bean就类似是定义的一个组件，而这个组件的作用就是实现某个功能的，在spring里给定义的bean就是说，我给你了一个更为简便的方法来调用这个组件去实现你要完成的功能







### @Resource

@ResponseBody
@RequestMapping(value = "/adRequest", method = RequestMethod.GET)



### @Service



[Spring系列之Spring常用注解总结](http://www.cnblogs.com/xiaoxi/p/5935009.html)



----



# spring mvc 学习笔记



## 一.spring mvc 初探

### 1.1 Spring Web MVC是什么

Spring Web MVC是一种基于Java的实现了Web MVC设计模式的请求驱动类型的轻量级Web框架，即使用了MVC架构模式的思想，将web层进行职责解耦，基于请求驱动指的就是使用请求-响应模型，框架的目的就是帮助我们简化开发，Spring Web MVC也是要简化我们日常Web开发的。

另外还有一种基于组件的、事件驱动的Web框架在此就不介绍了，如Tapestry、JSF等。



Spring Web MVC也是服务到工作者模式的实现，但进行可优化。

1. 前端控制器是`DispatcherServlet；`
2. 应用控制器其实拆为处理器映射器(Handler Mapping)进行处理器管理和视图解析器(View Resolver)进行视图管理；
3. 页面控制器/动作/处理器为Controller接口（仅包含`ModelAndView handleRequest(request, response)` 方法）的实现（也可以是任何的POJO类）；
4. 支持本地化（Locale）解析、主题（Theme）解析及文件上传等；
5. 提供了非常灵活的数据验证、格式化和数据绑定机制；
6. 提供了强大的约定大于配置（惯例优先原则）的契约式编程支持。

### 1.2 Spring Web MVC能帮我们做什么

√让我们能非常简单的设计出干净的Web层和薄薄的Web层；

√进行更简洁的Web层的开发；

√天生与Spring框架集成（如IoC容器、AOP等）；

√提供强大的约定大于配置的契约式编程支持；

√能简单的进行Web层的单元测试；

√支持灵活的URL到页面控制器的映射；

√非常容易与其他视图技术集成，如Velocity、FreeMarker等等，因为模型数据不放在特定的API里，而是放在一个Model里（`Map`数据结构实现，因此很容易被其他框架使用）；

√非常灵活的数据验证、格式化和数据绑定机制，能使用任何对象进行数据绑定，不必实现特定框架的API；

√提供一套强大的JSP标签库，简化JSP开发；

√支持灵活的本地化、主题等解析；

√更加简单的异常处理；

√对静态资源的支持；

√支持Restful风格。

### 1.3 Spring Web MVC架构





#### 请求处理流程



![点击查看原始大小图片](http://sishuok.com/forum/upload/2012/7/14/529024df9d2b0d1e62d8054a86d866c9__1.JPG)



#### Spring Web MVC核心架构图

![点击查看原始大小图片](http://sishuok.com/forum/upload/2012/7/14/57ea9e7edeebd5ee2ec0cf27313c5fb6__2.JPG)



### 1.4spring中的DI  AOP是什么

#### 依赖注入（DI）：

Spring最有确定的技术是依赖注入控制反转（DI）。控制反转（IoC）是一个笼统的概念，它可以表现在许多不同的方式和依赖注入仅仅是控制反转的一个具体的例子。

当编写一个复杂的Java应用程序，应用程序类应该尽可能独立其他Java类来增加重复使用这些类，并独立于其他类别的测试它们，而这样做单元测试的可能性。依赖注入有助于粘合这些类在一起，同时保持他们的独立。

什么是依赖注入是什么呢？让我们来看看这两个词分开。这里的依赖性部分转化为两个类之间的关联。例如，A类是依赖B类，现在，让我们来看看第二部分，注入。这一切都意味着，B类将由IOC注入到A类得到。

依赖注入可以将参数传递给构造函数的方式或使用后建设setter方法发生。依赖注入是Spring框架的核心，所以会在一个单独的章节，一个不错的例子解释这个概念。



控制反转是基于类A而言的，控制权转移了，类A不在掌握主动权了，反而被动了。依赖注入是对容器而言的，将各种依赖通过容器注入，以达到解耦和的目的

参考链接

1. [控制反转（IOC）和依赖注入（DI）的区别](http://blog.csdn.net/doris_crazy/article/details/18353197)

#### 面向切面编程（AOP）：



![Spring Framework Architecture](http://www.yiibai.com/uploads/allimg/131213/2223014C2-0.png)















## 二.技术点

### 2.1日志的使用SLF4J

1. [日志组件slf4j介绍及配置详解 ](http://blog.csdn.net/foreverling/article/details/51385128)
2. [java日志框架log4j详细配置及与slf4j联合使用教程](http://www.cnblogs.com/ywlaker/p/6124067.html)



### 2.2  helloworld  idea spring mvc



参考链接

1. [使用IntelliJ IDEA开发Spring MVC HelloWorld](http://blog.csdn.net/industriously/article/details/52851588)
2. ​




X-Token

http 请求中的 X-Token字段

[基于Token的WEB后台认证机制](http://www.cnblogs.com/xiekeli/p/5607107.html)






参考

![img](https://pic2.zhimg.com/50/38a79c3585ae7cbb20ea5bfbb4698f2e_hd.jpg)

















































--------



# redis相关

参考链接

1. [Redis 教程](http://www.runoob.com/redis/redis-intro.html)

## 一.redis简介

Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

Redis 与其他 key - value 缓存产品有以下三个特点：

- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
- Redis支持数据的备份，即master-slave模式的数据备份。

### Redis 优势

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

### Redis与其他key-value存储有什么不同？

- Redis有着更为复杂的数据结构并且提供对他们的原子性操作，这是一个不同于其他数据库的进化路径。Redis的数据类型都是基于基本数据结构的同时对程序员透明，无需进行额外的抽象。
- Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问。     

## 二.redis的部署使用

参考链接

1. [Redis 教程](http://www.runoob.com/redis/redis-intro.html)

### 2.1 在 Ubuntu 系统安装 Redi

可以使用以下命令:

```
$sudo apt-get update
$sudo apt-get install redis-server
```

启动 Redis

```
$ redis-server
```

查看 redis 是否启动？

```
$ redis-cli
```

以上命令将打开以下终端：

```
redis 127.0.0.1:6379>
```

127.0.0.1 是本机 IP ，6379 是 redis 服务端口。现在我们输入 PING 命令。

```
redis 127.0.0.1:6379> ping
PONG
```

以上说明我们已经成功安装了redis。

### 2.2 安装测试

```
$ cd src
$ ./redis-cli
redis> set foo bar
OK
redis> get foo
"bar"

redis 127.0.0.1:6379> ping
PONG
```

### 2.3 Redis 配置

Redis 的配置文件位于 Redis 安装目录下，文件名为 redis.conf。



### 2.4 redis数据类型

Redis支持五种数据类型：string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

链接

[redis数据类型](http://www.runoob.com/redis/redis-data-types.html)

命令

```
redis-cli -h host -p port -a password
```



判断制定的key是否存在，若 key 存在返回 1 ，否则返回 0 。

EXISTS  key



```
redis.hostName=42.51.146.212
redis.port=60791
redis.password=1Q3e#5t%
```

## 三. java 编程使用redis

### 3.1 RedisTemplate





参考链接

1. [spring  整合 redis，以及spring的RedisTemplate如何使用](http://blog.csdn.net/liang_love_java/article/details/50497281)
2. [如何使用RedisTemplate访问Redis数据结构






当前目标

1. lua语言的特点，开发环境，基本语法的用法、

读《Lua程序设计4th》



## 第 1 章 起点

### 1.1 window下 lua的开发环境

常见编译命令

lua   luac



1. -i 和 dofile 在调试或者测试 Lua 代码时是很方便的。 
2. 注释：单行注释:--    多行注释： --[[ --]] 
3. Lua 是动态类型语言，变量不要类型定义。Lua 中有 8 个基本类型分别为：nil、boolean、
   number、 string、 userdata、 function、 thread 和 table。函数 type 可以测试给定变量或者值
   的类型 





### 参考资料

1. Lua程序设计4th.pdf
2. http://lua-users.org 

# 克鲁赛德战记



游戏考察



秒杀功能



# 腾讯的捕鱼     头脑王者