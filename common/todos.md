



计算机视觉

### todo

1. [计算机视觉新手入门：大佬推荐我这样学习](https://blog.csdn.net/u013341341/article/details/79639670)
2. [一文详解计算机视觉五大技术 ](https://www.sohu.com/a/231713369_178408)               
3. [opencv 官方文档](https://docs.opencv.org/3.1.0/index.html)
4. ImageJ
5. https://www.cnblogs.com/yhlx125/category/782386.html
6. [为什么深度学习不能取代传统的计算机视觉技术？](https://blog.csdn.net/tkkzc3E6s4Ou4/article/details/79578161)
7. [图像领域深度学习的七个境界](https://blog.csdn.net/weixin_41923961/article/details/82721843)



《AI算法工程师手册》

http://www.huaxiaozhuan.com/

1. [数据挖掘领域十大经典算法之—朴素贝叶斯算法（超详细附代码）](https://blog.csdn.net/fuqiuai/article/details/79458943)



人脸识别

1. [人脸识别](https://blog.csdn.net/zchang81/article/details/76251001/)
2. [计算机视觉人脸相关开源项目总结](https://blog.csdn.net/chaipp0607/article/details/78885720)





#### 点云是什么



参考链接

1. [使用深度学习的三维点云分类的介绍](https://www.cnblogs.com/li-yao7758258/p/8182846.html)

2. [点云数据处理学习笔记](https://www.cnblogs.com/yhlx125/p/4952522.html)



# 一，openGL



### 1，OpenGL第三方库：GLFW入门篇

#### 前言：

1. GLFW是继GLUT，FreeGLUT之后，当前最新的用来创建OpenGL上下文，以及操作窗口的第三方库。
2. 官方网址为：http://www.glfw.org/。

#### 错误处理机制：

在使用GLFW之前，有必要设置一个错误处理机制，这样如果出现任何问题，GLFW都可以及时的告知我们。设置接口定义如下：
GLFWWerrorfun* glfwSetErrorCallback(GLFWWerrorfun cbfunc)
其中错误回调函数的声明如下所示：
void ExampleGLFWerrorfun(int error, const char* description)：
.error将被设置为GLFW的某个错误编码值。
.description中包含一个字符串，用于描述错误的原因。

#### GLFW使用步骤：

GLFW可以使OpenGL创建窗口变得十分简单，只需要简单四个步骤就可以完成创建窗口。流程如下：
1.初始化GLFW库。
2.创建一个GLFW窗口以及OpenGL环境。
3.渲染你的场景。
4.将输出结果呈现给用户。

#### 初始化并创建窗口：常用接口如下：

##### 1,int glfwInit(void)：

必须在其他任何GLFW函数之前被调用，因为它负责初始化整个GLFW库。如果成功的话，该接口将返回GL_TRUE，否则就会返回GL_FALSE。

##### 2,GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share)：

负责创建一个新的OpenGL环境和窗口。
.monitor非NULL的话，窗口会被全屏创建到指定的监视器上，分辨率由width和height来指定。否则窗口会被创建到桌面上，并且尺寸由width和height来指定。
.title是一个UTF-8字符串的指针，可以用来创建窗口的初始标题。
.share非NULL的话，新创建的窗口所关联的OpenGL环境将与share所给定的关联环境共享资源。

##### 3.void glfwMakeContextCurrent(GLFWwindow* window)：

设置参数window中的窗口所关联的OpenGL环境为当前环境。这个环境在当前线程中会一直保持为当前环境，直到另一个环境被设置为当前环境，或者窗口被删除为止。

##### 4.int glfwWindowShouldClose(GLFWwindow* window)：

如果用户准备关闭参数window所指定的窗口，那么此接口将会返回GL_TRUE，否则将会返回GL_FALSE。

##### 5.void glfwSwapBuffers(GLFWwindow* window)：

请求窗口系统将参数window关联的后缓存画面呈现给用户。通常这一步是通过窗口的前后缓存的交换完成的。也可能是在一个“预备显示”的帧缓存队列中进行截取，窗口系统可能需要等待一次垂直刷新事件完成，再显示帧的内容。

##### 6.void glfwPollEvents(void)：

告诉GLFW检查所有等待处理的事件和消息，包括操作系统和窗口系统中应当处理的消息。如果有消息正在等待，它会先处理这些消息再返回；否则该函数会立即返回。

##### 7.void glfwWaitEvents(void)：

等待一个或多个事件传递到应用程序，并且处理它们再返回。对应的调用线程在事件到达之前会保持睡眠状态。

#### 处理用户输入：主要是对键盘和鼠标的用户输入进行处理。常见接口如下：

##### 1.GLFWkeyfun glfwSetKeyCallback(GLFWwindow* window, GLFWkeyfun cbfun)：

设置一个新的键盘消息回调函数cbfun给指定的窗口window。如果按下或者放开键盘按键，系统会调用这个函数。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中键盘消息回调函数的声明如下所示：
void ExampleGLFWkeyfun(GLFWwindow* window, int key, int scancode, int action, int mods)：
.window就是接受到键盘消息的窗口句柄。
.key是按下或者松开的键盘按键。
.scancode是一个系统平台相关的键位扫描码信息。
.action可以是GLFW_PRESS（按下键），GLFW_RELEASE（松开键），GLFW_REPEAT（连续输入模式）中的一个。
.mods对应着辅助键的设置，例如shift和ctrl是否同时被按下。

##### 2.int glfwGetKey(GLFWwindow* window, int key)：

返回指定窗口window中指定按键key的状态，可以是GLFW_PRESS（按下键），GLFW_RELEASE（松开键），GLFW_REPEAT（连续输入模式）中的一个。

##### 3.GLFWcursorposfun glfwSetCursorPosCallback(GLFWwindow* window, GLFWcursorposfun cbfun)：

设置一个新的鼠标光标位置回调函数cbfun给指定窗口window。每当鼠标光标位置发生变化的时候，这个回调函数就会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中鼠标光标位置回调函数的声明如下所示：
void GLFWcursorposfun(GLFWwindow* window, double x, double y)：
.window就是接受到鼠标光标消息的窗口句柄。
.x和y就是鼠标光标相对于窗口左上角的新位置。

##### 4.GLFWwindowsizefun glfwSetWindowSizeCallback(GLFWwindow* window, GLFWwindowsizefun cbfun)：

设置一个新的鼠标按键回调函数cbfun给指定窗口window。当用户按下或者松开鼠标按键时，这个回调函数将会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中鼠标按键回调函数的声明如下所示：
void GLFWmousebuttonfun(GLFWwindow* window, int button, int action, int mods)：
.window就是接受到鼠标按键消息的窗口句柄。
.button就是当前的鼠标键。其中button可以是GLFW_MOUSE_BUTTON_1到GLFW_MOUSE_BUTTON_8中的一个值。
.action就是可以是GLFW_PRESS（按下键），GLFW_RELEASE（松开键），GLFW_REPEAT（连续输入模式）中的一个。
.mods对应着辅助键的设置，例如shift和ctrl是否同时被按下。

##### 5.int glfwGetMouseButton(GLFWwindow* window, int button)：

返回指定窗口window中指定鼠标键button的状态。

##### 6.GLFWscrollfun glfwSetScrollCallback(GLFWwindow* window, GLFWscrollfun cbfun)：

设置一个新的鼠标滚轮回调函数cbfun给指定窗口window。当用户滚动鼠标滚轮时，这个回调函数将会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中鼠标滚轮回调函数的声明如下所示：
void GLFWscrollfun(GLFWwindow* window, double xoffset, double yoffset)：
.window就是接受到鼠标滚轮消息的窗口句柄。
.xoffset和yoffset对应滚轮在x和y两个方向的运动。

#### 控制窗口属性：

可以在创建窗口时进行指定，也可以在程序中进行指定。常用接口如下：

##### 1.void glfwWindowHint(int hint, int value)：

设置窗口提示参数。设置以后就会影响之后创建的所有窗口。
.hint表示GLFW内部定义的状态。
.value表示状态值。

##### 2.void glfwDefaultWindowHints(void)：

恢复所有提示参数到默认值。建议在每次设置窗口提示参数之前都调用一次这个函数，这样才能保证提示参数设置值不发生混乱。

##### 3.void glfwSetWindowSize(GLFWwindow* window, int width, int height)：

设置窗口的尺寸大小。
.window表示操作的窗口句柄。
.width和height表示窗口的宽高大小。

##### 4.void glfwGetWindowSize(GLFWwindow* window, int* width, int* height)：获取窗口当前的尺寸大小。

.window表示操作的窗口句柄。
.width和height表示保存窗口宽高大小的地址。

##### 5.GLFWwindowsizefun glfwSetWindowSizeCallback(GLFWwindow* window, GLFWwindowsizefun cbfun)：

设置一个新的窗口大小回调函数cbfun给指定窗口window。当窗口大小发生变化时，这个回调函数将会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中窗口大小回调函数的声明如下所示：
void GLFWwindowsizefun(GLFWwindow* window, int width, int height)：
.window表示操作的窗口句柄。
.width和height表示窗口的宽高大小。

##### 6.void glfwSetWindowPos(GLFWwindow* window, int xpos, int ypos)：

设置窗口的坐标位置。
.window表示操作的窗口句柄。
.xpos和ypos表示窗口的横纵坐标。

##### 7.void glfwGetWindowPos(GLFWwindow* window, int* xpos, int* ypos)：

获取窗口当前位置。
.window表示操作的窗口句柄。
.xpos和ypos表示保存窗口横纵坐标的地址。

##### 8.GLFWwindowposfun glfwSetWindowPosCallback(GLFWwindow* window, GLFWwindowposfun cbfun)：

设置一个新的窗口坐标回调函数cbfun给指定窗口window。当窗口位置发生变化时，这个回调函数将会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中窗口坐标回调函数的声明如下所示：
void GLFWwindowposfun(GLFWwindow* window, int xpos, int ypos)：
.window表示操作的窗口句柄。
.xpos和ypos表示窗口的横纵坐标。

##### 9.void glfwGetFramebufferSize(GLFWwindow* window, int* width, int* height)：

获取窗口帧缓存尺寸大小。
.window表示操作的窗口句柄。
.width和height表示保存窗口帧缓存宽高大小的地址。

##### 10.GLFWframebuffersizefun glfwSetFramebufferSizeCallback(GLFWwindow* window, GLFWframebuffersizefun cbfun)：

设置一个新的窗口帧缓存大小回调函数cbfun给指定窗口window。当窗口帧缓存大小发生变化时，这个回调函数将会被触发。它的返回值是前一个回调函数的返回值，从而用来恢复之前的回调函数。
其中窗口帧缓存大小回调函数的声明如下所示：
void GLFWframebuffersizefun(GLFWwindow* window, int width, int height)：
.window表示操作的窗口句柄。
.width和height表示窗口帧缓存的宽高大小。

##### 11.void glfwSetWindowUserPointer(GLFWwindow* window, void* pointer)：

设置窗口关联的用户数据指针。这里GLFW仅做存储，不做任何的特殊处理和应用。
.window表示操作的窗口句柄。
.pointer表示用户数据指针。

##### 12.void* glfwGetWindowUserPointer(GLFWwindow* window)：

获取窗口关联的用户数据指针。
.window表示操作的窗口句柄。

#### 清理和关闭程序：

通常用在退出GLFW时进行的操作。常用接口如下：

##### 1.void glfwDestroyWindow(GLFWwindow* window)：

销毁窗口对象以及关联的OpenGL环境。
.window表示操作的窗口句柄。

##### 2.void glfwTerminate(void)：

##### 关闭glfw库本身。





glfwInit

参考链接

1. [OpenGL第三方库：GLFW入门篇](https://blog.csdn.net/zjz520yy/article/details/83000081)





### 常用接口

1.  glPushMatrix、glPopMatrix操作其实就相当于栈里的入栈和出栈。


# 深度相机的原理

### todo

1. [深度相机（一）——分类：TOF、RGB双目、结构光优劣分析](https://blog.csdn.net/qq_37764129/article/details/81011221)
2. 



### 结构光是什么

**结构光**是一组由投影仪和摄像头组成的系统结构。用投影仪投射特定的光信息到物体表面后及背景后，由摄像头采集。根据物体造成的光信号的变化来计算物体的位置和深度等信息，进而复原整个三维空间。



就iPhone X 来说，主要会在以下这几个领域中使用到和 3D 结构光相关的技术：

　　1.Face ID 人脸解锁

　　2.Apple Pay 移动支付

　　3.网站账密自动填写

　　4.前置人像虚化

　　5.Animoji 动态表情

　　6.少部分第三方应用的加密功能



### 激光散斑原理总结







1. [激光散斑原理总结](https://blog.csdn.net/u013360881/article/details/51395427)





### 双目立体视觉原理

#### todo：

1. 同名点是什么
2. 视差的原理
3. 视差与深度的关系



双目视觉简化原理图

![](https://img-blog.csdn.net/20160827135850576)



通过这张图，我们得出视差的计算表达式为：
$$
disparity=x-x^{'}=\frac{BF}{Z}
$$
其中x和x′对应的是场景中的3D点和相机中心在图像平面上的投影点的距离，

B是两个相机中心的距离，

f是相机的焦距，

Z就是对应点的深度了.

通过上面的表达式我们也能看出来深度和视差成反比.



Disparity refers to the distance between two corresponding points in the left and right image of a stereo pair. If you look at the image below you see a labelled point X (ignore X1, X2 & X3). By following the dotted line from X to OL you see the intersection point with the left hand plane at XL. The same principal applies with the right-hand image plane. 



![](https://img-blog.csdn.net/20160827141522506)



If X projects to a point in the left frame XL = (u,v) and to the right frame at XR = (p,q) you can find the disparity for this point as the magnitude of the vector between (u,v) and (p,q). Obviously this process involves choosing a point in the left hand frame and then finding its match (often called the corresponding point) in the right hand image; often this is a particularly difficult task to do without making a lot of mistakes





#### 参考链接

1. https://wenku.baidu.com/view/7c8ccd0ff61fb7360a4c6543.html
2. https://wenku.baidu.com/view/b801a64bcf84b9d528ea7a1c.html
3. [视差和深度分析与计算](https://blog.csdn.net/linear_luo/article/details/52334990)





### 单目结构光深度相机原理



### 视差图与深度图





参考链接

1. https://www.jianshu.com/p/ee3872dc988b









# windows环境编程



[线程中CreateEvent和SetEvent及WaitForSingleObject的用法](https://www.cnblogs.com/MrYuan/p/5238749.html)





# cmake的使用



### 一. cmake初识

#### 1，简介

CMake是一个跨平台的安装(编译)工具,可以用简单的语句来描述所有平台的安装(编译过程)。他能够输出各种各样的makefile或者project文件,能测试编译器所支持的C++特性,类似UNIX下的automake。

```
Cmake不再使你在构建项目时郁闷地想自杀了.
                                  --一位KDE开发者
```



#### 2，特点：

cmake的特点主要有：
1，开放源代码，使用类BSD许可发布。http://cmake.org/HTML/Copyright.html
2，跨平台，并可生成native编译配置文件，在Linux/Unix平台，生成makefile，在
苹果平台，可以生成xcode，在Windows平台，可以生成MSVC的工程文件。
3，能够管理大型项目，KDE4就是最好的证明。
4，简化编译构建过程和编译过程。Cmake的工具链非常简单：cmake+make。
5，高效虑，按照KDE官方说法，CMake构建KDE4的kdelibs要比使用autotools来
构建KDE3.5.6的kdelibs快40%，主要是因为 Cmake在工具链中没有libtool。
6，可扩展，可以为cmake编写特定功能的模块，扩充cmake功能。

#### 3，问题，难道就没有问题？

1，cmake很简单，但绝对没有听起来或者想象中那么简单。
2，cmake编写的过程实际上是编程的过程，跟以前使用autotools一样，不过你需要编
写的是CMakeLists.txt(每个目录一个)，使用的是”cmake语言和语法”。
3，cmake跟已有体系的配合并不是特别理想，比如pkgconfig，您在实际使用中会有所
体会，虽然有一些扩展可以使用，但并不理想。



#### 4，个人的建议：

1，如果你没有实际的项目需求，那么看到这里就可以停下来了，因为cmake的学习过程就
是实践过程，没有实践，读的再多几天后也会忘记。
2，如果你的工程只有几个文件，直接编写Makefile是最好的选择。
3，如果使用的是C/C++/Java之外的语言，请不要使用cmake(至少目前是这样)
4，如果你使用的语言有非常完备的构建体系，比如java的ant，也不需要学习cmake，虽然有成功的例子，比如QT4.3的csharp绑定qyoto。
5，如果项目已经采用了非常完备的工程管理工具，并且不存在维护问题，没有必要迁移到
cmake
4，如果仅仅使用qt编程，没有必要使用cmake，因为qmake管理Qt工程的专业性和自
动化程度比cmake要高很多

#### 5，一个简单的例子

##### CMake 支持的命令

​    CMake的所语句都写在一个叫:CMakeLists.txt的文件中。当CMakeLists.txt文件确定后,可以用ccmake命令对相关 的变量值进行配置。这个命令必须指向CMakeLists.txt所在的目录。配置完成之后,应用cmake命令生成相应的makefile（在Unix  like系统下）或者 project文件（指定用window下的相应编程工具编译时）。

​    其基本操作流程为：

```

    $> ccmake directory
    $> cmake directory
    $> make
```

其中directory为CMakeList.txt所在目录；

- 第一条语句用于配置编译选项，如VTK_DIR目录 ，一般这一步不需要配置，直接执行第二条语句即可，但当出现错误时，这里就需要认为配置了，这一步才真正派上用场；
- 第二条命令用于根据CMakeLists.txt生成Makefile文件；
- 第三条命令用于执行Makefile文件，编译程序，生成可执行文件；



cmake 没有clean 命令，so 只能靠自己

也可以实现一个

//todo

CMake的执行就是这么简单，其难点在于如何编写CMakeLists.txt文件，下面结合例子简单介绍



##### 第一个实例

CMakeLists.txt的编写，看下面这个CMakeLists.txt

```cmake
# cmake version
cmake_minimum_required(VERSION 2.8)
#
set(OpenCV_DIR "/usr/local/opencv2.4/share/OpenCV")

project(test)
find_package(OpenCV 2.4.13  REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})


add_executable(test src/test.cpp)
target_link_libraries(test ${OpenCV_LIBS})
```

##### 下面对其进行解释：

//todo

1. add_library

该指令的主要作用就是将指定的源文件生成链接文件，然后添加到工程中去。该指令常用的语法如下：

```
add_library(<name> [STATIC | SHARED | MODULE][EXCLUDE_FROM_ALL]
            [source1][source2] [...])
```

其中<name>表示库文件的名字，该库文件会根据命令里列出的源文件来创建。而STATIC、SHARED和MODULE的作用是指定生成的库文件的类型。STATIC库是目标文件的归档文件，在链接其它目标的时候使用。SHARED库会被动态链接（动态链接库），在运行时会被加载。MODULE库是一种不会被链接到其它目标中的插件，但是可能会在运行时使用dlopen-系列的函数。默认状态下，库文件将会在于源文件目录树的构建目录树的位置被创建，该命令也会在这里被调用。

而语法中的source1 source2分别表示各个源文件。



link_directories

该指令的作用主要是指定要链接的库文件的路径，该指令有时候不一定需要。因为find_package和find_library指令可以得到库文件的绝对路径。不过你自己写的动态库文件放在自己新建的目录下时，可以用该指令指定该目录的路径以便工程能够找到。



target_link_libraries

该指令的作用为将目标文件与库文件进行链接。该指令的语法如下：

```
target_link_libraries(<target> [item1][item2] [...][[debug|optimized|general] <item>] ...)
```

上述指令中的<target>是指通过add_executable()和add_library()指令生成已经创建的目标文件。而[item]表示库文件没有后缀的名字。默认情况下，库依赖项是传递的。当这个目标链接到另一个目标时，链接到这个目标的库也会出现在另一个目标的连接线上。这个传递的接口存储在interface_link_libraries的目标属性中，可以通过设置该属性直接重写传递接口。



### cmake的基本概念



1. https://www.cnblogs.com/lidabo/p/7359422.html



### 二.cmake常用变量及环境变量

#### 1，cmake 变量引用的方式:

使用${}进行变量的引用。在 IF 等语句中,是直接使用变量名而不通过${}取值

#### 2，cmake 变量的定义方式

隐式定义和显式定义两种

一个隐式定义的例子, PROJECT 指令,他会隐式的定义<projectname>_BINARY_DIR 和<projectname>_SOURCE_DIR 

显式定义 使用SET

SET(HELLO_SRC main.SOURCE_PATHc),就 PROJECT_BINARY_DIR 可以通过${HELLO_SRC}来引用这个自定义变量了.



#### 3，cmake  常用变量:

##### CMAKE_BINARY_DIR，PROJECT_BINARY_DIR， <projectname>_BINARY_DIR

这三个变量指代的内容是一致的,如果是  in source 编译,指得就是工程顶层目录,如果是 out-of-source 编译,指的是工程编译发生的目录。PROJECT_BINARY_DIR  跟其他指令稍有区别,现在,你可以理解为他们是一致的。

##### CMAKE_SOURCE_DIR，PROJECT_SOURCE_DIR， <projectname>_SOURCE_DIR

这三个变量指代的内容是一致的,不论采用何种编译方式,都是工程顶层目录。

也就是在  in source 编译时,他跟 CMAKE_BINARY_DIR 等变量一致。

PROJECT_SOURCE_DIR  跟其他指令稍有区别,现在,你可以理解为他们是一致的。

3,CMAKE_CURRENT_SOURCE_DIR

指的是当前处理的  CMakeLists.txt 所在的路径,比如上面我们提到的 src 子目录。

4,CMAKE_CURRRENT_BINARY_DIR

如果是  in-source 编译,它跟 CMAKE_CURRENT_SOURCE_DIR 一致,如果是 out-of-source 编译,他指的是 target  编译目录。

使用我们上面提到的  ADD_SUBDIRECTORY(src bin)可以更改这个变量的值。

使用  SET(EXECUTABLE_OUTPUT_PATH <新路径>)并不会对这个变量造成影响,它仅仅修改了最终目标文件存放的路径。

5,CMAKE_CURRENT_LIST_FILE

输出调用这个变量的  CMakeLists.txt 的完整路径

 

6,CMAKE_CURRENT_LIST_LINE

输出这个变量所在的行

7,CMAKE_MODULE_PATH

这个变量用来定义自己的  cmake 模块所在的路径。如果你的工程比较复杂,有可能会自己编写一些 cmake 模块,这些 cmake 模块是随你的工程发布的,为了让 cmake  在处理CMakeLists.txt 时找到这些模块,你需要通过 SET 指令,将自己的 cmake 模块路径设置一下。

比如

SET(CMAKE_MODULE_PATH  ${PROJECT_SOURCE_DIR}/cmake)

这时候你就可以通过  INCLUDE 指令来调用自己的模块了。

8,EXECUTABLE_OUTPUT_PATH  和 LIBRARY_OUTPUT_PATH

分别用来重新定义最终结果的存放目录,前面我们已经提到了这两个变量。

9,PROJECT_NAME

返回通过  PROJECT 指令定义的项目名称。



#### 4，cmake  调用环境变量

 使用$ENV{NAME}指令就可以调用系统的环境变量了。
比如
MESSAGE(STATUS  “HOME dir: $ENV{HOME}”)
设置环境变量的方式是:
SET(ENV{变量名}  值)
1,CMAKE_INCLUDE_CURRENT_DIR
自动添加  CMAKE_CURRENT_BINARY_DIR 和 CMAKE_CURRENT_SOURCE_DIR 到当前处理
的  CMakeLists.txt。相当于在每个 CMakeLists.txt 加入:
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_BINARY_DIR}
${CMAKE_CURRENT_SOURCE_DIR})

2,CMAKE_INCLUDE_DIRECTORIES_PROJECT_BEFORE
将工程提供的头文件目录始终至于系统头文件目录的前面,当你定义的头文件确实跟系统发生冲突时可以提供一些帮助。  

#### 5，系统信息

1,CMAKE_MAJOR_VERSION,CMAKE  主版本号,比如 2.4.6 中的 2

2,CMAKE_MINOR_VERSION,CMAKE  次版本号,比如 2.4.6 中的 4

3,CMAKE_PATCH_VERSION,CMAKE  补丁等级,比如 2.4.6 中的 6

4,CMAKE_SYSTEM,系统名称,比如  Linux-2.6.22

5,CMAKE_SYSTEM_NAME,不包含版本的系统名,比如  Linux

6,CMAKE_SYSTEM_VERSION,系统版本,比如  2.6.22

7,CMAKE_SYSTEM_PROCESSOR,处理器名称,比如  i686.

8,UNIX,在所有的类  UNIX 平台为 TRUE,包括 OS X 和 cygwin

9,WIN32,在所有的  win32 平台为 TRUE,包括 cygwin

#### 6，主要的开关选项:

1,CMAKE_ALLOW_LOOSE_LOOP_CONSTRUCTS,用来控制  IF ELSE 语句的书写方式,在

下一节语法部分会讲到。

2,BUILD_SHARED_LIBS

这个开关用来控制默认的库编译方式,如果不进行设置,使用  ADD_LIBRARY 并没有指定库

类型的情况下,默认编译生成的库都是静态库。

如果  SET(BUILD_SHARED_LIBS ON)后,默认生成的为动态库。

3,CMAKE_C_FLAGS

设置  C 编译选项,也可以通过指令 ADD_DEFINITIONS()添加。

4,CMAKE_CXX_FLAGS

设置  C++编译选项,也可以通过指令 ADD_DEFINITIONS()添加。



### 三.常用指令



#### 1，ADD_DEFINITIONS

向C/C++编译器添加-D定义，比如:

```
ADD_DEFINITIONS(-DENABLE_DEBUG  -DABC)，参数之间用空格分割。
```

如果你的代码中定义了#ifdef ENABLE_DEBUG #endif，这个代码块就会生效。
相当于代码中有定义了 ENABLE_DEBUG 

#### ２，ADD_DEPENDENCIES

定义target依赖的其他target，确保在编译本target之前，其他的target已经被构
建。

```cmake
ADD_DEPENDENCIES(target-name depend-target1
depend-target2 ...)
```

#### ３，ADD_EXECUTABLE、ADD_LIBRARY、ADD_SUBDIRECTORY

通过ADD_EXECUTABLE或者ADD_LIBRARY定义的目标文件，可能是可执行二进制、动态库、静态库

```cmake
add_executable(<name> [WIN32] [MACOSX_BUNDLE]
               [EXCLUDE_FROM_ALL]
               [source1] [source2 ...])
```



实例

```cmake
ADD_EXECUTABLE(hello main.c)
```



ADD_SUBDIRECTORY指令

```cmake
ADD_SUBDIRECTORY(source_dir [binary_dir][EXCLUDE_FROM_ALL])
```

这个指令用于向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存
放的位置。EXCLUDE_FROM_ALL参数的含义是将这个目录从编译过程中排除





#### ４，ADD_TEST与ENABLE_TESTING指令。

ENABLE_TESTING指令用来控制Makefile是否构建test目标，涉及工程所有目录。语
法很简单，没有任何参数，ENABLE_TESTING()，一般情况这个指令放在工程的主
CMakeLists.txt中.
ADD_TEST指令的语法是:
ADD_TEST(testname Exename arg1 arg2 ...)
testname是自定义的test名称，Exename可以是构建的目标文件也可以是外部脚本等
等。后面连接传递给可执行文件的参数。如果没有在同一个CMakeLists.txt中打开
ENABLE_TESTING()指令，任何ADD_TEST都是无效的。





#### 5，MESSAGE

```
MESSAGE([SEND_ERROR | STATUS | FATAL_ERROR] "message to display"
...)
```

这个指令用于向终端输出用户定义的信息，包含了三种类型:
​	SEND_ERROR，产生错误，生成过程被跳过。
​	SATUS，输出前缀为—的信息。
​	FATAL_ERROR，立即终止所有cmake过程.



### 四，应用实例

#### 2，cmake option的使用



##### 参考链接

1. [cmake option的使用](https://blog.csdn.net/haima1998/article/details/23352881)

#### 1，在cmake中设置宏

先说一下 if else的用法

```cmake
if(" ${CMAKE_SOURCE_DIR}" STREQUAL " ${CMAKE_BINARY_DIR}")
  message(FATAL_ERROR "
FATAL: In-source builds are not allowed.
       You should create a separate directory for build files.
")
else()
	message("build in")
endif()

```



关系操作符

| **NOT**        | 非，NOT E1                                                   |
| -------------- | ------------------------------------------------------------ |
| **AND**        | 与，E1 AND E2                                                |
| **OR**         | 或，E1 OR E2                                                 |
| **EXIST**      | ~ E，存在 name 的文件或者目录（应该使用绝对路径），真        |
| **COMMAND**    | ~ E，存在 command-name 命令、宏或函数且能够被调用，真        |
| **DEFINED**    | ~ E，变量被定义了，真                                        |
| **EQUAL**      | E1 ~ E2，变量值或者字符串匹配 regex 正则表达式               |
| **LESS**       |                                                              |
| **GREATER**    |                                                              |
| **STRLESS**    | E1 ~ E2，变量值或者字符串为有效的数字且满足小于（大于、等于）的条件 |
| **STRGREATER** |                                                              |
| **STREQUAL**   |                                                              |



实现

CmakeList

```
set (VERSION_MAJOR 0)
set (VERSION_MINOR 0)
set (VERSION_REVISION 1)
set (VERSION_BUILD 0)

set (SUPPORT_TEST 1)


configure_file (
  "${PROJECT_SOURCE_DIR}/version.h.in"
  "${PROJECT_BINARY_DIR}/version.h"
  )

```

version.h.in

```
#define SUPPORT_TEST @SUPPORT_TEST@
#define VERSION_MAJOR @VERSION_MAJOR@
#define VERSION_MINOR @VERSION_MINOR@
#define VERSION_REVISION @VERSION_REVISION@
#define VERSION_BUILD @VERSION_BUILD@
```



可自动生成   "${PROJECT_BINARY_DIR}/version.h"

@SUPPORT_TEST@  使用对应的值代替



### 参考链接

1. [cmake 常用变量和常用环境变量查表手册---整理 .](https://www.cnblogs.com/xianghang123/p/3556425.html)
1. [cmake 学习笔记(二)](https://blog.csdn.net/dbzhang800/article/details/6329068)
1. [官方参考手册](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#)



参考链接

1. [](https://www.cnblogs.com/lidabo/p/7359422.html)
2. [CMAKE的使用](https://www.cnblogs.com/lidabo/p/3974305.html)



### 进阶

1. [cmake的命令execute_process](https://www.cnblogs.com/the-capricornus/p/4759157.html)
2. https://cmake.org/cmake/help/v3.13/manual/cmake.1.html
3. [cmake使用示例与整理总结](https://blog.csdn.net/wzzfeitian/article/details/40963457/)



### cmake Q&A

1，检测仅支持out source方式编译

- 内部构建：in-source build，在项目的入口配置文件目录下执行“cmake .”时，就是内部构建；这种方式下，生成的临时中间文件就放在了构建目录下，导致和源文件混在一起

- 外部构建：out-of-source build，在其他目录下执行cmake构建命令，然后指定入口配置文件的目录，这样就可以将临时文件存放于单独的目录中。比如我们在项目下新建一个build目录，然后在build目录下执行“cmake ..”，那么我们就可以看到构建后的所有临时文件都产生在build目录中，这样就方便我们管理和清理了

```
if(" ${CMAKE_SOURCE_DIR}" STREQUAL " ${CMAKE_BINARY_DIR}") message(FATAL_ERROR " FATAL: In-source builds are not allowed. You should create a separate directory for build files. ") endif()
```





2，设置支持c++11

```
if(CONAN_LIBCXX STREQUAL "libstdc++11")
    add_definitions(-D_GLIBCXX_USE_CXX11_ABI=1)
elseif(CONAN_LIBCXX STREQUAL "libstdc++")
    add_definitions(-D_GLIBCXX_USE_CXX11_ABI=0)
endif()
```



### linux 中关于

1. [GCC 命令行详解 -L 指定库的路径 -l 指定需连接的库名](https://www.cnblogs.com/wangf/archive/2012/04/28/2474579.html)





## qt vs c ++问题集锦

### 0x01 std::__cxx11::basic_string...@GLIBCXX_3.4.21’未定义的引用

std::allocator<char> >::str() const@GLIBCXX_3.4.21’未定义的引用

```
/usr/bin/ld: warning: libomp.so.5, needed by libs/depthengine/libOBDepthEngineCPP.so, not found (try using -rpath or -rpath-link)
libs/depthengine/libOBDepthEngineCPP.so：对‘VTT for std::__cxx11::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_ostringstream<char, std::char_traits<char>, std::allocator<char> >::basic_ostringstream(std::_Ios_Openmode)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >::basic_stringstream(std::_Ios_Openmode)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_assign(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘cv::Exception::Exception(int, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int)’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘__kmpc_for_static_fini@VERSION’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::logic_error::logic_error(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::compare(char const*) const@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_append(char const*, unsigned long)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘__kmpc_global_thread_num@VERSION’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘VTT for std::__cxx11::basic_istringstream<char, std::char_traits<char>, std::allocator<char> >@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::reserve(unsigned long)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::find(char, unsigned long) const@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘__kmpc_fork_call@VERSION’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘VTT for std::__cxx11::basic_ostringstream<char, std::char_traits<char>, std::allocator<char> >@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::domain_error::domain_error(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_replace(unsigned long, unsigned long, char const*, unsigned long)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_istringstream<char, std::char_traits<char>, std::allocator<char> >::basic_istringstream(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::_Ios_Openmode)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_create(unsigned long&, unsigned long)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::basic_istream<char, std::char_traits<char> >& std::getline<char, std::char_traits<char>, std::allocator<char> >(std::basic_istream<char, std::char_traits<char> >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, char)@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘vtable for std::__cxx11::basic_stringbuf<char, std::char_traits<char>, std::allocator<char> >@GLIBCXX_3.4.21’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘__kmpc_for_static_init_4@VERSION’未定义的引用
libs/depthengine/libOBDepthEngineCPP.so：对‘std::__cxx11::basic_stringbuf<char, std::char_traits<char>, std::allocator<char> >::str() const@GLIBCXX_3.4.21’未定义的引用
collect2: error: ld returned 1 exit status

```



```
libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f0c2aeb2000)
	libomp.so.5 => not found
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f0c2ac9b000)

```



```
$ strings  /lib/x86_64-linux-gnu/libm.so.6   |grep  GLIBC
GLIBC_2.2.5
GLIBC_2.4
GLIBC_2.15
GLIBC_2.18
GLIBC_PRIVATE

```

原因分析：  引用的第三方库 依赖高版本的glibc 特性     GLIBCXX_3.4.21  升级glibc 或者升级gcc







std::__cxx11::basic_stringstream  在那个库中   libstdc++中



##### 检测是否支持

nm   -D  /usr/lib/x86_64-linux-gnu/libstdc++.so.6 |grep  _ZTTNSt7__cxx1119basic_ostringstreamIcSt11char_traitsIcESaIcEEE
0000000000380c48 V _ZTTNSt7__cxx1119basic_ostringstreamIcSt11char_traitsIcESaIcEEE





参考链接

1. [关于编译报错 error: cannot convert 'const std::__cxx11::basic_string<char>' to 'const char*' 的处理](https://blog.csdn.net/ufolr/article/details/52669333?locationNum=2&fps=1)
2. [ubuntu14.04 升级gcc的方法](https://blog.csdn.net/qingrenufo/article/details/78661513)
3. [linux glibc升级](https://blog.csdn.net/fan_fan_feng/article/details/79598804)
4. https://blog.csdn.net/changqing5818/article/details/79679104
5. [于编译报错 error: cannot convert 'const std::__cxx11::basic_string<char>' to 'const char*' 的处理](https://blog.csdn.net/ufolr/article/details/52669333?locationNum=2&fps=1)



vs编程问题集锦

```

```

### 0x02 vs2015::无法解析的外部符号 __snprintf



简介

vs2015链接vs2012的库时，提示无法解析的外部符号 __snprintf



解决方案

附加链接库legacy_stdio_definitions.lib可以解决此问题    


    #pragma comment(lib, "legacy_stdio_definitions.lib")


#### 或在工程配置的附加依赖项中添加此库
```
legacy_stdio_definitions.lib
```



### 0x03 vs设置release版本可调试

属性->C/C++->优化->优化     选择为 "已禁止/-Od"

属性->连接器->调试->生成调试信息        “是/debug”



属性->C/C++->常规->调试信息格式     选择为 "程序数据库/Zi"

https://blog.csdn.net/caoshangpa/article/details/76575640



### 0x04 如何使用VS2015开发Qt5程序



https://jingyan.baidu.com/article/19020a0a7e49ab529d2842e9.html

### qt 项目转vs工程

在windows下，运行Qt Command Prompt。

输入命令行：

qmake -tp vc XXX.pro

会生成文件XXX.vcxproj





### QtCreator  快捷键





# C++

### todo

1. https://github.com/sindresorhus/awesome
2. https://github.com/fffaraz/awesome-cpp#readme
3. [国外经典C++书籍推荐(根据自身体会)](https://www.cnblogs.com/mydec1220/articles/4351489.html)



### c++  内存检测工具



#### 参考链接

1. [C++内存错误检测工具](https://blog.csdn.net/woshichenjiacheng/article/details/78884822)
2. [linuxC++内存泄露检查工具2](https://blog.csdn.net/ttomqq/article/details/81937561)
3. [C++中的RAII介绍](https://www.cnblogs.com/jiangbin/p/6986511.html)



1. [动态库版本号管理](https://blog.csdn.net/fouweng/article/details/53435514)



### std::move

[C++ std::move/std::forward/完美转发](https://www.cnblogs.com/jianhui-Ethan/p/4670399.html)



### 智能指针 std::shared_ptr

shared_ptr 是一个标准的共享所有权的智能指针, 允许多个指针指向同一个对象. 定义在 memory 文件中(非memory.h), 命名空间为 std.

　　shared_ptr 是为了解决 auto_ptr 在对象所有权上的局限性(auto_ptr 是独占的), 在使用引用计数的机制上提供了可以共享所有权的智能指针, 当然这需要额外的开销:
　　(1) shared_ptr 对象除了包括一个所拥有对象的指针外, 还必须包括一个引用计数代理对象的指针.
　　(2) 时间上的开销主要在初始化和拷贝操作上, *和->操作符重载的开销跟auto_ptr是一样.
　　(3) 开销并不是我们不使用shared_ptr的理由, 永远不要进行不成熟的优化, 直到性能分析器告诉你这一点.

　　使用方法:

 可以使用模板函数 make_shared 创建对象, make_shared 需指定类型('<>'中)及参数('()'内), 传递的参数必须与指定的类型的构造函数匹配. 如:
​        　　std::shared_ptr<int> sp1 = std::make_shared<int>(10);
​        　　std::shared_ptr<std::string> sp2 = std::make_shared<std::string>("Hello c++");
​    也可以定义 auto 类型的变量来保存 make_shared 的结果.
​        　　auto sp3 = std::make_shared<int>(11);
​        　　printf("sp3=%d\n", *sp3);
​        　　auto sp4 = std::make_shared<std::string>("C++11");
​        　　printf("sp4=%s\n", (*sp4).c_str());



参考链接

1. [C++智能指针 shared_ptr](https://www.cnblogs.com/diysoul/p/5930361.html)

### c++  风格指南



#### ABI（Application Binary Interface）



 应用程序二进制接口 描述了应用程序和操作系统之间，一个应用和它的库之间，或者应用的组成部分之间的低接口。

ABI涵盖了各种细节，如：

- 数据类型的大小、布局和对齐;
- 调用约定（控制着函数的参数如何传送以及如何接受返回值），例如，是所有的参数都通过栈传递，还是部分参数通过寄存器传递；哪个寄存器用于哪个函数参数；通过栈传递的第一个函数参数是最先push到栈上还是最后；
- [系统调用](https://baike.baidu.com/item/%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8)的编码和一个应用如何向操作系统进行系统调用；
- 以及在一个完整的操作系统ABI中，[目标文件](https://baike.baidu.com/item/%E7%9B%AE%E6%A0%87%E6%96%87%E4%BB%B6)的[二进制](https://baike.baidu.com/item/%E4%BA%8C%E8%BF%9B%E5%88%B6/361457)格式、程序库等等



它描述了应用程序与OS之间的底层接口。ABI涉及了程序的各个方面，比如：目标文件格式、数据类型、数据对齐、[函数调用约定](https://baike.baidu.com/item/%E5%87%BD%E6%95%B0%E8%B0%83%E7%94%A8%E7%BA%A6%E5%AE%9A)以及函数如何传递参数、如何返回值、[系统调用](https://baike.baidu.com/item/%E7%B3%BB%E7%BB%9F%E8%B0%83%E7%94%A8/861110)号、如何实现系统调用等。

一套完整的ABI（比如：[Intel](https://baike.baidu.com/item/Intel) Binary Compatibility Standard (iBCS)），可以让程序在所有支持该ABI的系统上运行，而无需对程序进行修改。



参考链接

1. [Google开源项目c++风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/contents/)



1. 



### function、bind以及lamda表达式

1. std::function是一个**函数包装器模板**，最早来自boost库，对应其**boost::function**函数包装器。在c++0x11中，将boost::function纳入标准库中。该函数包装器模板能包装任何类型的**可调用元素**（callable element）
2. 利用Lambda表达式，可以方便的定义和创建匿名函数
3. 

参考链接

1. [function、bind以及lamda表达式总结](https://www.cnblogs.com/yyxt/p/4253088.html)
2. [C++ 11 Lambda表达式](https://www.cnblogs.com/DswCnblog/p/5629165.html)
3. 

### c++11中的同步机制



#### 1,std::condition_variable

​	C++11中引入了条件变量，其相关内容均在<condition_variable>中。这里主要介绍std::condition_variable类。

​	条件变量std::condition_variable用于多线程之间的通信，它可以阻塞一个或同时阻塞多个线程。std::condition_variable需要与std::unique_lock配合使用。

​	当std::condition_variable对象的某个wait函数被调用的时候，它使用std::unique_lock(通过std::mutex)来锁住当前线程。当前线程会一直被阻塞，直到另外一个线程在相同的std::condition_variable对象上调用了notification函数来唤醒当前线程。

​	std::condition_variable对象通常使用std::unique_lock<std::mutex>来等待，如果需要使用另外的lockable类型，可以使用std::condition_variable_any类。

​	std::condition_variable类的成员函数：

​	(1)、构造函数：仅支持默认构造函数，拷贝、赋值和移动(move)均是被禁用的；

​	(2)、wait：当前线程调用wait()后将被阻塞，直到另外某个线程调用notify_*唤醒当前线程；当线程被阻塞时，该函数会自动调用std::mutex的unlock()释放锁，使得其它被阻塞在锁竞争上的线程得以继续执行。一旦当前线程获得通知(notify，通常是另外某个线程调用notify_*唤醒了当前线程)，wait()函数也是自动调用std::mutex的lock()；

​	(3)、wait_for：与wait()类似，只是wait_for可以指定一个时间段，在当前线程收到通知或者指定的时间超时之前，该线程都会处于阻塞状态。而一旦超时或者收到了其它线程的通知，wait_for返回，剩下的步骤和wait类似；

​	(4)、wait_until：与wait_for类似，只是wait_until可以指定一个时间点，在当前线程收到通知或者指定的时间点超时之前，该线程都会处于阻塞状态。而一旦超时或者收到了其它线程的通知，wait_until返回，剩下的处理步骤和wait_until类似；

​	(5)、notify_all: 唤醒所有的wait线程，如果当前没有等待线程，则该函数什么也不做；

​	(6)、notify_one：唤醒某个wait线程，如果当前没有等待线程，则该函数什么也不做；如果同时存在多个等待线程，则唤醒某个线程是不确定的(unspecified)；

​	条件变化存在虚假唤醒的情况，因此在线程被唤醒后需要检查条件是否满足。无论是notify_one或notify_all都是类似于发出脉冲信号，如果对wait的调用发生在notify之后是不会被唤醒的，所以接收者在使用wait等待之前也需要检查条件是否满足。



#### 2, std :: lock_guard

该类lock_guard是一个互斥包装，它提供了一个方便的RAII风格的机制，用于在作用域的持续时间内拥有互斥体。

当lock_guard创建对象时，它会尝试获取给定的互斥体的所有权。当控件离开lock_guard创建对象的范围时，lock_guard被破坏并释放互斥体。

该lock_guard班是不可复制的。



简单的说，它是与mutex配合使用，把锁放到lock_guard中时，mutex自动上锁，lock_guard析构时，同时把mutex解锁。

std::lock_guard是一个局部变量，创建时，g_i_mutex 上锁，析构时g_i_mutex解锁。这个功能在函数体比较长，尤其是存在多个分支的时候很有用。





#### 参考链接

1. [C++11中std::condition_variable的使用](https://www.cnblogs.com/gvlthu23061/p/7315572.html)









### 5, c++工具



作者：Pegasus Wang

链接：https://www.zhihu.com/question/23357089/answer/35258954

主要是linux下的工具：

编辑器

- vim
- emacs
- kate（KDE下一个功能强大的编辑器）

IDE(集成开发环境）

- eclipse+cdt
- clion
- qt cteator

编译器

- gcc
- g++
- clang

调试器

- gdb

构建工具

- cmake
- make

内存工具

- Purify
- Valgrind工具集(包括剖析工具Callgrind和线程分析工具Helgrind等)
- KCachegrind

剖析工具

- gprof开源剖析工具，通常作为gcc编译器的一部分。
- Quantify是IBM的一个功能强大的商业剖析工具。

静态检查器

- Lint
- google cpplint
- C++test
- cppcheck

并行编程工具

- Posix Threads
- MPI(Message Passing Interface)
- MapReduce（并行计算框架）

代码工具（命令行工具）

- nm 列出来自对象文件的符号
- objdump 显示对象文件信息
- strings 列出二进制文件中可输出的字符串
- strip 删除来自对象文件的符号
- m4 宏处理程序
- indent 代码格式化工具

监测工具

- time 计时工具
- ps 显示运行进程的当前状态
- top 给出系统的详细信息
- strace 记录对操作系统的所有访问，例如内存分配、文件I/O、系统调用和子进程的启动



###  0x04，C++的四种强制转型形式：

　　C++ 同时提供了四种新的强制转型形式（通常称为新风格的或 C++ 风格的强制转型）： 
　　

```

```



-  dynamic_cast 主要用于执行“安全的向下转型（safe downcasting）”，也就是说，要确定一个对象是否是一个继承体系中的一个特定类型。它是唯一不能用旧风格语法执行的强制转型，也是唯一可能有重大运行时代价的强制转型。
- static_cast 可以被用于强制隐型转换（例如，non-const 对象转型为 const 对象，int 转型为  double，等等），它还可以用于很多这样的转换的反向转换（例如，void* 指针转型为有类型指针，基类指针转型为派生类指针），但是它不能将一个  const 对象转型为 non-const 对象（只有 const_cast 能做到），它最接近于C-style的转换。
- const_cast 一般用于强制消除对象的常量性。它是唯一能做到这一点的 C++ 风格的强制转型。 

- 　reinterpret_cast 是特意用于底层的强制转型，导致实现依赖（implementation-dependent）（就是说，不可移植）的结果，例如，将一个指针转型为一个整数。这样的强制转型在底层代码以外应该极为罕见。


旧风格的强制转型依然合法，但是新的形式更可取。

首先，在代码中它们更容易识别（无论是人还是像 grep 这样的工具都是如此），这样就简化了在代码中寻找类型系统被破坏的地方的过程。

第二，更精确地指定每一个强制转型的目的，使得编译器诊断使用错误成为可能。例如，如果你试图使用一个
const_cast 以外的新风格强制转型来消除常量性，你的代码将无法编译。



### 0x03,vs 编译只有dll没有lib的问题

需要头文件中，使用__declspec(dllexport)  标识导出函数

参考如下：

```c++
#if defined(WIN32)
#define OS_API_EXPORT __declspec(dllexport)
#else 
#define OS_API_EXPORT  extern
#endif

OS_API_EXPORT int init_logger(const char *log_dir, slog_level level, slog_out_location logLocation);
OS_API_EXPORT void write_log(slog_level level, int print_stacktrace, const char *func_name, int line, const char *fmt, ...);


```







### 0x02，一个人极简日志模块的第二种实现

基于以下开源库实现，并作轻微定制：

https://github.com/ZZMarquis/slog

基本需求

1. win平台日志记录功能，多线程安全，支持写日志级别的设置，日志格式包含日志等级，日志时间，文件名，行号信息
2. 输出的标准输出， 或落地到文件
3. 适用于c和c++





#### slog.h

```c++
#ifndef _S_LOG_H_
#define _S_LOG_H_

#ifndef NULL
#define NULL         (0)
#endif

#ifndef TRUE
#define TRUE         (1)
#endif

#ifndef FALSE        
#define FALSE        (0)
#endif

#ifdef __cplusplus
extern "C"  {
#endif

#if defined(WIN32)
#define OS_API_EXPORT __declspec(dllexport)
#else 
#define OS_API_EXPORT  extern
#endif

typedef enum _slog_level {
    S_TRACE = 1,
    S_DEBUG = 2,
    S_INFO = 3,
    S_WARN = 4,
    S_ERROR = 5
} slog_level;

typedef enum _slog_out_location {
	LOCATION_NULL = 0,
	LOCATION_STDOUT = 1,
	LOCATION_FILE = 2
} slog_out_location;




//#define  PRINT_STACKTRACE
#define PRINT_STDOUT    0

//OS_API_EXPORT int init_logger(const char *log_dir, slog_level level);
OS_API_EXPORT int init_logger(const char *log_dir, slog_level level, slog_out_location logLocation);
OS_API_EXPORT void write_log(slog_level level, int print_stacktrace, const char *func_name, int line, const char *fmt, ...);


#if 0

#define SLOG_ST_ERROR(fmt, ...) write_log(S_ERROR, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_ST_WARN(fmt, ...) write_log(S_WARN, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_ST_INFO(fmt, ...) write_log(S_INFO, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_ST_DEBUG(fmt, ...) write_log(S_DEBUG, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_ST_TRACE(fmt, ...) write_log(S_TRACE, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)

#define SLOG_ERROR(fmt, ...) write_log(S_ERROR, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_WARN(fmt, ...) write_log(S_WARN, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_INFO(fmt, ...) write_log(S_INFO, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_DEBUG(fmt, ...) write_log(S_DEBUG, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define SLOG_TRACE(fmt, ...) write_log(S_TRACE, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)

#endif





#ifdef  PRINT_STACKTRACE


#define LOG_ERROR(fmt, ...)		write_log(S_ERROR, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_WARN(fmt, ...)		write_log(S_WARN, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_INFO(fmt, ...)		write_log(S_INFO, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_DEBUG(fmt, ...)		write_log(S_DEBUG, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_TRACE(fmt, ...)		write_log(S_TRACE, TRUE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)


#else

#define LOG_ERROR(fmt, ...)		write_log(S_ERROR, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_WARN(fmt, ...)		write_log(S_WARN, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_INFO(fmt, ...)		write_log(S_INFO, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_DEBUG(fmt, ...)		write_log(S_DEBUG, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)
#define LOG_TRACE(fmt, ...)		write_log(S_TRACE, FALSE, __FUNCTION__, __LINE__, fmt, ##__VA_ARGS__)

#endif


#ifdef __cplusplus
}
#endif

#endif // !_S_LOG_H_

```



#### slog.c



```c
#include "slog.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdarg.h>

#if defined(WIN32)
#include <io.h>
#include <direct.h>
#include <Windows.h>
#include <DbgHelp.h>
#pragma comment(lib, "Dbghelp.lib") 
#elif defined(linux)
#include <unistd.h>
#include <pthread.h>
#include <sys/stat.h>
#include <execinfo.h>
#endif

#define MAX_LEVEL_STR               (10)
#define MAX_DATE_STR                (10)
#define DATE_STR_FMT                "%04d%02d%02d"
#define MAX_TIME_STR                (20)
#define TIME_STR_FMT                "%04d/%02d/%02d %02d:%02d:%02d"
#define MAX_FILE_PATH               (260)
#define MAX_LOG_LINE                (4096)

#if defined(WIN32)
#define snprintf _snprintf
#define vsnprintf _vsnprintf
#define PROC_HANDLE HANDLE
#define SLOG_MUTEX CRITICAL_SECTION 
#elif defined(linux)
#define PROC_HANDLE void *
#define SLOG_MUTEX pthread_mutex_t
#endif

typedef struct _logger_cfg {
    PROC_HANDLE curr_proc;
    FILE *log_file;
    SLOG_MUTEX mtx;
    slog_level filter_levle;
    int inited;
	slog_out_location logLocation;
	char logFile[256];

} logger_cfg;

static logger_cfg g_logger_cfg = {
    NULL, NULL, {0}, S_INFO, FALSE };

static void _slog_init_mutex(SLOG_MUTEX *mtx)
{
#if defined(WIN32)
    InitializeCriticalSection(mtx);
#elif defined(linux)
    pthread_mutex_init(mtx, NULL);
#endif
}

static void _slog_lock(SLOG_MUTEX *mtx)
{
#if defined(WIN32)
    EnterCriticalSection(mtx);
#elif defined(linux)
    pthread_mutex_lock(mtx);
#endif
}

static void _slog_unlock(SLOG_MUTEX *mtx)
{
#if defined(WIN32)
    LeaveCriticalSection(mtx);
#elif defined(linux)
    pthread_mutex_unlock(mtx);
#endif
}

static void _get_curr_date(int datestr_size, char datestr[])
{
    time_t tt = { 0 };
    struct tm *curr_time = NULL;

    time(&tt);
    curr_time = localtime(&tt);
    snprintf(datestr, datestr_size - 1, DATE_STR_FMT,
        curr_time->tm_year + 1900, curr_time->tm_mon + 1, curr_time->tm_mday);
}

static void _get_curr_time(int timestr_size, char timestr[])
{
    time_t tt = { 0 };
    struct tm *curr_time = NULL;

    time(&tt);
    curr_time = localtime(&tt);
    snprintf(timestr, timestr_size - 1, TIME_STR_FMT,
        curr_time->tm_year + 1900, curr_time->tm_mon + 1, curr_time->tm_mday,
        curr_time->tm_hour, curr_time->tm_min, curr_time->tm_sec);
}

static char *_get_level_str(slog_level level)
{
    switch (level) {
    case S_TRACE:
        return "[TRACE]";
    case S_DEBUG:
        return "[DEBUG]";
    case S_INFO:
        return "[INFO ]";
    case S_WARN:
        return "[WARN ]";
    case S_ERROR:
        return "[ERROR]";
    default:
        return "[     ]";
    }
}

static void _write_stacktrace()
{
	if (LOCATION_NULL == g_logger_cfg.logLocation) {
		return;
	}

#define INNER_DEEP         (2)
#define MAX_DEEP           (24)
#define MAX_ST_INFO        (256)
#define MAX_ST_LINE        (512)

    unsigned int i = 0;
    unsigned short frames = 0;
    void *stack[MAX_DEEP] = { 0 };
    char st_line[MAX_ST_LINE] = { 0 };

#if defined(WIN32)
    SYMBOL_INFO *symbol = NULL;

    frames = CaptureStackBackTrace(INNER_DEEP, MAX_DEEP, stack, NULL);
    symbol = (SYMBOL_INFO *)calloc(sizeof(SYMBOL_INFO) + sizeof(char) * MAX_ST_INFO, 1);
    symbol->MaxNameLen = MAX_ST_INFO - 1;
    symbol->SizeOfStruct = sizeof(SYMBOL_INFO);
    for (i = 0; i < frames; ++i) {
        SymFromAddr(g_logger_cfg.curr_proc, (DWORD64)(stack[i]), 0, symbol);
        snprintf(st_line, sizeof(st_line) - 1, "    %d: %s [0x%X]\n", frames - i - 1, symbol->Name, symbol->Address);
        
		if (LOCATION_FILE == g_logger_cfg.logLocation) {
			fwrite(st_line, sizeof(char), strlen(st_line), g_logger_cfg.log_file);
		}
		else {
			printf("%s", st_line);
		}
    }
#elif defined(linux)
    char **st_arr = NULL;

    frames = backtrace(stack, MAX_DEEP);
    st_arr = backtrace_symbols(stack, frames);
    for (i = 0; i < frames; ++i) {
        snprintf(st_line, sizeof(st_line) - 1, "    %d: %s\n", frames - i - 1, st_arr[i]);
        fwrite(st_line, sizeof(char), strlen(st_line), g_logger_cfg.log_file);
    }
    free(st_arr);
#endif
}

static int _slog_mkdir(const char *log_dir)
{
#if defined(WIN32)
    if (mkdir(log_dir) != 0) {
        return FALSE;
    }
#elif defined(linux)
    if (mkdir(log_dir, 0744) != 0) {
        return FALSE;
    }
#endif
    return TRUE;
}

static int _get_curr_proc_handle()
{
#if defined(WIN32)
    g_logger_cfg.curr_proc = GetCurrentProcess();
    if (NULL == g_logger_cfg.curr_proc) {
        return FALSE;
    }
    if (SymInitialize(g_logger_cfg.curr_proc, NULL, TRUE) != TRUE) {
        return FALSE;
    }
#elif defined(linux)
    g_logger_cfg.curr_proc = NULL;
#endif
    return TRUE;
}

int init_logger(const char *log_dir, slog_level level, slog_out_location logLocation)
{
    char log_filepath[MAX_FILE_PATH] = { 0 };
    char datestr[MAX_DATE_STR] = { 0 };

    if (TRUE == g_logger_cfg.inited) {
        return TRUE;
    }

    if (access(log_dir, 0) != 0) {
        if (_slog_mkdir(log_dir) != TRUE) {
            return FALSE;
        }
    }
	g_logger_cfg.logLocation = logLocation;

    _slog_init_mutex(&g_logger_cfg.mtx);
    if (_get_curr_proc_handle() != TRUE) {
        return FALSE;
    }
    _get_curr_date(sizeof(datestr), datestr);
    snprintf(log_filepath, sizeof(log_filepath) - 1, "%s/%s.log", log_dir, datestr);
    g_logger_cfg.log_file = fopen(log_filepath, "a+");
    if (NULL == g_logger_cfg.log_file) {
        return FALSE;
    }
    g_logger_cfg.filter_levle = level;
    g_logger_cfg.inited = TRUE;

    return TRUE;
}

void write_log(slog_level level, int print_stacktrace, const char *func_name, int line, const char *fmt, ...)
{
	if (LOCATION_NULL == g_logger_cfg.logLocation) { return; }

    va_list args;
    char *level_str = NULL;
    char timestr[MAX_TIME_STR] = { 0 };
    char log_content[MAX_LOG_LINE] = { 0 };
    char log_line[MAX_LOG_LINE] = { 0 };

    if (g_logger_cfg.filter_levle > level) {
        return;
    }
	if (NULL == g_logger_cfg.log_file ) {
		printf("ERROR: NULL == g_logger_cfg.log_file\n");
		return;
	}
    va_start(args, fmt);
    vsnprintf(log_content, sizeof(log_content) - 1, fmt, args);
    va_end(args);
    _get_curr_time(sizeof(timestr), timestr);
    level_str = _get_level_str(level);
	//snprintf(log_line, sizeof(log_line) - 1, "%s %s %s:%d -| %s\n",
	snprintf(log_line, sizeof(log_line) - 1, "%s %s [%s(%d)]: %s\n",
        level_str, timestr, func_name, line, log_content);
    _slog_lock(&g_logger_cfg.mtx);

	if (LOCATION_FILE == g_logger_cfg.logLocation) {
		fwrite(log_line, sizeof(char), strlen(log_line), g_logger_cfg.log_file);
	}
	else  {
		printf("%s", log_line);
	}

	if (TRUE == print_stacktrace) {
		_write_stacktrace();
	}
	fflush(g_logger_cfg.log_file);
 
    _slog_unlock(&g_logger_cfg.mtx);
}

```





```
# ----------------------------------------------------------------------------
#  CMake file for liboblogger. See root CMakeLists.txt
#
# ----------------------------------------------------------------------------

project(${OBLOGGER_LIBRARY} C)

FILE(GLOB SLOG_SRC *.c *.h)

IF(WIN32)
	SET(SLOG_DPEND Dbghelp)
ELSEIF(UNIX)
	SET(SLOG_DPEND pthread)
ENDIF()


#添加头文件路径
include_directories(${PROJECT_BINARY_DIR} )

set(source
    slog.c
    )

file(GLOB_RECURSE CURRENT_HEADERS  *.h ${PROJECT_BINARY_DIR}/slog.h)
source_group("Include" FILES ${CURRENT_HEADERS}) 

add_library(${OBLOGGER_LIBRARY} SHARED  ${source} ${CURRENT_HEADERS})
#add_library(${OBLOGGER_LIBRARY} STATIC  ${source} ${CURRENT_HEADERS})


target_link_libraries(${OBLOGGER_LIBRARY}
	${SLOG_DPEND}
    -lm
    )

if(UNIX)
  if(CMAKE_COMPILER_IS_GNUCXX OR __ICC)
    set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
  endif()
endif()

```



### 

### 0x01，一个人极简日志模块的实现

基本需求

1. win平台日志记录功能，多线程安全，支持写日志级别的设置，日志格式包含日志等级，日志时间，文件名，行号信息
2. 输出的标准输出， 或落地到文件



#### 实现



```c++
//logger.h
/*
//类名：CLogger
//功能介绍：Win平台日志记录功能，多线程安全，支持写日志级别的设置，日志格式包含日志等级，日志时间，文件名，行号信息
//修订: 萧十一郎
//使用方法：
1：将logger.h，logger.cpp添加到项目中
2：设置logger.cpp的预编译头选项为“不使用预编译头”
3：使用代码示例：
#include "stdafx.h"
#include <iostream>
#include "logger.h"

using namespace std;
using namespace LOGGER;

int main()
{
cout << "Hello World\n" << endl;

#if 1
LOG_INFO("testee  LOG_INFO %d", 1);
LOG_WARN("testee  LOG_FATAL %s", "Tom");
LOG_ERROR("testee  high %f", 1.8);
LOG_FATAL("testee  LOG_FATAL %d",4);
#else
//不适用宏
CLogger *logger = CLogger::getInstance();
logger->fatal("TraceFatal %d", 1);
logger->error("TraceError %s", "sun");
logger->warning("TraceWarning");
logger->info("TraceInfo");
logger->setLogLevel(LOGGER::LogLevel_Error);
logger->fatal("TraceFatal %d", 2);
logger->error("TraceError %s", "sun2");
logger->warning("TraceWarning");
logger->info("TraceInfo");
#endif
return 0;
}
执行结果：test.log文件内容如下
Info	2018-11-23 15:50:28 [demo.cpp(18)] : testee  LOG_INFO 1
Warning	2018-11-23 15:50:28 [demo.cpp(19)] : testee  LOG_FATAL Tom
Error	2018-11-23 15:50:28 [demo.cpp(20)] : testee  high 1.800000
Fatal	2018-11-23 15:50:28 [demo.cpp(21)] : testee  LOG_FATAL 4
*/

#ifndef _LOGGER_H_
#define _LOGGER_H_
#include <Windows.h>
#include <stdio.h>
#include <string>


#ifdef WINDOWS
	#define TrimFilePath(x) strrchr(x,'\\')?strrchr(x,'\\')+1:x
#elif _WIN64 
	#define TrimFilePath(x) strrchr(x,'\\')?strrchr(x,'\\')+1:x
#else //*nix
	#define TrimFilePath(x) strrchr(x,'/')?strrchr(x,'/')+1:x
#endif


#define LOG_DEBUG(fmt, ...)   \
	CLogger::getInstance()->info("[%s(%d)] : " fmt"", TrimFilePath(__FILE__), __LINE__, ##__VA_ARGS__)

#define LOG_FATAL(fmt, ...)   \
	CLogger::getInstance()->fatal("[%s(%d)] : " fmt"", TrimFilePath(__FILE__), __LINE__, ##__VA_ARGS__)

#define LOG_ERROR(fmt, ...)   \
	CLogger::getInstance()->error("[%s(%d)] : " fmt"", TrimFilePath(__FILE__), __LINE__, ##__VA_ARGS__)

#define LOG_WARN(fmt, ...)   \
	CLogger::getInstance()->warning("[%s(%d)] : " fmt"", TrimFilePath(__FILE__), __LINE__, ##__VA_ARGS__)

#define LOG_INFO(fmt, ...)   \
	CLogger::getInstance()->info("[%s(%d)] : " fmt"", TrimFilePath(__FILE__), __LINE__, ##__VA_ARGS__)




namespace LOGGER
{
	//日志级别的提示信息
	static const std::string strFatalPrefix = "Fatal\t";
	static const std::string strErrorPrefix = "Error\t";
	static const std::string strWarningPrefix = "Warning\t";
	static const std::string strInfoPrefix = "Info\t";

	//日志级别枚举
	typedef enum EnumLogLevel
	{
		LogLevel_Stop = 0,	//什么都不记录
		LogLevel_Fatal,		//只记录严重错误
		LogLevel_Error,		//记录严重错误，普通错误
		LogLevel_Warning,	//记录严重错误，普通错误，警告
		LogLevel_Info		//记录严重错误，普通错误，警告，提示信息(也就是全部记录)
	}EnumLogLevel;

	class CLogger
	{
	public:
		
		static CLogger *getInstance() {
			//修改这里，定制日志记录器
			static CLogger * _instance = new  CLogger(LogLevel_Info, CLogger::GetAppPathA().append("log\\"), "test.log",1);
			return _instance;
		}
	private:

		//nLogLevel：日志记录的等级，可空
		//strLogPath：日志目录，可空
		//strLogName：日志名称，可空
		//m_isPrint: 是否打印日志到标准输出,可空 默认 不打印
		CLogger(EnumLogLevel nLogLevel = EnumLogLevel::LogLevel_Info, const std::string strLogPath = "", const std::string strLogName = "",bool isPrint = 0);
		//析构函数
		virtual ~CLogger();
		

	public:
		//写严重错误信息
		void fatal(const char *lpcszFormat, ...);
		//写错误信息
		void error(const char *lpcszFormat, ...);
		//写警告信息
		void warning(const char *lpcszFormat, ...);
		//写提示信息
		void info(const char *lpcszFormat, ...);
		//改变写日志级别
		void setLogLevel(EnumLogLevel nLevel);
		//获取程序运行路径
		static std::string GetAppPathA();
		//格式化字符串
		static std::string FormatString(const char *lpcszFormat, ...);
	private:
		//写文件操作
		void Trace(const std::string &strLog);
		//获取当前系统时间
		std::string GetTime();
		//文件全路径得到文件名
		const char *path_file(const char *path, char splitter);
	private:
		//写日志文件流
		FILE * m_pFileStream;
		//写日志级别
		EnumLogLevel m_nLogLevel;
		//日志目录
		std::string m_strLogPath;
		//日志的名称
		std::string m_strLogName;
		//日志文件全路径
		std::string m_strLogFilePath;
		//线程同步的临界区变量
		CRITICAL_SECTION m_cs;
		//是否打印日志到标准输出
		bool m_isPrint;
	};
}

#endif
```





```c++

//logger.cpp
#include "stdafx.h"
#include "logger.h"
#include <time.h>
#include <stdarg.h>
#include <direct.h>
#include <vector>
#include <Dbghelp.h>
#include <sstream>

#include <iostream>
#include <string>
#include <sstream>


#pragma comment(lib,"Dbghelp.lib")

using  std::cout;
using  std::endl;
using std::string;
using std::vector;

namespace LOGGER
{
	CLogger::CLogger(EnumLogLevel nLogLevel, const std::string strLogPath, const std::string strLogName, bool isPrint)
		:m_nLogLevel(nLogLevel),
		m_strLogPath(strLogPath),
		m_strLogName(strLogName),
		m_isPrint(isPrint)
	{
		//初始化
		
		m_pFileStream = NULL;
		if (m_strLogPath.empty())
		{
			m_strLogPath = GetAppPathA();
		}
		if (m_strLogPath[m_strLogPath.length() - 1] != '\\')
		{
			m_strLogPath.append("\\");
		}
		//创建文件夹
		MakeSureDirectoryPathExists(m_strLogPath.c_str());
		//创建日志文件
		if (m_strLogName.empty())
		{
			time_t curTime;
			time(&curTime);
			tm tm1;
			localtime_s(&tm1, &curTime);
			//日志的名称如：201601012130.log
			m_strLogName = FormatString("%04d%02d%02d_%02d%02d%02d.log", tm1.tm_year + 1900, tm1.tm_mon + 1, tm1.tm_mday, tm1.tm_hour, tm1.tm_min, tm1.tm_sec);
		}
		m_strLogFilePath = m_strLogPath.append(m_strLogName);

		//以追加的方式打开文件流
		fopen_s(&m_pFileStream, m_strLogFilePath.c_str(), "a+");

		InitializeCriticalSection(&m_cs);
	}


	//析构函数
	CLogger::~CLogger()
	{
		//释放临界区
		DeleteCriticalSection(&m_cs);
		//关闭文件流
		if (m_pFileStream)
		{
			fclose(m_pFileStream);
			m_pFileStream = NULL;
		}
	}

	//文件全路径得到文件名
	const char *CLogger::path_file(const char *path, char splitter)
	{
		return strrchr(path, splitter) ? strrchr(path, splitter) + 1 : path;
	}


	//写严重错误信息
	void CLogger::fatal(const char *lpcszFormat, ...)
	{
		//判断当前的写日志级别
		if (EnumLogLevel::LogLevel_Fatal > m_nLogLevel)
			return;
		string strResult;
		if (NULL != lpcszFormat)
		{
			va_list marker = NULL;
			va_start(marker, lpcszFormat); //初始化变量参数
			size_t nLength = _vscprintf(lpcszFormat, marker) + 1; //获取格式化字符串长度
			std::vector<char> vBuffer(nLength, '\0'); //创建用于存储格式化字符串的字符数组
			int nWritten = _vsnprintf_s(&vBuffer[0], vBuffer.size(), nLength, lpcszFormat, marker);
			if (nWritten > 0)
			{
				strResult = &vBuffer[0];
			}
			va_end(marker); //重置变量参数
		}
		if (strResult.empty())
		{
			return;
		}
		string strLog = strFatalPrefix;
		strLog.append(GetTime()).append(strResult);

		//写日志文件
		Trace(strLog);
	}

	//写错误信息
	void CLogger::error(const char *lpcszFormat, ...)
	{
		//判断当前的写日志级别
		if (EnumLogLevel::LogLevel_Error > m_nLogLevel)
			return;
		string strResult;
		if (NULL != lpcszFormat)
		{
			va_list marker = NULL;
			va_start(marker, lpcszFormat); //初始化变量参数
			size_t nLength = _vscprintf(lpcszFormat, marker) + 1; //获取格式化字符串长度
			std::vector<char> vBuffer(nLength, '\0'); //创建用于存储格式化字符串的字符数组
			int nWritten = _vsnprintf_s(&vBuffer[0], vBuffer.size(), nLength, lpcszFormat, marker);
			if (nWritten > 0)
			{
				strResult = &vBuffer[0];
			}
			va_end(marker); //重置变量参数
		}
		if (strResult.empty())
		{
			return;
		}
		string strLog = strErrorPrefix;
		strLog.append(GetTime()).append(strResult);

		//写日志文件
		Trace(strLog);
	}

	//写警告信息
	void CLogger::warning(const char *lpcszFormat, ...)
	{
		//判断当前的写日志级别
		if (EnumLogLevel::LogLevel_Warning > m_nLogLevel)
			return;
		string strResult;
		if (NULL != lpcszFormat)
		{
			va_list marker = NULL;
			va_start(marker, lpcszFormat); //初始化变量参数
			size_t nLength = _vscprintf(lpcszFormat, marker) + 1; //获取格式化字符串长度
			std::vector<char> vBuffer(nLength, '\0'); //创建用于存储格式化字符串的字符数组
			int nWritten = _vsnprintf_s(&vBuffer[0], vBuffer.size(), nLength, lpcszFormat, marker);
			if (nWritten > 0)
			{
				strResult = &vBuffer[0];
			}
			va_end(marker); //重置变量参数
		}
		if (strResult.empty())
		{
			return;
		}
		
		string strLog = strWarningPrefix;
		strLog.append(GetTime()).append(strResult);

		//写日志文件
		Trace(strLog);
	}


	//写一般信息
	void CLogger::info(const char *lpcszFormat, ...)
	{
		//判断当前的写日志级别
		if (EnumLogLevel::LogLevel_Info > m_nLogLevel)
			return;
		string strResult;
		if (NULL != lpcszFormat)
		{
			va_list marker = NULL;
			va_start(marker, lpcszFormat); //初始化变量参数
			size_t nLength = _vscprintf(lpcszFormat, marker) + 1; //获取格式化字符串长度
			std::vector<char> vBuffer(nLength, '\0'); //创建用于存储格式化字符串的字符数组
			int nWritten = _vsnprintf_s(&vBuffer[0], vBuffer.size(), nLength, lpcszFormat, marker);
			if (nWritten > 0)
			{
				strResult = &vBuffer[0];
			}
			va_end(marker); //重置变量参数
		}
		if (strResult.empty())
		{
			return;
		}
	
		string strLog = strInfoPrefix;
		strLog.append(GetTime()).append(strResult);

		//写日志文件
		Trace(strLog);
	}

	//获取系统当前时间
	string CLogger::GetTime()
	{
		time_t curTime;
		time(&curTime);
		tm tm1;
		localtime_s(&tm1, &curTime);
		//2016-01-01 21:30:00
		string strTime = FormatString("%04d-%02d-%02d %02d:%02d:%02d ", tm1.tm_year + 1900, tm1.tm_mon + 1, tm1.tm_mday, tm1.tm_hour, tm1.tm_min, tm1.tm_sec);

		return strTime;
	}

	//改变写日志级别
	void CLogger::setLogLevel(EnumLogLevel nLevel)
	{
		m_nLogLevel = nLevel;
	}

	//写文件操作
	void CLogger::Trace(const string &strLog)
	{
		if (m_isPrint) 
		{
			cout << strLog << endl;
		}
		
		try
		{
			//进入临界区
			EnterCriticalSection(&m_cs);
			//若文件流没有打开，则重新打开
			if (NULL == m_pFileStream)
			{
				fopen_s(&m_pFileStream, m_strLogFilePath.c_str(), "a+");
				if (!m_pFileStream)
				{
					return;
				}
			}
			//写日志信息到文件流
			fprintf(m_pFileStream, "%s\n", strLog.c_str());
			fflush(m_pFileStream);
			//离开临界区
			LeaveCriticalSection(&m_cs);
		}
		//若发生异常，则先离开临界区，防止死锁
		catch (...)
		{
			LeaveCriticalSection(&m_cs);
		}
	}

	string CLogger::GetAppPathA()
	{
		char szFilePath[MAX_PATH] = { 0 }, szDrive[MAX_PATH] = { 0 }, szDir[MAX_PATH] = { 0 }, szFileName[MAX_PATH] = { 0 }, szExt[MAX_PATH] = { 0 };
		GetModuleFileNameA(NULL, szFilePath, sizeof(szFilePath));
		_splitpath_s(szFilePath, szDrive, szDir, szFileName, szExt);

		string str(szDrive);
		str.append(szDir);
		return str;
	}

	string CLogger::FormatString(const char *lpcszFormat, ...)
	{
		string strResult;
		if (NULL != lpcszFormat)
		{
			va_list marker = NULL;
			va_start(marker, lpcszFormat); //初始化变量参数
			size_t nLength = _vscprintf(lpcszFormat, marker) + 1; //获取格式化字符串长度
			std::vector<char> vBuffer(nLength, '\0'); //创建用于存储格式化字符串的字符数组
			int nWritten = _vsnprintf_s(&vBuffer[0], vBuffer.size(), nLength, lpcszFormat, marker);
			if (nWritten > 0)
			{
				strResult = &vBuffer[0];
			}
			va_end(marker); //重置变量参数
		}
		return strResult;
	}
}
```



#### 参考链接

1. [几种C/C++ log库的比较](https://blog.csdn.net/yasi_xi/article/details/18356393)
2. [几种C/C++ log库的比较](https://www.cnblogs.com/lizhigang/p/7306777.html)
3. [简单的C/C++日志模块实现](https://www.cnblogs.com/lausaa/p/7594360.html)
4. [C++轻量级日志类CLogger的使用(更新)](https://blog.csdn.net/sunflover454/article/details/49758801)
5. https://blog.csdn.net/sunflover454/article/details/49758801



### 常用的系统宏



1. [编译器中和64位编程有关的预定义宏](https://blog.csdn.net/liangbch/article/details/36020391)





c++  调试生成奔溃日志



1. [Google Breakpad--VS2015 编译、使用、定位错误(如何使用gyp)](https://blog.csdn.net/wangshubo1989/article/details/53334033)



### 0x01 .png 文件格式初识

#### 概述

PNG是20世纪90年代中期开始开发的图像文件存储格式，其目的是企图替代GIF和TIFF文件格式，同时增加一些GIF文件格式所不具备的特性。流式网络图形格式(Portable Network Graphic Format，PNG)名称来源于非官方的“PNG's Not GIF”，是一种位图文件(bitmap file)存储格式，读成“ping”。PNG用来存储灰度图像时，灰度图像的深度可多到16位，存储彩色图像时，彩色图像的深度可多到48位，并且还可存储多到16位的α通道数据。PNG使用从LZ77派生的无损数据压缩算法。

  **PNG文件格式保留GIF文件格式的下列特性**：

1.  使用彩色查找表或者叫做调色板可支持256种颜色的彩色图像。 
2. 流式读/写性能(streamability)：图像文件格式允许连续读出和写入图像数据，这个特性很适合于在通信过程中生成和显示图像。                
3. 逐次逼近显示(progressive                display)：这种特性可使在通信链路上传输图像文件的同时就在终端上显示图像，把整个轮廓显示出来之后逐步显示图像的细节，也就是先用低分辨率显示图像，然后逐步提高它的分辨率。                
4. 透明性(transparency)：这个性能可使图像中某些部分不显示出来，用来创建一些有特色的图像。 
5. 辅助信息(ancillary                information)：这个特性可用来在图像文件中存储一些文本注释信息。 
6. 独立于计算机软硬件环境。 
7. 使用无损压缩。

**PNG文件格式中要增加下列GIF文件格式所没有的特性**：

1. 每个像素为48位的真彩色图像。 
2. 每个像素为16位的灰度图像。 
3. 可为灰度图和真彩色图添加α通道。 
4. 添加图像的γ信息。 
5. 使用循环冗余码(**c**yclic **r**edundancy **c**ode，CRC)检测损害的文件。                
6. 加快图像显示的逐次逼近显示方式。 
7. 标准的读/写工具包。 
8. 可在一个文件中存储多幅图像。





#### 文件结构

文件头 + png数据块 * n

| PNG文件标志             | PNG数据块 | ……   | PNG数据块 |
| ----------------------- | --------- | ---- | --------- |
| 89 50 4E 47 0D 0A 1A 0A |           |      |           |



##### PNG Chunk数据块的基本结构

表6-07 PNG文件数据块的结构

​             

| **名称**                       | **字节数** | **说明**                                                     |
| ------------------------------ | ---------- | ------------------------------------------------------------ |
| Length(长度)                   | 4字节      | 指定数据块中数据域的长度，其长度不超过                  (2^31－1)字节 |
| Chunk  Type Code(数据块类型码) | 4字节      | 数据块类型码由ASCII字母(A-Z和a-z)组成                        |
| Chunk   Data(数据块数据)       | 可变长度   | 存储按照Chunk Type Code指定的数据                            |
| CRC(循环冗余检测)              | 4字节      | 存储用来检测是否有错误的循环冗余码                           |



PNG定义了两种类型的数据块，

​	一种是称为关键数据块(critical chunk)，这是标准的数据块，关键数据块定义了4个标准数据块，每个PNG文件都必须包含它们，PNG读写软件也都必须要支持这些数据块.

​	另一种叫做辅助数据块(ancillary chunks)，这是可选的数据块。虽然PNG文件规范没有要求PNG编译码器对可选数据块进行编码和译码，但规范提倡支持可选数据块。



#### 关键数据块

#####  1. 文件头数据块IHDR(header  chunk)：

它包含有PNG文件中存储的图像数据的基本信息，并要作为第一个数据块出现在PNG数据流中，而且一个PNG数据流中只能有一个文件头数据块。

文件头数据块由13字节组成，

PNG文件头键数据块的结构

​             

| 域的名称                       | 字节数 | 说明                                                         |
| ------------------------------ | ------ | ------------------------------------------------------------ |
| Width                          | 4bytes | 图像宽度，以像素为单位                                       |
| Height                         | 4bytes | 图像高度，以像素为单位                                       |
| Bit                  depth     | 1 byte | 图像深度：                  索引彩色图像：1，2，4或8                  灰度图像：1，2，4，8或16                  真彩色图像：8或16 |
| ColorType                      | 1 byte | 颜色类型：                  0：灰度图像, 1，2，4，8或16                  2：真彩色图像，8或16                  3：索引彩色图像，1，2，4或84：带α通道数据的灰度图像，8或16                  6：带α通道数据的真彩色图像，8或16 |
| Compression method             | 1 byte | 压缩方法(LZ77派生算法)                                       |
| Filter                  method | 1 byte | 滤波器方法                                                   |
| Interlace method               | 1 byte | 隔行扫描方法：0：非隔行扫描                 1： Adam7(由Adam M. Costello开发的7                   遍隔行扫描方法) |



##### 2,调色板数据块PLTE(palette chunk)：

它包含有与索引彩色图像((indexed-color image))相关的彩色变换数据，它仅与索引彩色图像有关，而且要放在图像数据块(image data chunk)之前。真彩色的PNG数据流也可以有调色板数据块，目的是便于非真彩色显示程序用它来量化图像数据，从而显示该图像.

调色板实际是一个彩色索引查找表，它的表项数目可以是1～256中的一个数，每个表项有3字节，因此调色板数据块所包含的最大字节数为768。

调色板数据块结构

​             

| 域的名称 | 字节数 | 说明             |
| -------- | ------ | ---------------- |
| Red      | 1 byte | 0 = 黑，255 = 红 |
| Green    | 1 byte | 0 = 黑，255 = 绿 |
| Blue     | 1 byte | 0 = 黑，255 = 蓝 |



##### 3, 图像数据块IDAT(image data chunk)：

它存储实际的数据，在数据流中可包含多个连续顺序的图像数据块。

##### 4,  图像结束数据IEND(image trailer chunk)：

它用来标记PNG文件或者数据流已经结束，并且必须要放在文件的尾部。

除了表示数据块开始的IHDR必须放在最前面， 表示PNG文件结束的IEND数据块放在最后面之外，其他数据块的存放顺序没有限制。







| **PNG文件格式中的数据 块** |                        |              |            |                    |
| -------------------------- | ---------------------- | ------------ | ---------- | ------------------ |
| **数据块符号**             | **数据块名称**         | **多数据块** | **可选否** | **位置限制**       |
| IHDR                       | 文件头数据块           | 否           | 否         | 第一块             |
| cHRM                       | 基色和白色点数据块     | 否           | 是         | 在PLTE和IDAT之前   |
| gAMA                       | 图像γ数据块            | 否           | 是         | 在PLTE和IDAT之前   |
| sBIT                       | 样本有效位数据块       | 否           | 是         | 在PLTE和IDAT之前   |
| PLTE                       | 调色板数据块           | 否           | 是         | 在IDAT之前         |
| bKGD                       | 背景颜色数据块         | 否           | 是         | 在PLTE之后IDAT之前 |
| hIST                       | 图像直方图数据块       | 否           | 是         | 在PLTE之后IDAT之前 |
| tRNS                       | 图像透明数据块         | 否           | 是         | 在PLTE之后IDAT之前 |
| oFFs                       | (专用公共数据块)       | 否           | 是         | 在IDAT之前         |
| pHYs                       | 物理像素尺寸数据块     | 否           | 是         | 在IDAT之前         |
| sCAL                       | (专用公共数据块)       | 否           | 是         | 在IDAT之前         |
| IDAT                       | 图像数据块             | 是           | 否         | 与其他IDAT连续     |
| tIME                       | 图像最后修改时间数据块 | 否           | 是         | 无限制             |
| tEXt                       | 文本信息数据块         | 是           | 是         | 无限制             |
| zTXt                       | 压缩文本数据块         | 是           | 是         | 无限制             |
| fRAc                       | (专用公共数据块)       | 是           | 是         | 无限制             |
| gIFg                       | (专用公共数据块)       | 是           | 是         | 无限制             |
| gIFt                       | (专用公共数据块)       | 是           | 是         | 无限制             |
| gIFx                       | (专用公共数据块)       | 是           | 是         | 无限制             |
| IEND                       | 图像结束数据           | 否           | 否         | 最后一个数据块     |







### 参考链接

1. [PNG文件结构分析 ---Png解析](https://www.cnblogs.com/lidabo/p/3701197.html)
2. [Portable Network Graphics (PNG) Specification (Second Edition)](https://www.w3.org/TR/PNG/)
3. http://dev.gameres.com/Program/Visual/Other/PNGFormat.htm



### std：：function

https://www.cnblogs.com/jiayayao/p/6139201.html



# Git

### todo

https://git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-GitLab





git  历史版本代码



#### 下载历史版本代码

```

```



### git  储藏代码



#### 查看储藏的代码列表

```
git stash  list
stash@{0}: WIP on add_stream_depth_mono: 9f8983b save to local
```

#### 查看当前代码的状态

```
git status
```

储藏当前的代码

```
git stash
```

可以使用git stash list 查看

一般最新的代码编号会是0，像堆栈一样。  可以根据编号判断



恢复代码

```
git stash  pop  stash@{0}  #选择0的
```



放弃某个储藏

```sh
git stash drop stash@{0}  #选择0的
```



### 常用命令













**git常用命令：**

> - git init //初始化本地git环境
> - git clone XXX//克隆一份代码到本地仓库
> - git pull //把远程库的代码更新到工作台
> - git pull --rebase origin master //强制把远程库的代码跟新到当前分支上面
> - git fetch //把远程库的代码更新到本地库
> - git add . //把本地的修改加到stage中
> - git commit -m 'comments here' //把stage中的修改提交到本地库
> - git push //把本地库的修改提交到远程库中
> - git branch -r/-a //查看远程分支/全部分支
> - git checkout master/branch //切换到某个分支
> - git checkout -b test //新建test分支
> - git checkout -d test //删除test分支
> - git merge master //假设当前在test分支上面，把master分支上的修改同步到test分支上
> - git merge tool //调用merge工具
> - git stash //把未完成的修改缓存到栈容器中
> - git stash list //查看所有的缓存
> - git stash pop //恢复本地分支到缓存状态
> - git blame someFile //查看某个文件的每一行的修改记录（）谁在什么时候修改的）
> - git status //查看当前分支有哪些修改
> - git log //查看当前分支上面的日志信息
> - git diff //查看当前没有add的内容
> - git diff --cache //查看已经add但是没有commit的内容
> - git diff HEAD //上面两个内容的合并
> - git reset --hard HEAD //撤销本地修改
> - echo $HOME //查看git config的HOME路径
> - export $HOME=/c/gitconfig //配置git config的HOME路径





**团队协作git操作流程：**

- 克隆一个全新的项目，完成新功能并且提交：

> 1. git clone XXX //克隆代码库
> 2. git checkout -b test //新建分支
> 3. modify some files //完成修改
> 4. git add . //把修改加入stage中
> 5. git commit -m '' //提交修改到test分支
> 6. review代码
> 7. git checkout master //切换到master分支
> 8. git pull //更新代码
> 9. git checkout test //切换到test分支
> 10. git meger master //把master分支的代码merge到test分支
> 11. git push origin 分支名//把test分支的代码push到远程库

- 目前正在test分支上面开发某个功能，但是没有完成。突然一个紧急的bug需要处理

> 1. git add .
> 2. git stash
> 3. git checkout bugFixBranch
> 4. git pull --rebase origin master
> 5. fix the bug
> 6. git add .
> 7. git commit -m ''
> 8. git push
> 9. git checkout test
> 10. git stash pop
> 11. continue new feature's development

- git工作流

> ![img](https://images2015.cnblogs.com/blog/54367/201612/54367-20161209083626991-1934605466.png)

 



模拟需求



### 2，git  下载指定分支



1.下载

```

```

查看分支

```
git branch -a
```



下载指定分支

```

```

使用-t参数，它默认会在本地建立一个和远程分支名字一样的分支



### 1，创建分支，并提交修改到分支

（1）新建分支

> git branch  xxx (xxx填写你的分支名称)

（2）查看所有分支

> git branch -a

（3）切换到某一分支

> git checkout   xxx (xxx填写要切换的分支名称）

（4）添加修改代码到缓存（注意最后的"."前面有个空格

> git add .  
>
> 也可指定具体文件
>
> git add  xxx.c     (可以是新增的文件  或者修改的文件)

（5）添加提交代码的备注

> git commit -m "xxx" （xxx为本次提交代码的备注）

（6）提交代码到指定分支

> git push origin xxx （xxx为要提交代码的分支名称）





### 合并分支





# QT



qt项目打包

https://blog.csdn.net/windsnow1/article/details/78004265





# 环境搭建

## vs2015的环境相关

### 0x02 关于TODO 任务的使用

一个很棒的功能，大多数ide中都支持，vs也不例外。

 在开发中要有一个计划，在那里实现，怎么实现，可以先写下来，以后可以检查是否实现了

 TODO: 可以方便的帮助我们完成这样的任务

 编程可以这样标记

 //TODO: 未实现

 以后在任务列表中就可以看到

 任务列表在试图-->任务列表 打开

 

 VS2010中默认没有启用TODO功能(在任务列表中看不到),  设置方法:

 工具->选项->文本编辑器->C/C++->格式设置->杂项->枚举注释任务-> True

### 0x01 visual assist vs2015注释插件的使用



#### 下载链接：

链接：https://pan.baidu.com/s/17gF6TnMYbr0EJ9RFdAuf1g 
提取码：xnxn 

#### 安装说明：

[VS2015中安装VA](https://jingyan.baidu.com/article/75ab0bcbaa2403d6864db217.html)

#### 配置说明：

##### 1，如何配置函数的样式

“VAssistX”–>”Visual VAssistX Options”然后选择Suggestions,再点击”Edit VA Snippets”

在打开的窗口中选择Refactor Document Method，在这就可以更改你的显示样式了。



##### 2， 快捷键设置  VS shortcut setting:

tools --> options --> enviroment --> keyboard
set a shortcut for VAssistX.RefactorDocumentMethod

点击分配市值有效。    Shift+Alt+K





参数说明：

 You can modify the format of comment block by editing the [VA Snippet](http://demo.netfoucs.com/boyxiaolong/article/details/17552899#) for *Refactor Document Method*. There  are separate VA Snippets for C++, C# and VB.

 The VA Snippets entries include special characters expanded only when refactoring. These special characters are:

| Reserved String    | Meaning                                  |
| ------------------ | ---------------------------------------- |
| $SymbolName$       | Name of method                           |
| $SymbolContext$    | Context and name of method               |
| $SymbolType$       | Return type of method                    |
| $SymbolVirtual$    | Keyword virtual or blank                 |
| $SymbolPrivileges$ | Access of method                         |
| $SymbolStatic$     | Keyword static or blank                  |
| $MethodQualifier$  | Qualifier or blank                       |
| $MethodArg$        | One parameter of the method and its type |
| $MethodArgName$    | One parameter of the method              |
| $MethodArgType$    | Type of one parameter of the method      |

 The line of the VA Snippets entry containing $MethodArg$ or $MethodArgName$ is repeated for each parameter of the method.

 If you delete a VA Snippets entry and invoke *Document Method*, a default entry is created for you.



##### 参考链接

1. [Visual assistx设置函数注释格式](https://www.cnblogs.com/ferrisyu/p/8214295.html)
2. [vs2010番茄助手快速添加注释+快捷键]()
3. [visual assist常用快捷键](https://www.cnblogs.com/karlvin/p/3863893.html)

#### 推荐

**改进了Intellisense**

成员和完成列表框的出现更加频繁、迅速，并且结果更加准确。参数信息更加完善，并带有注释。含有所有符号的停驻工具提示。

**代码输入更迅速**

输入时观察suggestion列表框，其中将根据您的输入提供相应的备选字符。为了更加方便的选择字符，还可以提前定义Atuotext和代码模板。

**错误自动校正**

监控您的IDE，对那些简单但耗时的错误进行即时校正。

**信息获取更加快速**

更加迅速了解代码信息，在新的VA View中观察当前的停驻类浏览器，可以获得当前符号的更多信息。除此，资源窗口中还添加了小的内容和定义项，可以获取信息快照。

**增加了色彩和格式**

采用了更多的色彩和格式选项，代码解译更加迅速。增强了IDE的基本语法色彩，在您输入代码的同时，突出匹配和不匹配条目。另外，还添加了column indicator和print in color，将RTF置于剪切版内。

**简化了查找和浏览**

查找和浏览更加轻松。通过内容查找可以快速跳到相同名称的符号处，在您工作台的任何地方都可以找到符号定义，还可以转入您代码中的符号执行处。选择您文件的列表方式，锁定头文件和相应的cpp文件。从您的工作台文件列表中打开文件。含有最近行为列表，可以在代码的活动部分之间相互转换。Move  scope可以到达下一个方法，还包含往返浏览。

**拼写检查**

在您输入代码的同时进行检查，并且可以看到同Microsoft Word相似的红色下划线。含有Spell check comments and strings，另外，Spell check code可以检查错误的输入符号。

**拓展了基本编辑**

对编辑器进行了增强，编辑代码更加迅速。含有Surround selections，multiple clipboards. Sort lines。

适合您个人风格的配置特色：细化选项对话框，定义Visual Assist X特性以适应您的编程习惯。内容菜单中含多个命令，设置快捷方式可以加快访问您所偏好的命令。可以禁止或允许Visual Assist X，或者强制其重新剖析从而更加智能化。







### qt5.80.0 vs2015  x64  opencv 2.4.13.6





参考链接

1. https://www.cnblogs.com/AijunHe/p/6658741.html?utm_source=itdadao&utm_medium=referral
2. [**Qt-opencv-image-process**  ](https://www.cnblogs.com/gousheng/p/7849658.html)
3. [Ubuntu16.04.3 下安装Qt5.9.1 OpenCV3.2.0 (包括OpenCV_contrib)完美版](https://blog.csdn.net/chang_shuang/article/details/78239660)



4 [Windows下Qt creator调试器的安装与配置](https://blog.csdn.net/github_30605157/article/details/78702638)





### opencv  qt minggw

编译opencv  不顺

#### 程序版本下载

1. minggw： https://nchc.dl.sourceforge.net/project/mingw-w64/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe

2. qt：http://download.qt.io/archive/qt/5.10/5.10.1/

   qt中 已经自带了 minggw

点击下一步安装。



编译opencv with minggw







#### 参考链接

1. [【Qt_OpenCV基础篇 - 000】Qt5.10.1 + MingW5.3.0 + Win7_64 + CMake3.11.1环境下编译OpenCV 3.4.1](https://blog.csdn.net/qingyang8513/article/details/80339550)



### vmware



文件名：VMware-workstation-full-15.0.0-10134415.exe
下载地址：https://download3.vmware.com/software/wkst/file/VMware-workstation-full-15.0.0-10134415.exe?HashKey=407f7f08d1bd64a4724e4d9c43bcbaeb&ext=.exe&params={"custnumber"%3A"dGVqZEAlandAcA%3D%3D"%2C"sourcefilesize"%3A"511.75+MB"%2C"dlgcode"%3A"WKST-1500-WIN"%2C"languagecode"%3A"en"%2C"source"%3A"DOWNLOADS"%2C"downloadtype"%3A"manual"%2C"eula"%3A"Y"%2C"downloaduuid"%3A"71d53172-517a-4144-82a8-92765293af46"%2C"purchased"%3A"N"%2C"dlgtype"%3A"Product+Binaries"%2C"productversion"%3A"15.0.0"%2C"productfamily"%3A"VMware+Workstation+Pro"}&AuthKey=1537874903_7ff203b912694d8496e07014eb1a3ca9&ext=.exe

MD5SUM: e29580600a3beaf47df852fcc4f108c0
SHA1SUM: ede6d31a5bd5071f1fb0134992063e3ed9ae39a6
SHA256SUM: 409598a8ba29119b0aa4856f3486b4e3457e2a19098056f9ce500f02834bff9e

激活密钥：VV502-47Z16-M85AQ-Q7PX9-QLA8D



vs2013  

```
1>C:\Program Files (x86)\MSBuild\Microsoft\VisualStudio\v12.0\CodeAnalysis\Microsoft.CodeAnalysis.targets(214,5): error MSB4036: 未找到“SetEnvironmentVariable”任务。请检查下列各项:  1.) 项目文件中的任务名称与任务类的名称相同。2.) 任务类为“public”且实现 Microsoft.Build.Framework.ITask 接口。3.) 在项目文件中或位于“C:\Program Files (x86)\MSBuild\12.0\bin”目录的 *.tasks 文件中使用 <UsingTask> 正确声明了该任务。


```



### libomp 是啥

```
sudo  apt-get install  libomp-dev

```



参考链接

1. [OpenMP 入门教程](https://www.cnblogs.com/ospider/p/5265975.html)



### ubuntu opencv 2.4.13



```
安装编译工具 
sudo apt-get install build-essential 
安装依赖包 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev 
安装可选包 
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

```

#### 下载opencv

```
https://github.com/Itseez/opencv/archive/2.4.13.6.zip
```

#### 编译安装

```
打开文件夹"opencv-2.4.13"： 
cd opencv-2.4.13 
新建一个文件夹用于存放临时文件： 
mkdir release 切换到该临时文件夹： 
cd release 开始编译： 
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local/opencv2.4 .. 
make -j4 //开启线程 按照自己的配置 
sudo make install

```

#### 配置

```
将opencv的库加入到路径，从而让系统可以找到 
sudo gedit /etc/ld.so.conf.d/opencv.conf 
末尾加入/usr/local/opencv2.4，
保存退出 
sudo ldconfig 使配置生效 
sudo gedit /etc/bash.bashrc 末尾加入 PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig 
export PKG_CONFIG_PATH 
保存退出 
sudo source /etc/bash.bashrc #使配置生效

```



#### 测试实例



```c++
#include <stdio.h> 
#include <opencv2/opencv.hpp> 
using namespace cv; 

int main( ) { 
	Mat image; 
	image = imread("/home/elijah/lena.jpg", 1 );
	//目录按照自己的目录 
	if ( !image.data ) { 
		printf("No image data \n"); 
		return -1; 
	} 
	namedWindow("Display Image", WINDOW_AUTOSIZE ); 
	imshow("Display Image", image); 
	waitKey(0); 
	return 0; 
}

```



```bash
g++ test.cpp -o test.o `pkg-config --cflags --libs opencv`

```





env.sh

```
export LD_LIBRARY_PATH=/usr/local/opencv2.4/lib:$LD_LIBRARY_PATH 
```





#### 安装的问题

##### opencv 依赖库libjaster-dev  安装问题

近期需要在ubuntu18.04系统上安装opencv但是在安装依赖包的过程中，有一个依赖包，libjasper-dev在使用命令

​    sudo apt-get install libjaster-dev

提示：errorE: unable to locate libjasper-dev

后来google到解决办法，复制到这里

sudo add-apt-repository "deb <http://security.ubuntu.com/ubuntu> xenial-security main"
 sudo apt update
 sudo apt install libjasper1 libjasper-dev

成功的解决了问题，其中libjasper1是libjasper-dev的依赖包



##### **CMake Warning at cmake/OpenCVPackaging.cmake:23 (message): CPACK_PACKAGE_VER**



https://blog.csdn.net/mysea2004/article/details/72566730



#### 参考链接

1. [ubuntu 16.04 安装opencv 2.4.13](https://blog.csdn.net/u011557212/article/details/54706966?utm_source=itdadao&utm_medium=referral)
2. https://blog.csdn.net/wgshun616/article/details/81019536
3. [Ubuntu14.04安装OpenCV2.4.13(ZIP安装)](https://blog.csdn.net/c406495762/article/details/62896035)







### emacs 环境搭建



```
$sudo add-apt-repository ppa:ubuntu-elisp/ppa
$sudo apt update
$sudo apt install emacs-snapshot emacs-snapshot-el
 
$emacs --version    #查看emacs版本
```


