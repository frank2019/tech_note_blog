

# C/C++ layer



![](http://spacemacs.org/layers/+lang/c-c++/img/ccpp.jpg)![](http://spacemacs.org/layers/+lang/c-c++/img/cmake.png)







## 1 Description

本layer增加配置C/C++语言，同时完美支持Cmake脚本。

## 2 Features

- 通过flycheck Clang 实现语法检查支持；
- 通过disaster 实现代码汇编支持；
- 通过clang-format 实现代码格式化；
- 在底部显示函数和变量定义(需要包含semantic layer)；
- 在顶部显示函数游标。 See [stickyfunc-demos](https://github.com/tuhdo/semantic-stickyfunc-enhance) for demos in some programming languages.(需要包含semantic layer)；
- 通过[semantic-refactor](https://github.com/tuhdo/semantic-refactor) 支持重构(需要包含semantic layer)；
- 通过cscope支持代码导航和gtags(需要包含cscope ayer)；
- 通过company-clang（when `c-c++-enable-clang-support` is turned on）或者company-ycmd(when `ycmd` layer is included) 支持代码自动补全（when `auto-completion` layer is included）；

## 3 Install

 

### 3.1 Layer

使用configuration layer，在~/.spacemacs 中增加配置。需要在`dotspacemacs-configuration-layers`的列表中增加`c-c++`。

 **Note:** [semantic-refactor](https://github.com/tuhdo/semantic-refactor) is only available for Emacs 24.4+ 

### 3.2 Default mode for header files

默认头文件使用c-mode，可以指定 c++-mode 模式，方法是：

 



```lisp
(setq-default dotspacemacs-configuration-layers
  '((c-c++ :variables
           c-c++-default-mode-for-headers 'c++-mode)))
```



**Note:** To set the variable for a given project, create a directory local
variable at the root of your project. More info on directory local variables
can be found in the [dir-locals](http://www.gnu.org/software/emacs/manual/html_node/elisp/Directory-Local-Variables.html).



### 3.3 Enable Clang support

通过设置变量 `c-c++-enable-clang-support`的值为 `t` 打开Clang支持:

```
(setq-default dotspacemacs-configuration-layers
  '((c-c++ :variables c-c++-enable-clang-support t)))
```



#### 3.3.1 clang-format

```

```

 [clang-format](http://clang.llvm.org/docs/ClangFormat.html) 可以用来对指定区域代码 (`clang-format-region`) 进行格式化，也可以对整个buffer (`clang-format-buffer`) 。 格式的定义存在在 `.clang-format` 。这个文件可以放在代码的同一级目录中，也可以放在父目录中(否则会使用默认的)。



 You can add snippets similar to the following to bind clang-format to either a particular mode or all modes in your `dotspacemacs/user-config` (within your `~/.spacemacs`): 



```lisp

```



#### 3.3.2 Company-clang and flycheck

 This layer adds some fancy improvements to `company-clang`. It includes a hook to load a projects `.clang_complete` file, which is just a text file with one clang flag per line, a format also used by other text editor clang plugins. 

 Not only does this allow proper autocomplete on projects with extra includes and flags, but there is also support for flycheck so that it doesn't complain about missing header files. 



Company-clang   是一个代码补全的插件；



## 4 Key Bindings



| Key Binding | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `SPC m g a` | open matching file (e.g. switch between .cpp and .h)         |
| `SPC m g A` | open matching file in another window (e.g. switch between .cpp and .h) |
| `SPC m D`   | disaster: disassemble c/c++ code                             |
| `SPC m r`   | srefactor: refactor thing at point.                          |





[原文链接](http://spacemacs.org/layers/+lang/c-c++/README.html)