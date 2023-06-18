#include "batcher.h"
#include "heap.h"
#include "insert.h"
#include "quick.h"
#include "shell.h"
#include "stats.h"

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define DEFAULT_SEED 13371453
#define DEFAULT_SIZE 100
#define DEFINE_PRINT 100
#define OPTIONS      "aishqbr:n:p:H"

int main(int argc, char *argv[]) {
    uint32_t seed = DEFAULT_SEED;
    uint32_t size = DEFAULT_SIZE;
    uint32_t print = DEFINE_PRINT;

    uint32_t a = 0, i = 0, s = 0, h = 0, q = 0, b = 0, p = 0, H = 0; //r = 0, n = 0;
    int opt = 0;

    Stats stats;

    while ((opt = getopt(argc, argv, OPTIONS)) != -1) {
        switch (opt) {

        case 'a': a = 1; break;

        case 'i': i = 1; break;

        case 's': s = 1; break;

        case 'h': h = 1; break;

        case 'q': q = 1; break;

        case 'b': b = 1; break;

        case 'r':
            // r = 1;
            if (optarg != NULL) {
                seed = atoi(optarg);
            }
            break;

        case 'n':
            // n = 1;
            if (optarg != NULL) {
                size = atoi(optarg);
            }
            break;

        case 'p':
            p = 1;
            if (optarg != NULL) {
                print = atoi(optarg);
            }
            break;

        case 'H': H = 1; break;

        default: H = 1; break;
        }
    }

    if (argv[1] == NULL) {
        H = 1;
    }

    if (p) {
        if (print > 0) {
            if (print > size) {
                print = size;
            }
        }
    } else {
        print = size;
    }

    srandom(seed);

    uint32_t *arr = malloc(size * sizeof(uint32_t));
    if (arr == NULL) {
        exit(1);
    }

    for (uint32_t i = 0; i < size; i++) {
        arr[i] = rand();
    }

    reset(&stats);

    if (H) {
        printf("SYNOPSIS\n");
        printf("   A collection of comparison-based sorting algorithms.\n\n");

        printf("USAGE\n");
        printf("   ./sorting-x86 [-Hahbsqi] [-n length] [-p elements] [-r seed]\n\n");

        printf("OPTIONS\n");
        printf("   -H              Display program help and usage.\n");
        printf("   -a              Enable all sorts.\n");
        printf("   -h              Enable Heap Sort.\n");
        printf("   -b              Enable Batcher Sort.\n");
        printf("   -s              Enable Shell Sort.\n");
        printf("   -q              Enable Quick Sort.\n");
        printf("   -i              Enable Insertion Sort.\n");
        printf("   -n length       Specify number of array elements (default: 100).\n");
        printf("   -p elements     Specify number of elements to print (default: 100).\n");
        printf("   -r seed         Specify random seed (default: 13371453).\n");
    }

    if (a || i) {
        insertion_sort(&stats, arr, size);
        print_stats(&stats, "Insertion Sort", size);
        if (print) {
            for (uint32_t i = 0; i < print; i++) {
                if (i > 0 && i % 5 == 0)
                    printf("\n");
                printf("%13" PRIu32, arr[i]);
            }
            printf("\n");
        }
        reset(&stats);
    }

    if (a || h) {
        heap_sort(&stats, arr, size);
        print_stats(&stats, "Heap Sort", size);
        if (print) {
            for (uint32_t i = 0; i < print; i++) {
                if (i > 0 && i % 5 == 0)
                    printf("\n");
                printf("%13" PRIu32, arr[i]);
            }
            printf("\n");
        }
        reset(&stats);
    }

    if (a || s) {
        shell_sort(&stats, arr, size);
        print_stats(&stats, "Shell Sort", size);
        if (print) {
            for (uint32_t i = 0; i < print; i++) {
                if (i > 0 && i % 5 == 0)
                    printf("\n");
                printf("%13" PRIu32, arr[i]);
            }
            printf("\n");
        }
        reset(&stats);
    }

    if (a || q) {
        quick_sort(&stats, arr, size);
        print_stats(&stats, "Quick Sort", size);
        if (print) {
            for (uint32_t i = 0; i < print; i++) {
                if (i > 0 && i % 5 == 0)
                    printf("\n");
                printf("%13" PRIu32, arr[i]);
            }
            printf("\n");
        }
        reset(&stats);
    }

    if (a || b) {
        batcher_sort(&stats, arr, size);
        print_stats(&stats, "Batcher Sort", size);
        if (print) {
            for (uint32_t i = 0; i < print; i++) {
                if (i > 0 && i % 5 == 0)
                    printf("\n");
                printf("%13" PRIu32, arr[i]);
            }
            printf("\n");
        }
        reset(&stats);
    }

    free(arr);
    return 0;
}
