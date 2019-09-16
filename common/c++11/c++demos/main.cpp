#include <stdio.h>
#include <stdlib.h>

#include  "mychrono.h"
#include  "my_debug_helper.h"




int main(int argc, char *argv[])
{
    if (argc < 2){
        printf("Usage: %s FibonacciSequence index \n", argv[0]);
        return -1;
    }
    int  index  = atoi(argv[1]);
    int value = FibonacciSequence(index);

    //printf("FibonacciSequence index %d is %d\n", index, value);

    debug_helper_main(argc, argv);
    return 0;
}