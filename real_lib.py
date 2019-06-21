import pyenttec, math, time

global port

MAX = 60

panels = [408, 401, 404, 16]

def render():
    port.render()

def setColor(panel, color):
    if panels[panel]:
        port.set_channel(panels[panel] - 1, color[0])
        port.set_channel(panels[panel], color[1])
        port.set_channel(panels[panel] + 1, color[2])

def run(func):
    global port

    port = pyenttec.select_port()

    func()
