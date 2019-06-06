



Android系统编译 Android 9 Pistachio Ice Cream



```
不出户，知天下；不窥牖，见天道。其出弥远，其知弥少。是以圣人不行而知，不见而明，不为而成。
																-老子
```



#### 1，去哪里下载

由于墙的原因,这里我们采用国内的镜像源进行下载.目前,可用的镜像源一般是科大和清华的,

[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/)

 

#### 2, 编译环境：

ubuntu18 + 16G   虚拟机 vmware。

 

#### 3，安装配置git

```bash
sudo apt-get install git
git config –global user.email "test@test.com"
git config –global user.name "test"
```

#### 4，安装java

```bash
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install openjdk-8-jdk
```

 


如果电脑里面存在多个java 版本，则通过如下命令选择openjdk-8即可

```bash
sudo update-alternative --config java
sudo update-alternative --config javac
```

#### 5，配置PATH环境变量

添加~/bin 到环境变量PATH里面

```bash
mkdir ~/bin
echo "PATH=~/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc
```

 

#### 6，安装依赖库

```bash
sudo apt-get install libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-dev g++-multilib
sudo apt-get install -y git flex bison gperf build-essential libncurses5-dev:i386
sudo apt-get install tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
sudo apt-get install dpkg-dev libsdl1.2-dev libesd0-dev
sudo apt-get install git-core gnupg flex bison gperf build-essential
sudo apt-get install zip curl zlib1g-dev gcc-multilib g++-multilib
sudo apt-get install libc6-dev-i386
sudo apt-get install lib32ncurses5-dev x11proto-core-dev libx11-dev
sudo apt-get install libgl1-mesa-dev libxml2-utils xsltproc unzip m4
sudo apt-get install lib32z-dev ccache
sudo apt-get install libssl-dev
```

 

#### 7，下载配置 repo

```bash
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```

 

修改~/bin/repo 中的REPO_URL 字段为：

```bash
REPO_URL = 'https://gerrit-google.tuna.tsinghua.edu.cn/git-repo'
```



 



7.开始下载代码

##### 方法1

```bash
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-9.0.0_r3
repo sync –no-tags -j8
```



```bash
git clone https://aosp.tuna.tsinghua.edu.cn/kernel/common.git
git checkout "android-4.9-p"
```

##### 方法二

 我是使用初始化包，然后再同步。

由于首次同步需要下载约 30GB 数据，过程中任何网络故障都可能造成同步失败，我们强烈建议您使用初始化包进行初始化。下载 <https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar>，下载完成后记得根据 checksum.txt 的内容校验一下。

由于所有代码都是从隐藏的 `.repo` 目录中 checkout 出来的，所以我们只保留了 `.repo` 目录，下载后解压 再 `repo sync` 一遍即可得到完整的目录。

使用方法如下:

```bash
wget -c https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar # 下载初始化包
tar xf aosp-latest.tar
cd AOSP   # 解压得到的 AOSP 工程目录
# 这时 ls 的话什么也看不到，因为只有一个隐藏的 .repo 目录
repo sync # 正常同步一遍即可得到完整目录
# 或 repo sync -l 仅checkout代码
```

此后，每次只需运行 `repo sync` 即可保持同步。
**我们强烈建议您保持每天同步，并尽量选择凌晨等低峰时间**

#### 8，编译：



```bash
source build/envsetup.sh

lunch // → aosp_x86_64-eng

make update-api -j8

make -j8

```



 

#### 9，运行：

emulator 



#### 出错

如果编译出错，可以重新同步下，再编译

```bash
repo sync
```



#### 参考链接

1. [AOSP(Android) 镜像使用帮助](https://lug.ustc.edu.cn/wiki/mirrors/help/aosp)
2. https://mirrors.tuna.tsinghua.edu.cn/help/AOSP/