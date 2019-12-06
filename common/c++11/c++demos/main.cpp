#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include "timer.hpp"

#include  "mychrono.h"
#include  "my_debug_helper.h"


void func1()
{
    std::cout << "trigger func1" << std::endl;
}

void func2(int x)
{
    std::cout << "trigger func2, x: " << x << std::endl;
}

int main(int argc, char* argv[])
{
    Timer timer;

    // execute task every timer interval
    std::cout << "--- start period timer ----" << std::endl;
    timer.start(1000, std::bind(func2, 3));
    std::this_thread::sleep_for(std::chrono::milliseconds(5000));
    timer.stop();
    std::cout << "--- stop period timer ----" << std::endl;

    // execute task once after delay
    std::cout << "--- start one shot timer ----" << std::endl;
    timer.startOnce(1000, func1);
    std::cout << "--- stop one shot timer ----" << std::endl;

    getchar();
    return 0;
}





int main2(int argc, char *argv[])
{
    if (argc < 2){
        printf("Usage: %s FibonacciSequence index \n", argv[0]);
        //return -1;
    }


    std::string in1 = "21234568";
    std::string in2 = "87654321";
    std::string sum;

    int ret = BigNumberPlus(in1, in2, &sum);
    if (ret ) {
        printf("BigNumberPlus\n");
        return  0;
    }
    std::cout << "BigNumberPlus:" << std::endl;
    std::cout << in1 << "+" << in2 << " = " << sum << std::endl;
    return  0;


    int  index  = atoi(argv[1]);
    int value = FibonacciSequence(index);

    //printf("FibonacciSequence index %d is %d\n", index, value);

    debug_helper_main(argc, argv);
    return 0;
}