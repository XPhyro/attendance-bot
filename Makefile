CC	   = gcc
CFLAGS = -shared -O3 -lX11 -fPIC -Wl,-soname,scrnsht

scrnsht: scrnsht.c
	$(CC) $(CFLAGS) -o scrnsht.so scrnsht.c
