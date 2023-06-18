#include "mathlib.h"

#include <stdio.h>

/*
double sqrt_newton(double x);
int sqrt_newton_iters(void);
*/

// #pragma once

static int nn = 0;

double sqrt_newton(double x) {
    nn = 0;
    double next_y = 1.0;
    double y = 0.0;
    while (absolute(next_y - y) > EPSILON) {
        y = next_y;
        next_y = 0.5 * (y + (x / y));
        nn = nn + 1;
    }

    return next_y;
}

int sqrt_newton_iters(void) {
    return nn;
}
