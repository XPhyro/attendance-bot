CC	   = gcc
CFLAGS = -shared -O3 -lX11 -fPIC -Wl,-soname,scrnsht

SRC    = scrnsht.c

all: scrnsht

scrnsht: ${SRC}
	${CC} ${CFLAGS} -o scrnsht.so scrnsht.c

clean:
	rm -f scrnsht.so

install: all
	cp -f scrnsht.so /usr/lib
	cp -f main.py "/usr/bin/attendance-bot"
	mkdir -p /usr/share/attendance-bot
	cp -f reference.png /usr/share/attendance-bot/reference.png

uninstall:
	rm -rf /usr/lib/scrnsht.so \
		   /usr/bin/attendance-bot \
		   /usr/share/attendance-bot

.PHONY: all clean install uninstall
