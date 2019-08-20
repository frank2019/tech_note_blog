# clang-format的简单使用

## 1，简介

clang-format，它是基于clang的一个命令行工具，能够自动化格式C/C++/Obj-C代码，支持多种代码风格：Google, Chromium, LLVM, Mozilla, WebKit，也支持自定义风格（通过编写.clang-format文件）。

## 2，安装

### Ubuntu

```bash
#Ubuntu
sudo apt-get install clang-format 
```

### MacOS

```
//安装命令
$ brew install clang-format
//查看版本
$ clang-format -version
//输出信息 clang-format version 8.0.0 (tags/google/stable/2018-10-04)

```

### windows

可跟随clang一起安装。[下载](http://releases.llvm.org/download.html)

### 编辑器集成

- vim 使用 `clang-format`
- Visual Studio Code

- 另外clang-format还提供一个[`clang-format-diff.py`](https://github.com/llvm-mirror/clang/blob/master/tools/clang-format/clang-format-diff.py)脚本，用来格式化patch，code review提交代码前，可以先跑一下这个脚本，看有没有问题。

  ```bash
  # 格式化最新的commit，并直接在原文件上修改
  git diff -U0 HEAD^ | clang-format-diff.py -i -p1
  ```

## 3，配置文件说明

生成配置文件模板

```bash
clang-format -style=llvm -dump-config > .clang-format
```

- 配置文件.clang-format详细说明

```ini
# 基于那个配置文件
BasedOnStyle: LLVM
# 访问说明符的偏移(public private)
AccessModifierOffset: -4
# 括号之后,水平对齐参数: Align DontAlign AlwaysBreak
AlignAfterOpenBracket: Align
# 连续的赋值时,对齐所有的等号
AlignConsecutiveAssignments: true
# 连续声明时，对齐所有声明的变量名
AlignConsecutiveDeclarations: true
# 左对齐换行(使用反斜杠换行)的反斜杠 
AlignEscapedNewlinesLeft: true
# 水平对齐二元和三元表达式的操作数 
AlignOperands: true
# 对齐连续的尾随的注释  
AlignTrailingComments: true
# 允许函数声明的所有参数在放在下一行  
AllowAllParametersOfDeclarationOnNextLine: true
# 允许短的块放在同一行  
AllowShortBlocksOnASingleLine : false
# 允许短的case标签放在同一行
AllowShortCaseLabelsOnASingleLine: false
# 允许短的函数放在同一行: None, InlineOnly(定义在类中), Empty(空函数), Inline(定义在类中，空函数), All 
AllowShortFunctionsOnASingleLine: Empty
# 是否允许短if单行 If true, if (a) return; 可以放到同一行
AllowShortIfStatementsOnASingleLine: false
# 允许短的循环保持在同一行   
AllowShortLoopsOnASingleLine: false 
# 总是在定义返回类型后换行(deprecated)   
AlwaysBreakAfterDefinitionReturnType: None
# 每行字符的限制，0表示没有限制  
ColumnLimit: 100
# 描述具有特殊意义的注释的正则表达式，它不应该被分割为多行或以其它方式改变
CommentPragmas: '^ IWYU pragma:'
# 语言: None Cpp Java Objc Protp
Language: Cpp 
#指针的*的挨着哪边
PointerAlignment: Right
#缩进宽度
IndentWidth: 4
# 连续的空行保留几行
MaxEmptyLinesToKeep: 1
# 在 @property 后面添加空格, \@property (readonly) 而不是 \@property(readonly).
ObjCSpaceAfterProperty: true
# OC block后面的缩进
ObjCBlockIndentWidth: 4
# 是否允许短方法单行
AllowShortFunctionsOnASingleLine: false
# 换行的时候对齐操作符
#AlignOperands: true
# 中括号两边空格 [] 
SpacesInSquareBrackets: true
# 小括号两边添加空格
SpacesInParentheses : false
#等号两边的空格
SpaceBeforeAssignmentOperators: true
# 容器类的空格 例如 OC的字典
SpacesInContainerLiterals: true
#缩进
IndentWrappedFunctionNames: true
#在block从空行开始
KeepEmptyLinesAtTheStartOfBlocks: true
#在构造函数初始化时按逗号断行，并以冒号对齐
BreakConstructorInitializersBeforeComma: true
#括号后添加空格
SpaceAfterCStyleCast: false
# 允许排序#include, 造成编译错误
# SortIncludes: true 
# 缩进case 标签
IndentCaseLabels: true 
#tab键盘的宽度
TabWidth: 4
UseTab: Never
```

## 4，clang-format使用示例

### 示例

```bash
# 以Google代码风格格式化main.cpp, 结果输出到stdout
clang-format main.cpp -style=Google
# 以Google代码风格格式化main.cpp, 结果直接写到main.cpp
clang-format -i main.cpp -style=Google
# 当然也支持对指定行格式化，格式化main.cpp的第1，2行
clang-format -lines=1:2 main.cpp
```

### 命令使用

```bash
clang-format.exe [options] [<file> ...]
```

- 如果没有指定，从标准输入获取代码，格式化后输出到标准输出

- 如果<file>指定，则格式化指定文件；如果带-i属性，则回写格式化后的代码到文件

  



### Clang-format options:

####   -assume-filename=<string> 

When reading from stdin, clang-format assumes this  filename to look for a style config file (with -style=file) and to determine the language.

#### -cursor=<uint>           

The position of the cursor when invoking
   clang-format from an editor integration

#### -dump-config             

Dump configuration options to stdout and exit.
Can be used with -style option.

#### -fallback-style=<string>  

The name of the predefined style used as a
fallback in case clang-format is invoked with
-style=file, but can not find the .clang-format
file to use.
Use -fallback-style=none to skip formatting.

#### -i                        

Inplace edit <file>s, if specified.

#### -length=<uint>            

Format a range of this length (in bytes).
Multiple ranges can be formatted by specifying
several -offset and -length pairs.
When only a single -offset is specified without
-length, clang-format will format up to the end
of the file.
Can only be used with one input file.

#### -lines=<string>           - <start line>:<end line> 

format a range of
lines (both 1-based).
Multiple ranges can be formatted by specifying
several -lines arguments.
Can't be used with -offset and -length.
Can only be used with one input file.

#### -offset=<uint>            

Format a range starting at this byte offset.
Multiple ranges can be formatted by specifying
several -offset and -length pairs.
Can only be used with one input file.

#### -output-replacements-xml  

Output replacements as XML.

#### -sort-includes           

 - If set, overrides the include sorting behavior determined by the SortIncludes style flag

#### -style=<string>           

Coding style, currently supports:
LLVM, Google, Chromium, Mozilla, WebKit.
Use -style=file to load style configuration from
.clang-format file located in one of the parent
directories of the source file (or current
directory for stdin).
Use -style="{key: value, ...}" to set specific
parameters, e.g.:
-style="{BasedOnStyle: llvm, IndentWidth: 8}"

#### -verbose                  

If set, shows the list of processed files

### Generic Options:

-  -help                     - Display available options (-help-hidden for more)
- -help-list                - Display list of available options (-help-list-hidden for more)
- -version                  - Display the version of this program



## 5，参考链接

1. [Clang 10 documentation](https://clang.llvm.org/docs/index.html)
2. [ClangFormat 命令使用](http://clang.llvm.org/docs/ClangFormat.html)
3. [Clang-Format Style Options](http://clang.llvm.org/docs/ClangFormatStyleOptions.html)

