

graphviz



```

```



#### Graphviz 是什么

Graphviz的主题思想是

```
所思即所得
```

Graphviz是贝尔实验室开发的一个开源的工具包，它使用一个特定的DSL（领域特定语言）——Dot作为脚本语言，然后使用布局引擎解析脚本并完成自动布局。Graphviz的设计初衷是对图进行自动布局（有向图、无向图、），可以使用dot脚本来定义图形元素，选择一定的算法进行布局，通过对输入脚本的解析，分析出其中的点，边以及子图，然后根据属性进行绘制，继而将结果以自己需要的格式导出来。

Granphviz的特点有如下几个方面：

- 代码控制，所思即所得
- 布局引擎自动布局
- （导出格式非常丰富）

#### Granphviz安装

```bash
sudo apt-get install graphviz
```

#### 示例

##### step 1 编辑dot脚本

使用`UTF-8`

```c++
digraph G{
    main -> parse -> execute;
    main -> init;
    main -> cleanup;
    execute -> make_string;
    execute -> printf;
    init -> make_string;
    main -> printf;
    execute -> compare;
}
```

##### step 2 根据布局生成结果

```bash
dot -Tpng sample.dot -o sample.png
```

或者

```
dot -Kdot -Tpng sample.dot -o sample.png
```

其中

`dot`表示用dot布局， 这里是一条命令，安装Granphviz后会自动安装此命令。

`-Tpng`表示生成png图片格式

`sample.dot`是脚本文件名

`-o sample.png`表示生成输出的图片名称。

`-Kdot`表示使用dot布局



**Step 3**：查看生成结果

可以使用此命令

```
display sample.png
```



#### Graphviz支持的布局及输出图片格式

Graphviz支持几种布局引擎：

- dot ： 默认布局方式，主要用于有向图
- neato ： 主要用于无向图
- twopi ： 主要用于径向布局
- circo ： 圆环布局
- fdp ： 主要用于无向图
- sfdp ： 主要绘制较大的无向图
- patchwork ： 主要用于树哈希图（tree map）

Graphviz支持的输出图片格式更是相当的多，常用的有以下几种：

- pdf ：
- gif
- png ：
- jpeg ： 一种有损压缩图片格式
- bmp ： 一种位图格式
- svg ： 矢量图，一般用与Web，，可以用浏览器打开
- ps ： 矢量线图，多用于打印







#### 参考链接

1. [使用graphviz绘制流程图](http://icodeit.org/2012/01/%E4%BD%BF%E7%94%A8graphviz%E7%BB%98%E5%88%B6%E6%B5%81%E7%A8%8B%E5%9B%BE/)
2. http://www.graphviz.org/