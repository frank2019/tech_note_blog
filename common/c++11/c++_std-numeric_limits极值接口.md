>
>
>言者无罪，闻者足戒。  --诗经·大序

# std::numeric_limits

在C/C++11中，std::numeric_limits为模板类，在库编译平台提供基础算术类型的极值等属性信息。

用于取代<climits>和<limits.h>,浮点常数定义于<cfloat>和<float.h>。

## 新的极值概念有两个优点，

- 一是提供了更好的类型安全性，

- 二是程序员可借此写出一些template以核定这些极值。



## member



| member            | type                                                         | property                                                     |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| is_specialized    | `bool`                                                       | `true` for all [arithmetic types](http://www.cplusplus.com/is_arithmetic) (i.e., those for which numeric_limits is specialized).  `false` for all other types. |
| min()             | T                                                            | Minimum finite value.  For floating types with denormalization (variable number of exponent bits): minimum positive normalized value.  Equivalent to [CHAR_MIN](http://www.cplusplus.com/climits), [SCHAR_MIN](http://www.cplusplus.com/climits), [SHRT_MIN](http://www.cplusplus.com/climits), [INT_MIN](http://www.cplusplus.com/climits), [LONG_MIN](http://www.cplusplus.com/climits), [LLONG_MIN](http://www.cplusplus.com/climits), [FLT_MIN](http://www.cplusplus.com/cfloat), [DBL_MIN](http://www.cplusplus.com/cfloat), [LDBL_MIN](http://www.cplusplus.com/cfloat) or `0`, depending on type. |
| max()             | T                                                            | Maximum finite value.  Equivalent to [CHAR_MAX](http://www.cplusplus.com/climits), [SCHAR_MAX](http://www.cplusplus.com/climits), [UCHAR_MAX](http://www.cplusplus.com/climits), [SHRT_MAX](http://www.cplusplus.com/climits), [USHRT_MAX](http://www.cplusplus.com/climits), [INT_MAX](http://www.cplusplus.com/climits), [UINT_MAX](http://www.cplusplus.com/climits), [LONG_MAX](http://www.cplusplus.com/climits), [ULONG_MAX](http://www.cplusplus.com/climits), [LLONG_MAX](http://www.cplusplus.com/climits), [ULLONG_MAX](http://www.cplusplus.com/climits), [UINT_LEAST16_MAX](http://www.cplusplus.com/cstdint), [UINT_LEAST32_MAX](http://www.cplusplus.com/cstdint), [FLT_MAX](http://www.cplusplus.com/cfloat), [DBL_MAX](http://www.cplusplus.com/cfloat) or [LDBL_MAX](http://www.cplusplus.com/cfloat), depending on type. |
| lowest()          | T                                                            | Minimum finite value. (since C++11)  For integral types: the same as min().  For floating-point types: implementation-dependent; generally, the negative of max(). |
| digits            | int                                                          | For integer types: number of non-sign bits (radix base digits) in the representation.  For floating types: number of digits (in radix base) in the mantissa (equivalent to [FLT_MANT_DIG](http://www.cplusplus.com/cfloat), [DBL_MANT_DIG](http://www.cplusplus.com/cfloat) or [LDBL_MANT_DIG](http://www.cplusplus.com/cfloat)). |
| digits10          | `int`                                                        | Number of digits (in decimal base) that can be represented without change.  Equivalent to [FLT_DIG](http://www.cplusplus.com/cfloat), [DBL_DIG](http://www.cplusplus.com/cfloat) or [LDBL_DIG](http://www.cplusplus.com/cfloat) for floating types. |
| max_digits10      | `int`                                                        | Number of digits (in decimal base) required to ensure that values that differ are always differentiated. |
| is_signed         | `bool`                                                       | `true` if type is signed.                                    |
| is_integer        | `bool`                                                       | 测试目标类型是不是可以用整型来表示（比如char是1，float是0    |
| is_exact          | `bool`                                                       | `true` if type uses exact representations.                   |
| radix             | `int`                                                        | For integer types: base of the representation.  For floating types: base of the exponent of the representation (equivalent to [FLT_RADIX](http://www.cplusplus.com/cfloat)). |
| epsilon()         | T                                                            | 返回目标数据类型能表示的最逼近1的正数和1的差的绝对值         |
| round_error()     | T                                                            | Measure of the maximum rounding error.                       |
| min_exponent      | `int`                                                        | Minimum negative integer value such that radix raised to `(min_exponent-1)` generates a normalized floating-point number.  Equivalent to [FLT_MIN_EXP](http://www.cplusplus.com/cfloat), [DBL_MIN_EXP](http://www.cplusplus.com/cfloat) or [LDBL_MIN_EXP](http://www.cplusplus.com/cfloat) for floating types. |
| min_exponent10    | `int`                                                        | Minimum negative integer value such that 10 raised to that power generates a normalized floating-point number.  Equivalent to [FLT_MIN_10_EXP](http://www.cplusplus.com/cfloat), [DBL_MIN_10_EXP](http://www.cplusplus.com/cfloat) or [LDBL_MIN_10_EXP](http://www.cplusplus.com/cfloat) for floating types. |
| max_exponent      | `int`                                                        | Maximum integer value such that radix raised to `(max_exponent-1)` generates a representable finite floating-point number.  Equivalent to [FLT_MAX_EXP](http://www.cplusplus.com/cfloat), [DBL_MAX_EXP](http://www.cplusplus.com/cfloat) or [LDBL_MAX_EXP](http://www.cplusplus.com/cfloat) for floating types. |
| max_exponent10    | `int`                                                        | Maximum integer value such that 10 raised to that power generates a normalized finite floating-point number.  Equivalent to [FLT_MAX_10_EXP](http://www.cplusplus.com/cfloat), [DBL_MAX_10_EXP](http://www.cplusplus.com/cfloat) or [LDBL_MAX_10_EXP](http://www.cplusplus.com/cfloat) for floating types. |
| has_infinity      | `bool`                                                       | `true` if the type has a representation for positive infinity. |
| has_quiet_NaN     | `bool`                                                       | `true` if the type has a representation for a quiet (non-signaling) "Not-a-Number". |
| has_signaling_NaN | `bool`                                                       | `true` if the type has a representation for a signaling "Not-a-Number". |
| has_denorm        | [float_denorm_style](http://www.cplusplus.com/float_denorm_style) | 测试目标类型是不是可以非规范化表示                           |
| has_denorm_loss   | `bool`                                                       | 测试所有类型是不是能测出因为非规范化而造成的精度损失（不是因为结果本身的不精确） |
| infinity()        | T                                                            | 检查目标类型的无限类型（如果支持无限表示）                   |
| quiet_NaN()       | T                                                            | Representation of *quiet* (non-signaling) *"Not-a-Number"*, if available. |
| signaling_NaN()   | T                                                            | Representation of *signaling "Not-a-Number"*, if available.  |
| denorm_min()      | T                                                            | Minimum positive denormalized value.  For types not allowing denormalized values: same as `min()`. |
| is_iec559         | `bool`                                                       | 测试目标类型是不是符合IEC559标准                             |
| is_bounded        | `bool`                                                       | 检查目标类型的取值是否有限                                   |
| is_modulo         | `bool`                                                       | `true` if the type is modulo. A type is *modulo* if it is possible to add two positive numbers and have a result that wraps around to a third number that is less. |
| traps             | `bool`                                                       | `true` if trapping is implemented for the type.              |
| tinyness_before   | `bool`                                                       | `true` if tinyness is detected before rounding.              |
| round_style       | [float_round_style](http://www.cplusplus.com/float_round_style) | Rounding style. A type may have any of the following enum values:  [round_toward_zero](http://www.cplusplus.com/float_round_style), if it rounds toward zero.  [round_to_nearest](http://www.cplusplus.com/float_round_style), if it rounds to the nearest representable value.  [round_toward_infinity](http://www.cplusplus.com/float_round_style), if it rounds toward infinity.  [round_toward_neg_infinity](http://www.cplusplus.com/float_round_style), if it rounds toward negative infinity.  [round_indeterminate](http://www.cplusplus.com/float_round_style), if the rounding style is indeterminable at compile time. |



## sample code



```c++
#include<iostream>  
#include<string>  
#include<limits>   

using namespace std;  
int main(){  
	cout<<"numeric_limits<int>::min()= "<<numeric_limits<int>::min()<<endl;  
	cout<<"numeric_limits<int>::max()= "<<numeric_limits<int>::max()<<endl;  
	cout<<"numeric_limits<short>::min()= "<<numeric_limits<short>::min()<<endl;  
	cout<<"numeric_limits<short>::max()= "<<numeric_limits<short>::max()<<endl;  
	cout<<"numeric_limits<double>::min()= "<<numeric_limits<double>::min()<<endl;  
	cout<<"numeric_limits<double>::max()= "<<numeric_limits<double>::max()<<endl;  

	cout<<"numeric_limits<int>::is_signed()= "<<numeric_limits<int>::is_signed<<endl;//是否有正负号  
	cout<<"numeric_limits<string>::is_specialized()= "<<numeric_limits<string>::is_specialized<< endl;//是否定义了数值极限  
	system("pause");  
	return 0;  
}   
```



# 参考链接

1. [](https://blog.csdn.net/chdhust/article/details/9202941)

