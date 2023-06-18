#include "mathlib.h"

#include <stdio.h>

static int i = 1;

/*
double e(void);
int e_terms(void);
*/

double e(void) {
    double term = 1.0, sum = 0.0;
    long k = 1;
    while (absolute(term) > EPSILON) {
        term = 1.0 / k;
        sum = sum + term;
        i = i + 1;
        k = k * i;
    }

    return (sum + 1);
}

int e_terms(void) {

    return i;
}
