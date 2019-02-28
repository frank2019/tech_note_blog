





虚拟机编辑界面，添加硬盘。

虚拟机中挂载磁盘

1. **使用“fdisk -l”的命令查看当前系统的分区**

   ```
   xiao@ubuntu:~$ sudo  fdisk   -l
   [sudo] password for xiao: 
   Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x225789a4
   
   Device     Boot    Start      End  Sectors  Size Id Type
   /dev/sda1  *        2048 39942143 39940096   19G 83 Linux
   /dev/sda2       39944190 41940991  1996802  975M  5 Extended
   /dev/sda5       39944192 41940991  1996800  975M 82 Linux swap / Solaris
   
   
   Disk /dev/sdb: 64 GiB, 68719476736 bytes, 134217728 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   
   ```

   

**对新建的磁盘进行分区及格式化的工作**

创建分区

```
fdisk /dev/sda

3、 命令行提示下输入【m】

     输入命令【n】添加新分区。

     输入命令【p】创建主分区。

     输入【回车】

     输入【回车】

     输入命令【p】

     输入【w】，保持修改
```



格式化新增的硬盘为ext4格式

```
sudo mkfs.ext4  /dev/sdb1
```

   

 命令:mount  /dev/sdb    ./disk1/

​    拷贝到目录fdisk1即是将文件拷贝的新的磁盘

​    最后命令:df  查看当前系统磁盘的情况



ubuntu 自动挂载磁盘

编辑 /etc/fstab  



```
/dev/sdb1       /home/xiao/workspace         ext4    errors=remount-ro 0       1
```

