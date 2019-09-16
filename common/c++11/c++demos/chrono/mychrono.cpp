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

#include <chrono>
#include <stdint.h>
#include <time.h>       /* time_t, struct tm, time, gmtime */

#include  "mychrono.h"

/**
 * 返回 斐波那契数列 指定位置的元素
 * @param index 指定位置.
 * @return base raised to the power exponent.
 */
int FibonacciSequence(int index) {
    if (index < 3) {
        return  1;
    }
    return FibonacciSequence(index - 1) + FibonacciSequence(index - 2);
}

// 获取毫秒时间戳
int64_t GetTimeMillisecondsStamp() {
    auto time_now = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::system_clock::now().time_since_epoch());
    return time_now.count();
}



#if 0
//时间戳转日期
std::tm* gettm(int64_t timestamp) {
    int64_t milli = timestamp + (int64_t)8 * 60 * 60 * 1000;//此处转化为东八区北京时间，如果是其它时区需要按需求修改
    auto mTime = std::chrono::milliseconds(milli);
    auto tp = std::chrono::time_point<std::chrono::system_clock, std::chrono::milliseconds>(mTime);
    auto tt = std::chrono::system_clock::to_time_t(tp);
    std::tm* now = gmtime(&tt);
    printf("%4d年%02d月%02d日 %02d:%02d:%02d\n", now->tm_year + 1900, now->tm_mon + 1, now->tm_mday, now->tm_hour, now->tm_min, now->tm_sec);
    return now;
}
#endif
