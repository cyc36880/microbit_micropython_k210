import iic_base
import color

MODE_NONE  = 0
MODE_COLOR = 1 # 颜色
MODE_GRAY  = 2 # 灰度
MODE_BIN   = 3 # 二值（黑色为1 白色为0）

_color_map = \
{
    0:color.COLOR_NONE,
    1:color.RED,
    2:color.YELLOW,
    3:color.GREEN,
    4:color.CYAN,
    5:color.BLUE,
    6:color.PURPLE
}

def ret_data(data, port):
    if port is None:
        return data
    else:
        return data[port]

class six_gray_sensor(iic_base.iic_base):
    def __init__(self, port=0, addr=0x70):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)

    def gray_study(self): # 灰度学习
        self._handle.write_bytes([4])


    def gray(self, port=None): # 灰度
        self._handle.write_bytes([MODE_GRAY])
        data = self._handle.read_bytes(6)
        ret_val = [0]*6
        for i in range(6):
            ret_val[i] = data[i]
        return ret_data(ret_val, port)
    
    def color(self, port=None): # 颜色
        self._handle.write_bytes([MODE_COLOR])
        data = self._handle.read_bytes(6)
        ret_val = [0]*6
        for i in range(6):
            ret_val[i] = _color_map[data[i]]
        return ret_data(ret_val, port)

    def black(self, port=None): # 黑线
        self._handle.write_bytes([MODE_GRAY])
        data = self._handle.read_bytes(6)
        ret_val = [0]*6
        for i in range(6):
            ret_val[i] = 1 if data[i] > 120 else 0
        return ret_data(ret_val, port)

        

    

    


    