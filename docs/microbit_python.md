- 只能输入的称为 xx传感器，否则直接称为 xx

- 所有port 以 `1` 作为开始



# iic_base

- iic_base.py


```python
class iic_base:
   def __init__(self, port:int, addr:int):
    	pass
    
    def is_ready(self): # 是否在线
        pass
    
	def write_bytes(self, data:list, repeat=False):
        pass

    def read_bytes(self, length:int, repeat=False):
        pass
    
iic_init_flag = False
def iic_init():
    global iic_init_flag
    if iic_init_flag == False:
        iic_init_flag = True
        pass # 初始化iic
    	
iic_init()
```





# color

- color.py

```python
MAGENTA = 0
BLACK = 1 # 黑色必须为1；用于灰度黑线判断
PURPLE = 2
BLUE = 3
AZURE = 4
TURQUOISE = 5
GREEN = 6
YELLOW = 7
ORANGE = 8
RED = 9
WHITE = 10
UNKNOWN = -1
```





# 伺服电机

- server_motor.py


```python
# 控制单个电机
class motor(iic_base)：
	def __init__(self, port, addr):
        pass
    def run(self, velocity:int): # 以多少的速度运行电机
        pass
    
    def run_for_time(self, velocity, duration): # 以多少的速度运行多长时间
        pass
    
    def run_to_absolute_position(self, velocity, position):# 以多少的速度运行到绝对位置
        pass
    
    def run_to_relative_position(self, velocity, position):# 以多少的速度运行到相对位置
        pass

    
# 电机对，控制两个电机
class motor_pair(iic_base):
    def __init__(self, port1, port2, addr1:int, addr2:int):
        pass
    
    def move(self, velocity1，velocity2): #双电机恒速转动
        pass
    
    def move_for_time(self, velocity1，velocity2, duration): # 双电机以多少的速度转动多长时间
        pass
    
    def move_to_relative_position(self, velocity1，velocity2, position): # 双电机以多少的速度移动相对位置
        pass
```





# 摇杆传感器

- ### Joystick.py

```python
class joystick_sensor(iic_base):
	def __init__(self, port, addr:int):
        pass
    
    def get_x(self): #在x轴的输出值 -100 ~ 100
        pass
    
    def get_y(self): #在y轴的输出值 -100 ~ 100
        pass
    
    def is_up(self):# 操纵杆是否向上 
        pass
    
    def is_down(self): # 操纵杆是否向下 
        pass
    
    def is_left(self): # 是否向左
        pass
    
    def is_right(self): # 是否向右
        pass
    
```





# 录音



- recording.py

```python
MOTORCYCLE = 0 # 摩托车
WARBEGIN   = 1 # 战争开始
GUNSHOT    = 2 # 枪声
RECORD     = 3 # 录音


class recording(iic_base):
	def __init__(self, port:int, addr:int):
        pass
    
    def voice(self, index:int): # 按照给的索引播放声音播放
        pass
```





# 六路灰度传感器

- six_gray_sensor.py

```python
class six_gray_sensor:
    def __init__(self, port:int, addr:int):
        pass
    
	def mode(self, mod):  # 设置工作模式
        pass
    
    def gray_study(self): # 灰度学习
        # 阻塞？
        pass
    
    def black(self, port:int=None):# 是否检测到黑线 无port得到六个，有获取对应一个 port ：0-5
        pass
    
    def gray(self, port:int=None): # 得到灰度值 无port得到六个，有获取对应一个 port ：0-5
        pass
    
    def color(self, port:int=None): # 得到颜色 无port得到六个，有获取对应一个 port ：0-5
        pass
```





# OLED

```python
class oled:
    def __init__(self, port:int, addr:int):
        # clear
        pass
    
	def set_text(self, x, y, text, color):
        pass
    
    def clear_screen(srlf):
        pass
```







# 直流电机

- DC_motor.py

```python
# 控制单个电机
class motor:
    def __init__(self, port):
        pass
    def run(velocity): # -100 ~ 100
        pass

    
# 电机对，控制两个电机
class motor_pair:
    def __init__(self, port1, port2):
        pass
    
    def move(velocity1, velocity2): # -100 ~ 100
		pass
```







# 舵机

- Servos.py

```python
class servos:
    
    def __init__(self, port):
        pass
    
    def angle(self, angle:int): # 设置角度 0 - 180
        pass
```





# 灯环

- light_ring.py

```python

class light_ring: # ws2812 ???
    def __init__(self, port):
		pass
    
    def light(self, light): # 设置亮度
        pass
    
    def color(self, color:tuple): # 设置颜色；color为 (255，0，0 ) 这样一个元组 或者 color 里的常量
        # color type判断
        pass
```





# 超声波传感器

- ultrasonic.py

```python
class ultrasonic_sensor:
	def __init__(self, port):
        pass
    
    def get(self): # 单位为cm
        pass
```



