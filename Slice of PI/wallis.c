#include "mathlib.h"

#include <stdio.h>

static int nw = 1;

/*
double pi_wallis(void);
int pi_wallis_factors(void);
*/

double pi_wallis(void) {

    double factor = 2.0, prod = 1.0;
    double k = 1.0, ksquared;

    while (absolute(1.0 - factor) > EPSILON) {

        ksquared = k * k;
        factor = ksquared / (ksquared - 0.25);

        // print("term: %20.f\n", factor);

        prod = prod * factor;

        k = k + 1.0;

        // printf("%.20f\n", k);

        nw = nw + 1;
    }

    return (2.0 * prod);
}

int pi_wallis_factors(void) {

    return nw;
}
