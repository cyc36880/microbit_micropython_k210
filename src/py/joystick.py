import iic_base

def uigned8_to_signedInt(data:int):
    if data >= 128:
        return data - 256
    else:
        return data

class joystick_sensor(iic_base.iic_base):
    def __init__(self, port=0, addr:int=0x61):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)
    
    def get_x(self): #在x轴的输出值 -100 ~ 100
        data = self._handle.read_bytes(4)
        return uigned8_to_signedInt(data[1])
    
    def get_y(self): #在y轴的输出值 -100 ~ 100
        data = self._handle.read_bytes(4)
        return uigned8_to_signedInt(data[2])
    
    def is_up(self):# 操纵杆是否向上 
        return True if self.get_y()<-50 else False
    
    def is_down(self): # 操纵杆是否向下 
        return True if self.get_y()>50 else False
    
    def is_left(self): # 是否向左
        return True if self.get_x()<-50 else False
    
    def is_right(self): # 是否向右
        return True if self.get_x()>50 else False





