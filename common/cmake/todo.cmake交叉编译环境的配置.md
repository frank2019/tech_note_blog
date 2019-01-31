**CMake对交叉编译的支持**



交叉编译(即在host平台编译出target目标机的程序)时，牵扯到相关头文件的切换和编译器的选择以及环境变量的改变等。

CMake给交叉编译预留了一个变量即CMAKE_TOOLCHAIN_FILE,它定义了一个文件的路径，这个文件即toolChain,里面set了一系列你需要改变的变量和属性。

比如

- C_COMPILER,CXX_COMPILER,

- 如果用Qt的话需要更改QT_QMAKE_EXECUTABLE以及

- 如果用BOOST的话需要更改的BOOST_ROOT(具体查看相关Findxxx.cmake里面指定的路径)。

CMake为了不让用户每次交叉编译都要重新输入这些命令，因此它带来toolChain机制，简而言之就是一个cmake脚本，内嵌了你需要改变以及需要set的所有交叉环境的设置。

#### CMAKE_TOOLCHAIN_FILE中常用变量

#### 1，CMAKE_SYSTEM_NAME:  

目标机target所在的操作系统名称，比如ARM或者Linux你就需要写"Linux",如果Windows平台你就写"Windows",如果你的嵌入式平台没有相关OS你即需要写成"Generic",只有当CMAKE_SYSTEM_NAME这个变量被设置了，CMake才认为此时正在交叉编译，它会额外设置一个变量CMAKE_CROSSCOMPILING为TRUE.

####  2，CMAKE_C_COMPILER:  

顾名思义，即C语言编译器，这里可以将变量设置成完整路径或者文件名，设置成完整路径有一个好处就是CMake会去这个路径下去寻找编译相关的其他工具比如linker,binutils等，如果你写的文件名带有arm-elf等等前缀，CMake会识别到并且去寻找相关的交叉编译器。

####  3，CMAKE_CXX_COMPILER: 

同上，此时代表的是C++编译器。

#### 4，CMAKE_FIND_ROOT_PATH:  

代表了一系列的相关文件夹路径的根路径的变更，比如你设置了/opt/arm/,所有的Find_xxx.cmake都会优先根据这个路径下的/usr/lib,/lib等进行查找，然后才会去你自己的/usr/lib和/lib进行查找，如果你有一些库是不被包含在/opt/arm里面的，你也可以显示指定多个值给CMAKE_FIND_ROOT_PATH,比如

```
set(CMAKE_FIND_ROOT_PATH /opt/arm /opt/inst)
```

#### 5，CMAKE_FIND_ROOT_PATH_MODE_PROGRAM:  

对FIND_PROGRAM()起作用，有三种取值，NEVER,ONLY,BOTH,

第一个表示不在你CMAKE_FIND_ROOT_PATH下进行查找，

第二个表示只在这个路径下查找，

第三个表示先查找这个路径，再查找全局路径，对于这个变量来说，一般都是调用宿主机的程序，所以一般都设置成NEVER

####   6， CMAKE_FIND_ROOT_PATH_MODE_LIBRARY:

 对FIND_LIBRARY()起作用，表示在链接的时候的库的相关选项，因此这里需要设置成ONLY来保证我们的库是在交叉环境中找的.

#### ​    7，CMAKE_FIND_ROOT_PATH_MODE_INCLUDE:

  对FIND_PATH()和FIND_FILE()起作用，一般来说也是ONLY,如果你想改变，一般也是在相关的FIND命令中增加option来改变局部设置，有NO_CMAKE_FIND_ROOT_PATH,ONLY_CMAKE_FIND_ROOT_PATH,BOTH_CMAKE_FIND_ROOT_PATH

#### ​    8，BOOST_ROOT：

 对于需要boost库的用户来说，相关的boost库路径配置也需要设置，因此这里的路径即ARM下的boost路径，里面有include和lib。

#### ​    9，QT_QMAKE_EXECUTABLE: 

对于Qt用户来说，需要更改相关的qmake命令切换成嵌入式版本，因此这里需要指定成相应的qmake路径（指定到qmake本身）



示例

```cmake
# this is required
SET(CMAKE_SYSTEM_NAME Linux)

# specify the cross compiler
SET(CMAKE_C_COMPILER   /opt/arm/usr/bin/ppc_74xx-gcc)
SET(CMAKE_CXX_COMPILER /opt/arm/usr/bin/ppc_74xx-g++)

# where is the target environment 
SET(CMAKE_FIND_ROOT_PATH  /opt/arm/ppc_74xx /home/rickk/arm_inst)

# search for programs in the build host directories (not necessary)
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# configure Boost and Qt
SET(QT_QMAKE_EXECUTABLE /opt/qt-embedded/qmake)
SET(BOOST_ROOT /opt/boost_arm)
```







### 参考链接

1. [CMake交叉编译配置](https://www.cnblogs.com/rickyk/p/3875334.html)
2. https://cmake.org/Wiki/CMake_Cross_Compiling