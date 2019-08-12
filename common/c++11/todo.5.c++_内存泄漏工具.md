

# 好用的工具

## Valgrind memcheck



## _CrtDumpMemoryLeaks

只要每一个cpp在展开后都能看见这几行（[https://github.com/vczh-libraries/Vlpp/blob/master/Source/Basic.h](https://link.zhihu.com/?target=https%3A//github.com/vczh-libraries/Vlpp/blob/master/Source/Basic.h)）：

```cpp
#ifdef VCZH_CHECK_MEMORY_LEAKS
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#define VCZH_CHECK_MEMORY_LEAKS_NEW new(_NORMAL_BLOCK, __FILE__, __LINE__)
#define new VCZH_CHECK_MEMORY_LEAKS_NEW
#endif
```

在程序退出的时候，调用_CrtDumpMemoryLeaks函数，Visual Studio的output窗口就会打印所有没有释放的东西（包括全局变量——所以不要在全局变量里面使用非指针或数字类型），双击可以跳进代码。

我都配置成debug模式会检查，每次运行的时候都在检查，有时候我都忘记他在检查了然后突然就蹦出来了消息说我内存泄漏了，然后马上改。所以我的程序绝对没有内存泄漏（逃



# 参考链接



1. https://blog.csdn.net/baidu_38477614/article/details/78879158

2. https://blog.csdn.net/wetest_tencent/article/details/51121834
3. [C++不用工具，如何检测内存泄漏？](https://www.zhihu.com/question/29859828/answer/46024313)