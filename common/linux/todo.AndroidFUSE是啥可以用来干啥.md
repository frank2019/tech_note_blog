

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

mount 命令进行挂载



#### 比较知名的用户态文件系统：

目前FUSE支持的平台：

1. Linux 完全支持

2. BSD 部分支持

3. OX-X参考OSXFUSE



- ExpanDrive：商业文件系统，实现了SFTP/FTP/FTPS协议；
- GlusterFS：用于集群的分布式文件系统，可以扩展到PB级；

- SSHFS：通过SSH协议访问远程文件系统；


- GmailFS：通过文件系统方式访问GMail；


- EncFS：加密的虚拟文件系统


- NTFS-3G和Captive NTFS，在非Windows中对NTFS文件系统提供支持；


- WikipediaFS：支持通过文件系统接口访问Wikipedia上的文章；


- 升阳公司的Lustre：和GlusterFS类似但更早的一个集群文件系统


- ZFS：Lustre的Linux版；


- archivemount：


- HDFS: Hadoop提供的分布式文件系统。HDFS可以通过一系列命令访问，并不一定经过Linux FUSE







开发

安装fuse库

fuse3

```
sudo apt-get install fuse3 libfuse3-dev
```

fuse2

```
sudo apt-get install fuse libfuse-dev
```



#### libfuse 的示例程序

libfuse提供了几个示例程序，都在example目录下：

- hello.c ：最简单的libfuse用法，基本api用法
  hello_ll.c ：ll是low level的缩写，展示了低层次接口的基本用法
  null.c ：实现了一个类似linux下的/dev/null的设备
  fioc.c/fioclient.c ：fioc是fuse ioctl的缩写，这个例子展示的就像很多驱动一样，能够使用ioctl接口进行交互
  fsel.c/fselclient.c ： fsel是fuse select缩写，比较高级的用法。
  cusexmp.c/fusexmp.c/fusexmp_fh.c ： 这几个例子都是文件映射相关的，有一定的实用意义，实现的接口较全面。





#### 参考链接

1. [FUSE(Filesystem in Userspace)0](https://www.jianshu.com/p/c2b77d0bbc43)
2. https://wenku.baidu.com/view/86c61a4033687e21af45a994.html
3. [使用 FUSE 开发自己的文件系统](https://www.ibm.com/developerworks/cn/linux/l-fuse/)
4. [Fuse-2.9.7       ](http://www.linuxfromscratch.org/blfs/view/stable/postlfs/fuse2.html)
5. [用户态文件系统(FUSE)框架分析和实战](https://blog.csdn.net/juS3Ve/article/details/78237236)

