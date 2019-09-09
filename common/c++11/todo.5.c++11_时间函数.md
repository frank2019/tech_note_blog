

chrono是一个time library, 源于boost，现在已经是C++标准。



　　要使用chrono库，需要#include<chrono>，其所有实现均在std::chrono namespace下。

注意标准库里面的每个命名空间代表了一个独立的概念。所以下文中的概念均以命名空间的名字表示！ 

chrono是一个模版库，使用简单，功能强大，只需要理解三个概念：

duration、time_point、clock





### 线程休眠函数



休眠5秒

```c++
std::this_thread::sleep_for(std::chrono::seconds(5));
```

休眠

```
std::this_thread::sleep_for(std::chrono::milliseconds(100))
```





### 计算时间差

```c++
std::chrono::time_point<std::chrono::high_resolution_clock> stub, last_stub;
stub = std::chrono::high_resolution_clock::now();
//printf("costs %u ms\n", (unsigned)std::chrono::duration_cast<std::chrono::milliseconds>( stub - last_stub).count());
int num = (unsigned)std::chrono::duration_cast<std::chrono::milliseconds>(stub - last_stub).count();
				last_stub = stub;
```

