



### 1，restrict修饰符

```c++
int pthread_create（pthread_t * restrict thread,const pthread_attr_t *restrictattr,void *(*start_routine)(void*),void*restrict arg）;
```



#### 作用

restrict的定义是It can be applied only to pointers, and it indicates that a pointer is the sole initial means of accessing a data object.

restrict是一个限定符，这个关键字据说来源于古老的FORTRAN，主要用来修饰指针指向的内存不能被别的指针引用。
restrict同样可以用于数组的声明：

If you specify type qualifiers such as void foo(int * restrict a);, the C compiler expresses it with array syntax void foo(int a[restrict]); which is essentially the same as declaring a restricted pointer.

其实restrict同const或valiate一样是一个修饰符而已，告诉编译器被restrict修饰的指针所指 向的对象，只能通过这个指针或基于这个指针的其他指针进行操作，即限制访问用restrict限制的指针指向的对象只能通过这个指针访问，这对编译器的优 化很有好处。

#### vs 和 gcc上的差异

gcc上直接使用： restrict

vs2015:  使用__restrict

```c++
int *__restrict a=（int *)mallco(sieof(int)*size);
```

