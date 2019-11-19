



```
 int* p = new (std::nothrow) int; // 这样如果 new 失败了，就不会抛出异常，而是返回空指针
 if ( p == 0 ) // 如此这般，这个判断就有意义了
 return -1;
 // 其它代码
```





首先按c++标准的话，new失败会抛出bad_alloc异常，但是有些编译器对c++标准支持不是很好，比如vc++6.0中new失败不会抛出异常，而返回0.

//标准推荐做法一。

```
try
{
    double *ptr=new double[1000000];
}
catch(bad_alloc &memExp)
{
    //失败以后，要么abort要么重分配
    cerr<<memExp.what()<<endl;
}

```





## 参考链接

1. [C++ new失败的处理](https://www.cnblogs.com/avril/p/3175175.html)