



```
天下万物生於有，有生於无
																		-老子
```





浏览 Quickfix 列表的命令 

| Key Binding | Description                  |
| ----------- | ---------------------------- |
| `:cl`       | 在快速修改窗口中列出错误     |
| `:cr`       | 定位到第一个错误             |
| `:cnext`    | 跳转到下一项                 |
| `:cprev`    | 跳转到上一项                 |
| `:cfirst`   | 跳转到第一项                 |
| `:clast`    | 跳转到最后一项               |
| `:cnfile`   | 跳转到下一个文件中的第一项   |
| `:cpfile`   | 跳转到上一个文件中的最后一项 |
| `:cc N`     | 跳转到第 n 项                |
| `:copen`    | 打开 quickfix 窗口           |
| `:cclose`   | 关闭 quickfix 窗口           |





## [13.2 ctags](http://www.cnblogs.com/jiqingwu/archive/2012/06/14/vim_notes.html#id103)

- ctags -R: 生成tag文件，-R表示也为子目录中的文件生成tags
- :set tags=path/tags – 告诉ctags使用哪个tag文件
- :tag xyz – 跳到xyz的定义处，或者将光标放在xyz上按C-]，返回用C-t
- :stag xyz – 用分割的窗口显示xyz的定义，或者C-w ]， 如果用C-w n ]，就会打开一个n行高的窗口
- :ptag xyz – 在预览窗口中打开xyz的定义，热键是C-w }。
- :pclose – 关闭预览窗口。热键是C-w z。
- :pedit abc.h – 在预览窗口中编辑abc.h
- :psearch abc – 搜索当前文件和当前文件include的文件，显示包含abc的行。

有时一个tag可能有多个匹配，如函数重载，一个函数名就会有多个匹配。 这种情况会先跳转到第一个匹配处。

- :[n]tnext – 下一[n]个匹配。
- :[n]tprev – 上一[n]个匹配。
- :tfirst – 第一个匹配
- :tlast – 最后一个匹配
- :tselect tagname – 打开选择列表

tab键补齐

- :tag xyz<tab> – 补齐以xyz开头的tag名，继续按tab键，会显示其他的。
- :tag /xyz<tab> – 会用名字中含有xyz的tag名补全。

## [13.3 cscope](http://www.cnblogs.com/jiqingwu/archive/2012/06/14/vim_notes.html#id104)

- cscope -Rbq: 生成cscope.out文件
- :cs add /path/to/cscope.out /your/work/dir
- :cs find c func – 查找func在哪些地方被调用
- :cw – 打开quickfix窗口查看结果

## gtags

Gtags综合了ctags和cscope的功能。 使用Gtags之前，你需要安装GNU Gtags。 然后在工程目录运行 gtags 。

```
sudo apt install global
```



- :Gtags funcname 定位到 funcname 的定义处。
- :Gtags -r funcname 查询 funcname被引用的地方。
- :Gtags -s symbol 定位 symbol 出现的地方。
- :Gtags -g string Goto string 出现的地方。 :Gtags -gi string 忽略大小写。
- :Gtags -f filename 显示 filename 中的函数列表。 你可以用 :Gtags -f % 显示当前文件。
- :Gtags -P pattern 显示路径中包含特定模式的文件。 如 :Gtags -P .h$ 显示所有头文件， :Gtags -P /vm/ 显示vm目录下的文件。



## 5 Key bindings

| Key Binding | Description                                               |
| ----------- | --------------------------------------------------------- |
| `SPC m g c` | create a tag database                                     |
| `SPC m g f` | jump to a file in tag database                            |
| `SPC m g g` | jump to a location based on context                       |
| `SPC m g G` | jump to a location based on context (open another window) |
| `SPC m g d` | find definitions                                          |
| `SPC m g i` | present tags in current function only                     |
| `SPC m g l` | jump to definitions in file                               |
| `SPC m g n` | jump to next location in context stack                    |
| `SPC m g p` | jump to previous location in context stack                |
| `SPC m g r` | find references                                           |
| `SPC m g R` | resume previous helm-gtags session                        |
| `SPC m g s` | select any tag in a project retrieved by gtags            |
| `SPC m g S` | show stack of visited locations                           |
| `SPC m g u` | manually update tag database                              |





#### 参考链接

1. [Helm Gtags layer](http://spacemacs.org/layers/+tags/gtags/README.html)

2. [ggtags](https://github.com/leoliu/ggtags)