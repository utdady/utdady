CC = clang
CFLAGS = -Wall -Wextra -Werror -pedantic -Wstrict-prototypes
LFLAGS = -lm

EXEC1 = colorb
OBJS1 = colorb.o bmp.o io.o

EXEC2 = iotest
OBJS2 = iotest.o io.o

all: $(EXEC1)

all: $(EXEC2)

$(EXEC1): $(OBJS1)
        $(CC) $(LFLAGS) -o $(EXEC1) $(OBJS1)

$(EXEC2): $(OBJS2)
        $(CC) $(LFLAGS) -o $(EXEC2) $(OBJS2)

%.o: %.c
        $(CC) $(CFLAGS) -c $<

clean:
        rm -f $(EXEC1) $(OBJS1)
        rm -f $(EXEC2) $(OBJS2)

format:
        clang-format -i --style=file *.[ch]