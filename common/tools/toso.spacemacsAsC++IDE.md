



### emacs spacemacs基本安装

1. 安装emacs25以上版本，
2. spacemacs 安装参照官网说明



#### 字体的支持

1. 查看当前的字体
2. 

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





#### 打开c++ layer





### 参考链接

```
git checkout -b v0.9rc1 origin/v0.9rc1
```



1. https://segmentfault.com/q/1010000007778370
2. [用spacemacs打造c++ IDE](https://blog.csdn.net/csfreebird/article/details/71194235)
3. https://blog.csdn.net/samjjx/article/details/52242740
4. [因为刚好遇见你：Spacemacs](https://www.jianshu.com/p/8a8a35596b9d)
5. [子龙山人spacemacs](https://zilongshanren.com/blog/2015-12-06-spacemacs-rocks.html)

