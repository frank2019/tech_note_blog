

## 1,安装

### 下载 Msys2

从[官网](http://mingw-w64.org/doku.php)下载

进入[Download 页面](http://mingw-w64.org/doku.php/download)，这里选择 Msys2 下载Msys2  [msys2 下载链接，及安装说明](http://www.msys2.org/)



## 2,修改更新源

 进入msys64/etc/pacman.d/目录中，分别在三个文件中增加
 mirrorlist.mingw32
 Server = http://mirrors.ustc.edu.cn/msys2/mingw/i686

mirrorlist.mingw64
 Server = http://mirrors.ustc.edu.cn/msys2/mingw/x86_64

mirrorlist.msys
 Server = http://mirrors.ustc.edu.cn/msys2/msys/$arch

## 3,更新Msys2

```bash
pacman -Syu
```

## 4,安装Mingw工具链

```bash
pacman -S --needed base-devel mingw-w64-x86_64-toolchain
git mingw-w64-x86_64-cmake
```

## 5,配置环境变量

将msys2(你的msys2安装目录一般在C:\msys64)/mingw64/bin/
添加到PATH目录

## 6.测试

win+R打开cmd终端
使用命令

```bash
gcc -v
```



## 7, 安装中遇到的问题

### 7.1 错误：GPGME 错误：Invalid argument

```ini
# pacman   -Syu
错误：GPGME 错误：Invalid argument
错误：GPGME 错误：Invalid argument
错误：GPGME 错误：Invalid argument
:: 正在同步软件包数据库...
 mingw32                  554.2 KiB  1866K/s 00:00 [#####################] 100%
 mingw32.sig              119.0   B  0.00B/s 00:00 [#####################] 100%
错误：GPGME 错误：Invalid argument
错误：无法升级 mingw32 (无效或已损坏的数据库 (PGP 签名))
 mingw64                  556.0 KiB  9.05M/s 00:00 [#####################] 100%
 mingw64.sig              119.0   B  0.00B/s 00:00 [#####################] 100%
错误：GPGME 错误：Invalid argument
错误：无法升级 mingw64 (无效或已损坏的数据库 (PGP 签名))
 msys                     185.3 KiB  6.70M/s 00:00 [#####################] 100%
 msys.sig                 119.0   B  0.00B/s 00:00 [#####################] 100%
错误：GPGME 错误：Invalid argument
错误：无法升级 msys (无效或已损坏的数据库 (PGP 签名))
错误：同步所有数据库失败

```



#### 原因 

公司电脑安装了加密系统

以下目录中的文件被加密。 

```
C:\msys64\etc\pacman.d\gnupg
```

#### 解决

解密文件后重试。



## 8，参考链接 

1. [manjaro 更新报错-无效或已损坏的软件包 (PGP 签名)](https://blog.csdn.net/weixin_43968923/article/details/86517381)

2. [windows + msys2替换源](https://blog.csdn.net/wrzfeijianshen/article/details/82820105)
3. [Windows 搭建msys2+mingw32开发环境，编译安装vlc](https://blog.csdn.net/guo_lei_lamant/article/details/85260217)
4. https://github.com/msys2/msys2/wiki/MSYS2-reinstallation





