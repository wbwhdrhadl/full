#include <stdio.h>
#include "libcheckprime.h"

void main() {
        int n;
        while (1) {
        printf("Input number: ");
        scanf("%d", &n);
        if(n == 0) {
            printf("Program Exit~!!\n\n");
            break;
        } else {
            if(checkprime(n) == 0) 
                printf("%d is not prime number\n\n", n);
            else
                printf("%d is prime number\n\n", n);
        }
    }
}