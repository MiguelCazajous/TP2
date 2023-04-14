CC = gcc
CFLAGS = -g -m32 -Wall -Werror -pedantic -I.
LDFLAGS = --shared
OBJ = libConverter.o
BUILD = libConverter.so

libConverter.so: $(OBJ)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
	rm -f $(BUILD) $(OBJ)


