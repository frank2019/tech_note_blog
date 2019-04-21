

spacemacs 中的窗口管理



```
养心莫若寡欲，至乐无如读书   --戚继光
```



#### 窗口操作

| Keybinding           | Function                                    |
| -------------------- | ------------------------------------------- |
| `SPC w v or :vsplit` | 右侧打开一个垂直分屏窗口                    |
| `SPC w s or :split`  | 底部水平打开分屏窗口                        |
| `SPC w h/j/k/l`      | 多个窗口进行窗口切换                        |
| `SPC w .`            | 窗口瞬时状态                                |
| `SPC w c`            | w c 	window close                        |
| `SPC w m`            | w m 	window 最大化                       |
| `SPC b m`            | Kill all buffers except the current buffer. |
| `SPC w /`            | w / 	window竖切                          |
| `spc w -`            | w - 	window横切                          |
| `ctrl+w ctrl+w`      | 切换到下一个窗口。或者是ctrl+w w            |
| `ctrl+w p`           | 切换到前一个窗口                            |
| `ctrl+w h(l,j,k)`    | 切换到左（右，下，上）的窗口                |
| `ctrl+w t(b)`        | 切换到最上（下）面的窗口。                  |
| `ctrl+w H(L,K,J)`    | 将当前窗口移动到最左（右、上、下）面        |
| `ctrl+w r`           | 旋转窗口的位置                              |
| `ctrl+w T`           | 将当前的窗口移动到新的标签页上              |
| ctrl+w +             | 当前窗口增高一行。也可以用n增高n行          |



buffer操作

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