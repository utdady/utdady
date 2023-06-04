#include "bmp.h"
#include "io.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    const char *input_filename = NULL;
    const char *output_filename = NULL;

    // Parse command-line arguments
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-i") == 0) {
            if (i + 1 < argc) {
                input_filename = argv[i + 1];
            } else {
                printf("Error: Input filename not provided.\n");
                printf("Usage: colorb -i <input_file> -o <output_file>\n");
                printf("Options:\n");
                printf("  -i : Sets the name of the input file. Requires a filename as an "
                       "argument.\n");
                printf("  -o : Sets the name of the output file. Requires a filename as an "
                       "argument.\n");
                printf("  -h : Prints this help message.\n");
                return 1;
            }
        } else if (strcmp(argv[i], "-o") == 0) {
            if (i + 1 < argc) {
                output_filename = argv[i + 1];
            } else {
                printf("Error: Output filename not provided.\n");
                printf("Usage: colorb -i <input_file> -o <output_file>\n");
                printf("Options:\n");
                printf("  -i : Sets the name of the input file. Requires a filename as an "
                       "argument.\n");
                printf("  -o : Sets the name of the output file. Requires a filename as an "
                       "argument.\n");
                printf("  -h : Prints this help message.\n");
                return 1;
            }
        } else if (strcmp(argv[i], "-h") == 0) {
            printf("Usage: colorb -i <input_file> -o <output_file>\n");
            printf("Options:\n");
            printf("  -i : Sets the name of the input file. Requires a filename as an argument.\n");
            printf(
                "  -o : Sets the name of the output file. Requires a filename as an argument.\n");
            printf("  -h : Prints this help message.\n");
            return 0;
        }
    }

    // Check if required options are provided
    if (input_filename == NULL || output_filename == NULL) {
        printf("Error: Input and output filenames are required.\n");
        printf("Usage: colorb -i <input_file> -o <output_file>\n");
        printf("Options:\n");
        printf("  -i : Sets the name of the input file. Requires a filename as an argument.\n");
        printf("  -o : Sets the name of the output file. Requires a filename as an argument.\n");
        printf("  -h : Prints this help message.\n");
        return 1;
    }

    // Read BMP image
    Buffer *read_buffer = read_open(input_filename);
    if (read_buffer == NULL) {
        printf("Failed to open input file: %s\n", input_filename);
        return 1;
    }

    BMP *bmp = bmp_create(read_buffer);
    read_close(&read_buffer);
    if (bmp == NULL) {
        printf("Failed to read BMP image: %s\n", input_filename);
        return 1;
    }

    // Modify the BMP image (e.g., reduce the palette)
    bmp_reduce_palette(bmp);

    // Write modified BMP image
    Buffer *write_buffer = write_open(output_filename);
    if (write_buffer == NULL) {
        printf("Failed to open output file: %s\n", output_filename);
        bmp_free(&bmp);
        return 1;
    }

    bmp_write(bmp, write_buffer);
    write_close(&write_buffer);
    bmp_free(&bmp);
    printf("Color manipulation complete. Output file: %s\n", output_filename);
    return 0;
}