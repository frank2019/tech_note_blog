



### 常见元素



- Person:人员
- System:系统，包含DB、Application、WebPage等
- System_ext:外部系统
- System_Boundary:系统边界，在这个边界中的都是系统的组成部分，里面一般是Container级别的组件
- Container:容器，不是Docker之类的容器，简单点可以直接理解为System的组成部分，比如DB、Application等
- ContainerDb:DB
- Container_Boundary:容器边界，在这个边界范围内的都是容器的组成部分，里面一般都是Component级别的数据
- Component:组件，比如一个Controller，一个Service逻辑处理类，一个Domain等
- Rel:连接线

### 指定图的模式

##### LAYOUT_WITH_LEGEND()

```
LAYOUT_WITH_LEGEND()
```

在include之后加上这行代码，会在生成图形的右下角生成如下内容

##### LAYOUT_AS_SKETCH()

加上这个表示草稿，整个渲染生成的图形都是草稿样式

##### LAYOUT_TOP_DOWN

排列方向，顾名思义为从上到下排列，注意不需要加括号

##### LAYOUT_LEFT_RIGHT

排列方向，顾名思义为从左到右排列，注意不需要加括号





如何控制架构图中元素的相对位置？

