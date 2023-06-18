#include "insert.h"

void insertion_sort(Stats *stats, uint32_t *arr, uint32_t length) {
    uint32_t j;
    uint32_t temp;
    for (uint32_t i = 1; i < length; i++) {
        j = i;
        temp = move(stats, arr[i]);
        while (j > 0 && cmp(stats, temp, arr[j - 1]) < 0) {
            arr[j] = move(stats, arr[j - 1]);
            j = j - 1;
        }
        arr[j] = move(stats, temp);
    }
}
