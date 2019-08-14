

> 把处理不同类型的公共逻辑抽象成函数，就得到了函数模板。
>
> 函数模板可以声明为inline或者constexpr的，将它们放在template之后，返回值之前即可。





## 函数模板的返回值是模板类型参数

函数模板中的参数和返回值都可以是模板类型参数。编译器必须通过调用函数模板的实参来推断模板类型参数的具体类型。但是，当函数模板的返回值是模板类型参数时，编译器无法通过函数调用来推断返回值的具体类型。此时，在调用函数时必须提供一个显式模板实参（explicit template argument）。



### 显式模板实参

显式模板实参在尖括号中给出，位于函数名之后，实参列表之前。显式模板实参按由左向右的顺序与对应的模板参数匹配



```c++
template<typename T1, typename T2, typename T3>
T1 sum(T2 v2, T3 v3) {
    return static_cast<T1>(v2 + v3);
}

void  testSum(){
	int a =1;
	char b = 2;
	float f = 3.3f;
	//a = sum<int,char,float>(b,f);
	a = sum<int>(b,f);
	cout<<"a="<<a<<endl;
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








