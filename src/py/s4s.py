from microbit import *
import s4s_gray
import s4s_mainBoard
import s4s_ultr
import music
import speech
mainBoard = s4s_mainBoard.s4s_mainBoard()
gray = s4s_gray.s4s_gray()
ultr = s4s_ultr.s4s_ultr()

def uartReadLine():
    ic_uart_read = uart.readline()
    if not ic_uart_read:
        return ""
    return ic_uart_read.strip()

def toggle(x,y):
  if display.get_pixel(x,y) > 0:
      display.set_pixel(x,y,0)
  else:
      display.set_pixel(x,y,9)

'''
电机【】以【】运行【0-...】【】
dir : 0 正转；1反转
state: 0圈，1度，2秒
data:
'''
def encoder_motor_run_dir_3state(motor, dir, state, data):
    if state == 0:
        mainBoard.encoder_motor_set_ring(motor, data)
        mainBoard.encoder_motor_set_action(motor, dir+5)
    elif state == 1:
        mainBoard.encoder_motor_set_relative_angle(motor, data)
        mainBoard.encoder_motor_set_action(motor, dir+7)
    elif state == 2:
        mainBoard.encoder_motor_set_run_time(motor, data)
        mainBoard.encoder_motor_set_action(motor, dir+9)

'''
电机【】以【】启动电机
dir : 0 正转；1反转
'''
def encoder_motor_run(motor, dir):
    mainBoard.encoder_motor_set_action(motor, dir+1)

'''
电机【】停止
'''
def encoder_motor_stop(motor):
    mainBoard.encoder_motor_set_action(motor, 0)

'''
电机【】速度【0-100】
'''
def encoder_motor_set_speed(motor, speed):
    mainBoard.encoder_motor_set_speed(motor, speed)

'''
电机【】位置
'''
def encoder_motor_get_angle(motor):
    return mainBoard.encoder_motor_get_angle(motor)

'''
电机【】速度
'''
def encoder_motor_get_speed(motor):
    return mainBoard.encoder_motor_get_speed(motor)

'''
电机【】设置当前位置为0
'''
def encoder_motor_reset_angle(motor):
    mainBoard.encoder_motor_reset_angle(motor)

'''
电机【】动力【-100~100】启动
'''
def encoder_motor_set_power(motor, power):
    mainBoard.encoder_motor_set_power(motor, abs(power))
    mainBoard.encoder_motor_set_action(motor, (power<0)+3)

'''
电机【】动力
'''
def encoder_motor_get_power(motor):
    return mainBoard.encoder_motor_get_power(motor)

''''
设置运动电机端口【】和【】
'''
def encoder_motor_pair_set_group(l_motor, r_motor):
    mainBoard.encoder_motor_pair_set_group(l_motor, r_motor)

'''
开始移动【】
state : 0前进；1后退；2左转；3右转
'''
def encoder_motor_pair_run(state):
    mainBoard.encoder_motor_pair_set_action(state+1)

'''
以【】移动【0~...】秒
state : 0前进；1后退；2左转；3右转
'''
def encoder_motor_pair_run_time(state, time):
    mainBoard.encoder_motor_pair_set_run_time(time)
    mainBoard.encoder_motor_pair_set_action(state+5)

'''
停止运动
'''
def encoder_motor_pair_stop():
    mainBoard.encoder_motor_pair_set_action(0)

'''
设置移动速度为【0-100】%
'''
def encoder_motor_pair_set_speed(l_speed, r_speed):
    mainBoard.encoder_motor_pair_set_run_speed(l_speed, r_speed)

'''
以【0-100】【0-100】%速度移动
'''
def encoder_motor_pair_set_run_speed(speed):
    encoder_motor_pair_set_speed(speed, speed)
