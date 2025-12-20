from microbit import *
import iic_base
import color

def ret_data(data, port):
    if port is None:
        return data
    else:
        return data[port]

class s4s_gray(iic_base.iic_base):
    MODE_NONE  = 0
    MODE_COLOR = 1 # 颜色
    MODE_GRAY  = 2 # 灰度
    MODE_BIN   = 3 # 二值（黑色为1 白色为0）
    MODE_PHOTOSENSITIVE = 15
    
    _color_identify_map = \
    {
        0:color.COLOR_NONE,
        1:color.RED,
        2:color.GREEN,
        3:color.BLUE,
        4:color.YELLOW,
        5:color.CYAN,
        6:color.PURPLE,
    }

    _color_study_map = \
    {
        color.RED:7,
        color.GREEN:8,
        color.BLUE:9,
        color.YELLOW:10,
        color.PURPLE:12,
    }

    def __init__(self, port=0, addr=0x6F):
        super().__init__(port, addr)
    
    def gray_study(self): # 灰度学习
        self.write_bytes([4])
        sleep(100)
        # while self.read_bytes(5)[4] == 4:
        #     sleep(1)

    def binary_study(self): # 二值学习
        self.write_bytes([5])
        sleep(100)
        # while self.read_bytes(5)[4] == 5:
        #     sleep(1)

    def color_study(self, color): # 颜色学习
        if color not in self._color_study_map:
            raise ValueError("color must be in %s" % self._color_study_map)
        self.write_bytes([self._color_study_map[color]])
        sleep(100)
        # while self.read_bytes(5)[4] == self._color_study_map[color]:
        #     sleep(1)

    def clear_color(self):
        self.write_bytes([6])
        sleep(100)
    
    def gray(self, port=None): # 灰度
        self.write_bytes([self.MODE_GRAY])
        data = self.read_bytes(4)
        ret_val = [0]*4
        for i in range(4):
            ret_val[i] = data[i]
        return ret_data(ret_val, port)
    
    def color(self, port=None): # 颜色
        self.write_bytes([self.MODE_COLOR])
        data = self.read_bytes(4)
        ret_val = [0]*4
        for i in range(4):
            ret_val[i] = self._color_identify_map[data[i]]
        return ret_data(ret_val, port)

    def black(self, port=None): # 黑线
        self.write_bytes([self.MODE_BIN])
        data = self.read_bytes(4)
        ret_val = [0]*4
        for i in range(4):
            ret_val[i] = data[i] 
        return ret_data(ret_val, port)

    def photosensitive(self, port=None): # 光敏值
        self.write_bytes([self.MODE_PHOTOSENSITIVE])
        data = self.read_bytes(4)
        ret_val = [0]*4
        for i in range(4):
            ret_val[i] = data[i] 
        return ret_data(ret_val, port)
