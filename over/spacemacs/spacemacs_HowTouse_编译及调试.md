



```
朝菌不知晦朔，蟪蛄不知春秋
																		-庄子
```





vim提供了:make来编译程序，默认调用的是make， 如果你当前目录下有makefile，简单地:make即可。

如果你没有make程序，你可以通过配置makeprg选项来更改make调用的程序。 如果你只有一个abc.[Java](http://lib.csdn.net/base/java)文件，你可以这样设置：

```
set makeprg=javac\ abc.java
```

然后:make即可。如果程序有错，可以通过quickfix窗口查看错误。 不过如果要正确定位错误，需要设置好errorformat，让vim识别错误信息。 如：

```
:setl efm=%A%f:%l:\ %m,%-Z%p^,%-C%.%#
```

%f表示文件名，%l表示行号， %m表示错误信息，其它的还不能理解。 请参考 :help errorformat。

#### 快速修改窗口

其实是quickfix插件提供的功能， 对编译调试程序非常有用 :)

快速修改窗口在make程序时非常有用，当make之后：

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



**不改变光标位置**
当我们运行 :make 命令时， Vim 会自动跳转到第一处错误上（除非没有出现任何
错误）。如果我们想保持光标位置不变，可用以下命令来代替原来的命令：
➾:make!
位于结尾处的符号 ! 将指示 Vim 只更新 quickfix 列表，而不跳到第一处错误。现
在假设在我们运行 :make 之后，突然发现应该使用带叹号的版本，我们要怎样才能让
光标回到运行 :make 之前的位置呢？很简单， 使用 <C-o> 命令将返回跳转列表（jump
list）的上一处位置

#### spacemacs 使用gdb

1, [spacemacs 使用gdb](https://blog.csdn.net/csfreebird/article/details/71171559)