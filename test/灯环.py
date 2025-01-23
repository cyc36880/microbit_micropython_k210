# Imports go at the top
from microbit import *

import color
import light_ring

rl = light_ring.light_ring(light_ring.P14P1)

while True:
    rl.color((255, 0, 0))
    sleep(1000)
    rl.color( color.GREEN )
    sleep(1000)

