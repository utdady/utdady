#include "stack.h"

#include "graph.h"
#include "path.h"
#include "vertices.h"

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct stack {
    uint32_t capacity;
    uint32_t top;
    uint32_t *items;
} Stack;

Stack *stack_create(uint32_t capacity) {
    // Attempt to allocate memory for a stack
    // Cast it to a stack pointer too!
    Stack *s = (Stack *) malloc(sizeof(Stack));
    s->capacity = capacity;
    s->top = 0;

    // We need enough memory for <capacity> numbers
    s->items = calloc(s->capacity, sizeof(uint32_t));

    // We created our stack, return it!
    return s;
}

void stack_free(Stack **sp) {
    // sp is a double pointer, so we have to check if it,
    // or the pointer it points to is null.
    if (sp != NULL && *sp != NULL) {
        // Of course, we have to remember to free the
        // memory for the array of items first,
        // as that was also dynamically allocated!
        // If we freed the Stack first then we would
        // not be able to access the array to free it.
        if ((*sp)->items) {
            free((*sp)->items);
            (*sp)->items = NULL;
        }
        // Free memory allocated for the stack
        free(*sp);
    }
    if (sp != NULL) {
        // Set the pointer to null! This ensures we don't ever do a double free!
        *sp = NULL;
    }
}

bool stack_push(Stack *s, uint32_t val) {
    // If the stack is empty, return false;
    if (s->top == s->capacity) {
        return false;
    }
    // Set val
    s->items[s->top] = val;
    s->top++;

    return true;
}

bool stack_pop(Stack *s, uint32_t *val) {
    if (s->top == 0) {
        return false; // Stack is empty, cannot pop
    }

    // Decrement the top index
    s->top--;
    *val = s->items[s->top]; // Set val to the top item
    return true;
}

bool stack_peek(const Stack *s, uint32_t *val) {
    if (s->top == 0) {
        return false; // Stack is empty, cannot peek
    }

    *val = s->items[s->top - 1]; // Set val to the top item
    return true;
}

bool stack_empty(const Stack *s) {
    return s->top == 0;
}

bool stack_full(const Stack *s) {
    return s->top == s->capacity; // If top is equal to capacity - 1, the stack is full
}

uint32_t stack_size(const Stack *s) {
    return s->top; // The size of the stack is the value of top + 1
}

void stack_copy(Stack *dst, const Stack *src) {
    assert(dst->capacity == src->capacity); // Ensure dst has sufficient capacity
    dst->top = src->top; // Update dst's top to match src's top
    // Copy elements from src to dst
    for (uint32_t i = 0; i <= src->top; i++) {
        dst->items[i] = src->items[i];
    }
}

void stack_print(const Stack *s, FILE *f, char *vals[]) {
    for (uint32_t i = 0; i <= s->top - 1; i += 1) {
        fprintf(f, "%s\n", vals[s->items[i]]);
    }
}
