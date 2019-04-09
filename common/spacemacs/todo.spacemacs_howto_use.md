



https://ruby.ctolib.com/article/wiki/96881



#### 0x04 跳转和移动光标

1，查看函数 变量的定义    alt-m  m g g

2，跳转到上一次的光标位置    ctl +  o



| Key Binding            | Description                                |
| ---------------------- | ------------------------------------------ |
| `alt-m  m g g`         | 查看函数 变量的定义                        |
| `ctl+o`                | 跳转到上一次的光标位置，可反复使用         |
| `` (跟~同一个位置的键) | 在上一次光标位置和这一次的光标位置之间切换 |
| `gg`                   | 跳转到第一行                               |
| `G`                    | 跳转到最后一行                             |
| '8G'                   | 跳转到第8行                                |
| '8gg'                  | 跳转到第8行                                |
| 'ctl + f'              | 移动到上一屏                               |
| 'ctl + b'              | 移动到下一屏                               |
|                        |                                            |
|                        |                                            |

##### 

##### 光标



```
h, j, k, l
w, W - 下一个词首(跳过标点)
e, E - 下一个词尾
b, B - 回退一个词(跳过标点)
0 - 到这一行的最开头
^ - 到这一行的非空白最开头
$ - 到这行的行尾
g_ - 到这一行的非空白行为
( - 句首
) - 句尾
```





```
} - Move to end of next paragraph or code block.
{ - Move to start of previous paragraph or code block.
Ctrl+F - Move forward one screenful.
Ctrl+B - Move backward one screenful.
ctrl+d - 向下翻页(down)
ctrl+u - 向上翻页(up)
H, M, L - 屏幕位置，分别为顶部，中间，尾部
zz -  normal模式下区中
ctrl-o zz - insert模式下区中 (利用insert normal模式)
```







```
gg  - 到文件头
G   - 到文件尾

Ngg - 到N行
NG  -
:N  -

gi  - 返回上一次插入文本的地方。
g;  - 返回上一个修改位置
g,  - 返回下一个修改位置

gd       - 跳转到局部定义
gf       - 跳转到文件

ctrl + o - 跳转到上一位置
ctrl + i - 跳转下一位置（和ctrl + o配合在代码间跳转）

ctrl + ]
ctrl + t
```







```
'. - 跳转到最后一次修改的地方(.代表最后一次修改的地方)
'" - 上一次编辑文件的地方
'' - 跳转到上次跳转之前的位置
'( - 当前句子的开头
') - 当前句子的结尾
'{ - 当前段落的开头
'} - 当前段落的结尾
'[ - 上一次修改或复制的第一行的第一个字符
'] - 上一次修改或复制的最后一行的最后一个字符
'< - 上一次Visual area的开始位置
'> - 上一次Visual area的结束位置
```



##### 参考链接

1. [vi/vim使用进阶: 指随意动，移动如飞](https://blog.easwy.com/archives/advanced-vim-skills-advanced-move-method/)
2. [vim 移动跳转](https://mapan1984.github.io/tool/2016/04/22/Vim-%E7%A7%BB%E5%8A%A8%E8%B7%B3%E8%BD%AC/)



#### 0x03窗口管理

SPC 键激活

##### Windows操作

右侧打开一个垂直分屏窗口

```
SPC w v or :vsplit
```

底部水平打开分屏窗口

```
SPC w s or :split
```

多个窗口进行窗口切换

```
SPC w h/j/k/l
```

移除当前窗口

```
SPC w H/J/K/L
```

窗口瞬时状态

```
SPC w .
```

w - 	window横切 	
w / 	window竖切 	
w c 	window close 	
w m 	window 最大化 



`

| Keybinding                | Function                                                     |
| ------------------------- | ------------------------------------------------------------ |
| `SPC b b <buffer-name>`   | Create a buffer named `<buffer-name>`.                       |
| `SPC b b`                 | Search through open buffers and recent files.                |
| `SPC b n` or `:bnext`     | Switch to the next buffer. (See [Special buffers](http://spacemacs.org/doc/VIMUSERS.html#special-buffers)) |
| `SPC b p` or `:bprevious` | Switch to the previous buffer. (See [Special buffers](http://spacemacs.org/doc/VIMUSERS.html#special-buffers)) |
| `SPC b d` or `:bdelete`   | Kill current buffer.                                         |
| `SPC b C-d`               | Kill buffers using a regular expression.                     |
| `SPC b m`                 | Kill all buffers except the current buffer.                  |
| `SPC b .`                 | Buffer transient-state.                                      |



##### Buffers操作

创建名称为<buffer-name>的buffer

```
SPC b b <buffer-name>
```

从已打开的buffers以及最近打开的文件中搜索buffer

```
SPC b b
```

切换到下一个buffer

```
SPC b n or :bnext
```

切换到上一个buffer

```
SPC b p or :bprevious
```

关闭当前buffer

```
SPC b d or :bdelete
```

用表达式关闭buffers

```
SPC b C-d
```

关闭其他buffers

```
SPC b m
```

buffer瞬时状态

```
SPC b .
```





参考链接

1. https://www.liangzl.com/get-article-detail-18899.html



#### 0x02，常用命令

按M-x可弹出支持的命令列表



- 显示日历： M-x  calendar     在日历窗口 按q 退出
- 显示计算器





#### 0x01，侧边栏显示函数列表imenu-list



| Key Binding | Description              |
| ----------- | ------------------------ |
| `SPC b i`   | toggle imenu-list window |

##### From imenu-list buffer

| Key Binding | Description                                            |
| ----------- | ------------------------------------------------------ |
| `q`         | quit imenu-list window                                 |
| `RET`       | go to current entry                                    |
| `d`         | display current entry, keep focus on imenu-list window |
| `f`         | fold/unfold current section                            |

##### 参考链接

1. https://github.com/syl20bnr/spacemacs/blob/master/layers/+tools/imenu-list/README.org

​	











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



https://www.emacswiki.org/emacs/%e7%b6%b2%e7%ab%99%e5%9c%b0%e5%9c%96





1. https://segmentfault.com/q/1010000007778370
2. [用spacemacs打造c++ IDE](https://blog.csdn.net/csfreebird/article/details/71194235)
3. https://blog.csdn.net/samjjx/article/details/52242740
4. [因为刚好遇见你：Spacemacs](https://www.jianshu.com/p/8a8a35596b9d)
5. [子龙山人spacemacs](https://zilongshanren.com/blog/2015-12-06-spacemacs-rocks.html)
6. http://spacemacs.org/doc/QUICK_START.html

