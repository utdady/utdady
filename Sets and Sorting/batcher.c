#include "batcher.h"

#include "stats.h"

#include <math.h>

void comparator(Stats *stats, uint32_t *A, int x, int y) {
    if (cmp(stats, A[y], A[x]) < 0) {
        swap(stats, &A[x], &A[y]);
    }
}

void batcher_sort(Stats *stats, uint32_t *A, uint32_t n) {
    if (n == 0) {
        return;
    }

    uint32_t t = (uint32_t) (log2(n) + 1);
    uint32_t p = 1 << (t - 1);

    while (p > 0) {
        uint32_t q = 1 << (t - 1);
        uint32_t r = 0;
        uint32_t d = p;
        while (d > 0) {
            for (uint32_t i = 0; i < (n - d); i++) {
                if ((i & p) == r) {
                    comparator(stats, A, i, i + d);
                }
            }
            d = q - p;
            q >>= 1;
            r = p;
        }
        p >>= 1;
    }
}
