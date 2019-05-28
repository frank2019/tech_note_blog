Emacs



```
sudo apt install build-essential checkinstall
sudo apt-get install gnutls-bin gnutls-dev
```



```
./configure

make
```



```
//生成deb文件
sudo checkinstall     
```



```
sudo dpkg -I iptux.deb #查看iptux.deb软件包的详细信息，包括软件名称、版本以及大小等（其中-I等价于--info）
sudo dpkg -c iptux.deb #查看iptux.deb软件包中包含的文件结构（其中-c等价于--contents）
sudo dpkg -i iptux.deb #安装iptux.deb软件包（其中-i等价于--install）
sudo dpkg -l iptux #查看iptux软件包的信息（软件名称可通过dpkg -I命令查看，其中-l等价于--list）
sudo dpkg -L iptux #查看iptux软件包安装的所有文件（软件名称可通过dpkg -I命令查看，其中-L等价于--listfiles）
sudo dpkg -s iptux #查看iptux软件包的详细信息（软件名称可通过dpkg -I命令查看，其中-s等价于--status）
sudo dpkg -r iptux #卸载iptux软件包（软件名称可通过dpkg -I命令查看，其中-r等价于--remove）
注：dpkg命令无法自动解决依赖关系。如果安装的deb包存在依赖包，则应避免使用此命令，或者按照依赖关系顺序安装依赖包。 

```



### 安装Source Code Pro

1，下载源码[Source Code Pro](https://github.com/adobe/source-code-pro/downloads)

2，安装工具

```
pip install afdko
pip install --upgrade pip    （如果安装afdko，可以尝试更新pip后再试）
```

3，编译

```
./build
```

4,安装

```
cp  -rf   target/OTF/*.otf     ~/.fonts/
fc-cache -f -v

```





### Emacs 主题设置

```
sudo apt-get update
```

首先安装emacs的辅助插件：

sudo apt-get install emacs-goodies-el


然后进入Emacs:

Emacs 最新版本已经自带各种主题，只要敲入命令：﻿﻿﻿﻿color-theme-select 就会看到一大堆主题，选择一个Emacs就会切换过去。，

当选中了自己喜欢的，记住名称，然后像我这样填入~/.emacs文件中。以后就自动加载了。


默认推荐一个主题，添加到~/.emacs文件中

    (require 'color-theme)
    (color-theme-initialize)
    (color-theme-arjen)

重启emacs，试一下。







### 参考链接

1. [在Ubuntu 中使用Source Code Pro字体](https://blog.csdn.net/android_hasen/article/details/50523013)
2. [Emacs 主题设置](https://blog.csdn.net/csfreebird/article/details/7367099)





----



Ubuntu 14.04:

```
[ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
sudo fc-cache -f -v
```

