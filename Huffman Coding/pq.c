#include "pq.h"

#include "node.h"

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct ListElement ListElement;
struct ListElement {
    Node *tree;
    ListElement *next;
};

struct PriorityQueue {
    ListElement *list;
};

PriorityQueue *pq_create(void) {
    PriorityQueue *queue = calloc(1, sizeof(PriorityQueue));
    return queue;
}

bool pq_less_than(Node *n1, Node *n2);

void pq_free(PriorityQueue **q) {
    if (*q == NULL)
        return;

    ListElement *current = (*q)->list;
    while (current != NULL) {
        ListElement *next = current->next;
        free(current);
        current = next;
    }

    free(*q);
    *q = NULL;
}

bool pq_is_empty(PriorityQueue *q) {
    return (q == NULL || q->list == NULL);
}

bool pq_size_is_1(PriorityQueue *q) {
    return (q != NULL && q->list != NULL && q->list->next == NULL);
}

void enqueue(PriorityQueue *q, Node *tree) {
    ListElement *new_element = malloc(sizeof(ListElement));
    if (new_element == NULL) {
        perror("Memory allocation failed");
        return;
    }

    new_element->tree = tree;
    new_element->next = NULL;

    if (q->list == NULL) {
        q->list = new_element;
    } else if (pq_less_than(tree, q->list->tree)) {
        new_element->next = q->list;
        q->list = new_element;
    } else {
        ListElement *current = q->list;
        while (current->next != NULL && pq_less_than(current->next->tree, tree)) {
            current = current->next;
        }
        new_element->next = current->next;
        current->next = new_element;
    }
}

bool dequeue(PriorityQueue *q, Node **tree) {
    if (pq_is_empty(q))
        return false;

    ListElement *element = q->list;
    *tree = element->tree;
    q->list = element->next;
    free(element);

    return true;
}

void pq_print(PriorityQueue *q) {
    assert(q != NULL);

    ListElement *e = q->list;
    int position = 1;

    while (e != NULL) {
        if (position++ == 1) {
            printf("=============================================\n");
        } else {
            printf("---------------------------------------------\n");
        }
        node_print_tree(e->tree, '<', 2);
        e = e->next;
    }
    printf("=============================================\n");
}

bool pq_less_than(Node *n1, Node *n2) {
    if (n1->weight < n2->weight)
        return true;
    if (n1->weight > n2->weight)
        return false;
    return n1->symbol < n2->symbol;
}
