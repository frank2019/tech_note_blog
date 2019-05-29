



```
水滴石穿
```



#### 1，概述

scons是一个Python写的自动化构建工具，从构建这个角度说，它跟GNU make是同一类的工具。它是一种改进，并跨平台的gnu make替代工具，其集成功能类似于autoconf/automake 。scons是一个更简便，更可靠，更高效的编译软件。

- 移植性：使用 Python 脚本做为配置文件 python能运行的地方，就能运行scons


-  扩展性：理论上scons只是提供了python的类，scons使用者可以在这个类的基础上做所有python能做的事情。比如想把一个已经使用
  了Makefile大型工程切换到scons，就可以保留原来的Makefile，并用python解析Makefile中的编译选项、源/目标文件等，
  作为参数传递给scons，完成编译。
- 智能：Scons继承了autoconf/automake的功能，自动解析系统的include路径、typedef等；“以全局的观点来看所有的依赖关系”

- 对于 C,C++ 和 Fortran, 内建支持可靠自动依赖分析 . 不用像 make 工具那样需要 执行"make depends"和"make clean"就可以获得所有的依赖关系。
- 内建支持 C, C++, D, Java, Fortran, Yacc, Lex, Qt，SWIG 以及 Tex/Latex。 用户还可以根据自己的需要进行扩展以获得对需要编程语言的支持。
- 支持 make -j 风格的并行建造。相比 make -j, SCons 可以同时运行 N 个工作，而 不用担心代码的层次结构。
- 使用 Autoconf 风格查找头文件，函数库，函数和类型定义。
- 良好的夸平台性。SCons 可以运行在 Linux, AIX, BSD, HP/UX, IRIX, Solaris,   Windows, Mac OS X 和 OS/2 上。



#### 2，安装

##### on ubuntu

```bash
sudo apt install scons
```



```
conda install scons
```



#### 3，Hello World编译示例

##### 源码文件hello.c

```c++
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world" << endl;
    return 0;
}
```

##### SConstruct文件

编译构建文件，相当于makefile

语法使用python

```
Program('hello.cc')
```

##### 编译

```bash
$ scons
scons: Reading SConscript files ...
scons: done reading SConscript files.
scons: Building targets ...
g++ -o hello.o -c hello.cc
g++ -o hello hello.o
scons: done building targets.

```

生成可执行文件 hello



#### 4，scons命令

scons: 执行SConstruct中脚本
    scons -c   clean
    scons -Q  只显示编译信息，去除多余的打印信息
    scons -Q   --implicit-cache hello 保存依赖关系
                   --implicit-deps-changed   强制更新依赖关系
                   --implicit-deps-unchanged  强制使用原先的依赖关系，即使已经改变



#### 5，使用 scons 编译输出 

##### 5.1 scons 支持的多种编译类型

SCons 支持多种编译类型，你可以根据自己的需要，任意选用其中的一种。SCons 支持的编译类型有： 

- Program： 编译成可执行程序（在 Windows 平台上即是 exe 文件），这是最常用的一种编译类型。
- Object： 只编译成目标文件。使用这种类型，编译结束后，只会产生目标文件。在 POSIX 系统中，目标文件以 .o 结尾，在 Windows 平台上以 .OBJ 结尾。
- Library： 编译成库文件。SCons 默认编译的库是指静态链接库。
- StaticLibrary： 显示的编译成静态链接库，与上面的 Library 效果一样。
- SharedLibrary： 在 POSIX 系统上编译动态链接库，在 Windows 平台上编译 DLL。



##### 5.2 生成可执行文件

```python
	
    Program('hello.c')  		#编译hello.c可执行文件
    Program('hello','hello.c') 	#指定Output文件名(hello.exe on Windows; hello on POSIX)
    Program(['hello.c', 'file1.c', 'file2.c']) 	#编译多个文件，Output文件名以第一个文件命名
    Program(source = "hello.c",target = "hello") #编译 source 制定源码文件名，target 输出
    Program('hello', Split('hello.c file1.c file2.c'))  #编译多个文件

    Program(Glob("*.c"))			#编译多个文件
    src = ["hello.c","foo.c"];Program(src)  #编译  使用变量指定源码
```





```
Program('helloscons2', ['helloscons2.c', 'file1.c', 'file2.c'], 
       LIBS = 'm', 
       LIBPATH = ['/usr/lib', '/usr/local/lib'], 
       CCFLAGS = '-DHELLOSCONS')
```



 配置文件中 LIBS,LIBAPTH 和 CCFLAGS 是 SCons 内置的关键字，它们的作用如下： 

- LIBS： 显示的指明要在链接过程中使用的库，如果有多个库，应该把它们放在一个列表里面。这个例子里，我们使用一个称为 m 的库。
- LIBPATH： 链接库的搜索路径，多个搜索路径放在一个列表中。这个例子里，库的搜索路径是 /usr/lib 和 /usr/local/lib。
- CCFLAGS： 编译选项，可以指定需要的任意编译选项，如果有多个选项，应该放在一个列表中。这个例子里，编译选项是通过 -D 这个 gcc 的选项定义了一个宏 HELLOSCONS。

##### 5.3生成目标文件

5.2 中的其他选项也一样支持

```python
Object('hello.c') #编译hello.c目标文件
```



##### 5.4 Library：生成静态/动态库文件

​    

```python
	Library('foo', ['f1.c', 'f2.c', 'f3.c']) #编译library
    SharedLibrary('foo', ['f1.c', 'f2.c', 'f3.c']) #编译 shared library
    StaticLibrary('bar', ['f4.c', 'f5.c', 'f6.c']) #编译 static library
```

​    库的使用：

```python
 Program('prog.c', LIBS=['foo', 'bar'], LIBPATH='.') #连接库，不需加后缀或是前缀
```

 

#### 6，scons 常用控制

  

6.1 SourceSignatures：判断源文件是否修改
    

```python
	SourceSignatures('MD5')     #根据内容是否改变，默认方式
    SourceSignatures('timestamp') #根据修改时间
```

 

##### 6.2 TargetSignatures：判断目标文件是否改变

```python
	TargetSignatures('build')   #根据编译结果
    TargetSignatures('content')  #根据文件内容，如果只是加了句注释，将不会被重新编译
```

##### 6.3 Ignore：忽略依赖关系

```python
 Ignore(hello, 'hello.h')  #忽略某个依赖关系
```

##### 6.4 Depends：明确依赖关系

```python
Depends(hello, 'other_file') #明确依赖关系 
```

​    

##### 6.5 多目录配置

源文件的目录结构如下：
    src：
    |    SConstruct
    |    test.cpp
    |    mA(目录)：
         |     SConscript
         |     func.cpp

​    其中test.cpp为主文件，中调用func.cpp中定义的函数

SConstruct内容如下

```python
	subobj = SConscript(['mA/SConscript'])
 	obj = subobj + Object(Glob("*.cpp"))
 	Program("test",list(obj))

```

SConscript内容 ：

```python
	obj = Object(Glob("*.cpp"))
 	Return("obj")
```



上例中，在主目录中执行 scons就可以编译整个"工程"。SConstruct编译主目录中的test.cpp，并通过SConscript编译mA目录下的源文件，并最终生成可执行文件；SConscript用于编译mA中的func.cpp并把生成的func.o传递给主目录的SConstruct。



#### 7，参考链接

1. [scons官网](https://www.scons.org/)
2. [scons user guide](https://scons.org/doc/3.0.5/PDF/scons-user.pdf)
3. [scons api ](https://scons.org/doc/3.0.5/PDF/scons-api.pdf)