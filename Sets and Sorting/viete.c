#include "mathlib.h"

#include <stdio.h>

static int nv = 1;

/*
double pi_viete(void);
int pi_viete_factors(void);
*/

double pi_viete(void) {

    double factor = 2.0, prod = 1.0;
    double a = sqrt_newton(2);

    while (absolute(1.0 - factor) > EPSILON) {

        factor = a / 2.0;

        // print("term: %20.f\n", factor);

        prod = prod * factor;

        a = sqrt_newton(2 + a);

        // printf("%.20f\n", a);

        nv = nv + 1;
    }

    return (2.0 / prod);
}

int pi_viete_factors(void) {

    return nv;
}
