// #include "shell.h"

#include "gaps.h"
#include "stats.h"

void shell_sort(Stats *stats, uint32_t *A, uint32_t n) {
    for (int g = 0; g < GAPS; g++) {
        uint32_t gap = gaps[g];
        uint32_t i, j, temp;
        for (i = gap; i < n; i++) {
            temp = A[i];
            move(stats, A[i]);
            j = i;
            while (j >= gap && cmp(stats, A[j - gap], temp) > 0) {
                A[j] = move(stats, A[j - gap]);
                j -= gap;
            }
            A[j] = move(stats, temp);
        }
    }
}
