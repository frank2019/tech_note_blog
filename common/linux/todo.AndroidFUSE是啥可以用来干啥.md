

```

```



#### FUSE 是什么

FUSE(Filesystem in Userspace)顾名思义，即在用户空间的文件系统。文件系统一般是实现在内核里面的，比如，Ext4、Fat32、NTFS(Kernel原生版)等常见的文件系统，其代码都在内核中，而FUSE特殊之处就是，其文件系统的**核心逻辑**是在**用户空间**实现的。

FUSE

1.  Filesystem in Userspace 用户空间的文件系统。
2. 是为开发用户空间的文件系统提供的框架。
3. 为用户提供编写用户态文件系统的接口。
4. 用户可以不必熟悉Kernel 代码。也可以使用用户空间的第三方库。

#### FUSE组成及功能实现

三部分组成： FUSE 内部模块 ，FUSE库 挂载工具

##### FUSE内部模块

1. 实现了和VFS的对接，看起来像一个普通的文件系统模块
2. 实现了一个可以被用户空间进程访问的设备假设为：/dev/fuse。
3. VFS通过该设备节点与实际的文件系统逻辑通讯
4. VFS发出文件操作请求，将请求转为特定格式，并通过设备传递给用户空间进程，用户进程处理完请求后将请求结果传递给设备，设备将其还原为Linux Kernel需要的格式 返回给VFS。s

##### FUSE库

负责与FUSE内核模块通讯，接收哦来自/dev/fuse的请求，将其转化为一系列的函数调用，并将结果写回到/dev/fuse.



##### 挂载工具







#### 参考链接

1. [FUSE(Filesystem in Userspace)0](https://www.jianshu.com/p/c2b77d0bbc43)
2. https://wenku.baidu.com/view/86c61a4033687e21af45a994.html