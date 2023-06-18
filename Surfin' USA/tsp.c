#include "graph.h"
#include "path.h"
#include "stack.h"
#include "vertices.h"

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Helper function to perform depth-first search to find the shortest Hamiltonian path
void dfs_shortest_hamiltonian_path(
    Graph *g, uint32_t v, uint32_t start, uint32_t count, Path *current_path, Path *shortest_path) {
    graph_visit_vertex(g, v); // Mark the current vertex as visited
    path_add(current_path, v, g); // Add the current vertex to the current path
    path_add(shortest_path, v, g);

    // If all vertices have been visited and the current path forms a Hamiltonian cycle
    if (count == graph_vertices(g) && graph_get_weight(g, v, start) != 0) {
        path_add(current_path, start, g); // Add the starting vertex to complete the cycle

        // If the current path is shorter than the shortest path found so far, update the shortest path
        if (path_distance(current_path) < path_distance(shortest_path)) {
            path_copy(shortest_path, current_path);
        }

        path_remove(current_path, g); // Remove the starting vertex to backtrack
        return;
    }

    // Explore the neighbors of the current vertex
    for (uint32_t i = 0; i < graph_vertices(g); ++i) {
        if (!graph_visited(g, i) && graph_get_weight(g, v, i) != 0) {
            dfs_shortest_hamiltonian_path(g, i, start, count + 1, current_path, shortest_path);
        }
    }

    path_remove(current_path, g); // Remove the current vertex to backtrack
    graph_unvisit_vertex(g, v); // Mark the current vertex as unvisited
}

Path *shortest_hamiltonian_path(Graph *g) {
    // Create a path to store the current path during the DFS traversal
    Path *current_path = path_create(graph_vertices(g));
    // Create a path to store the shortest Hamiltonian path found so far
    Path *shortest_path = path_create(graph_vertices(g));

    // Start the DFS traversal from each vertex in the graph
    for (uint32_t i = 0; i < graph_vertices(g); ++i) {
        dfs_shortest_hamiltonian_path(g, i, START_VERTEX, 1, current_path, shortest_path);
    }

    // Free the memory allocated for the current path
    path_free(&current_path);

    return shortest_path;
}

Graph *readGraphFromFile(const char *filename, bool isDirected) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Error opening file: %s\n", filename);
        return NULL;
    }

    uint32_t numVertices;

    if (fscanf(file, "%u\n", &numVertices) != 1) {
        fprintf(stderr, "tsp: error reading number of vertices\n");
        fclose(file);
        return NULL;
    }
    // printf("Vertices: %u\n", numVertices);

    // Create the graph
    Graph *graph = graph_create(numVertices, isDirected);

    for (uint32_t i = 0; i < numVertices; i++) {
        char vertexName[100];
        fgets(vertexName, sizeof(vertexName), file);
        if (vertexName[0] == '\n') {
            fprintf(stderr, "Invalid file format: missing vertex name\n");
            graph_free(&graph);
            fclose(file);
            return NULL;
        }
        // printf("Vertex Name: %s\n", vertexName);
        graph_add_vertex(graph, vertexName, i);
    }

    uint32_t numEdges;

    if (fscanf(file, "%u\n", &numEdges) != 1) {
        fprintf(stderr, "Invalid file format: missing number of edges\n");
        graph_free(&graph);
        fclose(file);
        return NULL;
    }
    // printf("Edges: %u\n", numEdges);

    uint32_t vertexFrom, vertexTo, weight;

    for (uint32_t i = 0; i < numEdges; i++) {
        if (fscanf(file, "%u %u %u", &vertexFrom, &vertexTo, &weight) != 3) {
            fprintf(stderr, "Invalid file format: missing edge information\n");
            graph_free(&graph);
            fclose(file);
            return NULL;
        }
        // printf("From: %u, To: %u, Dist: %u\n", vertexFrom, vertexTo, weight);
        graph_add_edge(graph, vertexFrom, vertexTo, weight);
    }

    fclose(file);
    return graph;
}

int main(int argc, char *argv[]) {
    char *inputFile = NULL;
    char *outputFile = NULL;
    bool isDirected = false;

    // Parsing command-line options
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-i") == 0) {
            if (i + 1 < argc) {
                inputFile = argv[++i];
            } else {
                fprintf(stderr, "Missing argument for -i option\n");
                return 1;
            }
        } else if (strcmp(argv[i], "-o") == 0) {
            if (i + 1 < argc) {
                outputFile = argv[++i];
            } else {
                fprintf(stderr, "Missing argument for -o option\n");
                return 1;
            }
        } else if (strcmp(argv[i], "-d") == 0) {
            isDirected = true;
        } else if (strcmp(argv[i], "-h") == 0) {
            printf("Usage: tsp [OPTIONS]\n");
            printf("Options:\n");
            printf("  -i FILE    Sets the input file (default: stdin)\n");
            printf("  -o FILE    Sets the output file (default: stdout)\n");
            printf("  -d         Treats all graphs as directed\n");
            printf("  -h         Prints this help message\n");

            return 0;
        } else {
            fprintf(stderr, "Unknown option: %s\n", argv[i]);
            return 1;
        }
    }
    // Set up file pointers for input and output
    FILE *input = (inputFile != NULL) ? fopen(inputFile, "r") : stdin;
    FILE *output = (outputFile != NULL) ? fopen(outputFile, "w") : stdout;

    // Read the graph from the input file
    Graph *graph = readGraphFromFile(inputFile, isDirected);
    // graph_print(graph);

    // Solve the travelling salesman problem;
    Path *shortest_path = shortest_hamiltonian_path(graph);
    fprintf(stdout, "Alissa starts at:\n");
    path_print(shortest_path, stdout, graph);
    fprintf(stdout, "Total Distance: %u\n", path_distance(shortest_path));

    // Close file pointers
    if (inputFile != NULL) {
        fclose(input);
    }
    if (outputFile != NULL) {
        fclose(output);
    }

    graph_free(&graph);

    return 0;
}
