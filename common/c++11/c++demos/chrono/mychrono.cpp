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
#include <string>
#include <iostream>

#include  "mychrono.h"
#include  "mz_status.h"

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

bool  IsIntegerNumberStr(std::string& n) {
    //TODO 
    return true;
}


int BigNumberPlus(std::string &in1, std::string &in2, std::string * p_out) {
	if (nullptr == p_out) {
		return  -kMzStatusInputNullPtr;
	}
	if (in1.empty()) {
		*p_out = in2;
		return  0;
	}
	else if (in2.empty()) {
		*p_out = in1;
		return  0;
	}
    if (!IsIntegerNumberStr(in1) || !IsIntegerNumberStr(in2)) {
        return  -kMzStatusInvalid;
    }
    size_t max_length = in1.length() > in2.length() ? (in1.length() + 2) : (in2.length() + 2);
    char* p_sum = new (std::nothrow)char[max_length];
    if (nullptr == p_sum) {
        return  -kMzStatusNoMemory;
    }
    memset(p_sum, 0, max_length);

    std::string* p_long = nullptr, *p_short = nullptr;

    in1.length() > in2.length() ? (p_long = &in1, p_short = &in2) : (p_long = &in2, p_short = &in1);
    int tmp = 0;
    int carry = 0;
    for (int i = 0; i <p_short->length(); i++) {
        tmp = p_long->at(p_long->length()-i-1) - '0' + p_short->at(p_short->length()-i-1) - '0' + carry;
        p_sum[max_length-2-i] = tmp % 10 + '0';
        carry = tmp / 10;
    }
    if (p_long->length() - p_short->length() > 0) {
        for (int i = 0;i< p_long->length() - p_short->length() ;i++) {
            tmp = p_long->at(p_long->length() -  i- 1- p_short->length()) - '0' + carry;
            p_sum[max_length-2-i- p_short->length()] = tmp % 10 + '0';
            carry = tmp / 10;
        }
    }
 
    //if (carry) 
    {
        p_sum[0] = carry + '0';
        
    }
    printf("sum:%s\n", p_sum);
    std::cout << p_sum << std::endl;
    *p_out = p_sum;

    //delete[] p_out;
	return  kMzStatusOK;
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
