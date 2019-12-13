## 场景

已经提交了代码，但是发现有问题，想要撤销？

## 如何操作？



```

        首先使用 git reset —hard <版本号> 让 HEAD 指针指向 merge 前的 commit ID。(注意，这是直接放弃之后所有的提交，采用 --hard，这里因为是没有别人提交别的代码)
        再使用 git push origin <分支名> —force 命令强行把提交 push 到服务器即可。

```









## 参考链接

1. [git revert 还有这个坑？](https://www.cnblogs.com/liushilin/p/9584045.html)
2. https://www.cnblogs.com/chucklu/p/4812168.html