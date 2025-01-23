# Imports go at the top
from microbit import *

import server_motor

sm = server_motor.motor(addr = server_motor.LIGHT_RED)
while True:
    sm.run_to_absolute_position(50, 360)
    sleep(400)
    sm.run_to_absolute_position(50, 0)
    sleep(400)
    

