

>



# 常见Visual Studio编译链接问题及解决



## 简介

本文描述主要常见Visual Studio 2015 编译报错 包括警告和错误，及其解决办法。

笔者使用的编译器是 Visual Studio 2015。



## 编译警告



### warning C4819的解决

```ini
警告	C4819	该文件包含不能在当前代码页(936)中表示的字符。请将该文件保存为 Unicode 格式以防止数据丢失
```



1. 打开出现warning的文件，
2. 选择文件/高级保存选项/编码：Unicode - 代码页 1200，
3. 点确定，保存文件，即可解决





```
警告	C4996	'strdup': The POSIX name for this item is deprecated. Instead, use the ISO C and C++ conformant name: _strdup. See online help for details.	
```



## 编译报错