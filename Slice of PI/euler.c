#include "mathlib.h"

#include <stdio.h>

static int ne = 1;

/*
double pi_euler(void);
int pi_euler_terms(void);
*/

double pi_euler(void) {

    double term = 1.0, sum = 0.0;
    double k = 1.0;
    while (absolute(term) > EPSILON) {
        term = 1.0 / (k * k);
        // print("term: %20.f\n", term);

        sum = sum + term;

        k = k + 1.0;

        // printf("%.20f\n", k);

        ne = ne + 1;
    }

    return (sqrt_newton(6 * sum));
}

int pi_euler_terms(void) {

    return ne;
}
