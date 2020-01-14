

### 简介

```ini
/* 介绍<chrono>
*    一个精确中立的时间和日期库
* 时钟:
*
* std::chrono::system_clock:  依据系统的当前时间 (不稳定)
* std::chrono::steady_clock:  以统一的速率运行(不能被调整)
* std::chrono::high_resolution_clock: 提供最小可能的滴答周期
*                   (可能是steady_clock或者system_clock的typedef)
*
* std:ratio<>表示时钟周期，即时间的计量单位
*/
```





### 使用的头文件

```
#include <chrono>
```



### monotonic_to_realtime

用于绝对是件到相对时间的转换。

- CLOCK_MONOTONIC：以绝对时间为准，获取的时间为系统重启到现在的时间，更改系统时间对它没有影响。
- CLOCK_REALTIME：相对时间，从1970.1.1到目前的时间。更改系统时间会更改获取的值。它以系统时间为坐标。

```c++
double librealsense::monotonic_to_realtime(double monotonic)
{
    auto realtime = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch()).count();
    auto time_since_epoch = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now().time_since_epoch()).count();
    return monotonic + (realtime - time_since_epoch);
}
```



### GetTimeMillisecondsStamp()

```
// 获取毫秒时间戳
int64_t GetTimeMillisecondsStamp() {
    auto time_now = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch());
    return time_now.count();
}
```

