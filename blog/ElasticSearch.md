

# Elasticsearch  全文检索



### toRead

1. [spring-boot-samples](https://github.com/spring-projects/spring-boot/tree/master/spring-boot-samples)

2. [使用Java Low Level REST Client操作elasticsearch](https://www.cnblogs.com/ginb/p/8682092.html)

3. [Elasticsearch－基础介绍及索引原理分析](https://www.cnblogs.com/dreamroute/p/8484457.html)

4. [《死磕 Elasticsearch 方法论》：普通程序员高效精进的 10 大狠招！（完整版）](https://blog.csdn.net/laoyang360/article/details/79293493)

5. 官方向导   
   <http://www.elasticsearch.cn/guide/> 中文版    
   <http://es-cn.medcl.net/guide/> 中文版    
   <http://www.elasticsearch.org/guide/> 英文

   翻译【ElasticSearch Server】第一章：开始使用ElasticSearch集群   
   <http://www.cnblogs.com/jefurry/tag/ElasticSearch/>







访问的是elastic search的tcp端口，需换成http端口。

elastic search默认tcp端口9300，http端口9200





### Python Elasticsearch Client







### elasticSearch 搜索示例



#### 多重条件过滤

1. 查询eventType 字段为 event_first_visit 的数据
2. 接上  过滤  0 < createtime  < 1636128296935
3. 使用 cardinality  做 去重

```
{
    "size": 0,
    "query": {
        "constant_score": {
            "filter": {
                "terms": {
                    "eventType.keyword": [
                        "event_first_visit"
                    ]
                }
            }
        }
    },
    "aggs": {
        "user_status": {
            "filter": {
                "range": {
                    "createtime": {
                        "gte": 0,
                        "lte": 1636128296935
                    }
                }
            },
            "aggs": {
                "uv": {
                    "cardinality": {
                        "field": "userId.keyword"
                    }
                }
            }
        }
    }
}
```



返回数据

```
{
    "took": 0,
    "timed_out": false,
    "_shards": {
        "total": 5,
        "successful": 5,
        "failed": 0
    },
    "hits": {
        "total": 344,
        "max_score": 0,
        "hits": []
    },
    "aggregations": {
        "user_status": {
            "doc_count": 344,
            "uv": {
                "value": 123
            }
        }
    }
}
```

返回字段的定义

took：是查询花费的时间，毫秒单位

time_out：标识查询是否超时

_shards：描述了查询分片的信息，查询了多少个分片、成功的分片数量、失败的分片数量等

hits：搜索的结果，total是全部的满足的文档数目，hits是返回的实际数目（默认是10）

_score是文档的分数信息，与排名相关度有关，参考各大搜索引擎的搜索结果，就容易理解。 



#### 查看集群统计信息

统计信息包含 集群的分片数，文档数，存储空间，缓存信息，内存作用率，插件内容，文件系统内容，JVM作用状况，系统CPU，OS信息，段信息。 

查看全部统计信息命令：

```
curl -XGET 'http://localhost:8200/_cluster/stats?pretty'
```

返回信息：

```


```









#### 参考链接

1. [Elasticsearch 统计代码例子](https://www.cnblogs.com/didda/p/5485681.html)
2. [Elasticsearch 常用基本查询](https://www.cnblogs.com/sunfie/p/6653778.html)





### ElasticSearch 查询



#### **1. 基本匹配查询(Basic Match Query)**

　　基本匹配查询主要有两种形式：

1）使用Search Lite API，并将所有的搜索参数都通过URL传递；

2）使用Elasticsearch DSL，其可以通过传递一个JSON请求来获取结果。下面是在所有的字段中搜索带有"John"的结果

```
curl -XGET 'localhost:9200/megacorp/_search' -d '
{
    "query": {
        "multi_match" : {
            "query" : "John",
            "fields" : ["_all"]
        }
    }
}'
```



上面的multi_match关键字通常在查询多个fields的时候作为match关键字的简写方式。fields属性指定需要查询的字段，如果我们想查询所有的字段，这时候可以使用_all关键字，正如上面的一样。以上两种方式都允许我们指定查询哪些字段。

```
curl -XGET 'localhost:9200/megacorp/employee/_search' -d '
{
    "query": {
        "multi_match" : {
            "query" : "rock",
            "fields": ["about", "interests"]
        }
    }
}'
```

####  **Boosting**

　　我们上面使用同一个搜索请求在多个field中查询，你也许想提高某个field的查询权重,在下面的例子中，我们把interests的权重调成3，这样就提高了其在结果中的权重，这样把_id=4的文档相关性大大提高了，如下：

```
curl -XGET 'localhost:9200/megacorp/employee/_search' -d '
{
    "query": {
        "multi_match" : {
            "query" : "rock",
            "fields": ["about", "interests^3"]
        }
    }
}'
```

Boosting不仅仅意味着计算出来的分数(calculated score)直接乘以boost factor，最终的boost value会经过归一化以及其他一些内部的优化

#### 4.Bool Query

我们可以在查询条件中使用AND/OR/NOT操作符，这就是布尔查询(Bool
Query)。布尔查询可以接受一个must参数(等价于AND)，一个must_not参数(等价于NOT)，以及一个should参数(等价于OR)。比如，我想查询about中出现music或者climb关键字的员工，员工的名字是John，但姓氏不是smith，我们可以这么来查询：

```
curl -XGET 'localhost:9200/megacorp/employee/_search' -d '
{
    "query": {
        "bool": {
                "must": {
                    "bool" : { 
                        "should": [
                            { "match": { "about": "music" }},
                            { "match": { "about": "climb" }} ] 
                    }
                },
                "must": {
                    "match": { "first_nale": "John" }
                },
                "must_not": {
                    "match": {"last_name": "Smith" }
                }
            }
    }
}'
```









参考链接

1. [](https://www.elastic.co/guide/cn/elasticsearch/guide/current/_finding_exact_values.html)
2. [elasticsearch常用操作](https://www.cnblogs.com/fclbky/p/7238494.html)
3. https://www.elastic.co/guide/en/elasticsearch/client/java-api/current/java-search.html
4. https://www.iteblog.com/archives/1768.html







### 使用Python Elasticsearch Client 方法ES



安装Elasticsearch模块

```
pip install elasticsearch
```



https://blog.csdn.net/y472360651/article/details/76468327





### Elasticsearch及插件安装



<http://localhost:5601/>



1. [Elasticsearch入门教程(一)：Elasticsearch及插件安装](https://blog.csdn.net/vbirdbest/article/details/79194244)



```
curl -XGET -H 'Content-Type: application/json' 'http://localhost:9200/_analyze?pretty' -d '{"analyzer" : "ik_max_word","text": "中华人民共和国国歌"}'
```





### ElasticSearch tips



#### 1.Invalid index name [MoviePool], must be lowercase

索引名字必须市小写

#### 2.定义Repository

```java
public interface FLMoviePoolRepository extends ElasticsearchRepository<FLMovieEntiry,Integer> 
```

其中 ElasticsearchRepository<FLMovieEntiry,Integer>      Integer  是主键id的类型。



#### 3.可以在浏览器直接测试：查看索引结构  http://127.0.0.1:9200/moviepool

#### 4.查看索引元素信息： http://127.0.0.1:9200/moviepool/_search



```
Fielddata is disabled on text fields by default. Set fielddata=true on [titleCn] in order to load fielddata in memory by uninverting the inverted index. Note that this can however use significant memory. Alternatively use a keyword field instead.

```





@Field(type = FieldType.String, index = FieldIndex.not_analyzed)

### 使用python api 访问ES



参考链接

1. [python对elasticsearch进行数据的增删改查](https://blog.csdn.net/chinabestchina/article/details/80905147)









### 数据查询统计



```
{"query":{"bool":{"must":[{"term":{"results.req.searchFunc":"searchmusic"}},{"range":{"results.response.data.total":{"gte":"1"}}}]}},"size":0,"aggregations":{"topSearch":{"terms":{"field":"results.req.text.keyword","size":100}}}}

```



统计字段为指定字符串的所有集合



```
{
    "query": {
        "constant_score": {
            "filter": {
                "terms": {
                    "eventType.keyword": [
                        "event_heartbeat",
                        "event_start_show"
                    ]
                }
            }
        }
    }
}

```







```
{
    "query": {
        "constant_score": {
            "filter": {
                "terms": {
                    "eventType.keyword": [
                        "event_heartbeat",
                        "event_start_show"
                    ]
                },
                "range": {
                    "@timestamp": {
                        "gt": "now-2m",
                        "lt": "now"
                    }
                }
            }
        }
    }
}

```





```
{
  "size": 0,
  "aggs": {
    "filtered_aggs": {
      "filter": {
        "range": {
          "@timestamp": {
            "gt": "now-15m",
            "lt": "now"
          }
        }
      },
      "aggs": {
        "ipv": {
          "cardinality": {
            "field": "userId"
          }
        }
      }
    }
  }
}

```





collapse  去重

```
{
    "query": {
        "match": {
		   "eventType": "event_start_show"
        }
    },
    "collapse": {
        "field": "userId.keyword"
    },
    "size": 3,
    "from": 0
}

```





```
{
	"size":0,
    "query": {
        "constant_score": {
            "filter": {
                "terms": {
                    "eventType.keyword": [
                        "event_heartbeat",
                        "event_start_show",
                        "event_first_visit",
                        "event_register"
                    ]
                }
            }
        }
    },
    "collapse": {
        "field": "userId.keyword"
    }
}

```





多条件过滤 统计   获取 

```
{
    "size": 0,
    "query": {
        "constant_score": {
            "filter": {
                "terms": {
                    "eventType.keyword": [
                        "event_first_visit"
                        
                    ]
                }
            }
        }
    },
    "aggs": {
        "user_status": {
            "filter": {
                "range": {
                    "createtime": {
                        "gte": 0,
                        "lte": 1636128296935
                    }
                }
            },
            "aggs": {
                "uv": {
                    "cardinality": {
                        "field": "userId.keyword"
                    }
                }
            }
        }
    }
}

```





#### 统计去重后的数据

1. [统计去重后的数据](https://www.elastic.co/guide/cn/elasticsearch/guide/current/cardinality.html#cardinality)
2. 

统计独立网站访问数

```
{
    "size": 0,
    "aggs": {
        "distinct_colors": {
            "cardinality": {
                "field": "userId"
            }
        }
    }
}

```



统计    1636128296935> createtime >0  的，按照 userId  字段去重

```
{
    "size": 0,
    "aggs": {
        "recent_sales": {
            "filter": {
                "range": {
                    "createtime": {
                        "gte": 0,
                        "lte": 1636128296935
                    }
                }
            },
            "aggs": {
                "distinct_colors": {
                    "cardinality": {
                        "field": "userId.keyword"
                    }
                }
            }
        }
    }
}

```







### spring boot 中增加一个es 接口





参考链接

1. [使用Java Low Level REST Client操作elasticsearch](https://www.cnblogs.com/ginb/p/8682092.html)





### 基于ES 使用用户统计

代码中增加定义



http://42.51.192.68:10802/userevent/_search



http://42.51.192.68:10802/userevent/_mapping/userevent



http://35.172.3.21:39200/userevent/_mapping/userevent



#### 错误提示

```
Caused by: NotSerializableExceptionWrapper[: Fielddata is disabled on text fields by default. Set fielddata=true on [id] in order to load fielddata in memory by uninverting the inverted index. Note that this can however use significant memory. Alternatively use a keyword field instead.]; nested: IllegalArgumentException[Fielddata is disabled on text fields by default. Set fielddata=true on [id] in order to load fielddata in memory by uninverting the inverted index. Note that this can however use significant memory. Alternatively use a keyword field instead.];


```



参考链接

1. [Elasticsearch 统计代码例子](https://www.cnblogs.com/didda/p/5485681.html)



#### ava.lang.NoClassDefFoundError: org/elasticsearch/transport/Netty3Plugin





#### 模糊查询



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



1. [elasticsearch使用索引模板和别名高效地处理日志类索引](http://www.javacoder.cn/?p=812)
2. [Elasticsearch－基础介绍及索引原理分析](https://www.cnblogs.com/dreamroute/p/8484457.html)



### 0x04  elasticsearch  动态索引名

```
@Document(indexName = "userevent-#{T(com.mx.video.utils.MyUtils).getTodayDateString()}",type = UserEventEntiry.TYPE)
public class UserEventEntiry implements Serializable {

    public static final String INDEX = "userevent";
    public static final String TYPE = "userevent";


    private String id;
    private String userId;
  }
```



@Document  属性支持SpEL表达式

#### 参考链接

1. [Spring ES动态索引](https://www.jianshu.com/p/0b603db1278f)



### 0x03  elasticsearch  tips

在使用Elasticsearch之前，先给大家聊一点干货。 

1. ES和solr都是作为全文搜索引擎出现的。都是基于Lucene的搜索服务器。 

2. ES不是可靠的存储系统，不是数据库，它有丢数据的风险。 

3. ES不是实时系统，数据写入成功只是trans log成功（类似于MySQL的bin 
  log），写入成功后立刻查询查不到是正常的。因为数据此刻可能还在内存里而不是进入存储引擎里。同理，删除一条数据后也不是马上消失。写入何时可查询。ES内部有一个后台线程，定时将内存中的一批数据写入到存储引擎，此后数据可见。默认后台线程一秒运行一次。该线程运行的越频繁，写入性能越低。运行的频率越低，写入的性能越高（不会无限高）。


4. 目前已知的单ES集群可以存储PB级别的数据，不过这个就非常费劲了。TB级别数据没压力。 

5. 如果使用ES官方提供的jar包访问，需要JDK1.7及以上。 

6. 使用对应的版本访问ES server。如果ES server端的版本是1.7，那么请使用ES 1.7的client。如果ES server是2.1，请使用2.1的client。 

7. ES索引存在Linux服务器的文件系统之上（背后是文件系统，不是类似于HDFS的分布式文件系统） 

8. ES Java client是线程安全的，全局构建一个即可满足读写需求，不要每次都创建ES client。每次访问ES都构建新的es client即会抛出次异常。 

9. 非常不建议使用ES的动态识别和创建的机制，因为很多情况下这并非你所需要。推荐的做法是在写数据之前仔细的创建mapping。 

10. 强烈不建议在ES中使用深分页。可能会导致集群不可用。 

11. ES是静态分片，一旦分片数在创建索引时确定那么后继不能修改。 

12. 
   ES里提供了type，很多人以为type是物理表，一个type的数据是独立存储的；但是在ES内部并不是这样，type在ES内部仅仅是一个字段。所以在很多数据能分为独立index的情况下，不要放到一个index里用type去分。只有嵌套类和父子类的情况下使用type才是合理的。


13. ES并不提供原生的中文分词的能力。有第三方的中文分词的插件，比如ik等。Ik是个toy分词器，有严肃的分词需求的话，请在使用ES之前使用独立的分词器分好词后向ES写入。 

14. 
   ES中的index，首先会进行分片，每一个分片数据一般都会有自己的副本数据，ES分配分片的策略会保证同一个分片数据和自己的副本不会分配到同一个节点上。当集群中的某一节点宕机后，ES的master在ping该节点时通过一定的策略会发现该节点不存活；会开启ES的恢复过程


15. ES没有update的能力。所有的update都是标记删除老文档，然后重新insert一条新文档。



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

1. 启动  

   ```
   ./bin/elasticsearch
   
   ```

2. 测试

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



1. Index 里面单条的记录称为 Document（文档）。许多条 Document 构成了一个 Index。 

2. Document 使用 JSON 格式表示，下面是一个例子。 

   ```json
       {
         "user": "张三",
         "title": "工程师",
         "desc": "数据库管理"
       }
   ```

3. 同一个 Index 里面的 Document，不要求有相同的结构（scheme），但是最好保持相同，这样有利于提高搜索效率。 

4. Type  Document 可以分组，比如`weather`这个 Index 里面，可以按城市分组（北京和上海），也可以按气候分组（晴天和雨天）。这种分组就叫做 Type，它是虚拟的逻辑分组，用来过滤 Document。 

5. 列出每个 Index 所包含的 Type。 

   ```
   curl localhost:9200/_mapping?pretty=true
   
   ```

6. 根据[规划](https://www.elastic.co/blog/index-type-parent-child-join-now-future-in-elasticsearch)，Elastic 6.x 版只允许每个 Index 包含一个 Type，7.x 版将会彻底移除 Type。 





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





----

# 其他

### SpEL表达式

**Spring 表达式语言(简称SpEL)：**是一个支持运行时查询和操作对象图的强大的表达式语言。

**语法类似于 EL：**SpEL 使用 #{...} 作为定界符 , 所有在大括号中的字符都将被认为是 SpEL , SpEL 为 bean 的属性进行动态赋值提供了便利。

**通过 SpEL 可以实现：**

- 通过 bean 的 id 对 bean 进行引用。
- 调用方式以及引用对象中的属性。
- 计算表达式的值
- 正则表达式的匹配。



#### 示例



```
@Document(indexName = "bhpms-#{configProperties['index.version']}", type = "type2")
public class OrderItem implements Serializable {
```



```java
 @Test
    public void testConstructorExpression() throws Exception {
        ExpressionParser parser = new SpelExpressionParser();
        String result1 = parser.parseExpression("new String('haha')").getValue(String.class);
        //Assert.assertEquals("haha", result1);
        System.out.println("result1=" + result1);
        Date result2 = parser.parseExpression("new java.util.Date()").getValue(Date.class);
        Assert.assertNotNull(result2);
        System.out.println("result2=" + result2.toString());

        System.out.println("tm=" + tm);

        /*String result3 = parser.parseExpression("com.mx.video.utils.MyUtils.getTodayDateString()").getValue(String.class);
        Assert.assertNotNull(result2);
        System.out.println("result3=" + result3);*/
    }

    @Value("userevent-#{T(com.mx.video.utils.MyUtils).getTodayDateString()}")
    //@Value("userevent")
     String tm ;
```





#### 参考链接

1. [SpEL表达式](https://www.cnblogs.com/goodcheap/p/6490896.html)
2. [跟我学Spring3（5.3）：Spring 表达式语言之 SpEL 语法](http://www.importnew.com/17724.html)