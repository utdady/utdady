#include "mathlib.h"

#include <math.h>
#include <stdio.h>
#include <unistd.h>

#define OPTIONS "aebmrvwnsh"

double pi = M_PI;
double ee = M_E;

int main(int argc, char **argv) {

    int opt = 0;
    int a = 0, ie = 0, b = 0, m = 0, r = 0, v = 0, w = 0, n = 0, s = 0, h = 0;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {

        switch (opt) {

        case 'a': a = 1; break;

        case 'e': ie = 1; break;

        case 'b': b = 1; break;

        case 'm': m = 1; break;

        case 'r': r = 1; break;

        case 'v': v = 1; break;

        case 'w': w = 1; break;

        case 'n': n = 1; break;

        case 's': s = 1; break;

        case 'h': h = 1; break;

        default: h = 1; break;
        }
    }

    if (argv[1] == NULL) {
        h = 1;
    }

    if ((s == 1) && (a == 0) && (ie == 0) && (b == 0) && (m == 0) && (r == 0) && (v == 0)
        && (w == 0) && (n == 0)) {
        h = 1;
    }

    if (h) {
        printf("Usage: %s\n", argv[0]);
        printf("Options:\n");
        printf("-a: Run all the tests\n");
        printf("-b: Calculate pi using the Bailey-Borwein-Plouffe method\n");
        printf("-m: Calculate pi using the Madhava method\n");
        printf("-r: Calculate pi using the Euler method\n");
        printf("-v: Calculate pi using the Viete method\n");
        printf("-w: Calculate pi using the Wallis method\n");
        printf("-n: Calculate the square root using the Newton method\n");
        printf("-s: Display the number of terms\n");
        printf("-e: Approximate e using Taylor Series\n");
        printf("-h: Display this help message\n");

        a = 0, ie = 0, b = 0, m = 0, r = 0, v = 0, w = 0, n = 0, s = 0;
    }

    if (a) {
        ie = 1, b = 1, m = 1, r = 1, v = 1, w = 1, n = 1;
    }

    if (ie) {
        double eval = e();
        int eterms = e_terms();

        printf("e() = %16.15lf, M_E = %16.15lf, diff = %16.15lf\n", eval, ee, ee - eval);
        if (s) {
            printf("e() terms = %d\n", eterms);
        }
    }

    if (b) {
        double bval = pi_bbp();
        int bterms = pi_bbp_terms();

        printf("pi_bbp() = %16.15lf, M_PI = %16.15lf, diff = %16.15lf\n", bval, pi, pi - bval);
        if (s) {
            printf("pi_bbp() terms = %d\n", bterms);
        }
    }

    if (m) {
        double mval = pi_madhava();
        int mterms = pi_madhava_terms();

        printf("pi_madhava() = %16.15lf, M_PI = %16.15lf, diff = %16.15lf\n", mval, pi, pi - mval);
        if (s) {
            printf("pi_madhava() terms = %d\n", mterms);
        }
    }

    if (r) {
        double rval = pi_euler();
        int rterms = pi_euler_terms();

        printf("pi_euler() = %16.15lf, M_PI = %16.15lf, diff = %16.15lf\n", rval, pi, pi - rval);
        if (s) {
            printf("pi_euler() terms = %d\n", rterms);
        }
    }

    if (v) {
        double vval = pi_viete();
        int vterms = pi_viete_factors();

        printf("pi_viete() = %16.15lf, M_PI = %16.15lf, diff = %16.15lf\n", vval, pi, pi - vval);
        if (s) {
            printf("pi_viete() terms = %d\n", vterms);
        }
    }

    if (w) {
        double wval = pi_wallis();
        int wterms = pi_wallis_factors();

        printf("pi_wallis() = %16.15lf, M_PI = %16.15lf, diff = %16.15lf\n", wval, pi, pi - wval);
        if (s) {
            printf("pi_wallis() terms = %d\n", wterms);
        }
    }

    if (n) {
        for (double i = 0.0; i < 9.95; i = i + 0.1) {
            printf("sqrt_newton(%.2lf) = %16.15lf, sqrt(%.2lf) = %16.15lf, diff = %16.15lf\n", i,
                sqrt_newton(i), i, sqrt(i), sqrt(i) - sqrt_newton(i));
            if (s) {
                printf("sqrt_newton() terms = %d\n", sqrt_newton_iters());
            }
        }
    }

    return 0;
}
