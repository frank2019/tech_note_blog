#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

#include  "mychrono.h"
#include  "my_debug_helper.h"




int main(int argc, char *argv[])
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