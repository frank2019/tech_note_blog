

Android 8.0   引入了一个新的特性 Project Treble 机制。



## Android 系统是如何进行更新的

在理解 Project Treble 的原理、作用及其意义之前，我们很有必要先来了解一下 Android 系统进行大版本升级的大致流程：

1. Google 将新系统源码发布至 AOSP
2. 启动/硬件适配：芯片制造商（高通、三星、联发科等等）对源码进行有针对性的修改，来让自家芯片能够在新版本 Android 系统源码的基础上正常启动、各功能有效运作
3. OEM 适配：芯片制造商将修改后的源码交给 OEM 厂商，厂商根据自己的需求进一步修改新系统，加入特色功能和定制应用等等
4. QA/测试：OEM 厂商对系统进行内部测试，部分厂商还会与合作运营商一起检测新版系统的兼容性
5. 最终版本：测试无误后的新版系统通过 OTA 推送给用户



Project Treble 机制的简易示意图。

![](https://s3.ifanr.com/wp-content/uploads/2017/11/WechatIMG458.png!720)



## 参考链接

1. [Project Treble 是什么，又将为 Android 带来怎样的改变?](https://sspai.com/post/40890)
2. [Project Treble 让 Android 告别升级慢，还让刷机更好玩](https://www.ifanr.com/946585)