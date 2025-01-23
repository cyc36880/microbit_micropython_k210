# Imports go at the top
from microbit import *

import server_motor

sm = server_motor.motor(addr = server_motor.LIGHT_RED)
while True:
    sm.run(50) # 以50的速度转动
    
