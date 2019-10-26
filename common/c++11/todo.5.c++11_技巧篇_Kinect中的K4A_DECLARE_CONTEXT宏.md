# K4A_DECLARE_CONTEXT



## 代码来源

代码位置：Azure-Kinect-Sensor-SDK\include\k4ainternal\handle.h



## 解析

### KSELECTANY

```ini
#ifdef _WIN32
#define KSELECTANY __declspec(selectany)
#else
#define KSELECTANY __attribute__((weak))
#endif
```

#### selectany

在MFC，ATL的源代码中充斥着__declspec(selectany)  的声明。selectany可以让我们在.h文件中初始化一个全局变量而不是只能放在.cpp中。比如有一个类，其中有一个静态变量，那么我们可以在.h
中通过类似__

```
 _declspec(selectany)   type   class::variable   =   value; 
```


"这样的代码来初始化这个全局变量。既是该.h被多次include，链接器也会为我们剔除多重定义的错误。这个有什么好处呢，我觉得对于teamplate的编程会有很多便利。

#### weak

场景：

A,B两个模块，A模块调用了不确定B模块是否提供了函数，但是又不得不调用，这个时候在A模块中再申明一个弱符号函数，即用weak，如果外部提供了调用外部的，如果没提供调用申明的。


弱符号：

若两个或两个以上全局符号（函数或变量名）名字一样，而其中之一声明为weak属性，则这些全局符号不会引发重定义错误。链接器会忽略弱符号，去使用普通的全局符号来解析所有对这些符号的引用，但当普通的全局符号不可用时，链接器会使用弱符号。当有函数或变量名可能被用户覆盖时，该函数或变量名可以声明为一个弱符号。




## K4A_DECLARE_CONTEXT



```c++
#ifdef __cplusplus
#define ALLOCATE(type) (type *)(::new (std::nothrow) type()) /* init to zero */
#define DESTROY(ptr) ::delete ptr
#define PRIV_HANDLE_TYPE(type) _handle_##type##_cpp
#define PUB_HANDLE_TYPE(type) type##_wrapper_##_cpp
#define STR_INTERNAL_CONTEXT_TYPE(type) STRINGIFY(type##_cpp)
#else
#define ALLOCATE(type) (type *)(calloc(sizeof(type), 1)) /*Zero initialized*/
#define DESTROY(ptr) free(ptr)
#define PRIV_HANDLE_TYPE(type) _handle_##type##_c
#define PUB_HANDLE_TYPE(type) type##_wrapper_##_c
#define STR_INTERNAL_CONTEXT_TYPE(type) STRINGIFY(type##_c)
#endif
```

**备注**

STRINGIFY 定义在common.h

//#define STRINGIFY(string) #string

理解可参考： [](c++11_语法篇_##和#操作符.md)



```c++
/* K4A_DECLARE_CONTEXT creates type matched C functions to create, destroy and get the context. The create and destroy
functions will ensure matched CPP constructor and destructor are called. To protext against the create function being used with CPP and destroy being used with C, or vise-vesa, the types get c or cpp appended to them. */
#define K4A_DECLARE_CONTEXT(_public_handle_name_, _internal_context_type_)  
...
```



- K4A_DECLARE_CONTEXT  宏 用来帮我们创建c形式的  create, destroy 和 get the context函数。
- 函数名按照约定好的格式，参看源代码。
- create, destroy 函数会确保对应的CPP 类的构造函数和析构函数被调用，
- 针对和  todo



使用示例

// Declare the handle in your public header
K4A_DECLARE_HANDLE(foo_t);

