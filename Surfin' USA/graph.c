#include "graph.h"

#include "path.h"
#include "stack.h"
#include "vertices.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct graph {
    uint32_t vertices;
    bool directed;
    bool *visited;
    char **names;
    uint32_t **weights;
} Graph;

Graph *graph_create(uint32_t vertices, bool directed) {
    Graph *g = calloc(1, sizeof(Graph));
    g->vertices = vertices;
    g->directed = directed;

    // use calloc to initialize everything with zeroes
    g->visited = calloc(vertices, sizeof(bool));
    g->names = calloc(vertices, sizeof(char *));

    // allocate g->weightts with a pointer for each row
    g->weights = calloc(vertices, sizeof(g->weights[0]));

    //allocate each row in the adjacency matrix
    for (uint32_t i = 0; i < vertices; ++i) {
        g->weights[i] = calloc(vertices, sizeof(g->weights[0][0]));
    }
    return g;
}

void graph_free(Graph **gp) {
    if (gp == NULL || *gp == NULL) {
        return; // No graph or already freed, nothing to do
    }

    Graph *g = *gp; // Dereference the double pointer to get the graph object

    // Free dynamically allocated memory in reverse order of allocation
    for (uint32_t i = 0; i < g->vertices; ++i) {
        free(g->names[i]);
        free(g->weights[i]);
    }

    free(g->names);
    free(g->weights);
    free(g->visited);
    free(g);

    *gp = NULL; // Set the graph pointer to NULL to prevent dangling references
}

uint32_t graph_vertices(const Graph *g) {
    return g->vertices;
}

void graph_add_vertex(Graph *g, const char *name, uint32_t v) {
    if (g->names[v]) {
        free(g->names[v]);
    }
    g->names[v] = strdup(name);
}

const char *graph_get_vertex_name(const Graph *g, uint32_t v) {
    return g->names[v];
}

char **graph_get_names(const Graph *g) {
    return g->names;
}

void graph_add_edge(Graph *g, uint32_t start, uint32_t end, uint32_t weight) {
    g->weights[start][end] = weight;
}

uint32_t graph_get_weight(const Graph *g, uint32_t start, uint32_t end) {
    if (g->directed) {
        return g->weights[start][end];
    } else {
        uint32_t weight = g->weights[start][end];
        if (weight != 0) {
            return weight;
        } else {
            return g->weights[end][start];
        }
    }
}

void graph_visit_vertex(Graph *g, uint32_t v) {
    g->visited[v] = true;
}

void graph_unvisit_vertex(Graph *g, uint32_t v) {
    g->visited[v] = false;
}

bool graph_visited(const Graph *g, uint32_t v) {
    return g->visited[v];
}

void graph_print(const Graph *g) {
    printf("Graph:\n");
    printf("Number of vertices: %u\n", g->vertices);
    printf("Directed: %s\n", g->directed ? "True" : "False");

    printf("Vertex Names:\n");
    for (uint32_t v = 0; v < g->vertices; ++v) {
        printf("Vertex %u: %s\n", v, g->names[v]);
    }

    printf("Adjacency Matrix:\n");
    for (uint32_t i = 0; i < g->vertices; ++i) {
        for (uint32_t j = 0; j < g->vertices; ++j) {
            printf("%5" PRIu32 "|", g->weights[i][j]);
        }
        printf("\n");
    }
}
