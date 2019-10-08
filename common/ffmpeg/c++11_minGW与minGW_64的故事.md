



试试问答体。首先得绕个远路，从Win32开始说起，否则之后容易乱……

### Q：什么是Win32？

A：嘛，**32自然是指32位了？不一定。**
正式地说，Win32主要是指跑在Windows NT内核上的Win32子系统。现在x64的Windows上的大部分程序也是跑在这个子系统上的，system32目录也没叫成system64。
尽管32的语源的确来自于“32位”。

### Q：那么为什么还有Win64？

这倒可以肯定，这里的64是指64位目标平台，因为没有上面的那种歧义。
有一点值得注意，在MSVC中，32位环境（当然是说跑的Intel 兼容CPU的PC）预定义宏_WIN32，但64位环境同时预定义了_WIN32和_WIN64。
顺便，通常64位主要指x86_64（微软称为AMD64，这个兼容x86的基础架构一开始的确是AMD先搞出来的，后来才有Intel EM64T）。
64位Itanium也有`_WIN64`，不过一般见不到且跟MinGW没什么关系且现在都不正式支持了，不管了……
对于MinGW来说，这里也有类似的坑：预定义宏得先优先检查64位的。实际情况更加复杂，另说。

### Q：MinGW和MinGW-W64有什么区别？

这个是个关键问题，但是……是个很长的故事。没有铺垫不好回答。
首先，MinGW是GNU工具（包括编译器GCC和GNU binutils和调试器GDB等）在Win32上的一个移植，是从Cygwin里fork出来的。当初只考虑32位。和Cygwin相比，不强调POSIX兼容性而相对强调性能和减小依赖。
具体来说MinGW除了以上工具外，还提供了一个适配于Win32的运行时环境。其中C标准库实现用的直接是微软随Windows分发的MSVCRT。MinGW自己的运行时库依赖于MSVCRT和其它系统库。
而MinGW GCC依赖于MinGW运行时以及libgcc和其它系统库。编译出来的程序一般也要依赖这些库，所以才会写死在默认specs里（可以用gcc -dumpspecs查看）免得用户随便编译链接个程序还得手动指定一大堆-l选项。
用三元组表示目标平台，当年的MinGW是指i386-pc-mingw32。这里i386也可以是i486等等……总之是32位x86指令集架构的名称。中间的pc可选，表示厂商名。mingw32表示系统名。
特别注意，事实上成为标准的“专有名词”mingw32里的32是固定的。另外，所有这些大小写一般也是固定的。GCC等的源码配置里面也有硬编码进去。
然后，因为只支持32位，有人觉得不够用。这里的一个主要人物，就是现在MinGW-W64的主要维护者Kai Tietz。因为工作需要他想MinGW提供扩充x64支持，但对方态度很不友好。于是愤而fork出来，这就是MinGW-W64的由来。
可见，MinGW-W64和原版MinGW有所渊源，但是独立的两个项目。
W64虽然用意是Win64，但是也算是个专有名词，**在三元组里占据厂商名，例如常见的：i686-w64-mingw32。（在GCC源码的配置文件中，\*-w64-mingw32和\*-pc-mingw32是分别对待的。）**
**MinGW-W64是同时支持32位和64位的。甚至还支持32位和64位的交叉编译**（启用multilib支持的MinGW发行版例如mingw-builds可以用-m32或-m64指定）。
显然，W64和支持的架构无关。上面i686就不是64位的平台（而且可以看出这里的32也和架构没关系）。支持64为的对应三元组是x86_64-w64-mingw32。
……容易让人头疼的是，这两个项目现在都没死，偏偏还很容易因为这些字面上的原因搞错。为了下文描述方便，原版MinGW称为MinGW.org。
这里有一点非常重要：**只有MinGW-W64是GCC官方支持的（尽管mingw32平台是二等公民）。Kai Tietz拥有GCC官方repo的提交权限。**
**所以，使用MinGW-W64的GCC一般比MinGW.org有更新更全面的支持，所以现在一般推荐MinGW-W64发行版。**
说到这里……维护mingw.org的Keith Marshall还和Kai Tietz等GCC官方人员在bugzilla上对噗过：gcc.gnu.org/bugzilla/show_bug.cgi?id=52015。
其中Keith Marshall对MinGW-W64使用MinGW一名造成混淆表示愤慨。嘛，这倒也是事实。
当然，也不是说MinGW.org就一无是处了。*-w64-mingw32原则上向后兼容*-pc-mingw32，不过也有一些接口上的差别。BSD流的DT_*在MinGW.org上能用，在MinGW-W64的就没有。（虽然DT_*也不怎么推荐用就是了……）

### Q：什么是MinGW发行版(distribution) ？

这个说法习惯上可以说是从Linux等软件中借用过来的。
类似Linux内核，不管MinGW.org还是MinGW-W64，本身都是相对集中于特定软件包（MinGW运行时库）开发的项目，并不着力于提供整个开箱即用的环境。
因此除了官方的一些编译版本外，有很多人基于MinGW运行时上进行定制封装供用户下载整个环境，有的还提供包管理服务等。这就是发行版。一般提供直接解压加上PATH就能用的环境和/或安装包。
早期比较著名的有TDM-GCC、rubenvb等。
以前用的MinGW.org，不过现在主要转到MinGW-W64上来了。
比较新的发行版，一开始就着眼于MinGW-W64。最著名的发行版之一应该是mingw-builds，基本上近年来（GCC4.7以后）Windows上能用支持最新版本最快的，支持交叉编译。
mingw-builds一开始在sf.net上有自己的项目，不过后来表示要求加入MinGW-W64项目作为official   builds，所以停更了，更新都在MinGW-W64里面，不过残念的是好像到现在MinGW-W64看来都不提供唯一的官方发行版，所以还是叫做personal  builds。
另外提一下还有微软VC++标准库Dinkumware维护者之一Mr.STL(Stephan T. Lavavej) 个人的发行版，默认specs里加了-std=c++11。
还有MSYS2项目的MinGW发行版（这里可能有新的混乱，下文再说），也是mingw-builds一伙人搞的，最近（4.9.1）比mingw-builds更新还快几个小时。
其它发行版可以参照mingw-w64.sourceforge.net，更新相对没那么快。
最后，不嫌闲着蛋疼也可以自己编译。不过迫不得已外最好别这样做（GCC的编译过程和hacking实在无力吐槽）。重复一遍，非常不推荐。

### Q：上面为什么要强调更新呢？

如果不想使用新的特性生成更高质量的代码，其实也没必要盯着上面这么多版本混乱的MinGW了。即便要兼容性，也可以用古董嘛（逃……
对于C++前端来说MinGW尤为重要，现阶段根本没有能顶替的。作为系统默认ABI新锐代表的MSVC2013——前端还是残的……各种bug。
GCC也有各种傻缺bug，不过至少在前端来说，程度上绝逼打不过cl（Microsoft C&C++ Optimizing Compiler）。
VC++调试支持当然好得多，但是编译器一坑爹集成调试再好也没用了。
嘛，Clang++？libc++什么时候能在Windows上跑顺再说——即便这样MinGW兼容的还是得依赖MinGW的libgcc。至于和VC++兼容的clang-cl，看起来还在折腾微软的坑爹ABI黑箱（这没像大部分平台上GCC用的Itanium  ABI公开文档），一年半载别指望了。

### Q：什么是异常模型和线程模型，用哪种比较好？

这两个都是对于C++实现（G++、libgcc、libsup++等等）而言的。
首先，异常模型。C++标准没规定异常怎么实现。MinGW GCC使用的Itanium ABI也没规定必须怎么实现（但规定了一些公共接口），这部分由实现自行考虑。
GCC一般提供了SjLj（C的setjmp/longjmp）实现的stub。对于x86，允许使用Dwarf2调试信息的实现。两者的区别在于sjlj比较通用，但是即便不抛出捕获异常而只是使用异常中立的风格隐式传递异常，也有运行时开销。而Dwarf2兼容性（考虑多层C++和C的DLL互相调用来看）相对较差，但没有这种开销。
**两者ABI并不兼容（知道C++坑爹了吧，不仅不同实现不兼容，同一个编译器同一个平台自己都能跟自己不兼容……）**——前者依赖类似libgcc_s_sjlj.dll这样的dll，后者则是类似libgcc_s_dw2.dll这样的。旧一点的可能也没有这种后缀差异。
另外，libstdc++作为C++标准库实现显然依赖异常，但名字一样的dll可能依赖的不是同一种。所以混用多个版本MinGW   GCC且没把path清理干净的时候容易出现找不到符号定义导致链接失败。这还不是最坑的，有时候gdb载入不同位置的dll在运行时挂掉，还不只是一个PATH的问题……这种情况下先拿system  internals的process exporler之类的工具看看进程加载的DLL是不是预期的再说。
为什么说要有这么坑爹不兼容的，像VC++一样用一种不就好了……其实Win32 x86上最理想的应该是和VC++一样基于SEH（Windows结构化异常处理）的实现，但是Borland关于这个的专利才没过期几天……所以你懂的。
x64上没专利的麻烦，有sjlj和SEH的实现，一般还是SEH。
第二，线程模型。
Windows线程API和POSIX(pthread) 有很大不同，而ISO C++的std::thread为代表的接口是很接近pthread的。
所以在libstdc++上实现这些接口，首先依赖的是pthread在Win32上的移植libwinpthread，也就是POSIX线程模型。因此发布的时候需要带上libwinpthread-1.dll之类的dll。
至于Win32线程模型，GCC mailing list是有提过，不过到现在还是没实现。也就是说ISO C++的实现是残的，没法用。如果只打算用Win32多线程API倒是的可以用。
所以取决于具体需要。要兼容性好点的一般还是POSIX。

### Q：什么是MSYS，和MinGW有什么区别？

MSYS是提供一套“系统”，三元组是*-pc-msys。
**和MinGW相比，MSYS更接近Cygwin（强调POSIX兼容性），提供了一个sysroot（下面有/bin啊/etc什么的），因此移植POSIX环境的程序一般更方便。**
代价也是有的。MSYS环境下原生编译的程序一般需要多依赖MSYS运行时库（当然比Cygwin要轻量多了）。
所以常规的实践是，如果只是开发Windows程序，能用MinGW就不要用MSYS原生的编译器来构建。当然，使用MSYS上的sh等工具还是没问题，跟GNU工具配套怎么说比cmd总好用。（虽然也有不少琐碎坑爹bug。）

### Q：什么是MSYS2，MSYS2上的MinGW发行版是怎么回事？

字面意思，MSYS 2.0。比起1.0来说更加像Cygwin（例如/etc/fstab配置）。项目在sf.net上托管。
一个特色是基础系统附带ArchLinux移植的包管理器pacman，可以同时独立部署/mingw32（i686-w64-mingw32）和/mingw64（x86-w64-mingw32）下的开发和运行环境。
下载依赖相当方便（就是没有靠谱的镜像，网速可能非常拙计）。具体使用参考ArchLinux Wiki。
虽然不支持交叉编译，不过可以分别装所以不是什么问题，比mingw-builds的-m32和-m64来说更加稳定靠谱。
只提供Dwarf2异常模型和POSIX线程模型对于成套系统也不是什么大问题。包虽然比不上ArchLinux那么丰富不过常用的很多都有，免去自己编译的麻烦。**打算长期使用MinGW和相关工具的，推荐使用。**
虽然滚挂了也没多大事，不过版本是个问题。如果需要特定版本的GCC就不适用（比如规避GCC 4.9的坑爹bug……），除非有耐心自己找到.xz手动安装。

### Q：部署程序需要提供哪些文件？

Windows默认安装自然不带MinGW运行时环境，所以除了编译出来的程序和可能附带的数据，一些dll是要准备好的——除非有耐心折腾全部静态链接。
不同版本不同语言不同编译器编译出来的东西都不太一样。最简单暴力也可靠（？）的方法就是复制可执行程序到没装环境的白板测试机上看少了哪些东西（不过未必一目了然）。
简单可靠的方式是用Dependency Walker等工具查看依赖。
对于C++，除非不用POSIX   thread可以省掉libwinpthread，一般至少得确保上面异常模型和线程模型讨论中提到的三个dll（注意就算你不显示使用标准库，编译器生成的代码也可能用到——典型的如默认::operator  new，所以得带上libstdc++）。

### Q：现在还有什么新坑？

就提一个GCC 4.9的问题。
GCC 4.9的LTO（链接时优化）默认使用新的目标文件格式，生成的文件不包含冗余的二进制代码。
但是LTO有特定的phase（内部会多编译几个pass），传统的静态链接器(ar) 不知道这里的约定，所以原来好好的东西，升级4.9以后开了-flto就可能找不到符号链接失败。
现在MinGW发行版应该都没实现gcc-ar（运行会提示没支持linker plugin）。兼容旧版本的行为还得加上-ffat-lto-objects编译选项。

 

来源

https://tieba.baidu.com/p/3186232510

[[科普\]MinGW vs MinGW-W64及其它（比较有意思，来自mingw吧）](https://www.cnblogs.com/findumars/p/7492636.html)