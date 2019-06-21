from real_lib import *
from lib import *

def rainbow():
    hue = 0
    while True:
        hue += 0.02
        if hue > 1:
            hue -= 1

        for panel in range(0, 4):
            phue = (hue + (0.15 * panel))
            if phue > 1:
                phue -= 1
            rgb = colorsys.hsv_to_rgb(phue, 1, 255)
            setColor(panel, tuple(map(int, rgb)))

        render()
        delay(100)

def ripple(duration, from_, to):
    level = 0
    timer = 0
    while True:
        level += 0.02
        if level > 1:
            level -= 1

        for panel in range(0, 4):
            plevel = (level + (0.15 * panel))
            if plevel > 1:
                plevel -= 1

            slevel = (1 + math.sin(2 * math.pi * plevel)) / 2

            rgb = weighted(slevel, from_, to)
            setColor(panel, rgb)

        render()

        delay(100)
        timer += .1
        if timer >= duration:
            return


def weighted(weight, from_, to):
    opposite = 1 - weight
    return (
        int((weight * from_[0]) + (opposite * to[0])),
        int((weight * from_[1]) + (opposite * to[1])),
        int((weight * from_[2]) + (opposite * to[2])),
    )