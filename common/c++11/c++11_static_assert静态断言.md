



>如切如磋，如琢如磨



# c++静态断言(static_assert)

## 定义

C++0x中引入了**static_assert**这个关键字，用来做编译期间的断言，因此叫做静态断言。

其语法很简单：

```c++
static_assert(常量表达式，提示字符串)
```

如果第一个参数常量表达式的值为真(true或者非零值)，那么**static_assert**不做任何事情，就像它不存在一样，否则会产生一条编译错误，错误位置就是该**static_assert**语句所在行，错误提示就是第二个参数提示字符串。



在C++中，`<cassert>`或<cassert.h>中提供了assert宏（运行期断言）。可以定义NDEBUG来禁用assert宏。

## 优点

1，使用**static_assert**，我们可以在编译期间发现更多的错误，用编译器来强制保证一些契约，并帮助我们改善编译信息的可读性，尤其是用于模板的时候。

2，**static_assert**可以用在全局作用域中，命名空间中，类作用域中，函数作用域中，几乎可以不受限制的使用。

3，编译器在遇到一个**static_assert**语句时，通常立刻将其第一个参数作为常量表达式进行演算，但如果该常量表达式依赖于某些模板参数，则延迟到模板实例化时再进行演算，这就让检查模板参数成为了可能。

4，由于之前有望加入C++0x标准的**concepts**提案最终被否决了，因此对于检查模板参数是否符合期望的重任，就要靠**static_assert**来完成了，所以如何构造适当的常量表达式，将是一个值得探讨的话题。

5，性能方面，由于是**static_assert**编译期间断言，不生成目标代码，因此**static_assert**不会造成任何运行期性能损失。



## sample



```c++
#include<iostream>  
#include<string>  
#include<limits> 

int main(){
	static_assert(!std::is_arithmetic<int>::value, "only supports arithmetic types");
}

//g++  -std=c++11  assert.cpp
```

