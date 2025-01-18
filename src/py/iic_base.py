from microbit import *

class iic_base:
    def __init__(self, port:int, addr:int):
        self._port = port
        self._addr = addr
    
    def write_bytes(self, data:list):
        i2c.write(self._addr, bytes(data), False)

    def read_bytes(self, length:int):
        return i2c.read(self._addr, length, False)

    def read_reg(self, reg, length): # 返回列表
        i2c.write(self._addr, bytes([reg]), True)
        return i2c.read(self._addr, length, False)
        
    def write_reg(self, reg, data:list):
        data.insert(0, reg)
        i2c.write(self._addr, bytes(data),  False)
    
    def is_ready(self): # 是否在线
        try:
           self.read_bytes(1)
        except:
            return 0
        return 1
    
# iic_init_flag = False
def iic_init():
    # global iic_init_flag
    # if iic_init_flag == False:
    #     iic_init_flag = True
    #     # i2c.init() # 初始化iic
    i2c.init()
    	
iic_init()
