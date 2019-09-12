



chrono是一个time library, 源于boost，现在已经是C++标准。



　　要使用chrono库，需要#include<chrono>，其所有实现均在std::chrono namespace下。

注意标准库里面的每个命名空间代表了一个独立的概念。所以下文中的概念均以命名空间的名字表示！ 

chrono是一个模版库，使用简单，功能强大，只需要理解三个概念：

duration、time_point、clock



chrono 库主要包含了三种类型：时间间隔 Duration、时钟 Clocks 和时间点 Time point



## 应用示例



### 获取当前时间戳



```c++
std::time_t getTimeStamp()
{
    std::chrono::time_point<std::chrono::system_clock,std::chrono::milliseconds> tp = std::chrono::time_point_cast<std::chrono::milliseconds>(std::chrono::system_clock::now());
    auto tmp=std::chrono::duration_cast<std::chrono::milliseconds>(tp.time_since_epoch());
    std::time_t timestamp = tmp.count();
    //std::time_t timestamp = std::chrono::system_clock::to_time_t(tp);
    return timestamp;
}


//时间戳转日期
std::tm* gettm(int64 timestamp)
{
    int64 milli = timestamp+ (int64)8*60*60*1000;//此处转化为东八区北京时间，如果是其它时区需要按需求修改
    auto mTime = std::chrono::milliseconds(milli);
    auto tp=std::chrono::time_point<std::chrono::system_clock,std::chrono::milliseconds>(mTime);
    auto tt = std::chrono::system_clock::to_time_t(tp);
    std::tm* now = std::gmtime(&tt);
    printf("%4d年%02d月%02d日 %02d:%02d:%02d\n",now->tm_year+1900,now->tm_mon+1,now->tm_mday,now->tm_hour,now->tm_min,now->tm_sec);
   return now;
}

```







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

