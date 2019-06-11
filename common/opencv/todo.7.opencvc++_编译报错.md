```

```



### OpenCV3.0 + VS出现“ACCESS_MASK不明确”错误

#### 原因

**using namspace cv空间命名**，与系统头文件#include<windows.h>**，冲突，两者都有`ACCESS_MASK`定义，会导致该变量不明确，报错。

#### 解决办法

> 1. 不使用 `using namespace cv`，需要用到的地方用`cv::`代替；