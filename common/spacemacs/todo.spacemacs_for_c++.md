



### emacs spacemacs基本安装

1. 安装emacs25以上版本，
2. spacemacs 安装参照官网说明



#### 字体的支持

首先是下载Source Code Pro字体,github上的比较慢,下面网址的很快

http://www.fontsquirrel.com/

然后/usr/share/fonts/ 下新建一个目录

sudo mkdir /usr/share/fonts/opentype

接着解压下载的字体到该目录下,然后执行

sudo fc-cache -f -v       使字体生效



参考链接：

#### https://www.jianshu.com/p/1d5e1aaeb3f6

#### 网络配置使用国内镜像



```lisp
;修改  
vim .emacs.d/core/templates/.spacemacs.template  
  
  
(defun dotspacemacs/user-init ()  
  "Initialization function for user code.  
It is called immediately after `dotspacemacs/init', before layer configuration  
executes.  
 This function is mostly useful for variables that need to be set  
before packages are loaded. If you are unsure, you should try in setting them in  
`dotspacemacs/user-config' first."  
(setq configuration-layer--elpa-archives  
    '(("melpa-cn" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")  
      ("org-cn"   . "http://mirrors.tuna.tsinghua.edu.cn/elpa/org/")  
      ("gnu-cn"   . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/")))  
  )  
```



果然快了许多，备选的源

```lisp
(setq configuration-layer--elpa-archives
    '(("melpa-cn" . "http://elpa.emacs-china.org/melpa/")
      ("org-cn"   . "http://elpa.emacs-china.org/org/")
      ("gnu-cn"   . "http://elpa.emacs-china.org/gnu/")))
```



### C++  相关配置

#### 打开c++ layer



安装clang-format

```
sudo apt install clang-format
```

https://liu233w.github.io/2016/06/16/clang-format.org/





#### 侧边栏显示函数列表

1. https://github.com/syl20bnr/spacemacs/blob/master/layers/+tools/imenu-list/README.org







1. [emacs_247_spacemacs中选扩展选择代码区域](https://blog.csdn.net/grey_csdn/article/details/82974910)

#### 快捷键

1， Emacs风格中则绑定了M-m（一般情况下是 Alt + m）

如果一个函数就在这个文件中实现，在该文件buffer的其他地方想快速跳转过来，可以用如下命令

M-m m g g

如果想要打开新的buffer显示这个函数定义，用下面的命令

M-m m g g      M-RET g G



SPC   g  d     在 窗口下端显示 标识定义





https://blog.csdn.net/u011729865/article/details/52793134/



### 参考链接

```
git checkout -b v0.9rc1 origin/v0.9rc1
```









1. https://segmentfault.com/q/1010000007778370
2. [用spacemacs打造c++ IDE](https://blog.csdn.net/csfreebird/article/details/71194235)
3. https://blog.csdn.net/samjjx/article/details/52242740
4. [因为刚好遇见你：Spacemacs](https://www.jianshu.com/p/8a8a35596b9d)
5. [子龙山人spacemacs](https://zilongshanren.com/blog/2015-12-06-spacemacs-rocks.html)
6. http://spacemacs.org/doc/QUICK_START.html

