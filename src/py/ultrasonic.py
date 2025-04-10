from microbit import *
import machine
import time

P13P0 = 0
P14P1 = 1
P15P2 = 2

P7P8   = 3
P9P12  = 4
P10P16 = 5

_ultr_pin_map = \
{
    P13P0 : (pin0, pin13), # trigpin echopin
    P14P1 : (pin1, pin14),
    P15P2 : (pin2, pin15),
    
    P7P8  : (pin8 , pin7), 
    P9P12 : (pin12, pin9),
    P10P16: (pin16, pin10)
}

def _get_pin_time_pulse_us(pin):
    return machine.time_pulse_us(pin, 1, 25000)

class ultrasonic_sensor:
    def __init__(self, port):
        self.port = port
        self.trigpin = _ultr_pin_map[port][0]
        self.echopin = _ultr_pin_map[port][1]
        
    def get(self): #cm
        self.trigpin.write_digital(0)
        time.sleep_us(2)
        self.trigpin.write_digital(1)
        time.sleep_us(10)
        self.trigpin.write_digital(0)
        tim = _get_pin_time_pulse_us(self.echopin)
        distance = tim * 34 / 2 / 1000 * 3 / 2;
        return distance if distance > 0 else 0
        
        



        