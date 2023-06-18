#include "path.h"

#include "graph.h"
#include "stack.h"
#include "vertices.h"

#include <stdio.h>
#include <stdlib.h>

typedef struct path {
    uint32_t total_weight;
    Stack *vertices;
} Path;

Path *path_create(uint32_t capacity) {
    Path *p = malloc(sizeof(Path));
    p->total_weight = 0;
    p->vertices = stack_create(capacity);
    return p;
}

void path_free(Path **pp) {
    if (pp && *pp) {
        Path *p = *pp;
        stack_free(&p->vertices);
        free(p);
        *pp = NULL;
    }
}

uint32_t path_vertices(const Path *p) {
    return stack_size(p->vertices);
}

uint32_t path_distance(const Path *p) {
    return p->total_weight;
}

void path_add(Path *p, uint32_t val, const Graph *g) {
    if (p && g) {
        uint32_t prev_vertex;

        if (stack_empty(p->vertices)) {
            // If the path is empty, set the total weight to zero
            p->total_weight = 0;
        } else {
            // Get the previous vertex from the top of the stack
            stack_peek(p->vertices, &prev_vertex);

            // Lookup the weight of the edge between the previous vertex and the new vertex
            uint32_t weight = graph_get_weight(g, prev_vertex, val);

            // Update the total weight of the path by adding the weight of the new edge
            p->total_weight += weight;
        }

        // Add the new vertex to the path's stack
        stack_push(p->vertices, val);
    }
}

uint32_t path_remove(Path *p, const Graph *g) {
    if (p && g && !stack_empty(p->vertices)) {
        uint32_t removed_vertex;
        stack_pop(p->vertices, &removed_vertex);

        if (stack_empty(p->vertices)) {
            // If the path becomes empty, set the total weight to zero
            p->total_weight = 0;
        } else {
            uint32_t last_vertex;
            stack_peek(p->vertices, &last_vertex);

            // Lookup the weight of the edge between the last vertex and the new last vertex
            uint32_t weight = graph_get_weight(g, last_vertex, removed_vertex);

            // Update the total weight of the path by subtracting the weight of the removed edge
            p->total_weight -= weight;
        }
        return removed_vertex;
    }
    return UINT32_MAX; // Indicate an invalid removal
}

void path_copy(Path *dst, const Path *src) {
    stack_copy(dst->vertices, src->vertices);
    dst->total_weight = src->total_weight;
}

void path_print(const Path *p, FILE *outfile, const Graph *g) {
    char **names = graph_get_names(g);
    stack_print(p->vertices, outfile, names);
}
