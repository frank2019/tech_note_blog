# using的三种用法

## 1、命名空间的使用

一般为了代码的冲突，都会用命名空间。例如，对于Android代码会使用Android作为命名空间。

```c++
namespace android;
```

1. 在code中使用的时候可以用android::加具体的类方法。

2. 也可以直接使用

   ```c++
   using namespace android;
   ```

这样可以直接使用 命名空间 android 下的方法 类型 成员


2、在子类中引用基类的成员
--------------------- 
```c++
class T5Base {
public:
    T5Base() :value(55) {}
    virtual ~T5Base() {}
    void test1() { cout << "T5Base test1..." << endl; }
protected:
    int value;
};
 
class T5Derived : private T5Base {
public:
    //using声明只能指定一个名字，不能带形参表，且基类的该函数不能有私有版本，否则编译报错 
    //using父类方法，主要是用来实现可以在子类实例中调用到父类的重载版本  
    //using T5Base::test1;
    //using T5Base::value;
    void test2() { cout << "value is " << value << endl; }
};

/* 
“隐藏”是指派生类的函数屏蔽了与其同名的基类函数，规则如下： 
1、如果派生类的函数与基类的函数同名，但是参数不同。此时，不论有无virtual关键字，基类的函数将被隐藏（注意别与重载混淆） 
2、如果派生类的函数与基类的函数同名，并且参数也相同，但是基类函数没有virtual关键字。此时，基类的函数被隐藏（注意别与覆盖混淆） 
使用了using关键字，就可以避免1的情况，是的父类同名函数在子类中得以重载，不被隐藏 
*/  

```

基类中成员变量value是protected，在private继承之后，对于外界这个值为private，也就是说T5Derived的对象无法使用这个value。

如果想要通过对象使用，需要在public下通过using T5Base::value来引用，这样T5Derived的对象就可以直接使用。

同样的，对于基类中的成员函数test1()，在private继承后变为private，T5Derived的对象同样无法访问，通过using T5Base::test1 就可以使用了。



## **3、别名指定**

在C++11中提出了通过using指定别名

```c++
using value_type = _Ty
```

using  与typedef 的对比

```c++
typedef void (*FP) (int, const std::string&);
```

```c++
using FP = void (*) (int, const std::string&);
```

using可以用作模板别名，这一点 typedef 做不到

```c++
template <typename T>
using Vec = MyVector<T, MyAlloc<T>>;
// usage
Vec<int> vec;
```

**在C++11中，鼓励用using，而不用typedef的**



可参考Effective Modern C++