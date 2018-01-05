CFLAGS = -shared
LIBS = -lm
CC = gcc

all: libhmwk6p2

diffusion.o:	diffusion.c diffusion.h
	$(CC) $(CFLAGS)	-fpic -c diffusion.c

libhmwk6p2:	diffusion.o
	$(CC) $(CFLAGS) $(LIBS) -o libhmwk6p2.so diffusion.o

clean:
	rm -f *.o libhmwk6p2
