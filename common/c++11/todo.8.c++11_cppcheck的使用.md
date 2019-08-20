# cppcheck 

## 1，简介

cppcheck 是一个静态代码检查工具，支持c, c++ 代码；作为编译器的一种补充检查，cppcheck对产品的源代码执行严格的逻辑检查。 



## 2，检查内容

Cppcheck是c/c++代码的静态分析工具。Cppcheck 不是一个风格检查工具也不是语法错误检查。它提供了独特的代码分析来检测bug，并着重于检测未定义的行为和危险的编码结构。

1. 自动变量检查
2. 数组的边界检查
3. class类检查
4. 过期的函数，废弃函数调用检查
5. 异常内存使用，释放检查
6. 内存泄漏检查，主要是通过内存引用指针
7. 操作系统资源释放检查，中断，文件描述符等
8. 异常STL 函数使用检查
9. 代码格式错误，以及性能因素检查



## 3，安装

### windows下的安装

在linux中类似。

1. 从http://cppcheck.net/下载并安装msi文件，

2. 默认安装到C:\Program Files\Cppcheck，

3. 将C:\Program Files\Cppcheck添加path环境变量，便于以后的使用。  


### vs中配置

在vs1020中做如下设置，即可在vs的输出窗口中看到cppcheck的检查结果，当然可以随时修改cppcheck的级别

属性-> 生成事件->预先生成事件->命令行

```bash
cppcheck --enable=all --project=$(ProjectFileName)
```

在生成中使用  选择 是。

### Debian:

```
sudo apt-get install cppcheck
```

### Fedora:

```
sudo yum install cppcheck
```

### Mac:

```
brew install cppcheck
```



### Clients and plugins

Cppcheck is integrated with many popular development tools. For instance:

- **CLion** - [Cppcheck plugin](https://plugins.jetbrains.com/plugin/8143)
- **Codacy** - [integrated](https://www.codacy.com/) - Check for code style and security issues on every commit and pull request
- **Code::Blocks** - *integrated*
- **CodeDX** (software assurance tool) - [integrated](http://codedx.com/code-dx-standard/)
- **CodeLite** - *integrated*
- **CppDepend 5** - [integrated](http://www.cppdepend.com/CppDependV5.aspx)
- **Eclipse** - [Cppcheclipse](https://github.com/kwin/cppcheclipse/wiki/Installation)
- **KDevelop** - [integrated since v5.1](https://kdevelop.org/)
- **gedit** - [gedit plugin](http://github.com/odamite/gedit-cppcheck)
- **Hudson** - [Cppcheck Plugin](http://wiki.hudson-ci.org/display/HUDSON/Cppcheck+Plugin)
- **Jenkins** - [Cppcheck Plugin](http://wiki.jenkins-ci.org/display/JENKINS/Cppcheck+Plugin)
- **Mercurial (Linux)** - [pre-commit hook](http://sourceforge.net/p/cppcheck/wiki/mercurialhook/) - Check for new errors on commit (requires interactive terminal)
- **Tortoise SVN** - [Adding a pre-commit hook script](http://omerez.com/automatic-static-code-analysis/)
- **Git (Linux)** - [pre-commit hook](https://github.com/danmar/cppcheck/blob/master/tools/git-pre-commit-cppcheck) - Check for errors in files going into commit (requires interactive terminal)
- **Visual Studio** - [Visual Studio plugin](https://github.com/VioletGiraffe/cppcheck-vs-addin/releases/latest)
- **QtCreator** - [Qt Project Tool (qpt)](https://sourceforge.net/projects/qtprojecttool/files)

## 4，命令行的使用



# 参考链接

1. [Cppcheck -A tool for static C/C++ code analysis](http://cppcheck.net/)
2. https://www.cnblogs.com/lidabo/p/3489645.html