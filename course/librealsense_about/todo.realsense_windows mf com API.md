



## COM API

### 引用头文件

```
#include <Windows.h>
```



### CoInitializeEx

```
CoInitializeEx(nullptr, COINIT_MULTITHREADED)
```

### CoUninitialize();







## Media Foundation

### 头文件

```c++
#include <mfapi.h>
```



### MFStartup()

```
STDAPI MFStartup( ULONG Version, DWORD dwFlags = MFSTARTUP_FULL );
```



### MFShutdown()





## 参考链接

1. https://docs.microsoft.com/zh-cn/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex