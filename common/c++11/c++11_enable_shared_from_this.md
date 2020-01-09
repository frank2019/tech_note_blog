# C++11新特性 enable_shared_from_this



enable_shared_from_this是一个模板类，定义于头文件<memory>，其原型为：

```c++
template< class T > class enable_shared_from_this;
```

## 功能

 std::enable_shared_from_this 能让一个对象（假设其名为 t ，且已被一个 std::shared_ptr 对象 pt 管理）安全地生成其他额外的 std::shared_ptr 实例（假设名为 pt1, pt2, ... ） ，它们与 pt 共享对象 t 的所有权。
       若一个类 T 继承 std::enable_shared_from_this<T> ，则会为该类 T 提供成员函数： shared_from_this 。 当 T 类型对象 t 被一个为名为 pt 的 std::shared_ptr<T> 类对象管理时，调用 T::shared_from_this 成员函数，将会返回一个新的 std::shared_ptr<T> 对象，它与 pt 共享 t 的所有权。

## **使用场合**

当类A被share_ptr管理，且在类A的成员函数里需要把当前类对象作为参数传给其他函数时，就需要传递一个指向自身的share_ptr。



## Q&A

1.为何不直接传递this指针

   使用智能指针的初衷就是为了方便资源管理，如果在某些地方使用智能指针，某些地方使用原始指针，很容易破坏智能指针的语义，从而产生各种错误。

2.可以直接传递share_ptr<this>么？

   答案是不能，因为这样会造成2个非共享的share_ptr指向同一个对象，未增加引用计数导对象被析构两次。

## 代码示例

```c++
#include <memory>
#include <iostream>

struct Good :std::enable_shared_from_this<Good>
{
    ~Good() { std::cout << "Good::~Good() calld" << std::endl; }
};

int main(int argc, char **argv) {
    {
        std::shared_ptr<Good> gp1(new Good());
        std::shared_ptr<Good> gp2 = gp1->shared_from_this();

        std::cout << "gp1.use_count()=" << gp1.use_count() << std::endl;
        std::cout << "gp2.use_count()=" << gp2.use_count() << std::endl;
    }
    system("pause");
}
```



## 参考链接

[C++11新特性之十：enable_shared_from_this](https://blog.csdn.net/caoshangpa/article/details/79392878)

