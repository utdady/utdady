#include "mathlib.h"

#include <stdio.h>

static int nb = 1;

/*
double pi_bbp(void);
int pi_bbp_terms(void);
*/

double pi_bbp(void) {

    double term = 1.0, sum = 0.0;
    double sixteen_to_the_k = 1.0, k = 0.0;
    double left, right;

    while (absolute(term) > EPSILON) {

        left = 1.0 / sixteen_to_the_k;
        right = (4.0 / ((8.0 * k) + 1.0)) - (2.0 / ((8.0 * k) + 4.0)) - (1.0 / ((8.0 * k) + 5.0))
                - (1.0 / ((8.0 * k) + 6.0));
        term = left * right;

        // print("term: %20.f\n", term);

        sum = sum + term;

        sixteen_to_the_k = sixteen_to_the_k * 16;
        k = k + 1;

        // printf("%.20f, %.20f\n", sixteen_to_the_k, k);

        nb = nb + 1;
    }

    return (sum);
}

int pi_bbp_terms(void) {

    return nb;
}
