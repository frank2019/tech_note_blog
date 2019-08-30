

常见的命令行库有

- [boost 的program_options](http://www.boost.org/doc/libs/1_56_0/doc/html/program_options.html)
- [argtable](http://argtable.sourceforge.net/)
- [google flags](http://code.google.com/p/google-gflags/)



• Getopt:       Parsing program options using getopt.
• Argp:     Parsing program options using argp_parse.

https://www.gnu.org/software/libc/manual/html_node/Parsing-Program-Arguments.html







## Argtable3

Argtable是一款开源的ANSI C library，用来解析GNU样式的命令行选项。它通过定义可用于指定命令行语法的声明式API，从而简化了命令行的分析。argtable将自动生成一致的错误处理逻辑和命令行语法的文本描述

### 特点

以下列出了一些为什么你应该在你的C/C++ 工具箱中包含Argtable的原因：

- GNU-style command-line syntax: 使用标准和跨平台的方式来表达命令.
- Declarative API: 通过指定具体的、非详细说明如何做的方式来排除复杂的解析逻辑.
- Built-in error handling: 生成一致的错误处理逻辑.
- Built-in help messages: 生成一致的命令行语法描述.
- Written in ANSI C: 易于被其他语言创建绑定.
- Readable source code: 源码注释良好，具有100%的分支测试覆盖率.
- Single-file library: 没有繁琐的构建脚本。只需要将单个源文件放到你的项目中即可.
- Self-contained: 没有外部依赖.
- Cross-platform: 在大多数类Unix系统、Windows和嵌入式系统上都可以使用.
- BSD-licensed:可以将此库用于任何目的，包括商业程序.



## 快速开始

argtable3是一个单文件的ansi-c库。您需要做的只是将argtable3.c添加到项目中，并在源代码中包含argtable3.h。



### 参考链接

1. [Argtable3 学习(2)--教程](https://blog.csdn.net/ATOOHOO/article/details/88632903)
2. [argtable3](https://github.com/argtable/argtable3)