import iic_base
from microbit import *

class s4s_ultr(iic_base.iic_base):
    def __init__(self, port=0, addr=0x57):
        super().__init__(port, addr)

    def get_distance(self):
        sleep(50)
        ret = self.read_reg(0x01, 3)
        dis = ret[0]<<16 | ret[1]<<8 | ret[2]
        return dis//10000

    def set_color(self, light, r, g, b):
        sleep(50)
        self.write_reg(0x02, [light, r, g, b])
