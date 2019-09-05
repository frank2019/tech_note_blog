#include  "mymath.h"

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