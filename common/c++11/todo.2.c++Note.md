

### todo



#### imgui

1.  [imgui](https://github.com/ocornut/imgui)
2. [Simple2D-16（音乐播放器）ImGui 库介绍](https://www.cnblogs.com/ForEmail5/p/7224114.html)



#### libusb

https://blog.csdn.net/qccz123456/article/details/79984027



blocky

1. [来算google的可视化编程工具——Blockly，不仅仅是玩具](https://blog.csdn.net/benwdm/article/details/84910517)

2. https://github.com/google/blockly
3. [Avatar SDK ](https://avatarsdk.com/)





https://blog.csdn.net/xiaoyu21520/article/details/77159742?utm_source=blogxgwz8



#### c++  基础

1. [C++ 中using 的使用](https://blog.csdn.net/shift_wwx/article/details/78742459)
2. [C++11新特性之十：enable_shared_from_this](https://blog.csdn.net/caoshangpa/article/details/79392878)







## C++



### std::move

[C++ std::move/std::forward/完美转发](https://www.cnblogs.com/jianhui-Ethan/p/4670399.html)





[计算机视觉领域一些牛人博客](http://blog.sina.com.cn/s/blog_9d3b84e30102wfz8.html)

[计算机视觉 国际著名研究机构](https://blog.csdn.net/shenziheng1/article/details/52443195)





## windows环境编程



[线程中CreateEvent和SetEvent及WaitForSingleObject的用法](https://www.cnblogs.com/MrYuan/p/5238749.html)



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

```





```

```



### 

### 0x01，一个人极简日志模块的实现









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


