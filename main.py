#!/usr/bin/env python3


from os import path
from time import sleep
from datetime import datetime as dt
from ctypes import CDLL, c_ubyte
from PIL import Image, ImageChops
from pyautogui import click


libname = "scrnsht.so"
refimpath = "/usr/share/attendance-bot/reference.png"
scrnsht = CDLL(libname)
refim = Image.open(refimpath).convert("RGB")
yescoord = (29, 124)
submitcoord = (1281, 1059)
reqcount = 3


def grab_screen(x1, y1, x2, y2):
    w, h = x2 - x1, y2 - y1
    size = w * h
    objlength = size * 3

    scrnsht.capture.argtypes = []
    result = (c_ubyte * objlength)()
    scrnsht.capture(x1, y1, w, h, result)

    return Image.frombuffer("RGB", (w, h), result, "raw", "RGB", 0, 1)


if __name__ == "__main__":
    count = 0

    while count < reqcount:
        im = grab_screen(0, 0, 2560, 1080)
        sleep(5)

        if not ImageChops.difference(refim, im).getbbox():
            print("Taking attendance...")

            sleep(2)
            click(yescoord[0], yescoord[1])
            sleep(2)
            click(submitcoord[0], submitcoord[1])

            count += 1
            print(f"Took attendance on {dt.now()}.")

            sleep(900)
