#include <stdio.h>
#include <stdlib.h>
/**
 * ���� 쳲��������� ָ��λ�õ�Ԫ��
 * @param index ָ��λ��.
 * @return base raised to the power exponent.
 */
int FibonacciSequence(int index) {
    if (index < 3) {
        return  1;
    }
    return FibonacciSequence(index - 1) + FibonacciSequence(index - 2);
}


int main(int argc, char *argv[])
{
    if (argc < 2){
        printf("Usage: %s FibonacciSequence index \n", argv[0]);
        return -1;
    }
    int  index  = atof(argv[1]);
    int value = FibonacciSequence(index);

    printf("FibonacciSequence index %d is %d\n", index, value);
    return 0;
}