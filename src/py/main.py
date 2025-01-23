from microbit import *

import server_motor, joystick, servos, oled

m1 = server_motor.motor(addr=server_motor.LIGHT_BLUE)
joy = joystick.joystick_sensor()
s1 = servos.servos(servos.S1)
disp_oled = oled.oled()

while True:
    val = joy.get_x()
    m1.run(val)
    disp_oled.clear_screen()
    disp_oled.set_text(0, 0, "%d", val)
    s1.write_angle(val)

