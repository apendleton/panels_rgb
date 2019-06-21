from scenes import *
from lib import *

import colorsys

# def program():
#     while True:
#         bars(20)
#         threedeesin(20)
#         scan(20)
#         spotlight(20)
#         meander(20)
#         splotch(20)

# 30, 30, 30, 15, 15, 30, 15, 30, 30, 15
def program():
    while True:
        # 1) 30 seconds, red to pink
        ripple(30, (50, 0, 0), (255, 100, 100))

        # 2) 30 seconds, black to white
        ripple(30, (0, 0, 0), (255, 255, 255))

        # 3) 30 seconds, green to light green
        ripple(30, (0, 50, 0), (100, 255, 100))

        # 4) 15 seconds, black to white
        ripple(15, (0, 0, 0), (255, 255, 255))

        # 5) 15 seconds, blue to light blue
        ripple(15, (0, 0, 50), (100, 100, 255))

        # 6a) 30 seconds, black to white
        ripple(30, (0, 0, 0), (255, 255, 255))

        # 6b) 15 seconds, dark purple to light purple
        ripple(15, (25, 0, 25), (255, 25, 255))

        # 7) 30 seconds, black to white
        ripple(30, (0, 0, 0), (255, 255, 255))

        # 8) 30 seconds dark yellow to light yellow
        ripple(30, (25, 25, 0), (255, 255, 25))

        # 9) 15 seconds, black to white
        ripple(15, (0, 0, 0), (255, 255, 255))

        # one minute dark
        for panel in range(0,4):
            setColor(panel, (0, 0, 0))
        render()
        delay(60000)

run(program)