

```
合抱之木，生於毫末；九层之台，起於累土；千里之行，始於足下。
									     -老子
```



因为工作需要在linux环境下编辑开发，选了一个合适的代码编辑器emacs 和vim的混合体之一  spacemacs。

目前感觉很好用。  不过由于对键盘不够熟悉，效率还不够高，继续努力中。。。



### emacs spacemacs基本安装

1. 安装emacs25以上版本，
2. spacemacs 安装参照官网说明,可以使用我的spacemacs配置(https://github.com/frank2019/spacemacs )



#### 字体的支持

首先是下载Source Code Pro字体,github上的比较慢,下面网址的很快

http://www.fontsquirrel.com/

然后/usr/share/fonts/ 下新建一个目录

接着解压下载的字体到该目录下,然后执行

```
sudo mkdir /usr/share/fonts/opentype
sudo fc-cache -f -v       //使字体生效
```



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



#### 注释插件 Evil-commentary layer

| Key Binding | Description                   |
| ----------- | ----------------------------- |
| `SPC ;`     | comment operator              |
| `gcc`       | comment current line          |
| `gcap`      | comment paragraphs            |
| `gc SPC y`  | comment up to a line with avy |
| `gy`        | comment and yank              |

参考链接

1. [Evil-commentary layer](http://spacemacs.org/layers/+vim/evil-commentary/README.html)



#### spacemacs中选扩展选择代码区域

| Key Binding | Description                           |
| ----------- | ------------------------------------- |
| `SPC v`     | 选中区域，继续按v可以依次扩大选中区域 |



#### 参考链接

1. https://segmentfault.com/q/1010000007778370
2. [用spacemacs打造c++ IDE](https://blog.csdn.net/csfreebird/article/details/71194235)
3. https://blog.csdn.net/samjjx/article/details/52242740
4. [因为刚好遇见你：Spacemacs](https://www.jianshu.com/p/8a8a35596b9d)
5. [子龙山人spacemacs](https://zilongshanren.com/blog/2015-12-06-spacemacs-rocks.html)
6. http://spacemacs.org/doc/QUICK_START.html
7. [vim 操作命令大全（转）](https://www.cnblogs.com/uncle-qi/p/9356465.html)

