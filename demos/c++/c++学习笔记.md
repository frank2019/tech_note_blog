

### c++学习的几个阶段

#### step1

1. 熟悉基本语法
2. 熟悉常用的工具  spacemacs   makefile  g++
3. 熟悉基本的概念



参考链接：

1. [C++ 教程](http://www.runoob.com/cplusplus/cpp-data-types.html)



### 0x04  c++ 面向对象



http://www.runoob.com/cplusplus/cpp-interfaces.html

### 0x03 C++  常用接口函数

#### C++ 万能头文件

```c++
#include<bits/stdc++.h> 
```



#### 数学运算

1. 引用数学头文件 ‘ <cmath>’

#### 字符串操作

1.  c风格字符串操作  <cstring>
2.  c++ 的 string 类  <string>



#### 日期 & 时间

1. C++ 标准库没有提供所谓的日期类型。

2. C++ 继承了 C 语言用于日期和时间操作的结构和函数。为了使用日期和时间相关的函数和结构，需要在 C++ 程序中引用 <ctime> 头文件。

3. 有四个与时间相关的类型：**clock_t、time_t、size_t** 和 **tm**。类型 clock_t、size_t 和 time_t 能够把系统时间和日期表示为某种整数。

4. 结构类型 **tm** 把日期和时间以 C 结构的形式保存，tm 结构的定义如下：

   ```c++
   
   struct tm {
     int tm_sec;   // 秒，正常范围从 0 到 59，但允许至 61
     int tm_min;   // 分，范围从 0 到 59
     int tm_hour;  // 小时，范围从 0 到 23
     int tm_mday;  // 一月中的第几天，范围从 1 到 31
     int tm_mon;   // 月，范围从 0 到 11
     int tm_year;  // 自 1900 年起的年数
     int tm_wday;  // 一周中的第几天，范围从 0 到 6，从星期日算起
     int tm_yday;  // 一年中的第几天，范围从 0 到 365，从 1 月 1 日算起
     int tm_isdst; // 夏令时
   }
   
   ```


5.  C/C++ 中关于日期和时间的重要函数

| 序号 | 函数 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | [**time_t time(time_t \*time);**](http://www.runoob.com/cplusplus/c-function-time.html) 该函数返回系统的当前日历时间，自 1970 年 1 月 1 日以来经过的秒数。如果系统没有时间，则返回 .1。 |
| 2    | [**char \*ctime(const time_t *time);**](http://www.runoob.com/cplusplus/c-function-ctime.html) 该返回一个表示当地时间的字符串指针，字符串形式 *day month year hours:minutes:seconds year\n\0*。 |
| 3    | [**struct tm \*localtime(const time_t *time);**](http://www.runoob.com/cplusplus/c-function-localtime.html) 该函数返回一个指向表示本地时间的 **tm** 结构的指针。 |
| 4    | [**clock_t clock(void);**](http://www.runoob.com/cplusplus/c-function-clock.html) 该函数返回程序执行起（一般为程序的开头），处理器时钟所使用的时间。如果时间不可用，则返回 .1。 |
| 5    | [**char \* asctime ( const struct tm * time );**](http://www.runoob.com/cplusplus/c-function-asctime.html) 该函数返回一个指向字符串的指针，字符串包含了 time 所指向结构中存储的信息，返回形式为：day month date hours:minutes:seconds year\n\0。 |
| 6    | [**struct tm \*gmtime(const time_t *time);**](http://www.runoob.com/cplusplus/c-function-gmtime.html) 该函数返回一个指向 time 的指针，time 为 tm 结构，用协调世界时（UTC）也被称为格林尼治标准时间（GMT）表示。 |
| 7    | [**time_t mktime(struct tm \*time);**](http://www.runoob.com/cplusplus/c-function-mktime.html) 该函数返回日历时间，相当于 time 所指向结构中存储的时间。 |
| 8    | [**double difftime ( time_t time2, time_t time1 );**](http://www.runoob.com/cplusplus/c-function-difftime.html) 该函数返回 time1 和 time2 之间相差的秒数。 |
| 9    | [**size_t strftime();**](http://www.runoob.com/cplusplus/c-function-strftime.html) 该函数可用于格式化日期和时间为指定的格式。 |



##### demo

```c++

#include <iostream>
#include <ctime>
 
using namespace std;
 
int main( )
{
   // 基于当前系统的当前日期/时间
   time_t now = time(0);
   
   // 把 now 转换为字符串形式
   char* dt = ctime(&now);
 
   cout << "本地日期和时间：" << dt << endl;
 
   // 把 now 转换为 tm 结构
   tm *gmtm = gmtime(&now);
   dt = asctime(gmtm);
   cout << "UTC 日期和时间："<< dt << endl;
}


int main2( )
{
   // 基于当前系统的当前日期/时间
   time_t now = time(0);
 
   cout << "1970 到目前经过秒数:" << now << endl;
 
   tm *ltm = localtime(&now);
 
   // 输出 tm 结构的各个组成部分
   cout << "年: "<< 1900 + ltm->tm_year << endl;
   cout << "月: "<< 1 + ltm->tm_mon<< endl;
   cout << "日: "<<  ltm->tm_mday << endl;
   cout << "时间: "<< ltm->tm_hour << ":";
   cout << ltm->tm_min << ":";
   cout << ltm->tm_sec << endl;
}
```



#### 基本的输入输出

1. C++ 标准库提供了一组丰富的输入/输出功能

2. C++ 的 I/O 发生在流中，流是字节序列。如果字节流是从设备（如键盘、磁盘驱动器、网络连接等）流向内存，这叫做**输入操作**。

3. 如果字节流是从内存流向设备（如显示屏、打印机、磁盘驱动器、网络连接等），这叫做**输出操作**。

##### I/O 库头文件

| 头文件     | 函数和描述                                                   |
| ---------- | ------------------------------------------------------------ |
| <iostream> | 该文件定义了 **cin、cout、cerr** 和 **clog** 对象，分别对应于标准输入流、标准输出流、非缓冲标准错误流和缓冲标准错误流。 |
| <iomanip>  | 该文件通过所谓的参数化的流操纵器（比如 **setw** 和 **setprecision**），来声明对执行标准化 I/O 有用的服务。 |
| <fstream>  | 该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。 |



1. 预定义的对象 **cout** 是 **iostream** 类的一个实例。cout 对象"连接"到标准输出设备，通常是显示屏。**cout** 是与流插入运算符 << 结合使用的。
2. 预定义的对象 **cin** 是 **iostream** 类的一个实例。cin 对象附属到标准输入设备，通常是键盘。**cin** 是与流提取运算符 >> 结合使用的
3. C++ 编译器根据要输入值的数据类型，选择合适的流提取运算符来提取值，并把它存储在给定的变量中。
4. 预定义的对象 **cerr** 是 **iostream** 类的一个实例。cerr 对象附属到标准错误设备，通常也是显示屏，但是 **cerr** 对象是非缓冲的，且每个流插入到 cerr 都会立即输出。
5. 预定义的对象 **clog** 是 **iostream** 类的一个实例。clog 对象附属到标准错误设备，通常也是显示屏，但是 **clog** 对象是缓冲的。这意味着每个流插入到 clog 都会先存储在缓冲在，直到缓冲填满或者缓冲区刷新时才会输出。 **clog** 也是与流插入运算符 << 结合使用的
6. 



```c++
#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
    cout<<setiosflags(ios::left|ios::showpoint);  // 设左对齐，以一般实数方式显示
    cout.precision(5);       // 设置除小数点外有五位有效数字 
    cout<<123.456789<<endl;
    cout.width(10);          // 设置显示域宽10 
    cout.fill('*');          // 在显示区域空白处用*填充
    cout<<resetiosflags(ios::left);  // 清除状态左对齐
    cout<<setiosflags(ios::right);   // 设置右对齐
    cout<<123.456789<<endl;
    cout<<setiosflags(ios::left|ios::fixed);    // 设左对齐，以固定小数位显示
    cout.precision(3);    // 设置实数显示三位小数
    cout<<999.123456<<endl; 
    cout<<resetiosflags(ios::left|ios::fixed);  //清除状态左对齐和定点格式
    cout<<setiosflags(ios::left|ios::scientific);    //设置左对齐，以科学技术法显示 
    cout.precision(3);   //设置保留三位小数
    cout<<123.45678<<endl;
    return 0; 
}
```









### 0x02 C++基本语法

#### 类型存储限定符const ，volatile，restrict

类型限定符提供了变量的额外信息。

| 限定符   | 含义                                                         |
| -------- | ------------------------------------------------------------ |
| const    | **const** 类型的对象在程序执行期间不能被修改改变。           |
| volatile | 修饰符 **volatile** 告诉编译器不需要优化volatile声明的变量，让程序可以直接从内存中读取变量。对于一般的变量编译器会对变量进行优化，将内存中的变量值放在寄存器中以加快读写效率。 |
| restrict | 其实restrict同const或valiate一样是一个修饰符而已，告诉编译器被restrict修饰的指针所指 ，向的对象，只能通过这个指针或基于这个指针的其他指针进行操作，即限制访问用restrict限制的指针指向的对象只能通过这个指针访问，这对编译器的优
化很有好处。 |



#### const关键字的使用

const 是constant的缩写，“恒定不变”的意思。被const修饰的东西都受到强制保护，可以预防意外的变动，能提高程序的健壮性。所以很多C++程序设计书籍建议：“Useconst whenever you need”。

##### 用const修饰变量  

不管是参变量还是变量 表名其不可被修改。

1. 用const修饰函数的参数，表示改参数是输入参数，不可被修改。

2. 对于非内置数据类型的输入参数，应该将“值传递”的方式改为“const引用传递”，目的是提高效率。例如将voidFunc(A a) 改为voidFunc(const A &a)。


##### 用const修饰函数的返回值

1. 函数返回值（即指针）的内容不能被修改，该返回值只能被赋给加const修饰的同类型指针
2. 如果函数返回值采用“值传递方式”，由于函数会把返回值复制到外部临时的存储单元中，加const修饰没有任何价值。

##### const 成员函数

1. 在类中定义 ： intGetCount(void) const; // const 成员函数
2. 任何不会修改数据成员的函数都应该声明为const类型。如果在编写const成员函数时，不慎修改了数据成员，或者调用了其它非const成员函数，编译器将指出错误，这无疑会提高程序的健壮性
3. const对象只能访问const成员函数,而非const对象可以访问任意的成员函数,包括const成员函数.
4. const对象的成员是不可修改的,然而const对象通过指针维护的对象却是可以修改的.
5. const成员函数不可以修改对象的数据,不管对象是否具有const性质.它在编译时,以是否修改成员数据为依据,进行检查.
6. 然而加上mutable修饰符的数据成员,对于任何情况下通过任何手段都可修改,此时的const成员函数是可以修改它的



#### C++ 存储类

存储类定义 C++ 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。

1. 从 C++ 11 开始，auto 关键字不再是 C++ 存储类说明符，且 register 关键字被弃用。
2. 存储修饰符关键字 auto ， register， static ，extern ，mutable，thread_local (C++11)
3.  auto  声明变量时根据初始化表达式自动推断该变量的类型、声明函数时函数返回值的占位符。
4. **register** 存储类用于定义存储在寄存器中而不是 RAM 中的局部变量
5. static 修饰符也可以应用于全局变量。当 static 修饰全局变量时，会使变量的作用域限制在声明它的文件内。
6. 在 C++ 中，当 static 用在类数据成员上时，会导致仅有一个该成员的副本被类的所有对象共享。
7. extern  用于声明 该变量在其他文件中已经定义，本文件不需要分配直接使用即可。
8. thread_local   使用 thread_local 说明符声明的变量仅可在它在其上创建的线程上访问。 变量在创建线程时创建，并在销毁线程时销毁。 每个线程都有其自己的变量副本。
9. thread_local 说明符可以与 static 或 extern 合并。可以将 thread_local 仅应用于数据声明和定义，thread_local 不能用于函数声明或定义。
10. **mutable** 说明符仅适用于类的对象
11. 在c++的类中， 如果一个成员函数被const 修饰，那么它将无法修改其成员变量的，但是如果这个成员变量是被mutable修饰的话，则可以修改



#### C++ 中的引用与指针

1. 引用变量是一个别名，也就是说，它是某个已存在变量的另一个名字。一旦把引用初始化为某个变量，就可以使用该引用名称或变量名称来指向变量

2. 不存在空引用。引用必须连接到一块合法的内存。

3. 一旦引用被初始化为一个对象，就不能被指向到另一个对象。指针可以在任何时候指向到另一个对象

4. 引用必须在创建时被初始化。指针可以在任何时间被初始化。

5. C++ 支持把引用作为参数传给函数，这比传一般的参数更安全。

6. 可以从 C++ 函数中返回引用，就像返回其他数据类型一样。

7. 引用的定义 ：

   ```c++
      // 声明简单的变量
      int    i;
      double d;
    
      // 声明引用变量
      int&    r = i;
      double& s = d;
   ```

8. **引用是除指针外另一个可以产生多态效果的手段。这意味着，一个基类的引用可以指向它的派生类实例。**

9. 在引用的使用中，单纯给某个变量取个别名是毫无意义的，**引用的目的主要用于在函数参数传递中，解决大块数据或对象的传递效率和空间不如意的问题。**

10. **用引用传递函数的参数，能保证参数传递中不产生副本，提高传递的效率，且通过const的使用，保证了引用传递的安全性。**

11. **引用与指针的区别是，指针通过某个指针变量指向一个对象后，对它所指向的变量间接操作。程序中使用指针，程序的可读性差；而引用本身就是目标变量的别名，对引用的操作就是对目标变量的操作。**

12. **使用引用的时机。流操作符<<和>>、赋值操作符=的返回值、拷贝构造函数的参数、赋值操作符=的参数、其它情况都推荐使用引用。**



### 0x01  helloworld 用于测试环境

