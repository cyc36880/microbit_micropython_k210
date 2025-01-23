# Imports go at the top
from microbit import *

import oled

disp_oled = oled.oled()

count = 0

while True:
    count += 1
    if count > 50:
        count = 0
    disp_oled.set_text(0, 0, "test %d  ", count) 
    sleep(1000)
