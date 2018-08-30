# Spring Boot

## TODO

1. [Spring Boot 系列 - WebSocket 简单使用](https://www.cnblogs.com/magicalSam/p/7522060.html)
2. [APP接口安全token设计](https://blog.csdn.net/b452608/article/details/50967849)
3. [处理百万级以上的数据提高查询速度的方法](https://blog.csdn.net/netwinds/article/details/50977527)
4. [大用户并发系统API设计心得](https://blog.csdn.net/feiniao198751/article/details/51378892)
5. [URL短链接的实现原理和方法](http://blog.sina.com.cn/s/blog_a602def501031ksu.html)
6. [Spring Boot（5）一个极简且完整的后台框架](https://www.jianshu.com/p/923d26d705ed)
7. [Spring Boot 项目架构](https://www.cnblogs.com/loginloading/p/7599729.html)
8. [静态代码扫描之阿里java代码规范IDEA插件](https://www.cnblogs.com/findyou/p/7679026.html)
9. [SpringBoot企业级核心技术，对应简书《Spring Boot 核心技术》专题配套源码 ](https://gitee.com/hengboy/spring-boot-chapter)
10. [wireshark如何抓取本机包](https://www.cnblogs.com/lvdongjie/p/6110183.html)
11. 设计软件  ps  CDR和AI 
12. [为什么要培养自己的产品能力？](http://caibaojian.com/productions.html)
13. https://blog.csdn.net/zllww123/article/details/80549397
14. [spring boot 官网](http://spring.io/projects/spring-boot)







http://spring.io/projects/spring-boot



### java  获取请求IP



1. [处理java获取ip为0:0:0:0:0:0:0:1的问题](https://www.cnblogs.com/leiqiannian/p/7753156.html)







### token的验证



token的生成策略 



要包含的信息

1. 用户id
2. 到期时间
3. 密码md5 +  随机数



1. 客户端上传 userid +  keymd5
2. 服务端生成 token  下发给客户端
3. 客户端 发送任务  +  token
4. 服务端 验证token 是否有效   获取对应user信息  解析任务下发回应
5. 









#### 参考链接

1. [Token：服务端身份验证的流行方案](https://www.cnblogs.com/menyiin/p/token.html)
2. [深入了解Token认证的来龙去脉](https://baijiahao.baidu.com/s?id=1593244938986076867&wfr=spider&for=pc)
3. [基于 Token 的身份验证和安全问题](https://blog.csdn.net/qq_35246620/article/details/55049812)





### 邀请码的设计规则

1. [小而美的邀请码设计实现方案](https://www.jianshu.com/p/0201459f3c52)
2. https://github.com/dylang/shortid
3. [基于用户id的最优邀请码生成方案](https://blog.csdn.net/shamg/article/details/80385782)







Warning:java: 未知的枚举常量 javax.annotation.meta.When.MAYBE
  原因: 找不到javax.annotation.meta.When的类文件



### 解决前端调试时候的跨域问题



[springboot中通过cors协议解决跨域问题](https://www.cnblogs.com/520playboy/p/7306008.html)

https://docs.spring.io/spring-boot/docs/current/reference/html/using-boot-using-springbootapplication-annotation.html



1. [前端接口调试 -- 通过Nginx反向代理机制解决跨域问题](https://blog.csdn.net/github_36618205/article/details/53539933)



 [vok_think](https://www.cnblogs.com/vok-think/) 

 			[前端前后端分离开发调试过程中跨域问题解决方式](https://www.cnblogs.com/vok-think/p/7044556.html) 		

\1. 将后台代码部署到你的电脑(安装各种jdk或者环境软件) - 麻烦! 后台改了代码得找后台要

\2. 将前端代码放到跟服务器代码一起 - 麻烦! 前端改一下东西就得上传一次

\3. 使用方便快捷的nginx做代理 (仅仅需要下载nginx稍加配置 , 一次性避免上面两点缺点)

详情(有道云笔记个人记录总结): http://note.youdao.com/noteshare?id=97d0047e7a87d7809d2b15e6be04eec1





Chrome可以安装CORS Toggle。Safari本身自带该功能。 



所有的跨域2种解决办法
1前端提升js权限
2后端配合跨域

对于1，本地调试很多浏览器开发模式都是支持的。或者用浏览器插件。

对于2，后端在HTTP头中增加允许跨域标识。后端使用jsonp技术解决数据访问跨域。

本质跨域限制是浏览器造成的。后端这么强势也是有理由，不过出于同事关系在调试模式下增加跨域http头不是难事。

最好还是沟通好吧，还有就是既然不是联调，前后分离应该前后无疑离吧，自建mock server吧





#### 具体实现



后端配置 亲测有效

```java
import org.springframework.stereotype.Component;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@Component
public class CorsFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest request = (HttpServletRequest) req;
        HttpServletResponse response = (HttpServletResponse) res;
        response.setHeader("Access-Control-Allow-Origin", "*");
        response.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE, PUT, GET");
        response.setHeader("Access-Control-Max-Age", "3600");
        response.setHeader("Access-Control-Allow-Credentials", "true");
        response.setHeader("Access-Control-Allow-Headers", "x-requested-with");
        chain.doFilter(req, res);
    }
    @Override
    public void init(FilterConfig filterConfig) {}

    @Override
    public void destroy() {}
}
```





1. [SpringBoot之跨域过滤器配置允许跨域访问](https://blog.csdn.net/moshowgame/article/details/80364904)
2. 



#### 后端配合跨域



```java
    @RequestMapping(value = "/admininfo", method = RequestMethod.GET)
    public String  test_admininfo() {

        ServletRequestAttributes requestAttributes = (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        MyUtils.supportCrossDomain(requestAttributes.getResponse());

       return "{\"code\":20000,\"data\":{\"roles\":[\"admin\"],\"name\":\"admin\",\"avatar\":\"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif\"}}";
    }
  
  
  
  public static void supportCrossDomain(HttpServletResponse response){
        response.setHeader("Access-Control-Allow-Headers", "Content-Type,Content-Length, Authorization, Accept,X-Requested-With");
        response.setHeader("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");

        response.setHeader("Access-Control-Allow-Origin","*");
        response.setHeader("Access-Control-Allow-Credentials", "true");
        response.setHeader("Access-Control-Max-Age", "3600");
        response.setHeader("Access-Control-Allow-Headers", "x-requested-with");
    }
```





#### Spring Boot全局支持CORS（跨源请求）的配置方法

1. [Spring Boot全局支持CORS（跨源请求）的配置方法](https://blog.csdn.net/zhangchao19890805/article/details/53893735/)
2. 



### MYSQL limit用法

[MYSQL limit用法](https://www.cnblogs.com/cai170221/p/7122289.html)







### Java 数据库ORM 框架对比： JPA VS Mybatis 



#### 说一下我调查后对于这个问题的基本判断：

1. 入门情况的话是：   JPA 比 Mybatis 
2. 使用JPA  最好理解领域驱动设计
3. 如果需求变更比较快或者可能比较频繁的话，建议Mybatis 
4. 目前国内使用的人来说 Mybatis  较多



在我们平时的项目中，大家都知道可以使用 JPA 或者 Mybatis 作为 ORM 层。对 JPA 和 Mybatis 如何进行技术选型？

下面看看大精华总结如下：

首先表达个人观点，JPA必然是首选的。

个人认为仅仅讨论两者使用起来有何区别，何者更加方便，不足以真正的比较这两个框架。要评判出更加优秀的方案，我觉得可以从软件设计的角度来评判。个人对  mybatis 并不熟悉，但 JPA 规范和 springdata 的实现，设计理念绝对是超前的。软件开发复杂性的一个解决手段是遵循  DDD（DDD 只是一种手段，但不是唯一手段），而我着重几点来聊聊 JPA 的设计中是如何体现领域驱动设计思想的，抛砖引玉。

##### 聚合根和值对象

领域驱动设计中有两个广为大家熟知的概念，entity（实体）和 value object（值对象）。entity  的特点是具有生命周期的，有标识的，而值对象是起到一个修饰的作用，其具有不可变性，无标识。在 JPA中 ，需要为数据库的实体类添加 @Entity  注解，相信大家也注意到了，这并不是巧合。

```
@Entity
@Table(name = "t_order")
public class Order {
    @Id
    private String oid;

    @Embedded
    private CustomerVo customer;
    @OneToMany(cascade = {CascadeType.ALL}, orphanRemoval = true, fetch = FetchType.LAZY, mappedBy = "order")
    private List<OrderItem> orderItems;
}1234567891011
```

如上述的代码，Order 便是 DDD 中的实体，而 CustomerVo，OrderItem  则是值对象。程序设计者无需关心数据库如何映射这些字段，因为在 DDD  中，需要做的工作是领域建模，而不是数据建模。实体和值对象的意义不在此展开讨论，但通过此可以初见端倪，JPA 的内涵绝不仅仅是一个 ORM 框架。

##### 仓储

Repository 模式是领域驱动设计中另一个经典的模式。在早期，我们常常将数据访问层命名为：DAO，而在 SpringData JPA 中，其称之为 Repository（仓储），这也不是巧合，而是设计者有意为之。

熟悉 SpringData JPA 的朋友都知道当一个接口继承 JpaRepository 接口之后便自动具备了 一系列常用的数据操作方法，findAll， findOne ，save等。

```
public interface OrderRepository extends JpaRepository<Order, String>{
}12
```

那么仓储和DAO到底有什么区别呢？这就要提到一些遗留问题，以及一些软件设计方面的因素。在这次SpringForAll 的议题中我能够预想到有很多会强调 SpringData JPA 具有方便可扩展的 API，像下面这样：

```
public interface OrderRepository extends JpaRepository<Order, String>{

      findByOrderNoAndXxxx(String orderNo,Xxx xx);

    @Transactional
    @Modifying(clearAutomatically = true)
    @Query("update t_order set order_status =?1 where id=?2")
    int updateOrderStatusById(String orderStatus, String id);
}123456789
```

但我要强调的是，这是 SpringData JPA  的妥协，其支持这一特性，并不代表其建议使用。因为这并不符合领域驱动设计的理念。注意对比，SpringData JPA 的设计理念是将  Repository 作为数据仓库，而不是一系列数据库脚本的集合，findByOrderNoAndXxxx  方法可以由下面一节要提到的JpaSpecificationExecutor代替，而 updateOrderStatusById 方法则可以由  findOne + save 代替，不要觉得这变得复杂了，试想一下真正的业务场景，修改操作一般不会只涉及一个字段的修改， findOne +  save 可以帮助你完成更加复杂业务操作，而不必关心我们该如何编写 SQL 语句，真正做到了面向领域开发，而不是面向数据库 SQL  开发，面向对象的拥趸者也必然会觉得，这更加的 OO。

##### Specification

上面提到 SpringData JPA 可以借助 Specification 模式代替复杂的 findByOrderNoAndXxxx  一类 SQL 脚本的查询。试想一下，业务不停在变，你怎么知道将来的查询会不会多一个条件 变成  findByOrderNoAndXxxxAndXxxxAndXxxx…. 。SpringData JPA 为了实现领域驱动设计中的  Specification 模式，提供了一些列的 Specification 接口，其中最常用的便是  ：JpaSpecificationExecutor

```
public interface OrderRepository extends JpaRepository<Order,String>,JpaSpecificationExecutor<Order>{
}12
```

使用 SpringData JPA 构建复杂查询（join操作，聚集操作等等）都是依赖于 JpaSpecificationExecutor 构建的 Specification 。例子就不介绍，有点长。

请注意，上述代码并不是一个例子，在真正遵循 DDD 设计规范的系统中，OrderRepository  接口中就应该是干干净净的，没有任何代码，只需要继承 JpaRepository （负责基础CRUD）以及  JpaSpecificationExecutor （负责Specification 查询）即可。当然， SpringData JPA  也提供了其他一系列的接口，根据特定业务场景继承即可。

##### 乐观锁

为了解决数据并发问题，JPA 中提供了 @Version ，一般在 Entity 中 添加一个 Long version 字段，配合  @Version 注解，SpringData JPA 也考虑到了这一点。这一点侧面体现出，JPA 设计的理念和 SpringData  作为一个工程解决方案的双剑合璧，造就出了一个伟大的设计方案。

##### 复杂的多表查询

很多人青睐 Mybatis ，原因是其提供了便利的 SQL 操作，自由度高，封装性好……SpringData JPA对复杂 SQL  的支持不好，没有实体关联的两个表要做 join ，的确要花不少功夫。但 SpringData JPA  并不把这个当做一个问题。为什么？因为现代微服务的架构，各个服务之间的数据库是隔离的，跨越很多张表的 join  操作本就不应该交给单一的业务数据库去完成。解决方案是：使用 elasticSearch做视图查询 或者 mongodb 一类的Nosql  去完成。问题本不是问题。

##### 总结

真正走进 JPA，真正走进 SpringData 会发现，我们并不是在解决一个数据库查询问题，并不是在使用一个 ORM 框架，而是真正地在实践领域驱动设计。

（再次补充：DDD 只是一种手段，但不是唯一手段）

------

##### 第二名回答

spring data jpa 的好处我相信大家都了解，就是开发速度很快，很方便，大家不愿意使用spring data jpa  的地方通常是因为sql 不是自己写的，不可控，复杂查询不好搞，那么下面我要说的就是其实对于这种需求，spring data jpa  是完全支持的！！

第一种方式:@query 注解指定nativeQuery,这样就可以使用原生sql查询了,示例代码来自官方文档:

```
public interface UserRepository extends JpaRepository<User, Long> {

@Query(value = "SELECT * FROM USERS WHERE EMAIL_ADDRESS = ?1", nativeQuery = true)
User findByEmailAddress(String emailAddress);
}12345
```

如果单靠sql搞不定怎么办？必须要写逻辑怎么办?可以使用官方文档3.6.1 节：Customizing individual repositories 提供的功能去实现，先看官方文档的代码:

```
interface CustomizedUserRepository {
void someCustomMethod(User user);
}
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

public void someCustomMethod(User user) {
 // Your custom implementation
}
}
interface UserRepository extends CrudRepository<User, Long>, CustomizedUserRepository {

// Declare query methods here
}12345678910111213
```

我来解释下上面的代码，如果搞不定的查询方法，可以自定义接口，例如CustomizedUserRepository  ，和他的实现了类，然后在这个实现类里用你自己喜欢的dao 框架，比如说mybatis ,jdbcTemplate  ,都随意，最后在用UserRepository 去继承CustomizedUserRepository接口，就实现了和其他dao  框架的组合使用！！

那么下面我在总结1下，有了上面介绍的2种功能，你还在担心，使用spring data jpa 会有局限么，他只会加速你的开发速度，并允许你组合使用其他框架，只有好处，没有坏处。。 
 最后再说1点，我最近在看es ,然后看了下spring data es 的文档，大概扫了1下，我发现，学会spring data 其中某1个系列以后，在看其他的，我发现我都不用花时间学。。直接就可以用，对就是这么神奇～～

------

##### 第三

工作以来一直是使用 hibernate 和 mybatis，总结下来一般传统公司、个人开发（可能只是我）喜欢用jpa，互联网公司更青睐于 mybatis 
 原因：，而mybatis  更加灵活。开发迭代模式决定的，传统公司需求迭代速度慢，项目改动小，hibernate可以帮他们做到一劳永逸；而互联网公司追求快速迭代，需求快速变更，灵活的  mybatis  修改起来更加方便，而且一般每一次的改动不会带来性能上的下降，hibernate经常因为添加关联关系或者开发者不了解优化导致项目越来越糟糕（本来开始也是性能很好的）

1、mybatis官方文档就说了他是一个半自动化的持久层框架，相对于全自动化的 hibernate 他更加的灵活、可控 
 2、mybatis 的学习成本低于 hibernate。hibernate 使用需要对他有深入的理解，尤其是缓存方面，作为一个持久层框架，性能依然是第一位的。

hibernate 它有着三级缓存，一级缓存是默认开启的，二级缓存需要手动开启以及配置优化，三级缓存可以整合业界流行的缓存技术 redis，ecache 等等一起去实现 
 hibernate 使用中的优化点： 
 1、缓存的优化 
 2、关联查询的懒加载（在开发中，还是不建议过多使用外键去关联操作）

jpa（Java Persistence API） 与 hibernate 的关系： 
 Jpa是一种规范，hibernate 也是遵从他的规范的。 
 springDataJpa 是对 repository 的封装,简化了 repository 的操作

------

##### 第四

数据分析型的OLAP应用适合用MyBatis，事务处理型OLTP应用适合用JPA。 
 越是复杂的业务，越需要领域建模，建模用JPA实现最方便灵活。但是JPA想用好，门槛比较高，不懂DDD的话，就会沦为增删改查了。 
 复杂的查询应该是通过CQRS模式，通过异步队列建立合适查询的视图，通过视图避免复杂的Join，而不是直接查询领域模型。 
 从目前的趋势来看OLAP交给NoSQL数据库可能更合适

------

##### 第五

使用了一段时间jpa，而mybatis是之前一直在用的，不说区别是啥，因为有很多人比较这两个框架了！ 
 从国内开源的应用框架来看，国内使用jpa做orm的人还是比较少，如果换成hibernate还会多一些，所以面临的风险可能就是你会用，和你合作的人不一定会用，如果要多方协作，肯定要考虑这个问题！ 
 灵活性方面，jpa更灵活，包括基本的增删改查、数据关系以及数据库的切换上都比mybatis灵活，但是jpa门槛较高，另外就是更新数据需要先将数据查出来才能进行更新，数据量大的时候，jpa效率会低一些，这时候需要做一些额外的工作去处理！ 
 现在结合Springboot有Springdata jpa给到，很多东西都简化了，感兴趣并且有能力可以考虑在公司内部和圈子里推广！我的博客里有一些简单使用jpa的示例，<https://github.com/icnws/spring-data-jpa-demo>

------

##### 第六

1.相对来说，jpa的学习成本比mybatis略高 
 2.公司业务需求频繁变更导致表结构复杂，此处使用mybatis比jpa更灵活 
 3.就方言来讲，一般公司选定数据库后再变更微乎其微，所以此处方言的优势可以忽略



转自:  <http://www.spring4all.com/article/391> 





### Java中 VO、 PO、DO、DTO、 BO、 QO、DAO、POJO的概念

 			

#### PO(persistant object) 持久对象

在 o/r 映射的时候出现的概念，如果没有 o/r 映射，没有这个概念存在了。通常对应数据模型 ( 数据库 ),  本身还有部分业务逻辑的处理。可以看成是与数据库中的表相映射的 java 对象。最简单的 PO 就是对应数据库中某个表中的一条记录，多个记录可以用  PO 的集合。 PO 中应该不包含任何对数据库的操作。

#### DO（Domain Object）领域对象

就是从现实世界中抽象出来的有形或无形的业务实体。一般和数据中的表结构对应。

#### TO(Transfer Object) ，数据传输对象

在应用程序不同 tie( 关系 ) 之间传输的对象

#### DTO（Data Transfer Object）数据传输对象

这个概念来源于J2EE的设计模式，原来的目的是为了EJB的分布式应用提供粗粒度的数据实体，以减少分布式调用的次数，从而提高分布式调用的性能和降低网络负载，但在这里，我泛指用于展示层与服务层之间的数据传输对象。

#### VO(view object) 值对象

视图对象，用于展示层，它的作用是把某个指定页面（或组件）的所有数据封装起来。

#### BO(business object) 业务对象

从业务模型的角度看 , 见 UML 元件领域模型中的领域对象。封装业务逻辑的 java 对象 , 通过调用 DAO 方法 , 结合  PO,VO 进行业务操作。 business object: 业务对象  主要作用是把业务逻辑封装为一个对象。这个对象可以包括一个或多个其它的对象。 比如一个简历，有教育经历、工作经历、社会关系等等。  我们可以把教育经历对应一个 PO ，工作经历对应一个 PO ，社会关系对应一个 PO 。 建立一个对应简历的 BO 对象处理简历，每个 BO  包含这些 PO 。 这样处理业务逻辑时，我们就可以针对 BO 去处理。

#### POJO(plain ordinary java object) 简单无规则 java 对象

纯的传统意义的 java 对象。就是说在一些 Object/Relation Mapping 工具中，能够做到维护数据库表记录的  persisent object 完全是一个符合 Java Bean 规范的纯 Java 对象，没有增加别的属性和方法。我的理解就是最基本的  Java Bean ，只有属性字段及 setter 和 getter 方法！。

#### DAO(data access object) 数据访问对象

是一个 sun 的一个标准 j2ee 设计模式， 这个模式中有个接口就是 DAO  ，它负持久层的操作。为业务层提供接口。此对象用于访问数据库。通常和 PO 结合使用， DAO 中包含了各种数据库的操作方法。通过它的方法 ,  结合 PO 对数据库进行相关的操作。夹在业务逻辑与数据库资源中间。配合 VO, 提供数据库的 CRUD 操作

#### 参考链接

1. [Java中 VO、 PO、DO、DTO、 BO、 QO、DAO、POJO的概念](https://www.cnblogs.com/wang-meng/p/5645405.html) 	





### spring boot 图片的上传与显示



1. [spring boot 图片的上传与显示](https://blog.csdn.net/a625013/article/details/52414470)
2. [springMVC一次选择多个图片上传](https://blog.csdn.net/u013086392/article/details/53332151)
3. [multipart/form-data 文件上传表单中 传递参数无法获取的原因!](https://blog.csdn.net/zllww123/article/details/77587292)
4. [Spring Boot  文件上传](http://dowhile.net/2017/12/19/spring-boot-wen-jian-shang-chuan/)



### @ControllerAdvice 拦截异常并统一处理



1. [@ControllerAdvice 拦截异常并统一处理](https://www.cnblogs.com/magicalSam/p/7198420.html)
2. [Spring Boot 2 全局异常处理](https://blog.csdn.net/guo_mao_zhen/article/details/80419181)

3. [SpringBoot 统一异常处理 @ControllerAdvice 失效](https://blog.csdn.net/zx1323/article/details/78670778)
4. https://img-blog.csdn.net/20180702164038112?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RvbmdndWFiYWk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70



Detected @ExceptionHandler methods in globalExceptionHandler



#### Spring boot 分层







### Spring @Autowired注解在非Controller中注入为null

```
@Component
```

 **把Application类放到dao、service所在包的上级** 



Spring boot 中 Service  

@Service用于标注业务层组件 **： 将当前类注册为spring的Bean**

@Controller用于标注控制层组件（如struts中的action）

@Repository用于标注数据访问组件，即DAO组件

@Component泛指组件，当组件不好归类的时候，我们可以使用这个注解进行标注。**： 将当前类注册为spring的Bean**



####  参考链接



1. [spring boot: EL和资源 (一般注入说明(二) @Service注解 @Component注解)](https://www.cnblogs.com/achengmu/p/8117234.html)







Mysql 数据库乱码 

https://blog.csdn.net/u012410733/article/details/61619656

https://www.linuxidc.com/Linux/2017-05/144068.htm





### 使用curl   做模拟rest full 接口测试

curl -h来查看请求参数的含义   -v 显示请求的信息   -X 选项指定其它协议 



#### GET

```
curl   http://localhost:8080/movie/220
```

#### POST

```
curl -v -X POST http://localhost:8080/movie/ -d '{"id":2,"name":"2222"}'
```





使用restfull api  操作

1. https://www.cnblogs.com/Irving/p/4964489.html
2. [我所理解的RESTful Web API [设计篇\]](https://www.cnblogs.com/artech/p/restful-web-api-02.html)



### 使用spring boot 开发一个 rest full  接口



```
RESTful用法：
http://127.0.0.1/user/1 GET  根据用户id查询用户数据
http://127.0.0.1/user  POST 新增用户
http://127.0.0.1/user  PUT 修改用户信息
http://127.0.0.1/user  DELETE 删除用户信息
```



1. [基于SpringBoot开发一个Restful服务，实现增删改查功能](https://blog.csdn.net/qazwsxpcm/article/details/79028689)
2. 



### SpringBoot Controller接收参数的几种常用方式



1. [SpringBoot Controller接收参数的几种常用方式](https://blog.csdn.net/suki_rong/article/details/80445880)



# 常用库

TODO



1. [Fastjson生成json时Null属性不显示](https://blog.csdn.net/a258831020/article/details/47333807)







### fastjson  中有重复的对象

json  字符串中

"$ref": "$.viewItems[0].resource_objects[5].movie.actor_info[0]"





1. [fastjson 重复引用和循环引用问题](https://segmentfault.com/a/1190000013221859)





### FastJson



1. FastJson数度快,无论序列化和反序列化,都是当之无愧的fast   
2. 功能强大(支持普通JDK类包括任意Java Bean Class、Collection、Map、Date或enum)   
3. 零依赖(没有依赖其它任何类库) 



#### pom.xml 配置



```xml
<!-- https://mvnrepository.com/artifact/com.alibaba/fastjson -->
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.47</version>
</dependency>

```



1. [最新版本](http://mvnrepository.com/search?q=FastJson)

#### POJO对象和json字符串之间的转换



```
JSON.toJSONString(studentList)
```



参考链接

1. [为什么Fastjson能够做到这么快?](https://blog.csdn.net/xf_87/article/details/51872336)









# Dubbo

## todo

1. [Dubbo架构设计详解](http://shiyanjun.cn/archives/325.html)

2. http://www.itsource.com.cn/thread-5218-1-2.html

3. [spring Boot环境下dubbo+zookeeper的一个基础讲解与示例](https://blog.csdn.net/future_zhangkai/article/details/76660353)

4.  [Service Mesh是什么技术 下一代微服务？](https://blog.csdn.net/weixin_38044696/article/details/80257488)

5. [学习Spring Boot:使用Lombok来优雅的编码](https://www.cnblogs.com/qnight/p/8997493.html)

   可以用来使用@getter @setter代替函数   从而简化代码

6. 

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



```
 http and  http.request==1 and  http.request.method==POST and ip.dst == 192.168.1.9
```





### tomcat 部署 spring boot  项目



1. [下载tomcat ](https://tomcat.apache.org/download-90.cgi)   [apache-tomcat-9.0.11.zip](mirrors.hust.edu.cn/apache/tomcat/tomcat-9/v9.0.11/bin/apache-tomcat-9.0.11.zip)
2. 



#### Spring boot 代码适配

项目中的  Application主入口 需要继承 SpringBootServletInitializer  做如下类似修改



```
@SpringBootApplication
public class Main extends SpringBootServletInitializer{

    @Override
    protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
        return application.sources(Main.class);
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(Main.class, args);
    }

}
```



##### pom.xml文件中引入tomcat依赖

```
	<dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-tomcat</artifactId>
      <scope>provided</scope>
    </dependency>
```

备注 ：  引入依赖后 运行会报错 。

修改打包类型为  jar 改为 war

```
	<version>0.0.1-SNAPSHOT</version>
	<packaging>war</packaging>
```



接下来就要将该项目打包成war了，IDEA打包项目：点击Build->Build Artifacts-，然后进行build即可，生成的war包会放到对应的项目根目录下的target目录下面





最后将该war包移动到tomcat/webapps目录下即可，然后启动tomcat，打开浏览器输入网址：`localhost:`port`/`war包名`/`在SpringBoot中RequestMapping设置的url请求，即可进入到对应的页面或者返回结果



<http://localhost:8080/chapter1-0.0.1-SNAPSHOT/task>



#### 参考链接

1. [SpringgBoot入门系列篇(十三):部署SpringBoot到tomcat上并启动](https://blog.csdn.net/qq_27905183/article/details/79121759)
2. [利用IDEA将SpringBoot的项目打包成war文件](https://blog.csdn.net/linzhiqiang0316/article/details/52601292)
3. [使用Tomcat部署SpringBoot项目](https://blog.csdn.net/u013279563/article/details/81144154)







### Spring boot  性能优化





参考链接

1. [Spring Boot 性能优化](https://www.cnblogs.com/chen110xi/p/6198481.html)
2. [SpringBoot优化方案](https://www.jianshu.com/p/1e2beda1e098)





### spring boot  报错   远程主机强迫关闭了一个现有的连接]

```
2018-08-28 16:42:01.000  WARN 12936 --- [ient_boss][T#5]] o.e.transport.netty4.Netty4Transport     : exception caught on transport layer [[id: 0x1058a2fd, L:/192.168.1.9:42291 - R:/42.51.192.68:10803]], closing connection

java.io.IOException: 远程主机强迫关闭了一个现有的连接。
	at sun.nio.ch.SocketDispatcher.read0(Native Method) ~[na:1.8.0_101]
	at sun.nio.ch.SocketDispatcher.read(SocketDispatcher.java:43) ~[na:1.8.0_101]
	at sun.nio.ch.IOUtil.readIntoNativeBuffer(IOUtil.java:223) ~[na:1.8.0_101]
	at sun.nio.ch.IOUtil.read(IOUtil.java:197) ~[na:1.8.0_101]
	at sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:380) ~[na:1.8.0_101]
	at io.netty.buffer.PooledHeapByteBuf.setBytes(PooledHeapByteBuf.java:261) ~[netty-buffer-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.buffer.AbstractByteBuf.writeBytes(AbstractByteBuf.java:1108) ~[netty-buffer-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.socket.nio.NioSocketChannel.doReadBytes(NioSocketChannel.java:345) ~[netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:148) ~[netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:647) [netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.nio.NioEventLoop.processSelectedKeysPlain(NioEventLoop.java:547) [netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:501) [netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:461) [netty-transport-4.1.25.Final.jar:4.1.25.Final]
	at io.netty.util.concurrent.SingleThreadEventExecutor$5.run(SingleThreadEventExecutor.java:884) [netty-common-4.1.25.Final.jar:4.1.25.Final]
	at java.lang.Thread.run(Thread.java:745) [na:1.8.0_101]

```





参考链接

1. [elasticsearch中的java.io.IOException: 远程主机强迫关闭了一个现有的连接](https://blog.csdn.net/chengbai19/article/details/79172858)





未知的枚举常量 javax.annotation.meta.When.MAYBE   原因: 找不到javax.annotation.meta.When的类文件





[SpringBoot 利用过滤器Filter修改请求url地址](https://www.cnblogs.com/hongdada/p/9046376.html)



### T0x06  Spring boot  拦截器中处理token







1. https://blog.csdn.net/tomcyndi/article/details/79011093
2. [Spring Boot使用过滤器和拦截器分别实现REST接口简易安全认证](https://www.cnblogs.com/jeffwongishandsome/p/spring-boot-use-filter-and-interceptor-to-implement-an-easy-auth-system.html)

### T0x05 Spring boot  单元测试Controller



```

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.mx.usercenter.vo.Device;
import com.mx.usercenter.vo.request.RequestTouristLoginVo;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.*;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UsersControllerTest {

    @Test
    public void contextLoads() {
    }
    private MockMvc mockMvc; // 模拟MVC对象，通过MockMvcBuilders.webAppContextSetup(this.wac).build()初始化。

    @Autowired
    private WebApplicationContext wac; // 注入WebApplicationContext

    @Before // 在测试开始前初始化工作
    public void setup() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(this.wac).build();
    }



    @Test
    public void handlerBulletinBoardPost() throws Exception {
        Map<String, Object> map = new HashMap<>();
        Integer id =  1;
        map.put("id", id);

        MvcResult result = mockMvc.perform(post("/bulletinboard").content(JSONObject.toJSONString(map)))
                .andExpect(status().isOk())// 模拟向testRest发送get请求
                //.andExpect(content().contentType(MediaType.APPLICATION_JSON_UTF8))// 预期返回值的媒体类型text/plain;charset=UTF-8
                .andReturn();// 返回执行请求的结果

        System.out.println(result.getResponse().getContentAsString());
    }

  /*  @Test
    public void handlerDownloadReportPost() throws Exception {
        Map<String, Object> map = new HashMap<>();

        map.put("invitation_code", "ru68wk");
        map.put("inner_net_ip", "192.168.1.250");

        MvcResult result = mockMvc.perform(post("/download_report?invitation_code=ru68wk&inner_net_ip=192.168.1.9").content("invitation_code=ru68wk&inner_net_ip=192.168.1.250" ))
                .andExpect(status().isOk())// 模拟向testRest发送get请求
                //.andExpect(content().contentType(MediaType.APPLICATION_JSON_UTF8))// 预期返回值的媒体类型text/plain;charset=UTF-8
                .andReturn();// 返回执行请求的结果

        System.out.println(result.getResponse().getContentAsString());
    }
*/

    @Test
    public void handlerTouristLoginPost() throws Exception {
        RequestTouristLoginVo request =  new RequestTouristLoginVo();

        Device device = new Device("imei60","a","deviceid","from");
        device.setBrand("HuaWei");
        device.setModel("Honour");
        device.setMac("mac");
        device.setImsi("imsi");


        request.setUser(null);
        request.setDevice(device);
        //request.setInvitation_code("0");
        request.setInner_net_ip("192.168.1.9");


        String  requestStr = JSON.toJSONString(request);

        MvcResult result = mockMvc.perform(post("/tourist_login").content(requestStr))
                .andExpect(status().isOk())// 模拟向testRest发送get请求
                //.andExpect(content().contentType(MediaType.APPLICATION_JSON_UTF8))// 预期返回值的媒体类型text/plain;charset=UTF-8
                .andReturn();// 返回执行请求的结果

        System.out.println(result.getResponse().getContentAsString());
    }


    @Test
    public void handlerRegisterPost() throws Exception {

    }
}
```



参考链接

1. [Spring Boot Junit 测试Controller](https://blog.csdn.net/xiaolyuh123/article/details/73281522/)





### T0x04  Spring boot 的日志记录

已经有的日志框架  JUL、JCL、Jboss-logging、logback、log4j、log4j2、slf4j… 

Spring Boot：    底层是Spring框架，Spring框架默认是JCL，commons-logging   **Spirng Boot：  排除掉了commons-logging，选用SLF4j和logback** 



日志的抽象层    SLF4j



推荐的组合：  SLF4j和logback

#### SLF4j和logback配置

3.2 lobback-spring.xml 配置

 

\1. 我们先把 application.yml的关于日志的注释掉，新建一个文件   logback-spring.xml，为什么要取这个名字呢，Spring  Boot官方推荐优先使用带有-spring的文件名作为你的日志配置（如使用logback-spring.xml，而不是logback.xml），如果我们想自定义名字，也可以，可以在  application.yml中通过  logging.config=classpath:/xxx.xml等方式配置。







设置日志打印基本

设置日志落地级别





日志输出内容元素具体如下：

- 时间日期：精确到毫秒
- 日志级别：ERROR, WARN, INFO, DEBUG or TRACE
- 进程ID
- 分隔符：- - - 标识实际日志的开始
- 线程名：方括号括起来（可能会截断控制台输出）
- Logger名：通常使用源代码的类名
- 日志内容

## **日志依赖**



```html
<dependency>



    <groupId>org.springframework.boot</groupId>



    <artifactId>spring-boot-starter-logging</artifactId>



</dependency>
```

但是呢，实际开发中我们

不需要直接添加该依赖

，你会发现spring-boot-starter其中包含了 spring-boot-starter-logging，该依赖内容就是 Spring Boot 默认的日志框架 logback。



## **控制台输出**



日志级别从低到高分为TRACE < DEBUG < INFO < WARN < ERROR < FATAL，如果设置为WARN，则低于WARN的信息都不会输出。
Spring Boot中默认配置`ERROR`、`WARN`和`INFO`级别的日志输出到控制台。您还可以通过启动您的应用程序–debug标志来启用“调试”模式（开发的时候推荐开启）,以下两种方式皆可：

- 在运行命令后加入`--debug`标志，如：`$ java -jar springTest.jar --debug`
- 在`application.properties`中配置`debug=true`，该属性置为true的时候，核心Logger（包含嵌入式容器、hibernate、spring）会输出更多内容，但是你自己应用的日志并不会输出为DEBUG级别。
- 

## **文件输出**



默认情况下，Spring Boot将日志输出到控制台，不会写到日志文件。如果要编写除控制台输出之外的日志文件，则需在application.properties中设置logging.file或logging.path属性。

- logging.file，设置文件，可以是绝对路径，也可以是相对路径。如：`logging.file=log/my.log(相对)或者/log/my.log(绝对)`
- logging.path，设置目录，会在该目录下创建spring.log文件，并写入日志内容，如：`logging.path=/var/log`

如果只配置 logging.file，会在项目的当前路径下生成一个 xxx.log 日志文件。
如果只配置 logging.path，在 /var/log文件夹生成一个日志文件为 spring.log

**注：二者不能同时使用，如若同时使用，则只有logging.file生效**

默认情况下，日志文件的大小达到10MB时会切分一次，产生新的日志文件，默认级别为：ERROR、WARN、INFO



## **级别控制**



所有支持的日志记录系统都可以在Spring环境中设置记录级别（例如在application.properties中）
格式为：’logging.level.* = LEVEL’

- `logging.level`：日志级别控制前缀，`*`为包名或Logger名
- `LEVEL`：选项TRACE, DEBUG, INFO, WARN, ERROR, FATAL, OFF

举例：

- `logging.level.com.gwd=DEBUG`：`com.gwd`包下所有class以DEBUG级别输出
- `logging.level.root=WARN`：root日志以WARN级别输出







#### 参考链接

1. [Spring Boot 日志详解](https://blog.csdn.net/norrininthesky/article/details/80014469)
2. [Spring Boot干货系列：（七）默认日志logback配置解析  ](http://tengj.top/2017/04/05/springboot7/)  





### T0x03 Spring Boot  MyBatis的使用 



Mysql中    java中 boolean 对应的数据库数据类型是TINYINT(1)



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



# Elasticsearch  全文检索



参考链接

1. [spring-boot-samples](https://github.com/spring-projects/spring-boot/tree/master/spring-boot-samples)



访问的是elastic search的tcp端口，需换成http端口。

elastic search默认tcp端口9300，http端口9200





模糊查询



```
http://42.51.192.68:10802/movieresource/_search

{
  "query": {
    "multi_match": {
      "fields":  [ "id", "name" ],
      "query":     "铁血刚拳",
      "fuzziness": "AUTO"
    }
  }
}
```





elasticsearch  出错

### all shards failed [type=search_phase_execution_exception]

2018年02月28日 13:56:51

 				阅读数：1401 											

使用elasticsearch出现标题的异常， 
 出现原因: 
 当使用到term 查询的时候，由于是精准匹配，所以查询的关键字在es上的类型，必须是keyword而不能是text， 
 比如你的搜索条件是 “name”:”jack”,那么该name 字段的es类型得是keyword，而不能是text





#### java.lang.IllegalArgumentException: Fielddata is disabled on text fields by default. Set fielddata=true on [name] in order to load fielddata in memory by uninverting the inverted index. Note that this can however use significant memory. Alternatively use a keyword field instead.





### org.springframework.data.domain.Sort





参考链接

1. [Spring data 多字段排序方法](https://blog.csdn.net/flyaimo/article/details/24678081?locationNum=14)





### elastic search 设置可检索



参考链接

1. [ElasticSearch 6.2 Mapping参数说明及text类型字段聚合查询配置](https://www.cnblogs.com/dxf813/p/8447467.html)
2. [ElasticSearch查询 第四篇：匹配查询（Match）](https://www.cnblogs.com/ljhdo/p/4577065.html)
3. [Spring Boot+Elasticsearch实现简单全文搜索](https://www.jianshu.com/p/29944f3e9f95)
4. 



### Spring boot ElasticSearch的注解

#### @Document



chuco  



```
java.lang.IllegalArgumentException: Fielddata is disabled on text fields by default. Set fielddata=true on [id] in order to load fielddata in memory by uninverting the inverted index. Note that this can however use significant memory. Alternatively use a keyword field instead.
	at org.elasticsearch.index.mapper.TextFieldMapper$TextFieldType.fielddataBuilder(TextFieldMapper.java:336) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.index.fielddata.IndexFieldDataService.getForField(IndexFieldDataService.java:111) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.index.query.QueryShardContext.getForField(QueryShardContext.java:166) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.sort.FieldSortBuilder.build(FieldSortBuilder.java:277) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.sort.SortBuilder.buildSort(SortBuilder.java:156) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.SearchService.parseSource(SearchService.java:630) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.SearchService.createContext(SearchService.java:481) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.SearchService.createAndPutContext(SearchService.java:457) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.search.SearchService.executeDfsPhase(SearchService.java:222) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.action.search.SearchTransportService$5.messageReceived(SearchTransportService.java:319) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.action.search.SearchTransportService$5.messageReceived(SearchTransportService.java:316) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.transport.RequestHandlerRegistry.processMessageReceived(RequestHandlerRegistry.java:69) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.transport.TcpTransport$RequestHandler.doRun(TcpTransport.java:1544) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.common.util.concurrent.ThreadContext$ContextPreservingAbstractRunnable.doRun(ThreadContext.java:638) ~[elasticsearch-5.6.10.jar:5.6.10]
	at org.elasticsearch.common.util.concurrent.AbstractRunnable.run(AbstractRunnable.java:37) ~[elasticsearch-5.6.10.jar:5.6.10]
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[na:1.8.0_101]
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[na:1.8.0_101]
	at java.lang.Thread.run(Thread.java:748) ~[na:1.8.0_101]


```



### java项目中常用的分页对象Page



1. https://blog.csdn.net/cgs666/article/details/50465377





http://42.51.192.72:10802/_cat/indices?v



### tips

1. ES中默认的API的端口号是9300而不是9200。
2. ES系统中Elasticsearch.yml配置文件中要加入network.host: 0.0.0.0，否则外网地址访问不了。**
3. 最新的资料一定要去官网上面查看，博客上面好多都是过时的。官网地址：https://www.elastic.co
4. 注意JDK、ES、Springboot三者之间的版本，很多时候错误都是版本冲突引起的。



### T0x04  ES 的基本概念

1. Elasticsearch集群可以包含多个**索引(indices)**（数据库），每一个索引可以包含多个**类型(types)**（表），每一个类型包含多个**文档(documents)**（行），然后每个文档包含多个**字段(Fields)**（列）。 



#### T0x03  常用命令

http://42.51.192.68:10802/







```
my_index/_mapping/my_type
```



#### 修改id可索引

## fielddata

这里看下fielddata: 
 大多数字段默认都是索引的，这使得它们可以搜索。但是，在脚本中进行排序、聚合和访问字段值需要从搜索中获得不同的访问模式。

搜索需要回答“哪些文档包含这个术语？”排序和聚合需要回答一个不同的问题：“这个字段对这个文档的值是多少？”。

大多数字段可以使用索引时，找到值但是text文本字段不支持。 
 Text field使用fielddata的这种内存数据结构。它会在内存中存储反转整个索引的每个片段，包括文档关系。

因为它非常耗费内存所以默认是关闭的disabled，一般不必要设置的不要设置。 
 参



http://42.51.192.68:10802/movieresource/_mapping/movieresource 



```
{
  "properties": {
    "id": { 
      "type":     "text",
      "fielddata": true
    }
  }
}
```



```
{
  "properties": {
    "id": { 
      "type":     "text",
      "fielddata": true
    }
  }
}
```







#### 查看索引的元素

http://42.51.192.68:10802/movieresource/_search

##### 查看指定索引结构

http://42.51.192.68:10802/movieresource/_mapping/





elasticsearch rest api遵循的格式为：

```
curl -X<REST Verb> <Node>:<Port>/<Index>/<Type>/<ID>
```

1、检查es版本信息

```
curl localhost:9200
```

2、查看集群是否健康

```
curl  localhost:9200/_cat/health?v
```

3、查看节点列表

```
curl localhost:9200/_cat/nodes?v
```

4、列出所有索引及存储大小

```
curl localhost:9200/_cat/indices?v
```

5、创建索引

`创建索引名为XX,默认会有5个分片，1个索引`

`curl -XPUT ``'IP:9200/XX?pretty'`

6、添加一个类型

```
curl -XPUT 'IP:9200/XX/external/2?pretty' -d '
{
   "gwyy": "John"
}'
```

7、更新一个类型

```
curl -XPOST 'IP:9200/XX/external/1/_update?pretty' -d '
{
   "doc": {"name": "Jaf"}
}'
```

8、删除指定索引

```
curl -XDELETE 'IP:9200/_index?pretty'
```

9、elasticsearch定期删除策略

<http://www.jianshu.com/p/5e0ed65cd820>





### 0x02   ElasticSearch   与Spring boot 的集成测试



#### 搭建集群环境

参照。。。



#### pom中引入elasticsearch 

```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-data-elasticsearch</artifactId>
</dependency>
```



创建

 

```java
public class Customer {
	@Id
	private String id;

	private String firstName;

	private String lastName;
}
```

创建Index

```
curl -X PUT localhost:9200/customer
```

删除Index

```
curl -X DELETE localhost:9200/weather
```



#### 报错



```
org.elasticsearch.client.transport.NoNodeAvailableException: None of the configured nodes are available: [{#transport#-1}{RM2dlbtCRH6TACc11n445Q}{localhost}{127.0.0.1:9200}]
```



#### spring boot  elasticsearch的配置

[springboot elasticsearch 集成注意事项](https://www.cnblogs.com/guozp/p/8686904.html)



#### 参考链接

1. [spring-boot集成elasticsearch并实现简单的增删改查](https://blog.csdn.net/zhaoyahui_666/article/details/78688688)
2. [springBoot系列教程01：elasticsearch的集成及使用](https://www.cnblogs.com/xiaochangwei/p/8037110.html)
3. [elasticsearch常用命令](https://www.cnblogs.com/moonandstar08/p/6582362.html)
4. [elasticsearch配置](https://www.cnblogs.com/hanyouchun/p/5163183.html)







### 0x01 ElasticSearch 入门

#### ElasticSearch是什么

ElasticSearch是一个基于Lucene的搜索服务器。它提供了一个分布式多用户能力的全文搜索引擎，基于RESTful  web接口。Elasticsearch是用Java开发的，并作为Apache许可条款下的开放源码发布，是当前流行的企业级搜索引擎。设计用于[云计算](https://baike.baidu.com/item/%E4%BA%91%E8%AE%A1%E7%AE%97/9969353)中，能够达到实时搜索，稳定，可靠，快速，安装使用方便。

我们建立一个网站或应用程序，并要添加搜索功能，但是想要完成搜索工作的创建是非常困难的。我们希望搜索解决方案要运行速度快，我们希望能有一个零配置和一个完全免费的搜索模式，我们希望能够简单地使用JSON通过HTTP来索引数据，我们希望我们的搜索服务器始终可用，我们希望能够从一台开始并扩展到数百台，我们要实时搜索，我们要简单的多租户，我们希望建立一个云的解决方案。因此我们利用Elasticsearch来解决所有这些问题及可能出现的更多其它问题。



#### ElasticSearch 安装

1. Elastic 需要 Java 8 环境。注意要保证环境变量`JAVA_HOME`正确设置。 
2. 可以跟着[官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-targz.html)安装 Elastic   适用于window 和 linux
3. 下载  

```bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.2.zip
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.2.zip.sha512
shasum -a 512 -c elasticsearch-6.3.2.zip.sha512 
unzip elasticsearch-6.3.2.zip
cd elasticsearch-6.3.2/ 
```

4. 启动  

   ```
   ./bin/elasticsearch
   ```

5. 测试

   ```
    curl localhost:9200
   
   {                                                       
     "name" : "p764ksQ",                                   
     "cluster_name" : "elasticsearch",                     
     "cluster_uuid" : "JRtCfX_ITw2ZwuvMR7uKJA",            
     "version" : {                                         
       "number" : "6.3.2",                                 
       "build_flavor" : "default",                         
       "build_type" : "zip",                               
       "build_hash" : "053779d",                           
       "build_date" : "2018-07-20T05:20:23.451332Z",       
       "build_snapshot" : false,                           
       "lucene_version" : "7.3.1",                         
       "minimum_wire_compatibility_version" : "5.6.0",     
       "minimum_index_compatibility_version" : "5.0.0"     
     },                                                    
     "tagline" : "You Know, for Search"                    
   }                                                       
   ```

   请求9200端口，Elastic 返回一个 JSON 对象，包含当前节点、集群、版本等信息 



#### 基本概念

1. Elastic 本质上是一个分布式数据库，允许多台服务器协同工作，每台服务器可以运行多个 Elastic 实例 

2. 单个 Elastic 实例称为一个节点（node）。一组节点构成一个集群（cluster） 

3. Elastic 会索引所有字段，经过处理后写入一个反向索引（Inverted Index）。查找数据的时候，直接查找该索引 

4. Elastic 数据管理的顶层单位就叫做 Index（索引）。它是单个数据库的同义词。每个 Index （即数据库）的名字必须是小写。 

5. 查看当前节点的所有 Index 

   ```
   curl -X GET  http://localhost:9200/_cat/indices?v
   ```



6. Index 里面单条的记录称为 Document（文档）。许多条 Document 构成了一个 Index。 

7. Document 使用 JSON 格式表示，下面是一个例子。 

   ```json
       {
         "user": "张三",
         "title": "工程师",
         "desc": "数据库管理"
       }
   ```

8. 同一个 Index 里面的 Document，不要求有相同的结构（scheme），但是最好保持相同，这样有利于提高搜索效率。 

9. Type  Document 可以分组，比如`weather`这个 Index 里面，可以按城市分组（北京和上海），也可以按气候分组（晴天和雨天）。这种分组就叫做 Type，它是虚拟的逻辑分组，用来过滤 Document。 

10. 列出每个 Index 所包含的 Type。 

   ```
   curl localhost:9200/_mapping?pretty=true
   ```

11. 根据[规划](https://www.elastic.co/blog/index-type-parent-child-join-now-future-in-elasticsearch)，Elastic 6.x 版只允许每个 Index 包含一个 Type，7.x 版将会彻底移除 Type。 





#### elasticsearch  vs 数据库 

ES团队不推荐完全采用ES作为主要存储，缺乏访问控制还有一些数据丢失和污染的问题

建议还是采用专门的 DB存储方案，然后用ES来做serving。

es没有事务，而且是近实时。成本也比数据库高，几乎靠吃内存提高性能。最逆天的是，mapping不能改。





#### ElasticSearch vs Solr多维度分析对比

![](https://images2015.cnblogs.com/blog/855959/201703/855959-20170324173110455-1473254525.png)



**ElasticSearch vs Solr 总结**

　　（1）二者安装都很简单。

　　（2）Solr 利用 Zookeeper 进行分布式管理，而 Elasticsearch 自身带有分布式协调管理功能。

　　（3）Solr 支持更多格式的数据，比如JSON、XML、CSV，而 Elasticsearch 仅支持json文件格式。

　　（4）Solr 官方提供的功能更多，而 Elasticsearch 本身更注重于核心功能，高级功能多有第三方插件提供

　　（5）Solr 在传统的搜索应用中表现好于 Elasticsearch，但在处理实时搜索应用时效率明显低于 Elasticsearch。

　　（6）Solr 是传统搜索应用的有力解决方案，但 Elasticsearch 更适用于新兴的实时搜索应用。



[ElasticSearch vs Solr多维度分析对比](https://www.cnblogs.com/zlslch/p/6612639.html)







参考链接

1. [Elasticsearch 权威指南（中文版）](https://es.xiaoleilu.com/)
2. [Elasticsearch 权威指南（中文版）github](https://github.com/elasticsearch-cn/elasticsearch-definitive-guide)
3. [全文搜索引擎 Elasticsearch 入门教程](http://www.ruanyifeng.com/blog/2017/08/elasticsearch.html)
4. [Elasticsearch学习，请先看这一篇](https://blog.csdn.net/laoyang360/article/details/52244917)
5. [时间序列数据库的秘密(2)——索引](http://www.infoq.com/cn/articles/database-timestamp-02?utm_source=infoq)
6. https://www.jianshu.com/p/ed7e1ebb2fb7



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

