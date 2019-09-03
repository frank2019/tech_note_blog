

# Cmake 入门及简单使用



![ CMake](https://www.hahack.com/images/cmake/cmake100.png)

## 

## 引言



夫妻之间吵架，吵得不可开交，这时可以通过第三方调解，这第三方可以是一个心理咨询机构，可以是熟悉的朋友，甚至可以是上帝！

关于间接层，软件工程领域有个著名的结论：

> All problems in computer science can be solved by another level of 
> indirection, except for the problem of too many layers of indirection.
>
> （在计算机科学中所有问题都可以通过引入另外一个间接层来解决，除了因为间接层太多带来的新问题。）
>
> **David Wheeler**（计算机科学家）





## 什么是 CMake

​       你或许听过好几种 Make 工具，例如 GNU Make ，QT 的 [qmake](http://qt-project.org/doc/qt-4.8/qmake-manual.html) ，微软的 [MS nmake](http://msdn.microsoft.com/en-us/library/ms930369.aspx)，BSD Make（[pmake](http://www.freebsd.org/doc/en/books/pmake/)），[Makepp](http://makepp.sourceforge.net/)，等等。这些Make 工具遵循着不同的规范和标准，所执行的 Makefile 
格式也千差万别。这样就带来了一个严峻的问题：如果软件想跨平台，必须要保证能够在不同平台编译。而如果使用上面的 Make 工具，就得为每一种标准写一次 Makefile ，这将是一件让人抓狂的工作。

CMake就是针对上面问题所设计的工具：它首先允许开发者编写一种平台无关的CMakeList.txt 文件来定制整个编译流程，然后再根据目标用户的平台进一步生成所需的本地化 Makefile 和工程文件，

如 Unix的 Makefile 或 Windows 的 Visual Studio 工程。从而做到

**“Write once, run everywhere”**。

显然，CMake 是一个比上述几种 make 更高级的编译配置工具。

使用 CMake 作为项目架构系统的知名开源项目有 [VTK](http://www.vtk.org/)、[ITK](http://www.itk.org/)、[KDE](http://kde.org/)、[OpenCV](http://www.opencv.org.cn/opencvdoc/2.3.2/html/modules/core/doc/intro.html)、[OSG](http://www.openscenegraph.org/) 等 。



在 linux 平台下使用 CMake 生成 Makefile 并编译的流程如下：

1.  编写 CMake 配置文件 CMakeLists.txt 。
2. 执行命令 `cmake PATH` 或者 `ccmake PATH` 生成 Makefile  。其中， `PATH` 是 CMakeLists.txt 所在的目录。
3. 使用 `make` 命令进行编译。



`ccmake` 和 `cmake` 的区别在于前者提供了一个交互式的界面。

本文将从实例入手，一步步讲解 CMake 的常见用法，文中所有的实例代码可以在[这里](https://github.com/wzpan/cmake-demo)找到



## 入门案例：单个源文件

对于简单的项目，只需要写几行代码就可以了。例如，假设现在我们的项目中只有一个源文件 main.c，该程序的用途是计算一个斐波那契数。

### 源文件

```c++
#include <stdio.h>
#include <stdlib.h>
/**
 * 返回 斐波那契数列 指定位置的元素
 * @param index 指定位置.
 * @return base raised to the power exponent.
 */
int FibonacciSequence(int index) {
    if (index < 3) {
        return  1;
    }
    return FibonacciSequence(index - 1) + FibonacciSequence(index - 2);
}


int main(int argc, char *argv[])
{
    if (argc < 2){
        printf("Usage: %s FibonacciSequence index \n", argv[0]);
        return -1;
    }
    int  index  = atof(argv[1]);
    int value = FibonacciSequence(index);

    printf("FibonacciSequence index %d is %d\n", index, value);
    return 0;
}
```

### 编写 CMakeLists.txt

首先编写 CMakeLists.txt 文件，并保存在与 main.c 源文件同个目录下：

```cmake
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo1)
# 显示指定使用的C++编译器 
#set(CMAKE_CXX_COMPILER "g++")
# 指定生成目标
add_executable(Demo main.c)
```

CMakeLists.txt 的语法比较简单，由命令、注释和空格组成，其中命令是不区分大小写的。符号 `#` 后面的内容被认为是注释。命令由命令名称、小括号和参数组成，参数之间使用空格进行间隔。

对于上面的 CMakeLists.txt 文件，依次出现了几个命令：

1. `cmake_minimum_required`：指定运行此配置文件所需的 CMake 的最低版本；
2. `project`：参数值是 `Demo1`，该命令表示项目的名称是 `Demo1` 。
3. `add_executable`： 将名为 main.c 的源文件编译成一个名称为 Demo 的可执行文件。



### 编译项目

如图，使用CMake (cmake-gui) 如下操作即可生成vs项目工程

![](img/1.jpg)



## 多个源文件

上面的例子只有单个源文件。现在假如把 `FibonacciSequence`函数单独写进一个名为 `Math.c` 的源文件里，使得这个工程变成如下的形式：

```
CMakeLists.txt  build  main.c  mymath.c  mymath.h
```

### CMakeLists.txt 

```cmake
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo1)
# 显示指定使用的C++编译器 
#set(CMAKE_CXX_COMPILER "g++")
# 指定生成目标
add_executable(Demo main.c mymath.c)
```

唯一的改动只是在 `add_executable` 命令中增加了一个 `mymath.c` 源文件。这样写当然没什么问题，但是如果源文件很多，把所有源文件的名字都加进去将是一件烦人的工作。更省事的方法是使用 `aux_source_directory` 命令，该命令会查找指定目录下的所有源文件，然后将结果存进指定变量名。其语法如下：

```cmake
aux_source_directory(<dir> <variable>)
```

可以修改 CMakeLists.txt 如下：

```cmake
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 指定生成目标
add_executable(Demo ${DIR_SRCS})
```

这样，CMake 会将当前目录所有源文件的文件名赋值给变量 `DIR_SRCS` ，再在add_executable 中引用这个变量 指示变量 `DIR_SRCS` 中的源文件需要编译成一个名称为 Demo 的可执行文件。

## 多个目录，多个源文件



现在进一步将 mymath.h 和 mymath.c 文件移动到 math 目录下作为一个模块。

```bash
│  CMakeLists.txt
│  main.c
│
├─build
└─math
        mymath.c
        mymath.h
```

对于这种情况，需要分别在项目根目录  和 math 目录里各编写一个 CMakeLists.txt 文件。为了方便，我们可以先将 math 目录里的文件编译成静态库再由 main 函数调用。



### 根目录中的 CMakeLists.txt 

```cmake
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 添加 math 子目录
add_subdirectory(math)
# 指定生成目标 
add_executable(Demo main.c)
# 添加链接库
target_link_libraries(Demo MathFunctions)
```

该文件添加了下面的内容: 第3行，使用命令 `add_subdirectory` 指明本项目包含一个子目录 math，这样 math 目录下的 CMakeLists.txt 文件和源代码也会被处理 。第6行，使用命令 `target_link_libraries` 指明可执行文件 main 需要连接一个名为 MathFunctions 的链接库 。

### 子目录的 CMakeLists.txt

```cmake
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
aux_source_directory(. DIR_LIB_SRCS)
# 生成链接库
add_library (MathFunctions ${DIR_LIB_SRCS})
```

在该文件中使用命令 `add_library` 将 src 目录中的源文件编译为静态链接库。



## 自定义编译选项

CMake 允许为项目增加编译选项，从而可以根据用户的环境和需求选择最合适的编译方案。

例如，可以将 MathFunctions 库设为一个可选的库，如果该选项为 `ON` ，就使用该库定义的数学函数来进行运算。否则就调用标准库中的数学函数库。





https://www.hahack.com/wiki/tools-makefile.html

https://www.hahack.com/codes/cmake/