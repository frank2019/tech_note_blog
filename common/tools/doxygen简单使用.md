Doxygen是一种开源跨平台的，以类似JavaDoc风格描述的文档系统，可以从一套归档源文件开始，生成文档

使用组合：Doxygen + Graphviz

Doxygen可以生成动态文档

Graphviz可以生成视图连接将.c文件中所用到的函数、头文件生成一个树状结构并且设置之后可以生成相对应的函数的跳转，方便查询函数。  

Microsoft  HTML Help Workshop：   用于生成chm文件

### 1 Doxygen配置方法

#### 1.1 Doxygen的主页面

首先修改Project name，选择扫描源代码的目录，Source code directory：勾选Scan recursively：

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134632137-1911963824.png)

 

#### 1.2>在Wizard的Topics下的Mode，

选择All Entities，可以输出相对完整的功能，是否包含源代码看自身情况，在下面选择好自己的语言。这里得是C所以选择C or PHP

 

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134642684-653993343.png)

 

#### 1.3>在Output中，

如果你需要输出chm格式，勾选chm,没有要求的话html就可以了

![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134658340-528586268.png)

 

#### 1.4>在Diagrams中

选择使用GraphViz包，来输出UML，GraphViz包可以帮助建立一些树状视图。

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134708528-1390697158.png)

#### 1.5>Expert中，

你需要首选确定你所输出的语言，个人使用中文在Expert的Input中，很重要的是**INPUT_ENCODING**项，如果使用的为微软默认字符集请填写GBK，不然目录乱码,当前选择UTF-8，输出语言选择的是Chinese.

![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134726809-2009511434.png)

#### 1.6>Build页面，

这个页面是生成帮助信息中比较关键的配置页面：

EXTRACT_ALL 表示：输出所有的函数，但是private和static函数不属于其管制。

EXTRACT_PRIVATE 表示：输出private函数。

EXTRACT_STATIC 表示：输出static函数。同时还有几个EXTRACT，相应查看文档即可。

HIDE_UNDOC_MEMBERS 表示：那些没有使用doxygen格式描述的文档（函数或类等）就不显示了。当然，如果EXTRACT_ALL被启用，那么这个标志其实是被忽略的。

INTERNAL_DOCS 主要指：是否输出注解中的@internal部分。如果没有被启动，那么注解中所有的@internal部分都将在目标帮助中不可见。

CASE_SENSE_NAMES 表示：是否关注大小写名称，注意，如果开启了，那么所有的名称都将被小写。对于C/C++这种字母相关的语言来说，建议永远不要开启。

HIDE_SCOPE_NAMES 表示：域隐藏，建议永远不要开启。

SHOW_INCLUDE_FILES 表示：是否显示包含文件，如果开启，帮助中会专门生成一个页面，里面包含所有包含文件的列表。

INLINE_INFO ：如果开启，那么在帮助文档中，inline函数前面会有一个inline修饰词来标明。

SORT_MEMBER_DOCS ：如果开启，那么在帮助文档列表显示的时候，函数名称会排序，否则按照解释的顺序显示。

GENERATE_TODOLIST ：是否生成TODOLIST页面，如果开启，那么包含在@todo注解中的内容将会单独生成并显示在一个页面中，其他的GENERATE选项同。

SHOW_USED_FILES ：是否在函数或类等的帮助中，最下面显示函数或类的来源文件。

SHOW_FILES ：是否显示文件列表页面，如果开启，那么帮助中会存在一个一个文件列表索引页面。

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134751747-1962184024.png)

#### 1.7>Expert>Input页按照下图进行设置调整参数。

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134807309-166636080.png)

#### 

1.如果在 Wizard 的 Output Topics 中选择了 prepare for compressed HTML (.chm)选项，此处就会要求选择 hhc.exe 程序的位置。在 windows help workshop 安装目录下可以找到 hhc.exe。

2.为了解决Doxygen生成的CHM文件的左边树目录的中文变成了乱码，CHM_INDEX_ENCODING中输入GB2312即可。

3.GENERATE_CHI 表示索引文件是否单独输出，建议关闭。否则每次生成两个文件，比较麻烦。

4.TOC_EXPAND 表示是否在索引中列举成员名称以及分组（譬如函数，枚举）名称。

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134823278-868684241.png)

 

#### 1.8>运行doxygen

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134843418-1597837451.png)

#### 1.9>运行结束

 ![img](https://images2015.cnblogs.com/blog/662045/201608/662045-20160803134857278-1178824723.png)

 







### 2.问题

#### 2.1，制作成CHM文件目录乱码

 CHM_INDEX_ENCODING 设置为 'GBK' 



### 3参考链接

1. [Doxygen的使用步骤](https://www.cnblogs.com/chenyang920/p/5732643.html)



下载链接

1. [Microsoft  HTML Help Workshop](https://docs.microsoft.com/zh-cn/previous-versions/windows/desktop/htmlhelp/microsoft-html-help-downloads)