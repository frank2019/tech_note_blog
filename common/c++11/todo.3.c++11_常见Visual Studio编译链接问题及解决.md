

>



# 常见Visual Studio编译链接问题及解决



## 简介

本文描述主要常见Visual Studio 2015 编译报错 包括警告和错误，及其解决办法。

笔者使用的编译器是 Visual Studio 2015。



## 编译警告



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