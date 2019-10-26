

>



# 常见Visual Studio编译链接问题及解决



## 简介

本文描述主要常见Visual Studio 2015 编译报错 包括警告和错误，及其解决办法。

笔者使用的编译器是 Visual Studio 2015。



## 编译警告

 error C2220: 警告被视为错误 - 没有生成“object”文件

```
 error C2220: 警告被视为错误 - 没有生成“object”文件
```

解决办法

如果上述不能去掉错误，还可以点击项目，右击选择属性->配置属性->c/c++->常规，将“警告视为错误”的选项改为“否”。就可以！



### warning C4819的解决 Unicode 格式

```ini
警告	C4819	该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
```



1. 打开出现warning的文件，
2. 选择文件/高级保存选项/编码：Unicode - 代码页 1200，
3. 点确定，保存文件，即可解决





```
警告	C4996	'strdup': The POSIX name for this item is deprecated. Instead, use the ISO C and C++ conformant name: _strdup. See online help for details.	
```



```
警告	C4996	'strerror': This function or variable may be unsafe. Consider using strerror_s instead. To disable deprecation, use _CRT_SECURE_NO_WARNINGS. See online help for details.
```



原因解释
这种微软的警告，主要因为那些C库的函数，很多函数内部是不进行参数检测的（包括越界类的），微软担心使用这些会造成内存异常，所以就改写了同样功能的函数，改写了的函数进行了参数的检测，使用这些新的函数会更安全和便捷。关于这些改写的函数你不用专门去记忆，因为编译器对于每个函数在给出警告时，都会告诉你相应的安全函数，查看警告信息就可以获知



  解决方案：
1> 根据下面的warning提示：参见“fopen”的声明
        消息:“This
function or variable may be unsafe. Consider using fopen_s instead. To 
disable deprecation, use _CRT_SECURE_NO_DEPRECATE. See online help
for details.”
        所以可以将函数按warning提示的第二句，改为使用fopen_s函数即可：
        例如:FILE *pFile=fopen("1.txt", "w");
           改为：
           FILE* pFile;
           fopen_s(&pFile, "1.txt", "w"); 
2> 还是根据warning提示的地三句话:use _CRT_SECURE_NO_DEPRECATE
        项目|属性|配置属性|C/C++|命令行|附加选项,加入【/D "_CRT_SECURE_NO_DEPRECATE" 】(注：加入中括号中完整的内容)
3> 降低警告级别：项目|属性|配置属性|C/C++|常规,自己根据情况降低警告级别（此法不推荐）
    注意：高度重视警告：使用编译器的最高警告级别。应该要求构建是干净利落的（没有警告）。理解所有警告。通过 修改代码而不是降低警告级别来排除警告。
    编译器是你的朋友。如果它对某个构造发出警告，这经常是说明你的代码中存在潜在的问题。成功的构建应该是无声无息的（没有警告的）。【《C++编程规 范》】





## 编译报错

### 链接器工具错误 LNK2026 XXX模块对于 SAFESEH 映像是不安全的"



 解决方法：

 1.打开该项目的“属性页”对话框。

 2.单击“链接器”文件夹。

 3.单击“命令行”属性页。

 4.将 /SAFESEH:NO 键入“附加选项”框中，然后点击应用。







### error C2220: 警告被视为错误 - 没有生成“object”文件

产生这种错误的原因是：原因是该文件使用的编码格式与当前系统对应的代码页格式不一样，例如原文件的代码页为unicode或utf-8，而我们系统中的代码页为中文gb2312-936。

解决方案：（查看当前系统使用的代码页，使用cmd命令：chcp）

1. 启动Microsoft Visual Studio，文件->打开->选择该cpp，然后在文件->高级保存选项->编码，选择当前系统的代码页的编码格式(如中文gb2312-936)。然后保存。重新编译，此错误不再出现。

2. 如果上述不能去掉错误，还可以点击项目，右击选择属性->配置属性->c/c++->常规，将“警告视为错误”的选项改为“否”。


error： 

解决办法

```
把文件替换到这里C:\Program Files (x86)\MSBuild\Microsoft\VisualStudio\vxx.0\CodeAnalysis
                                                                      /\/\ xx=v10,v11,v12,v13,v14,v15
文件下载
                                                                      
```

```
链接：https://pan.baidu.com/s/1rSt254lLMuxipHhbOevKiQ 
提取码：27wu 
```





错误MSB3073	命令“setlocal
"D:\Program Files\CMake\bin\cmake.exe" -DBUILD_TYPE=Release -P cmake_install.cmake
if %errorlevel% neq 0 goto :cmEnd
:cmEnd
endlocal & call :cmErrorLevel %errorlevel% & goto :cmDone
:cmErrorLevel
exit /b %1
:cmDone
if %errorlevel% neq 0 goto :VCEnd
:VCEnd”已退出，代码为 1。	INSTALL	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	133	



原因

一般是安装的目录不存在 或者不拥有权限，可以通过设置CMAKE_INSTALL_PREFIX  变量来指定安装位置



### error LNK2026: 模块对于 SAFESEH 映像是不安全的

#### 解决方法1

1.打开该项目的“属性页”对话框。

2.单击“链接器”文件夹。

3.单击“命令行”属性页。

4.将 /SAFESEH:NO 键入“其他选项”框中，然后点击应用。

#### 解决方法2

在cmake中增加设置

```cmake
#模块对于SAFESEH映像是不安全
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO")
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO")
set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} /SAFESEH:NO")
```

