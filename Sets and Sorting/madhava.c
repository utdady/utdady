#include "mathlib.h"

#include <stdio.h>

static int nm = 1;

/*
double pi_madhava(void);
int pi_madhava_terms(void);
*/

double pi_madhava(void) {

    double term = 1.0, sum = 0.0;
    double sign = -1.0, three_to_the_k = 3.0, den = 3.0;
    while (absolute(term) > EPSILON) {
        term = sign / (three_to_the_k * den);
        // print("term: %20.f\n", term);

        sum = sum + term;

        den = den + 2.0;
        three_to_the_k = three_to_the_k * 3.0;
        sign = sign * (-1.0);

        // printf("%.20f, %.20f, %.20f\n", three_to_the_k, den, sign);

        nm = nm + 1;
    }

    return ((sum + 1.0) * sqrt_newton(12));
}

int pi_madhava_terms(void) {

    return nm;
}
