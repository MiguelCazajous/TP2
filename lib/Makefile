CC = gcc
CFLAGS = -g -m32 -Wall -Werror -pedantic -I.
LDFLAGS = --shared
#DEPS = .h
OBJ = libHelloWorld.o
BUILD = libHelloWorld.so

libHelloWorld.so: $(OBJ)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $^

%.o: %.c $(DEPS)
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
	rm -f $(BUILD) $(OBJ)


