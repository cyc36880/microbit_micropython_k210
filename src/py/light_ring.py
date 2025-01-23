from microbit import *
import color
import neopixel

P13P0 = pin0
P14P1 = pin1
P15P2 = pin2

P7P8   = pin8
P9P12  = pin12
P10P16 = pin16

_color_map = \
{
    color.BLACK:(0, 0, 0),
    color.BLUE :(0, 0, 255),
    color.COLOR_NONE:(0, 0, 0),
    color.CYAN:(0, 255, 255),
    color.GREEN:(0, 255, 0),
    color.ORANGE:(255, 165, 0),
    color.PURPLE:(128, 0, 128),
    color.WHITE : (255, 255, 255),
    color.RED : (255, 0, 0),
    color.YELLOW : (255, 255, 0)
}


class light_ring():
    def __init__(self, port):
        self._light = 0.05
        self._handle = neopixel.NeoPixel(port, 8)
        
    def light(self, light): # 设置亮度 0 - 255
        self._light = light/255
        
    def color(self, color):
        _color = None
        if isinstance(color, tuple):
            _color = color
        else:
            _color = _color_map[color]
        _color = (int(_color[0]*self._light), int(_color[1]*self._light), int(_color[2]*self._light))
        self._handle.fill(_color)
        self._handle.show()
    




