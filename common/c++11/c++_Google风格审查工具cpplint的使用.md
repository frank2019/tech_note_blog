# 代码风格审查工具Cpplint



## **1，简介**

Cpplint是一个Python脚本，作为一款开源免费的代码静态检测工具，Google也使用它作为自己的C++代码检测工具，也就是说，只要你想代码遵从Google C++代码规范，那么Cpplint将会提供很好的代码静态检测支持。

cpplint

- Cpplint.py支持的文件格式包括.cc、.h、.cpp、.cu、.cuh。

- Cpplint只是一个代码风格检测工具，其并不对代码逻辑、语法错误等进行检查。

  

## 2，安装

Cpplint在Window下可以如下几种方式使用

### 2.1运行命令行检测

使用命令即可对代码文件进行检测。

```bash
Python cpplint.py   <file>
```

### 2.2 集成到VS中使用

在vs中使用的配置

这样使用比较方便，支持错误双击跳转。

集成到VS：打开VS2015—》工具—》外部工具—》添加工具

写入如下代码：

```ini
Title：Cpplint.py
Command：E:\CpplintToPython\Python27\python.exe
Arguments：”E:\Cpplint\cpplint.py\cpplint.py” –output=vs7 $(ItemPath)
Initial directory：$（ItemDir）
Check Use Output window
```

### 2.3 使用python安装版本

也可以使用python安装cpplint模块，

```bash
pip install cpplint 
```

或者

```bash
easy_install  cpplint
```

最新版本v1.4.4  支持python2 python3版本。



注意：直接只用python源码版本或者安装版本的话，需要判断其是否支持python3

## 3，命令行的详细使用



```bash
cpplint.py    	[--verbose=#] 
				[--output=vs7] 
				[--filter=-x,+y,...]
                [--counting=total|toplevel|detailed] 
                [--root=subdir]
                [--linelength=digits] 
                [--headers=x,y,...]
                [--quiet]
        <file> [file] ...
```

### verbose指定输出错误级别

[--verbose=#]: 指定输出的错误级别

对于发现的每个问题，cpplint都会给出一个位于区间[1, 5]之间的置信度评分，分数越高就代表问题越肯定，可以通过verbose选项控制输出哪些级别，如下，置信度评分为1、2的将不会再输出

```bash
cpplint.py --verbose=3 test.cpp 
```

### cpplint的输出格式

[--output=vs7]:cpplint的输出格式有emacs和vs7两种, 默认是emacs，vs7是Visual Studio输出的兼容格式

### 指定输出错误类型

[--filter=-x,+y,...]:指定输出错误类型，-表示不输出，+表示输出（错误类型可以查看脚本中的_ERROR_CATEGORIES 定义的对应的列表）

例子：

```bash
--filter=-build,-whitespace,+whitespace/comma
```

-whitespace，所有的[whitespace*]都将不输出，但是有了+whitespace/comma，则[whitespace/comma]类型的错误将被输出

### 控制每行的最长长度

[--linelength=digits]:控制每行的最长长度，google cpplint默认是80字符

### 扩展检查文件后缀

[--headers=x,y,...]:扩展检查的文件的后缀

### 输出错误的方式

 [--counting=total|toplevel|detailed]：输出错误总数的方式，默认为total参数

例子：

```bash
--counting=total
#输出
Total errors found: 96
```



```bash
--counting=toplevel
#输出
Category 'whitespace' errors found: 88
Category 'build' errors found: 8
Total errors found: 96
```

```bash
--counting=detailed
#输出：
Category 'whitespace/braces' errors found: 28
Category 'whitespace/semicolon' errors found: 1
Total errors found: 29 
```


cpplint支持每个目录放置CPPLINT.cfg 单独配置,CPPLINT.cfg通过包含多组键值对实现配置

```ini
	  set noparent
      filter=+filter1,-filter2,...
      exclude_files=regex
      linelength=80
      root=subdir
      headers=x,y,...
```



### 屏蔽代码不被检查

假设代码中有些部分不希望被检查，或者觉得是cpplint产生的误报。仅仅须要在对应代码行尾加入凝视”// NOLINT”就可以，cpplint就会跳过这些行。如：

```c++
return 0; // NOLINT
```



### 控制过滤置信度

对于发现的每一个问题，cpplint都会给出一个位于区间[1, 5]之间的置信度评分，分数越高就代表问题越肯定，能够通过verbose选项控制输出哪些级别。例如以下。置信度评分为1、2的将不会再输出：

```bash
cpplint  --verbose=3 test.cpp
```





假设须要让cpplint支持其他文件扩展，又不想改动源代码。则能够通过extensions选项如：

`cpplint --extensions=hpp test.cpp`



能够通过filter选项。依照自己的须要过滤掉特定的警告，”-FOO”表示不输出带有FOO的警告，”+FOO”表示输出带有FOO的警告，如：

`cpplint --filter=-whitespace/tab,+whitespace/ending_newline  test.cpp`

能够通过counting选项。来显示每种Category有多少个错误，如：

` cpplint.py --counting=detailed test.cpp`

## 4, Q&A

### 常见报错原因

1. Tab found; better to use spaces 没有使用四个空格代替缩进
2. Lines should be <= 80 characters long 存在大于80字符的行
3. Should have a space between // and comment 应该在//和注释之间有一个空格
4. An else should appear on the same line as the preceding }
5. If an else has a brace on one side, it should have it on both [readability/braces] 上两个错误经常一起出现，为大括号的位置不合规范
6. Extra space for operator ++; ++符号和变量间不能有空格
7. Redundant blank line at the end of a code block should be deleted. 代码块最后的空行应该被删除
8. Line contains invalid UTF-8 (or Unicode replacement character) 使用了中文注释报的错
9. Line ends in whitespace. 代码行最后存在空格
10. Include the directory when naming .h files  [build/include_subdir] [4] 

### 屏蔽指定报错的具体示例

如下报错：

```
1.h:113:  Could not find a newline character at the end of the file.  [whitespace/ending_newline] [5]
```

其中 whitespace/ending_newline 是此类出错的标识。

使用如下配置可以屏蔽 readability/utf8,whitespace/ending_newline。多于1个以逗号作为分割，-代表屏蔽，+代表取消屏蔽。

```bash
cpplint.exe  --filter=-readability/utf8,-whitespace/ending_newline    info.h
```





## 5，参考链接

1. [谷歌编码风格](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/contents/)
2. [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
3. https://github.com/cpplint/cpplint

4. [microsoft CodeAnalysis](http://microsoft.github.io/CodeAnalysis/)