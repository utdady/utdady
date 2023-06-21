#include "bitwriter.h"
#include "io.h"
#include "node.h"
#include "pq.h"

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Code {
    uint64_t code;
    uint8_t code_length;
} Code;

uint64_t fill_histogram(Buffer *inbuf, double *histogram) {
    uint64_t filesize = 0;
    memset(histogram, 0, 256 * sizeof(double));

    uint8_t byte;
    while (read_uint8(inbuf, &byte)) {
        histogram[byte]++;
        filesize++;
    }

    histogram[0x00]++;
    histogram[0xff]++;

    return filesize;
}

Node *create_tree(double *histogram, uint16_t *num_leaves) {
    PriorityQueue *pq = pq_create();

    for (int i = 0; i < 256; i++) {
        if (histogram[i] > 0) {
            Node *new_node = node_create(i, histogram[i]);
            enqueue(pq, new_node);
        }
    }

    while (!pq_size_is_1(pq)) {
        Node *left, *right;
        dequeue(pq, &left);
        dequeue(pq, &right);

        Node *new_node = node_create(0, left->weight + right->weight);
        new_node->left = left;
        new_node->right = right;

        enqueue(pq, new_node);
    }

    Node *tree;
    dequeue(pq, &tree);
    *num_leaves = pq_is_empty(pq) ? 1 : 2;

    pq_free(&pq);

    return tree;
}

void fill_code_table(Code *code_table, Node *node, uint64_t code, uint8_t code_length) {
    if (node->left == NULL && node->right == NULL) {
        code_table[node->symbol].code = code;
        code_table[node->symbol].code_length = code_length;
    } else {
        fill_code_table(code_table, node->left, code, code_length + 1);
        code |= (uint64_t) 1 << code_length;
        fill_code_table(code_table, node->right, code, code_length + 1);
    }
}

void huff_write_tree(BitWriter *outbuf, Node *node) {
    if (node->left == NULL && node->right == NULL) {
        bit_write_bit(outbuf, 1);
        bit_write_uint8(outbuf, node->symbol);
    } else {
        bit_write_bit(outbuf, 0);
        huff_write_tree(outbuf, node->left);
        huff_write_tree(outbuf, node->right);
    }
}

void huff_compress_file(const char *input_filename, const char *output_filename) {
    Buffer *inbuf = read_open(input_filename);
    if (inbuf == NULL) {
        perror("Failed to open input file");
        return;
    }

    Buffer *outbuf = write_open(output_filename);
    if (outbuf == NULL) {
        perror("Failed to open output file");
        read_close(&inbuf);
        return;
    }

    double histogram[256];
    uint64_t filesize = fill_histogram(inbuf, histogram);

    uint16_t num_leaves;
    Node *code_tree = create_tree(histogram, &num_leaves);

    Code code_table[256];
    memset(code_table, 0, 256 * sizeof(Code));
    fill_code_table(code_table, code_tree, 0, 0);

    bit_write_uint8((BitWriter *) outbuf, 'H');
    bit_write_uint8((BitWriter *) outbuf, 'C');
    bit_write_uint32((BitWriter *) outbuf, filesize);
    bit_write_uint16((BitWriter *) outbuf, num_leaves);

    huff_write_tree((BitWriter *) outbuf, code_tree);

    inbuf = 0;
    uint8_t byte;
    while (read_uint8(inbuf, &byte)) {
        Code code = code_table[byte];
        for (uint8_t i = 0; i < code.code_length; i++) {
            bit_write_bit((BitWriter *) outbuf, code.code & 1);
            code.code >>= 1;
        }
    }

    write_close(&outbuf);
    read_close(&inbuf);
}

int main(int argc, char *argv[]) {
    const char *input_filename = NULL;
    const char *output_filename = NULL;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-i") == 0) {
            if (i + 1 < argc) {
                input_filename = argv[i + 1];
                i++;
            }
        } else if (strcmp(argv[i], "-o") == 0) {
            if (i + 1 < argc) {
                output_filename = argv[i + 1];
                i++;
            }
        } else if (strcmp(argv[i], "-h") == 0) {
            printf("Help message:\n");
            printf("Usage: huff -i <input file> -o <output file>\n");
            return 0;
        }
    }

    if (input_filename == NULL || output_filename == NULL) {
        printf("Error: Input and output filenames are required. Use -h for help.\n");
        return 1;
    }

    huff_compress_file(input_filename, output_filename);

    return 0;
}
