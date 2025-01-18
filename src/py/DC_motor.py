import iic_base
import time

M1 = 8
M2 = 10
M3 = 12
M4 = 14

_pca9685_init_flag = 0

def _initPCA9685(iic_handle):
    global _pca9685_init_flag
    if _pca9685_init_flag==1:
        return 
    _pca9685_init_flag = 1
    iic_handle.write_bytes([0, 0])
    prescaleval = 25000000
    prescaleval //= 4096
    prescaleval //= 50
    prescaleval -= 1
    prescale = prescaleval
    oldmode = iic_handle.read_reg(0, 1)[0]
    newmode = (oldmode & 0x7F) | 0x10

    iic_handle.write_bytes([0, newmode])
    iic_handle.write_bytes([254, prescale])
    iic_handle.write_bytes([0, oldmode])
    time.sleep_ms(5)
    iic_handle.write_bytes([0, oldmode | 0xa1])
    
def _setPwm(iic_handle, channel, on, off):
    if (channel < 0 or channel > 15):
            return
    buf22 = [0]*5
    buf22[0] = 6 + 4 * channel;
    buf22[1] = on & 0xff;
    buf22[2] = (on >> 8) & 0xff;
    buf22[3] = off & 0xff;
    buf22[4] = (off >> 8) & 0xff;
    iic_handle.write_bytes(buf22)



def MotorRun(iic_handle, index, speed):
    speed = speed * 16 # map 255 to 4096
    if (speed >= 4096):
        speed = 4095
    if (speed <= -4096):
        speed = -4095
    a = index
    b = index + 1
    if (a > 10):
        if (speed >= 0):
            _setPwm(iic_handle, a, 0, speed)
            _setPwm(iic_handle, b, 0, 0)
        else:
            _setPwm(iic_handle, a, 0, 0)
            _setPwm(iic_handle, b, 0, -speed)
    else:
        if (speed >= 0):
            _setPwm(iic_handle, b, 0, speed)
            _setPwm(iic_handle, a, 0, 0)
        else:
            _setPwm(iic_handle, b, 0, 0)
            _setPwm(iic_handle, a, 0, -speed)



class _dc_motor():
    def __init__(self):
        self._handle = iic_base.iic_base(0, 0x40)
        _initPCA9685(self._handle)

    def run(self, port, velocity):
        MotorRun(self._handle, port, velocity)
        


class motor():
    def __init__(self, port):
        self.port = port
        self._handle = _dc_motor()

    def run(self, velocity): # -255 ~ 255
        self._handle.run(self.port, velocity)


class motor_pair():
    def __init__(self, port1, port2):
        self.port1 = port1
        self.port2 = port2
        self._handle_left  = _dc_motor()
        self._handle_right = _dc_motor()
        
    def move(self, velocity1, velocity2): # -255 ~ 255
        self._handle_left.run(self.port1, velocity1)
        self._handle_right.run(self.port2, velocity2)






