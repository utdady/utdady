#include "io.h"

#include <fcntl.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct buffer {
    int fd;
    uint8_t a[BUFFER_SIZE];
    size_t num_remaining;
    size_t offset;
};

Buffer *read_open(const char *filename) {
    int fd = open(filename, O_RDONLY);
    if (fd == -1) {
        return NULL;
    }

    Buffer *buf = malloc(sizeof(Buffer));
    if (buf == NULL) {
        close(fd);
        return NULL;
    }

    buf->fd = fd;
    buf->num_remaining = 0;
    buf->offset = 0;

    return buf;
}

void read_close(Buffer **pbuf) {
    if (pbuf == NULL || *pbuf == NULL) {
        return;
    }

    Buffer *buf = *pbuf;
    close(buf->fd);
    free(buf);
    *pbuf = NULL;
}

bool read_uint8(Buffer *buf, uint8_t *x) {
    if (buf->num_remaining == 0) {
        ssize_t rc = read(buf->fd, buf->a, sizeof(buf->a));
        if (rc < 0) {
            // Report error
            return false;
        }
        if (rc == 0) {
            return false; // end of file
        }
        buf->num_remaining = rc;
        buf->offset = 0;
    }

    *x = buf->a[buf->offset];
    buf->offset++;
    buf->num_remaining--;

    return true;
}

bool read_uint16(Buffer *buf, uint16_t *x) {
    uint8_t byte1, byte2;
    if (!read_uint8(buf, &byte1) || !read_uint8(buf, &byte2)) {
        return false;
    }

    *x = byte2;
    *x <<= 8;
    *x |= byte1;

    return true;
}

bool read_uint32(Buffer *buf, uint32_t *x) {
    uint16_t value1, value2;
    if (!read_uint16(buf, &value1) || !read_uint16(buf, &value2)) {
        return false;
    }

    *x = value2;
    *x <<= 16;
    *x |= value1;

    return true;
}

Buffer *write_open(const char *filename) {
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        return NULL;
    }

    Buffer *buf = malloc(sizeof(Buffer));
    if (buf == NULL) {
        close(fd);
        return NULL;
    }

    buf->fd = fd;
    buf->offset = 0;

    return buf;
}

void write_close(Buffer **pbuf) {
    if (pbuf == NULL || *pbuf == NULL) {
        return;
    }

    Buffer *buf = *pbuf;
    ssize_t num_bytes = buf->offset;
    uint8_t *start = buf->a;

    while (num_bytes > 0) {
        ssize_t rc = write(buf->fd, start, num_bytes);
        if (rc < 0) {
            break;
        }
        start += rc;
        num_bytes -= rc;
    }

    close(buf->fd);
    free(buf);
    *pbuf = NULL;
}

void write_uint8(Buffer *buf, uint8_t x) {
    if (buf->offset == BUFFER_SIZE) {
        ssize_t num_bytes = write(buf->fd, buf->a, BUFFER_SIZE);
        if (num_bytes < 0) {
            // report error
            write_close(&buf);
            return;
        }
        buf->offset = 0;
    }
    buf->a[buf->offset] = x;
    buf->offset++;
}

void write_uint16(Buffer *buf, uint16_t x) {
    write_uint8(buf, x);
    write_uint8(buf, x >> 8);
}

void write_uint32(Buffer *buf, uint32_t x) {
    write_uint16(buf, x);
    write_uint16(buf, x >> 16);
}