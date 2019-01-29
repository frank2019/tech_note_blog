





安装[Source Code Pro](https://github.com/adobe/source-code-pro/downloads)

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





### 参考链接

1. [在Ubuntu 中使用Source Code Pro字体](https://blog.csdn.net/android_hasen/article/details/50523013)





----



Ubuntu 14.04:

```
[ -d /usr/share/fonts/opentype ] || sudo mkdir /usr/share/fonts/opentype
sudo git clone https://github.com/adobe-fonts/source-code-pro.git /usr/share/fonts/opentype/scp
sudo fc-cache -f -v
```

