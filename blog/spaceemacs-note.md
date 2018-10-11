<meta http-equiv="content-type" content="text/html; charset=UTF-8">

概述：
本文主要描述，spacemacs 下的使用
http://spacemacs.org/layers/LAYERS.html


##基本常用快捷键

###帮助文档

SPC h d 查看 describe 相关的文档
SPC h d f 查看指定函数的帮助文档
SPC h d b 查看指定快捷键绑定了什么命令
SPC h d v 查看指定变量的帮助文档

###文件管理  

SPC f f 打开文件（夹），相当于 $ open xxx 或 $ cd /path/to/project
SPC / 用合适的搜索工具搜索内容，相当于 $ grep/ack/ag/pt xxx 或 ST / Atom 中的 Ctrl + Shift + f

 SPC s c 清除搜索高亮

SPC f R 重命名当前文件

SPC b d 关闭当前 buffer (spacemacs 0.1xx 以后)
SPC SPC 搜索当前文件 
SPC b m 	删除其它buffer





C-x C-b 打开缓冲区列表

####窗口管理

SPC f t 或 SPC p t 用 NeoTree 打开/关闭侧边栏，相当于 ST / Atom 中的 Ctrl(cmd) + k + b
SPC f t 打开当前文件所在的目录
SPC p t 打开当前文件所在的根目录

SPC 0 光标跳转到侧边栏（NeoTree）中
SPC n(数字) 光标跳转到第 n 个 buffer 中

SPC w s 或 SPC w - 水平分割窗口
SPC w v 或 SPC w / 垂直分割窗口
SPC w c 关闭当前窗口 (spacemacs 0.1xx 以前)
SPC w d 关闭当前窗口 (spacemacs 0.1xx 以后)



####项目管理

SPC p p 切换项目
SPC p D 在 dired 中打开项目根目录
SPC p f 在项目中搜索文件名，相当于 ST / Atom 中的 Ctrl + p
SPC p R 在项目中替换字符串，根据提示输入「匹配」和「替换」的字符串，然后输入替换的方式：

    E 修改刚才输入的「替换」字符串
    RET 表示不做处理
    y 表示只替换一处
    Y 表示替换全部
    n 或 delete 表示跳过当前匹配项，匹配下一项
    ^ 表示跳过当前匹配项，匹配上一项
    , 表示替换当前项，但不移动光标，可和 n 或 ^ 配合使用

对齐

SPC j = 自动对齐，相当于 beautify
Shell 集成 (必须先配置 Shell layer)

SPC '(单引号) 打开/关闭 Shell
C-k 前一条 shell 命令，相当于在 shell 中按上箭头
C-j 后一条 shell 命令，相当于在 shell 中按下箭头
快速翻页 (在 spacemacs 0.1xx 中没测试过)

SPC n , 或 . 或 < 或 > 进入 scrolling transient state
然后重复按 , 或 . 或 < 或 > 即可，
按其他键会退出 scrolling transient state
, 向上翻一页
. 向下翻一页
< 向上翻半页
> 向下翻半页



###markdown模式的使用

#### 5.1 Element insertion

Key Binding 	Description    
SPC m - 	insert horizontal line		插入一条水平虚线
SPC m h i 	insert header dwim
SPC m h I 	insert header setext dwim
SPC m h 1 	insert header atx 1		标题1
SPC m h 2 	insert header atx 2		
SPC m h 3 	insert header atx 3
SPC m h 4 	insert header atx 4
SPC m h 5 	insert header atx 5
SPC m h 6 	insert header atx 6  
SPC m h ! 	insert header setext 1
SPC m h @ 	insert header setext 2
SPC m i l 	insert link
SPC m i L 	insert reference link dwim
SPC m i u 	insert uri
SPC m i f 	insert footnote
SPC m i w 	insert wiki link
SPC m i i 	insert image
SPC m i I 	insert reference image
SPC m x b 	make region bold or insert bold
SPC m x i 	make region italic or insert italic
SPC m x c 	make region code or insert code
SPC m x C 	make region code or insert code (Github Flavored Markdown format)
SPC m x q 	make region blockquote or insert blockquote
SPC m x Q 	blockquote region
SPC m x p 	make region or insert pre
SPC m x P 	pre region


SPC m k 	kill thing at point   删除数据
SPC m ] 	complete

SPC m o 	follow thing at point
SPC m j 	jump


SPC m > 	indent region      缩进
SPC m < 	exdent region





基本操作

复制一个单词  剪贴一个单词  



```
3 dd：剪切当前行
 4 ndd：n表示大于1的数字，剪切n行
 5 dw：从光标处剪切至一个单子/单词的末尾，包括空格
 6 de：从光标处剪切至一个单子/单词的末尾，不包括空格
 7 d$：从当前光标剪切到行末
 8 d0：从当前光标位置（不包括光标位置）剪切之行首
 9 d3l：从光标位置（包括光标位置）向右剪切3个字符
10 d5G：将当前行（包括当前行）至第5行（不包括它）剪切
11 d3B：从当前光标位置（不包括光标位置）反向剪切3个单词
12 dH：剪切从当前行至所显示屏幕顶行的全部行
13 dM：剪切从当前行至命令M所指定行的全部行
14 dL：剪切从当前行至所显示屏幕底的全部行
```





1. [Markdown layer](http://spacemacs.org/layers/+lang/markdown/README.html)
2. [ubuntu安装最新版node和npm](https://blog.csdn.net/l18710006370/article/details/78180489)


安装vmd 使用
```
npm install -g vmd --registry=https://registry.npm.taobao.org
```


sudo npm install npm@latest -g


sudo npm install -g electron --unsafe-perm=true --allow-root

sudo npm install --unsafe-perm -g vmd



### 支持vue.js

https://github.com/AdamNiederer/vue-mode

https://www.cnblogs.com/dreling/p/6892684.html



###python模式



| Key Binding | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `SPC m c c` | Execute current file in a comint shell                       |
| `SPC m c C` | Execute current file in a comint shell and switch to it in `insert state` |



函数跳转

https://www.cnblogs.com/yangyingchao/archive/2011/09/04/2178379.html





#### 如何调试

IPython 

应该用过 IPython 吧？想象一下，抛出异常时自动把你带到 IPython Shell 是不是很开心？而且和普通的IPython不同，这个时候可以调用 p (print), up(up stack), down(down stack) 之类的命令。还能创建临时变量，执行任意函数。



```python
import sys

class ExceptionHook:
    instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            from IPython.core import ultratb
            self.instance = ultratb.FormattedTB(mode='Plain',
                 color_scheme='Linux', call_pdb=1)
        return self.instance(*args, **kwargs)

sys.excepthook = ExceptionHook()
```

https://blog.csdn.net/qq_37423198/article/details/76180905





https://blog.csdn.net/nfr413/article/details/78387204

#### 1.应该把代码中的所有tab替换为4个空格

sed  -i  's/\t/    /g'  game.py

#### 出错提示

  File "game.py", line 33
​    print "Received input is : ", cmd
​    ^
IndentationError: unexpected indent




###spacemacs c-c++的支持
1. 在配置中打开c-c++

semantic
semantic模式是cedet包的一个重要部分，它提供了一个分析源代码语法结构的基础架构，包含两个内置的分析生成程序（Bovine和Wisent）semantic提供统一的、语言独立的API来访问分析器生成的输出结果。输出的结构可以被任何实现了syntax-aware接口的程序读取。



首先添加semantic 到   dotspacemacs-configuration-layers 中，

然后重新启动spacemacs，会自动安装semantic layer。

之后进入c++代码，将光标移动到一个变量上，运行快捷键

M-m m r 其实就是srefactor-refactor-at-point

然后按照提示填入新的变量名，这样一下子就批量修改了。




编译和调试

https://blog.csdn.net/haoel/article/details/2886/

1. [c++](https://blog.csdn.net/csfreebird/article/details/71194235)
2. [spacemacs配置自己的layers](https://www.jianshu.com/p/bdd64fecddce)
3. [C/C++ 编程有哪些值得推荐的工具？](https://www.zhihu.com/question/23357089)
4. https://github.com/Sarcasm/irony-mode/

####git的使用

magit是emacs编辑器用来管理git版本控制的插件，按照官网的说法是A Git Porcelain inside Emacs，











####参考链接
1. [Markdown layer](http://spacemacs.org/layers/+lang/markdown/README.html)
2. [致Python初学者：Anaconda入门使用指南](http://python.jobbole.com/87522/)
3. [anaconda_mode 0.1.8 ](https://pypi.org/project/anaconda_mode/0.1.8/)
4. [spacemacs中文文档](https://github.com/crazylxr/spacemacas-zh_CH-doc)
5. https://github.com/syl20bnr/spacemacs

-------------------------------------------------------------------------------

首发自我的独立博客： [欢迎访问我的博客：缤纷时光工作室25000li.top](http://www.25000li.top)

###spacemacs 快捷键

古语有说：工欲善其事，必先利其器；
Emacs无疑是编程的神器。通过这一系列的小文章，让我们一起记录熟练使用和打造这一神兵利器。

SPC SPC  -> M-x  进入命令模式
SPC TAB		last buffer
SPC !		shell cmd
SPC *  		smart search w/input  在当前目录下搜索
SPC /		smart search
SPC 0..9	goto  the buffer winnum
SPC ;		evilnc-comment-operator   注释
SPC `		winum-select-window-by-number   xua


####SPC a  applications
SPC a '		helm-available-repls
SPC a c		calc-dispatch
SPC a d		dired    父目录
SPC a k		paradox-list-packages 
SPC a P 	proced
SPC a p		list-processes
SPC a u		undo-tree-visualize










###0x05 spacemacs 窗口操作
古语有说：工欲善其事，必先利其器；
Emacs无疑是编程的神器。通过这一系列的小文章，让我们一起记录熟练使用和打造这一神兵利器。

SPC f T 	调出neoTree
SPC f t 	toggle neoTree
SPC 0 	光标跳转到侧边栏（NeoTree）中
SPC n(数字) 	光标跳转到第 n 个 buffer 中
SPC w m 	当前窗口最大化/还原
SPC w d 	删除窗口
SPC w - 	下分割窗口
SPC w / 	右分割窗口




SPC m c c 	Execute current file in a comint shell
SPC m c C 	Execute current file in a comint shell and switch to it in insert state



SPC w + 	窗口布局切换
SPC w H 	evil模式下 光标移动到最左边窗口
SPC w h 	evil模式下 光标向左移动
SPC w J 	evil模式下 光标移动到最下边窗口
SPC w j 	evil模式下 光标向下移动
SPC w K 	evil模式下 光标移动到最上边窗口
SPC w k 	evil模式下 光标向上移动
SPC w L 	evil模式下 光标移动到最右边窗口
SPC w l 	evil模式下 光标向右移动
SPC w f 	窗口联动跟随模式

SPC w c 	buffer居中模式
SPC w C 	buffer居中并满屏

###0x04 spacemacs 快捷键初识
古语有说：工欲善其事，必先利其器；
Emacs无疑是编程的神器。通过这一系列的小文章，让我们一起记录熟练使用和打造这一神兵利器。
####emacs中的名词解释

project 	在某目录里建立一个空文件.projectile。就成功创建了一个project目录。可以在这个目录进行grep操作
window 	窗口，可以分栏。
frame 	是一个emacs框架。可以包含多个window
buffer 	文件加载到emacs里，就称之为一个buffer。一个emacs可以存在很多很多buffer。可以在打开的多个buffer里搜索关键词或者文件名
layout 	emacs的窗口界面，以及emacs打开的buffer文件。作为一个session，保存下来。

####常用命令：
其中SPC  代表空格键。

1. 查看spacemacs版本  	SPC f e v
2. 跳转到文件的上一层    SPC  f j     辅助记忆：file-jump
3. spacemacs(vim 模式) 退出，这里有三种       C-X   C-c   ， SPC-qq    ， vim 的q
	. 进入命令模式 ：   	SPC SPC
	. SPC b b    		查找并切换到buffer/recent-file
6. SPC  b d             删除当前的buffer
	. SPC fed  		打开当前的配置文件 .spacemacs
	. SPC f e R 		同步配置文件
	. SPC q R 		重启 emacs
	0. SPC ft		spacemacs边栏目录树显示
11. SPC SPC   calendar    打开日历，  q健 退出。
12. SPC c l               增加删除注释
13. 向上C-k，向下C-j     spacemacs使用vim导航键在文件清单中移动
	4. SPC tab           	 在最近的两个buffer之间切换
		. SPC f y 	复制并显示当前buffer文件名。完整路径
		. SPC [1 2 3 … 9] 	跳转到第n个window窗口
17. 

[快捷键](https://blog.csdn.net/railsbug/article/details/79560081)



###0x03 spacemacs 的简单定制

#### emacs   tab 使用4个空格代替

```
;; 用空格替代TAB(nil) or not(t).

(setq-default indent-tabs-mode t)

;; 定义TAB的宽度为4个空格.

(setq-default default-tab-width 4)
```

####显示行号
配置文件中.spacemacs  
```
   ;; (default nil)
   ;;dotspacemacs-line-numbers nil
   dotspacemacs-line-numbers 'relative'
```
这个功能做的很棒，原因自己发现
#### sapcemacs  打开python模式  自动补全等

如对markown ，python等功能，只要在配置文件中打开相应的配置
```
   dotspacemacs-configuration-layers
   '(
     html
     python
     markdown
     ;; ----------------------------------------------------------------
     ;; Example of useful layers you may want to use right away.
     ;; Uncomment some layer names and press <SPC f e R> (Vim style) or
     ;; <M-m f e R> (Emacs style) to install them.
     ;; ----------------------------------------------------------------
     helm
     auto-completion
     ;; better-defaults
     emacs-lisp
```

重启emacs，即会自动加载

#### emacs --insecure
Launch Emacs. Spacemacs will automatically install the packages it requires. If you get an error regarding package downloads then you may try to disable the HTTPS protocol by starting Emacs with

emacs --insecure



window安装位置spacemacs

配置文件的加载顺序

1. 先加载%HOME%目录下的.emacs文件。如果不存在则加载
2. `%HOME%\.emacs.d\init.el文件`；

下载spacemacs 

```
git clone https://github.com/syl20bnr/spacemacs .emacs.d
```


###0x02 Emacs报错处理
古语有说：工欲善其事，必先利其器；
Emacs无疑是编程的神器。通过这一系列的小文章，让我们一起记录熟练使用和打造这一神兵利器。

####Emacs Invalid coding system `UTF-8' is specified
在 emacs 中编辑保存会报错：
Warning (mule): Invalid coding system `UTF-8' is specified


解决办法：

(define-coding-system-alias 'UTF-8 'utf-8)


####Emacs启动报错Failed to load module "canberra-gtk-module"
```sudo apt-get install libcanberra* 

```
应该只要安装libcanberra0， libcanberra-gtk-module，libcanberra-gtk3-module

####Emacs markdown 浏览器预览报中文乱码

Emacs markdown C-c C-c p在浏览器中预览书写的md文件，中文乱码。
解决办法：
在md文件开头添加
```
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
```


###0x01 Ubuntu 18.04  Emacs25.3 安装

####安装依赖的库

```
sudo apt-get install libgtk2.0-dev

;图形库
sudo apt-get install libxpm-dev
sudo apt-get install libjpeg62-dev
sudo apt-get install libgif-dev
sudo apt-get install libtiff5-dev

sudo apt-get install libncurses5-dev
sudo apt-get install libcanberra* 
```
####源码安装
1. 下载连接： http://mirrors.ustc.edu.cn/gnu/emacs/
2. 编译安装  ./configure  &&   make &&   sudo make install

卸载从源码安装的
```
./configure
sudo make uninstall
```

####参考连接
1. https://www.cnblogs.com/ini_always/archive/2011/04/05/2006218.html
2. [源码安装emacs 25.3](http://www.linuxfromscratch.org/blfs/view/svn/postlfs/emacs.html)




