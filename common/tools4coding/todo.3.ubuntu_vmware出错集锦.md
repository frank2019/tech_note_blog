vmware 



### ubuntu 18升级程序后，无法启动图形界面，卡在启动界面？

可以通过网络ssh 命令行登陆。



```
sudo  dpkg --configure  -a
```



**apt-get update: 升级安装包相关的命令,刷新可安装的软件列表(但是不做任何实际的安装动作)**

**apt-get upgrade: 进行安装包的更新(软件版本的升级)**

**apt-get dist-upgrade: 进行系统版本的升级(Ubuntu版本的升级)**

**do-release-upgrade: Ubuntu官方推荐的系统升级方式,若加参数-d还可以升级到开发版本,但会不稳定**



找到的方法就是重装桌面

```bash
sudo apt-get update
sudo apt-get install --reinstall ubuntu-desktop
sudo apt-get install unity
```

没有我解决

#  			[Ubuntu18.04 关闭和开启图形界面](https://www.cnblogs.com/schips/p/10577464.html) 		



关闭用户图形界面，使用tty登录。

```bash
sudo systemctl set-default multi-user.target
sudo reboot
```

开启用户图形界面。

```
sudo systemctl set-default graphical.target
sudo reboot
```





error while loading shared libraries:libmpfr.so.4: cannot open shared object file: No such file or directory.

解决：

sudo ln -s /usr/lib/x86_64-linux-gnu/libmpfr.so.6 /usr/lib/x86_64-linux-gnu/libmpfr.so.4

