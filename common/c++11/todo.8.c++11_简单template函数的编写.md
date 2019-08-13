

> 把处理不同类型的公共逻辑抽象成函数，就得到了函数模板。
>
> 函数模板可以声明为inline或者constexpr的，将它们放在template之后，返回值之前即可。



```c++
template<typename T1, typename T2, typename T3>
T1 sum(T2 v2, T3 v3) {
    return static_cast<T1>(v2 + v3);
}
```



```c++
/// @cond FALSE
/** Casts an arithmetic value, clamping to the supported range of the type being cast to
 *
 * \returns input represented in output_type
 *
 * \remarks
 * Clamps to 0 for unsigned types
 */
template<typename output_type, typename input_type> output_type clamp_cast(input_type input)
{
    static_assert(std::is_arithmetic<input_type>::value, "clamp_cast only supports arithmetic types");
    static_assert(std::is_arithmetic<output_type>::value, "clamp_cast only supports arithmetic types");
    const input_type min_value = std::is_signed<input_type>() ?
                                     static_cast<input_type>(std::numeric_limits<output_type>::min()) :
                                     0;

    input_type max_value = static_cast<input_type>(std::numeric_limits<output_type>::max());
    if (max_value < 0)
    {
        // Output type is of greater or equal size to input type and we've overflowed.
        //
        max_value = std::numeric_limits<input_type>::max();
    }
    input = std::min(input, max_value);
    input = std::max(input, min_value);
    return static_cast<output_type>(input);
}
```







| 函数                     | 类型   | 描述                                           |
| ------------------------ | ------ | ---------------------------------------------- |
| `std::is_signed<type>()` | bool   | checks if a type is an unsigned arithmetic typ |
| static_assert            | ``     | 静态断言                                       |
| std::min                 | void * | 暂时设置未NULL                                 |
| 返回                     | int    | 0: success; <0: error                          |





### std::numeric_limits

在C/C++11中，std::numeric_limits为模板类，在库编译平台提供基础算术类型的极值等属性信息。

用于取代<climits>和<limits.h>,浮点常数定义于<cfloat>和<float.h>。

新的极值概念有两个优点，一是提供了更好的类型安全性，二是程序员可借此写出一些template以核定这些极值。







### 静态断言(static_assert)

#### 定义

C++0x中引入了**static_assert**这个关键字，用来做编译期间的断言，因此叫做静态断言。

其语法很简单：

```c++
static_assert(常量表达式，提示字符串)
```

如果第一个参数常量表达式的值为真(true或者非零值)，那么**static_assert**不做任何事情，就像它不存在一样，否则会产生一条编译错误，错误位置就是该**static_assert**语句所在行，错误提示就是第二个参数提示字符串。

#### 优点

1，使用**static_assert**，我们可以在编译期间发现更多的错误，用编译器来强制保证一些契约，并帮助我们改善编译信息的可读性，尤其是用于模板的时候。

2，**static_assert**可以用在全局作用域中，命名空间中，类作用域中，函数作用域中，几乎可以不受限制的使用。

3，编译器在遇到一个**static_assert**语句时，通常立刻将其第一个参数作为常量表达式进行演算，但如果该常量表达式依赖于某些模板参数，则延迟到模板实例化时再进行演算，这就让检查模板参数成为了可能。

4，由于之前有望加入C++0x标准的**concepts**提案最终被否决了，因此对于检查模板参数是否符合期望的重任，就要靠**static_assert**来完成了，所以如何构造适当的常量表达式，将是一个值得探讨的话题。

5，性能方面，由于是**static_assert**编译期间断言，不生成目标代码，因此**static_assert**不会造成任何运行期性能损失。