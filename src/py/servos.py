from microbit import *
import DC_motor

S1 = 0
S2 = 1
S3 = 2
S4 = 3

class servos():
    def __init__(self, port):
        self.port = port
        self._handle = DC_motor.motor(port)

    def angle(self, angle:int): # 设置角度 0 - 180
        angle = 0 if angle<0 else angle
        angle = 180 if angle>180 else angle
        us = (angle * 1800 * 0.6 / 180 + 600) # 0.6 ~ 2.4
        pwm = us * 4096 / 20000;
        DC_motor._setPwm(self._handle._handle._handle, self._handle.port, 0, int(pwm) )
        