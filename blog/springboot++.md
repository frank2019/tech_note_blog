





# Dubbo

## todo

1. [Dubbo架构设计详解](http://shiyanjun.cn/archives/325.html)

2. http://www.itsource.com.cn/thread-5218-1-2.html

3. [spring Boot环境下dubbo+zookeeper的一个基础讲解与示例](https://blog.csdn.net/future_zhangkai/article/details/76660353)

4. # 

第一个 Dubbo 应用

https://developer.qiniu.com/pili/sdk/3919/a-short-video-the-white-paper

https://github.com/apache/incubator-dubbo-spring-boot-project

### SPI 与API的区别

### [SpringMVC和Springboot的区别（网摘）](https://www.cnblogs.com/kouryoushine/p/7872880.html)

spring boot  我理解就是把 spring spring mvc spring data jpa  等等的一些常用的常用的基础框架组合起来，提供默认的配置，然后提供可插拔的设计，就是各种 starter  ，来方便开发者使用这一系列的技术，套用官方的一句话， spring 家族发展到今天，已经很庞大了，作为一个开发者，如果想要使用 spring  家族一系列的技术，需要一个一个的搞配置，然后还有个版本兼容性问题，其实挺麻烦的，偶尔也会有小坑出现，其实蛮影响开发进度， spring boot  就是来解决这个问题，提供了一个解决方案吧，可以先不关心如何配置，可以快速的启动开发，进行业务逻辑编写，各种需要的技术，加入 starter  就配置好了，直接使用，可以说追求开箱即用的效果吧

 

spring 框架有超多的延伸产品例如 boot security jpa etc... 但它的基础就是 spring 的 ioc 和  aop ioc 提供了依赖注入的容器 aop 解决了面向横切面的编程 然后在此两者的基础上实现了其他延伸产品的高级功能 Spring MVC  呢是基于 Servlet 的一个 MVC 框架 主要解决 WEB 开发的问题 因为 Spring 的配置太复杂了 各种 XML  JavaConfig hin 麻烦 于是懒人改变世界推出了 Spring boot 约定优于配置 简化了 spring 的配置流程

 

Spring 最初利用“工厂模式”（ DI ）和“代理模式”（ AOP ）解耦应用组件。大家觉得挺好用，于是按照这种模式搞了一个 MVC  框架（一些用 Spring 解耦的组件），用开发 web 应用（ SpringMVC  ）。然后有发现每次开发都要搞很多依赖，写很多样板代码很麻烦，于是搞了一些懒人整合包（ starter ），这套就是 Spring Boot 。







## T0x02Spring boot Dubbo第一个程序

假设我要开发一个短视频的后台  基于spring boot dubbo  整体该如何设计









#### 参考链接

1. [dubbo的生态系统](http://dubbo.apache.org/#!/community?lang=zh-cn)
2. [spring boot dubbo 环境搭建](https://www.jianshu.com/p/69243fa4ddb0)
3. http://start.dubbo.io/
4. [Spring-boot:5分钟整合Dubbo构建分布式服务](https://www.cnblogs.com/jaycekon/p/SpringBootDubbo.html)
5. git  clone  https://github.com/dubbo/dubbo-samples





#### 安装zookeeper注册中心



##### 参考链接 

1. [下载地址](http://mirror.bit.edu.cn/apache/zookeeper/zookeeper-3.4.13/)
2. [ZooKeeper的部署以及简单使用](https://www.cnblogs.com/angelhu123/p/6707983.html) 
3. https://www.cnblogs.com/angelhu123/p/6707983.html





#### Spring boot Dubbo HelloWorld



springboot内置了tomcat服务器，我们在开发时，启动web项目不用再把项目部署到tomcat中了，只需要运行main方法，就可以搞定了，就和我们启动java application一样。 

https://www.linuxidc.com/Linux/2017-03/142101.htm



http://start.dubbo.io/



1. [创建一个简单的springboot项目](https://jingyan.baidu.com/article/48206aea8b3570216bd6b310.html)



创建一个简单的Springboot helloworld项目

1.  new -> project -> Spring initializr
2. default : https://start.spring.io
3. 创建项目
4. 新建一个控制器 

```java
package com.helloworld;


import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/")
    public String Hello() {
        return "Hello SpringBoot!";
    }

    
}
```



浏览器访问：

http://localhost:8080/



### 0x01 Dubbo是什么



#### **高性能Java RPC框架**

Apache Dubbo (incubating) |ˈdʌbəʊ| 是一款高性能、轻量级的开源Java RPC(Remote Procedure Call Protocol )框架，它提供了三大核心能力：面向接口的远程方法调用，智能容错和负载均衡，以及服务自动注册和发现.

Dubbo 是一个治理系统 用于分布式服务框架和流式计算框架



#### 特点

##### 面向接口代理的高性能RPC调用

提供高性能的基于代理的远程调用能力，服务以接口为粒度，为开发者屏蔽远程调用底层细节。

##### 智能负载均衡

内置多种负载均衡策略，智能感知下游节点健康状况，显著减少调用延迟，提高系统吞吐量。

##### 服务自动注册与发现

支持多种注册中心服务，服务实例上下线实时感知。

##### 高度可扩展能力

遵循微内核+插件的设计原则，所有核心能力如Protocol、Transport、Serialization被设计为扩展点，平等对待内置实现和第三方实现。

##### 运行期流量调度

内置条件、脚本等路由策略，通过配置不同的路由规则，轻松实现灰度发布，同机房优先等功能。

##### 可视化的服务治理与运维

提供丰富服务治理、运维工具：随时查询服务元数据、服务健康状态及调用统计，实时下发路由策略、调整配置参数。



#### 背景

分布式服务架构以及流动计算架构势在必行，亟需一个治理系统确保架构有条不紊的演进。 

![](http://dubbo.apache.org/docs/zh-cn/user/sources/images/dubbo-architecture-roadmap.jpg)





##### 单一应用架构

当网站流量很小时，只需一个应用，将所有功能都部署在一起，以减少部署节点和成本。此时，用于简化增删改查工作量的数据访问框架(ORM)是关键。

##### 垂直应用架构

当访问量逐渐增大，单一应用增加机器带来的加速度越来越小，将应用拆成互不相干的几个应用，以提升效率。此时，用于加速前端页面开发的Web框架(MVC)是关键。

##### 分布式服务架构

当垂直应用越来越多，应用之间交互不可避免，将核心业务抽取出来，作为独立的服务，逐渐形成稳定的服务中心，使前端应用能更快速的响应多变的市场需求。此时，用于提高业务复用及整合的分布式服务框架(RPC)是关键。

##### 流动计算架构

当服务越来越多，容量的评估，小服务资源的浪费等问题逐渐显现，此时需增加一个调度中心基于访问压力实时管理集群容量，提高集群利用率。此时，用于提高机器利用率的资源调度和治理中心(SOA)是关键。



#### 需求 要解决的问题







#### 架构

![](http://dubbo.apache.org/img/architecture.png)



##### 节点角色说明

| 节点        | 角色说明                               |
| ----------- | -------------------------------------- |
| `Provider`  | 暴露服务的服务提供方                   |
| `Consumer`  | 调用远程服务的服务消费方               |
| `Registry`  | 服务注册与发现的注册中心               |
| `Monitor`   | 统计服务的调用次数和调用时间的监控中心 |
| `Container` | 服务运行容器                           |

##### 调用关系说明

0. Container(服务容器)负责启动加载 运行服务提供者`Provider`
1. `Provider`服务提供者在启动时，向注册中心注册自己提供的服务。 
2. 服务消费者在启动时，向注册中心订阅自己所需的服务。 
3. 注册中心返回服务提供者地址列表给消费者，如果有变更，注册中心将基于长连接推送变更数据给消费者。
4. 服务消费者，从提供者地址列表中，基于软负载均衡算法，选一台提供者进行调用，如果调用失败，再选另一台调用。
5. 服务消费者和提供者，在内存中累计调用次数和调用时间，定时每分钟发送一次统计数据到监控中心。

Dubbo 架构具有以下几个特点，分别是连通性、健壮性、伸缩性、以及向未来架构的升级性。 



#### 连通性

- 注册中心负责服务地址的注册与查找，相当于目录服务，服务提供者和消费者只在启动时与注册中心交互，注册中心不转发请求，压力较小
- 监控中心负责统计各服务调用次数，调用时间等，统计先在内存汇总后每分钟一次发送到监控中心服务器，并以报表展示
- 服务提供者向注册中心注册其提供的服务，并汇报调用时间到监控中心，此时间不包含网络开销
- 服务消费者向注册中心获取服务提供者地址列表，并根据负载算法直接调用提供者，同时汇报调用时间到监控中心，此时间包含网络开销
- 注册中心，服务提供者，服务消费者三者之间均为长连接，监控中心除外
- 注册中心通过长连接感知服务提供者的存在，服务提供者宕机，注册中心将立即推送事件通知消费者
- 注册中心和监控中心全部宕机，不影响已运行的提供者和消费者，消费者在本地缓存了提供者列表
- 注册中心和监控中心都是可选的，服务消费者可以直连服务提供者



#### 健壮性

- 监控中心宕掉不影响使用，只是丢失部分采样数据
- 数据库宕掉后，注册中心仍能通过缓存提供服务列表查询，但不能注册新服务
- 注册中心对等集群，任意一台宕掉后，将自动切换到另一台
- 注册中心全部宕掉后，服务提供者和服务消费者仍能通过本地缓存通讯
- 服务提供者无状态，任意一台宕掉后，不影响使用
- 服务提供者全部宕掉后，服务消费者应用将无法使用，并无限次重连等待服务提供者恢复

#### 伸缩性

- 注册中心为对等集群，可动态增加机器部署实例，所有客户端将自动发现新的注册中心
- 服务提供者无状态，可动态增加机器部署实例，注册中心将推送新的服务提供者信息给消费者 



#### 升级性

当服务集群规模进一步扩大，带动IT治理结构进一步升级，需要实现动态部署，进行流动计算，现有分布式服务架构不会带来阻力。下图是未来可能的一种架构 

![](http://dubbo.apache.org/docs/zh-cn/user/sources/images/dubbo-architecture-future.jpg)

##### 节点角色说明

| 节点         | 角色说明                               |
| ------------ | -------------------------------------- |
| `Deployer`   | 自动部署服务的本地代理                 |
| `Repository` | 仓库用于存储服务应用发布包             |
| `Scheduler`  | 调度中心基于访问压力自动增减服务提供者 |
| `Admin`      | 统一管理控制台                         |
| `Registry`   | 服务注册与发现的注册中心               |
| `Monitor`    | 统计服务的调用次数和调用时间的监控中心 |



#### 参考链接

1. [Dubbo官网](http://dubbo.apache.org/#!/?lang=zh-cn)
2. [听听八年阿里架构师怎样讲述Dubbo和Spring Cloud微服务架构](http://baijiahao.baidu.com/s?id=1600174787011483381&wfr=spider&for=pc)
3. [github dubbo项目源码](https://github.com/apache/incubator-dubbo)







1. 

# Spring boot

## todo

[【转】Spring Boot干货系列：（一）优雅的入门篇](https://www.cnblogs.com/yw0219/p/8661439.html)

测试框架  JUnit4  mockito





### T0x03 Spring Boot  MyBatis的使用 

可用的数据库ORM框架 mybatis  JDBC、JPA、MyBatis、

#### 几种操作数据库的对比mybatis  JDBC、JPA、MyBatis  

###### JDBC (Java Data Base Connection,java数据库连接)

 JDBC(Java Data Base Connection,java数据库连接)是一种用于执行SQL语句的Java  API,可以为多种关系数据库提供统一访问,它由一组用Java语言编写的类和接口组成.JDBC提供了一种基准,据此可以构建更高级的工具和接口,使数据库开发人员能够编写数据库应用程序

- 优点：运行期：快捷、高效
- 缺点：编辑器：代码量大、繁琐异常处理、不支持数据库跨平台

 ![img](http://images2015.cnblogs.com/blog/862246/201601/862246-20160101132324182-822488795.jpg)

######  JDBCTemplate

 JdbcTemplate针对数据查询提供了多个重载的模板方法,你可以根据需要选用不同的模板方法.如果你的查询很简单，仅仅是传入相应SQL或者相关参数，然后取得一个单一的结果，那么你可以选择如下一组便利的模板方法

- 优点：运行期：高效、内嵌Spring框架中、支持基于AOP的声明式事务
- 缺点：必须于Spring框架结合在一起使用、不支持数据库跨平台、默认没有缓存

######  MyBatis

 MyBatis的前身就是iBatis,iBatis本是apache的一个开源项目,2010年这个项目由apahce sofeware foundation 迁移到了google code，并且改名

 总体来说 MyBatis 主要完成两件事情

1. 根据JDBC 规范建立与数据库的连接
2. 通过Annotaion/XML+JAVA反射技术,实现 Java 对象与关系数据库之间相互转化

 MyBatis优缺点如下:

- 优点: 高效、支持动态、复杂的SQL构建, 支持与Spring整合和AOP事务、结果集做了轻量级Mapper封装、支持缓存
- 缺点：不支持数据库跨平台, 还是需要自己写SQL语句

 

######  Hibernate

 Hibernate是一个开放源代码的对象关系映射框架，它对JDBC进行了非常轻量级的对象封装,使得Java程序员可以随心所欲的使用对象编程思维来操纵数据库.  Hibernate可以应用在任何使用JDBC的场合,既可以在Java的客户端程序使用,也可以在Servlet/JSP的Web应用中使用

 

 Hibernate的核心类和接口一共有6个,  分别为:Session、SessionFactory、Transaction、Query、Criteria和Configuration这6个核心类和接口在任何开发中都会用到。通过这些接口，不仅可以对持久化对象进行存取，还能够进行事务控制

 Criteria是一种比hql更面向对象的查询方式。Criteria 可使用 Criterion 和 Projection  设置查询条件.可以设置FetchMode(联合查询抓取的模式)设置排序方式，Criteria 还可以设置 FlushModel（冲刷  Session 的方式）和LockMode

```
1 Criteria crit = sess.createCriteria(Cat.class);
2 crit.setMaxResults(50);
3 List cats = crit.list();
```

##### 参考链接

1. [JDBC、JDBCTemplate、MyBatis、Hiberante 比较与分析](https://blog.csdn.net/sdmxdzb/article/details/72821571)
2. [springboot中application.properties 改成 application.yml详解](https://blog.csdn.net/tjcyjd/article/details/78129354?ref=myrecommend)
3. 



#### Spring boot 支持 mybatis



[SpringBoot（五）：SpringBoot整合MyBatis](https://blog.csdn.net/saytime/article/details/74783296)





##### 参考链接

1. [SpringBoot整合MyBatis](https://www.cnblogs.com/zhuxiaojie/p/5836159.html)
2. [spring boot+mybatis整合](https://www.cnblogs.com/peterxiao/p/7779188.html)
3. [二、spring Boot构建的Web应用中，基于MySQL数据库的几种数据库连接方式进行介绍](https://www.cnblogs.com/chenliangcl/p/7345847.html)



[最新版本查询](http://mvnrepository.com/artifact/org.mybatis.spring.boot)



#### 官方例子解析

1. [mybatis-spring-boot-samples](https://github.com/mybatis/spring-boot-starter/tree/master/mybatis-spring-boot-samples)





#### Spring boot 装配流程 

SpringBoot项目的Bean装配默认规则是根据Application类所在的包位置从上往下扫描！“Application类”是指SpringBoot项目入口类。这个类的位置很关键：如果Application类所在的包为：com.boot.app，则只会扫描com.boot.app包及其所有子包，如果service或dao所在包不在com.boot.app及其子包下，则不会被扫描！即, 把Application类放到dao、service所在包的上级，com.boot.Application知道这一点非常关键 



```
Caused by: org.springframework.beans.factory.NoSuchBeanDefinitionException: No qualifying bean of type 'com.mx.video.mapper.MovieMapper' available: expected at least 1 bean which qualifies as autowire candidate. Dependency annotations: {@org.springframework.beans.factory.annotation.Autowired(required=true)}
```

1. [Dependency annotations: {@org.springframework.beans.factory.annotation.Autowired(required=true)

   ](https://blog.csdn.net/qq_17555933/article/details/51385244)



Spring boot  全局统一异常处理

### T0x02  Spring MVC /SpringBoot HTTP通信加解密



参考链接

1. [Spring MVC /SpringBoot HTTP通信加解密](https://blog.csdn.net/lanmo555/article/details/77059879)
2. [spring-boot-starter-encrypt](https://github.com/yinjihuan/spring-boot-starter-encrypt)



### T0x01 Spring boot 入门Hello World 

# 短视频平台

从零搭建一个短视频后台都需要做哪些工作最有效



可以利用现有的云服务









https://help.aliyun.com/document_detail/61062.html?spm=a2c4g.11186623.6.751.MCWvah



http://dev.yunxin.163.com/docs/product/%E7%82%B9%E6%92%AD/%E6%9C%8D%E5%8A%A1%E7%AB%AFAPI%E6%96%87%E6%A1%A3





### 抖音短视频平台的设计分析



```
功能点：注册登录流程、关注、主页、活动、新建短视频、我的
参考产品：快手、抖音、秒拍等
个人要求：需要有短视频或者直播平台开发经验的后台架构师，能独立完成从0-1的后台架构，系统架构需要支持10W以上TPS，系统会涉及到APP消息推送、短信发送、搜索引擎、简单推荐系统、视频文件存储、CDN加速、微服务架构、弹性扩容、Docker容器部署；需要在3个月内上两个迭代版本，最好是手上有现在的框架代码，只需要做简单的裁剪与适配；要求开发者在深圳，周末可以驻点封闭开发。
```



http://www.woshipm.com/evaluating/864679.html

1. [短视频应用应该如何打造技术架构？](http://www.cocoachina.com/programmer/20160120/15058.html)
2. http://www.360doc.com/content/16/0414/08/31916802_550465254.shtml
3. [爬虫进阶教程：抖音APP无水印视频批量下载](http://cuijiahua.com/blog/2018/03/spider-5.html)

