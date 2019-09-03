#include <stdio.h>
#include <stdlib.h>

#include  "mymath.h"



int main(int argc, char *argv[])
{
    if (argc < 2){
        printf("Usage: %s FibonacciSequence index \n", argv[0]);
        return -1;
    }
    int  index  = atoi(argv[1]);
    int value = FibonacciSequence(index);

    printf("FibonacciSequence index %d is %d\n", index, value);
    return 0;
}