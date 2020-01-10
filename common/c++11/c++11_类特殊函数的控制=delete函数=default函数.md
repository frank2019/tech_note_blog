





C++ 的类有四类特殊成员函数，它们分别是：

- 默认构造函数、
- 析构函数、
- 拷贝构造函数
- 以及拷贝赋值运算符。

这些类的特殊成员函数负责创建、初始化、销毁，或者拷贝类的对象。
如果程序员没有显式地为一个类定义某个特殊成员函数，而又需要用到该特殊成员函数时，则编译器会隐式的为这个类生成一个默认的特殊成员函数。

## "=default"函数

C++11 标准引入了一个新特性："=default"函数。

程序员只需在函数声明后加上“=default;”，就可将该函数声明为 "=default"函数，编译器将为显式声明的 "=default"函数自动生成函数体。

"=default"函数特性仅适用于类的特殊成员函数，且该特殊成员函数没有默认参数。

## "=delete"函数

为了能够让程序员显式的禁用某个函数，C++11 标准引入了一个新特性："=delete"函数。

程序员只需在函数声明后上“=delete;”，就可将该函数禁用。

"=delete"函数特性还可用于禁用类的某些转换构造函数，从而避免不期望的类型转换

"=delete"函数特性还可以用来禁用某些用户自定义的类的 new 操作符，从而避免在自由存储区创建类的对象





```c++
 class environment
    {
    public:
        static environment& get_instance();

        extrinsics_graph& get_extrinsics_graph();

        int generate_stream_id() { return _stream_id.fetch_add(1); }

        void set_time_service(std::shared_ptr<platform::time_service> ts);
        std::shared_ptr<platform::time_service> get_time_service();

        environment(const environment&) = delete;
        environment(const environment&&) = delete;
        environment operator=(const environment&) = delete;
        environment operator=(const environment&&) = delete;
     
     	void *operator new(size_t) = delete;
    	void *operator new[](size_t) = delete;
    private:

        extrinsics_graph _extrinsics;
        std::atomic<int> _stream_id;
        std::shared_ptr<platform::time_service> _ts;

        environment(){_stream_id = 0;}

    };
```



## 关于参数的左值引用和右值引用



```c++
void foo(X& x); // 左值引用重载
void foo(X&& x); // 右值引用重载
 
X x;
X foobar();
 
foo(x); // 参数是左值，调用foo(X&)
foo(foobar()); // 参数是右值，调用foo(X&&)
```



- X&&就叫做X的右值引用，普通引用现在被称为左值引用

- 最重要的就是函数重载时左值使用左值引用的版本，右值使用右值引用的版本。
- 