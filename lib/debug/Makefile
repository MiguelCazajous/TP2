CC = gcc
AS = nasm
CFLAGS = -g -O3 -m32 -pedantic -I.
AFLAGS = -f elf32 -g
APATH = ../
OBJ = debug.o product.o
BUILD = debug

debug: $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

%.o: $(APATH)%.asm
	$(AS) $(AFLAGS) -o $@ $<

.PHONY: clean
clean:
	rm -f $(BUILD) $(OBJ)


