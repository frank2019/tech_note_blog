





名词解释

- project    在某目录里建立一个空文件.projectile。就成功创建了一个project目录。可以在这个目录进行grep操作

- window 	窗口，可以分栏

- frame 	是一个emacs框架。可以包含多个window

- buffer 	文件加载到emacs里，就称之为一个buffer。一个emacs可以存在很多很多buffer。可以在打开的多个buffer里搜索关键词或者文件名

- layout 	emacs的窗口界面，以及emacs打开的buffer文件。作为一个session，保存下来。

  







spacemacs常用快捷键

快捷键(启动键是SPC，即空格) 	描述 	推荐星级

, 	（注意：不需要SPC启动）当前模式下的lead-key快捷键，可以显示当前模式的常用命令，很不错！ 	*****
SPC x 	查找并跳转到“单词x或者X开头的单词位置”，x是char字符，可以是任意字符 	
! 	执行shell命令 	
‘ 	打开一个shell终端 	
*或者/ 	在project里搜索关键词 	*****
1 2 3 … 9 	跳转到第n个window窗口 	
: 	即emacs自带的M-x 	
; 	用来注释代码的，这个可以查看一下帮助手册。各种注释操作 	
? 	显示所有快捷键。可以grep关键词查找快捷键。 	
` 	mark相关。即标记位置，用于代码跳转的。就是标签。 	
a r 	ranger命令。打开当前文件所在目录，并能实时显示目录或文件内容 	*****
a u 	undo作用。可以上下操作，是undo的history列表。 	
b b 	查找并切换到buffer/recent-file 	
b d 	删除当前buffer 	
f f 	查找文件以及recent-files 	
f y 	复制并显示当前buffer文件名。完整路径 	*****
l s 	layout的保存，输入layout的名称 	*****
l L 	大写L。layout的load加载 	*****
n n 	narrow命令。就是把某段代码单独显示。操作完之后，SPC n w就可以回到之前的界面 	
n w 	narrow-widen命令。 	
p p 	打开某个project。 	*****
q q 	退出spacemacs 	
r r 	显示register里的值。一般是复制、删除、选中后的内容。这个需要查看emacs帮助手册理解。 	
s a p 	在project的所有文件里，使用ag（因为ag>ack>grep的搜索速度，所以只推荐ag。ag需要单独安装，很简单，百度即可）命令搜索关键词。 	*****
s s 	在当前buffer里搜索关键词。 	*****
s S 	在当前buffer里搜索关键词。SPC s S比*，结果要好看 	*****
T h 	选择主题。一般都选择spacemacs默认主题，另外就是monokai。 	
u 	这个命令，类似linux里的xargs，是一个神奇的命令。我还不熟悉。应该深入了解。 	
v 	外扩命令。就是代码不断增加选中的范围。很神奇的。会有提示下一个按键。v是继续外扩；V是缩小外扩。 	
w - 	window横切 	
w / 	window竖切 	
w c 	window close 	
w m 	window 最大化 	

x a 	代码对齐的。会有提示下一个按键。 	











#### 参考链接

1. https://blog.csdn.net/u011729865/article/details/52793134/ 
   