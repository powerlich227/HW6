CFLAGS = -g3 -O0
LIBS = -lm
CC = gcc

all: C_call

C_call.o:	C_call.c diffusion.h
	$(CC) $(CFLAGS)	-c -o C_call.o 	C_call.c
diffusion.o:	diffusion.c diffusion.h
	$(CC) $(CFLAGS)	-c -o diffusion.o diffusion.c
C_call:	C_call.o diffusion.o
	$(CC) $(CFLAGS) $(LIBS) -o C_call C_call.o diffusion.o

clean:
	rm -f *.o C_call
