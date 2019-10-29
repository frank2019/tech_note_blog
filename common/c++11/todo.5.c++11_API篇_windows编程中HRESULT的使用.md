## 定义

COM要求所有的方法都会返回一个HRESULT类型的错误号。HRESULT 其实就一个类型定义：

```
typedef LONG HRESULT;
HRESULT 类型的返回值反映了函数中的一些情况，其类型定义规范如下：
```

​    31 30 29 28                     16 15                                 0
   |-----|--|------------------------|-----------------------------------|

类别码 (30-31) 反映函数调用结果：
                 00 调用成功
                 01 包含一些信息
                 10 警告
                 11 错误
自定义标记(29) 反映结果是否为自定义标识，1 为是，0 则不是；
操作码 (16-28) 标识结果操作来源，在 Windows 平台上，其定义如下：

```
define FACILITY_WINDOWS          8

define FACILITY_STORAGE          3

define FACILITY_RPC              1

define FACILITY_SSPI             9

define FACILITY_WIN32            7

define FACILITY_CONTROL          10

define FACILITY_NULL             0

define FACILITY_INTERNET         12

define FACILITY_ITF              4

define FACILITY_DISPATCH         2

define FACILITY_CERT             11

```





操作结果码(0-15) 反映操作的状态，WinError.h 定义了 Win32 函数所有可能返回结果。
                 以下是一些经常用到的返回值和宏定义：
                S_OK             函数执行成功，其值为 0 (注意，其值与 TRUE 相反)
                 S_FALSE          函数执行成功，其值为 1
                 S_FAIL           函数执行失败，失败原因不确定
                 E_OUTOFMEMORY    函数执行失败，失败原因为内存分配不成功
                 E_NOTIMPL        函数执行失败，成员函数没有被实现
                 E_NOTINTERFACE  函数执行失败，组件没有实现指定的接口

不能简单地把返回值与 S_OK 和 S_FALSE 比较，而要用 SECCEEDED 和 FAILED 宏进行判断。 

​             

## 相关API



在头文件中定义了一系列宏，用来做判断

比如：





