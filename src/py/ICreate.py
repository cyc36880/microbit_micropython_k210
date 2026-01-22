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
import ai_camera
ICM_joy = joystick.joystick_sensor()
ICM_sm_LIGHT_BLUE = servo_motor.motor(addr=servo_motor.LIGHT_BLUE)
ICM_sm_LIGHT_RED = servo_motor.motor(addr=servo_motor.LIGHT_RED)
ICM_sm_LIGHT_GREEN = servo_motor.motor(addr=servo_motor.LIGHT_GREEN)
ICM_sm_LIGHT_YELLOW = servo_motor.motor(addr=servo_motor.LIGHT_YELLOW)
ICM_ult0=ultrasonic.ultrasonic_sensor(0)
ICM_ult1=ultrasonic.ultrasonic_sensor(1)
ICM_ult4=ultrasonic.ultrasonic_sensor(4)
ICM_ult2=ultrasonic.ultrasonic_sensor(2)
ICM_serS1 = servos.servos(servos.S1)
ICM_serS2 = servos.servos(servos.S2)
ICM_serS3 = servos.servos(servos.S3)
ICM_serS4 = servos.servos(servos.S4)
ICM_dcmM1 = DC_motor.motor(DC_motor.M1)
ICM_dcmM2 = DC_motor.motor(DC_motor.M2)
ICM_dcmM3 = DC_motor.motor(DC_motor.M3)
ICM_dcmM4 = DC_motor.motor(DC_motor.M4)
ICMBP_rec = recording.recording()
ICM_lightP13P0 = light_ring.light_ring(light_ring.P13P0)
ICM_lightP14P1 = light_ring.light_ring(light_ring.P14P1)
ICM_lightP15P2 = light_ring.light_ring(light_ring.P15P2)
ICM_lightP7P8 = light_ring.light_ring(light_ring.P7P8)
ICM_lightP9P12 = light_ring.light_ring(light_ring.P9P12)
ICM_lightP10P16 = light_ring.light_ring(light_ring.P10P16)
aiCamera = ai_camera.ai_camera()

def get_version():
    return "1.0.0"
