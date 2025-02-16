from microbit import *

class iic_base:
    def __init__(self, port:int, addr:int):
        self._port = port
        self._addr = addr
    
    def write_bytes(self, data:list):
        try:
            i2c.write(self._addr, bytes(data), False)
        except:
            return

    def read_bytes(self, length:int):
        try:
            return i2c.read(self._addr, length, False)
        except:
            return [0]*length

    def read_reg(self, reg, length): # 返回列表
        try:
            i2c.write(self._addr, bytes([reg]), True)
            return i2c.read(self._addr, length, False)
        except:
            return [0]*length
        
    def write_reg(self, reg, data:list):
        try:
            data.insert(0, reg)
            i2c.write(self._addr, bytes(data),  False)
        except:
            return
    
    def is_ready(self): # 是否在线
        try:
           self.read_bytes(1)
        except:
            return 0
        return 1

def iic_init():
    i2c.init()
    	
iic_init()
