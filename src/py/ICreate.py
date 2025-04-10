import speech
import servos
import DC_motor
import servo_motor
import light_ring
import oled
import recording
import ultrasonic
import joystick
import music
ICM_joy = joystick.joystick_sensor()
ICM_sm_LIGHT_BLUE = servo_motor.motor(addr=servo_motor.LIGHT_BLUE)
ICM_sm_LIGHT_RED = servo_motor.motor(addr=servo_motor.LIGHT_RED)
ICM_sm_LIGHT_GREEN = servo_motor.motor(addr=servo_motor.LIGHT_GREEN)
ICM_sm_LIGHT_YELLOW = servo_motor.motor(addr=servo_motor.LIGHT_YELLOW)
ICM_ult0=ultrasonic.ultrasonic_sensor(0)
ICM_ult1=ultrasonic.ultrasonic_sensor(1)
ICM_ult4=ultrasonic.ultrasonic_sensor(4)
ICM_ult2=ultrasonic.ultrasonic_sensor(2)
