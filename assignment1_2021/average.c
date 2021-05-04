#include <stdio.h>


double average(int n, double arr[]) {
    double acc = 0.0;

    for (int i = 0; i < n; i++) {
        acc += arr[i];
    }

    return acc / n;
}
