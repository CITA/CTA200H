#include <stdio.h>
#include "average.h"


int main() {
    double arr[] = {1.0, 2.0, 3.0, 4.0};

    double result = average(4, arr);

    printf("The average of 1, 2, 3 and 4 is: %.4f\n", result);
    return 0;    
}

