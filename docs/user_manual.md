- 在microbit中，iic的端口（port）没有意义，为兼容考虑保留。使用时不用填写



基本示例：

```python
import server_motor # 文件名

m1 = server_motor.motor() # 创建设备对象

while True:
    m1.run(20) # 对象使用
```





# color



<big>***文件：color.py***</big>



```python
WHITE = 0
BLACK = 1
RED   = 2
ORANGE= 3
YELLOW= 4
GREEN = 5
CYAN  = 6
BLUE  = 7
PURPLE= 8

COLOR_NONE = -1

```





# 伺服电机



<big>***文件：server_motor.py***</big>




```python

# 控制单个电机
class motor(iic_base.iic_base):
    def __init__(self, port=0, addr=0x50):
		pass
        
    def run(self, velocity:int): # 以多少的速度运行电机
        pass
        
    def run_for_time(self, velocity, duration, isBlock=True): # 以多少的速度运行多长时间
        pass
    
    def run_to_absolute_position(self, velocity, position, isBlock=True):# 以多少的速度运行到绝对位置
        pass
    
    def run_to_relative_position(self, velocity, position, isBlock=True):# 以多少的速度运行到相对位置
        pass

    
    
# 电机对，控制两个电机
class motor_pair():
    def __init__(self, port1=0, port2=0, addr1:int=0xff, addr2:int=0xff):  # port1 port2 左右电机
        pass
        
    def move(self, velocity1, velocity2):
        pass

    def move_for_time(self, velocity1, velocity2, duration):# 双电机以多少的速度转动多长时间
        pass
            
    def move_to_relative_position(self, velocity1, velocity2, position):# 双电机以多少的速度移动相对位置
        pass
```



## motor

```python
m1 = server_motor.motor(addr = 0x51)
```

> 控制单个电机

参数 `isBlock` 表示是否阻塞等待电机完成动作，默认`True` 等待电机完成动作。一般不会修改，下文不再介绍。



### run

> 以多少的速度运行电机

- `velocity` : 速度；-100 ~ 100

### run_for_time

> 以多少的速度运行多长时间电机

- `velocity` : 速度；-100 ~ 100
- `duration` : 运行时间； 单位 s

### run_to_absolute_position

> 以多少的速度运行到绝对位置

- `velocity` : 速度；-100 ~ 100
- `position` : 位置；单位 度°

### run_to_relative_position

> 以多少的速度运行到相对位置

- `velocity` : 速度；-100 ~ 100
- `position` : 位置；单位 度°





## motor_pair

```python
motor = server_motor.motor_pair(addr1=0x51, addr2=0x52)
```

> 控制两个电机；两个电机转动方向相反

### move

> 以多少的速度运行

- `velocity1` : 左电机速度；-100 ~ 100
- `velocity2` : 右电机速度；-100 ~ 100

### move_for_time

> 以多少的速度运行多长时间电机

- `velocity1` : 左电机速度；-100 ~ 100
- `velocity2` : 右电机速度；-100 ~ 100
- `duration` :  运行时间； 单位 s

### move_to_relative_position

> 以多少的速度运行到相对位置

- `velocity1` : 左电机速度；-100 ~ 100
- `velocity2` : 右电机速度；-100 ~ 100
- `position` : 位置；单位 度°



# 遥感传感器



<big>***文件：joystick.py***</big>



```python

class joystick_sensor(iic_base.iic_base):
    def __init__(self, port=0, addr:int=0x61):
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



## joystick_sensor

```python
js = joystick.joystick()
```

> 读取iic遥感的值

### get_x

> 在x轴的输出值 -100 ~ 100

### get_y

> 在y轴的输出值 -100 ~ 100


### is_up

>  操纵杆是否向上 
>
> True / False


### is_down

>  操纵杆是否向下
>
> True / False


### is_left

>  操纵杆是否向左 
>
> True / False


### is_right

>  操纵杆是否向右 
>
> True / False





# 录音



<big>***文件：recording.py***</big>



```python
GUNSHOT       = 1 # 枪声
LASER         = 2 # 激光
MOTORCYCLE    = 3 # 摩托车
WARBEGIN      = 4 # 战争开始
COUNTDOWN     = 5 # 倒计时
PLAYRECORDING = 6 # 播放录音

class recording(iic_base.iic_base):
    def __init__(self, port=0, addr=0x18):
        pass

    def voice(self, index:int):
        pass
```



## recording

```python
re = recording.recording()
```

### voice

> 按照给的索引播放声音播放

- `index` : 播放的索引；值为 `GUNSHOT` 等；





#  六路灰度传感器



<big>***文件：six_gry.py***</big>



```python
class six_gray_sensor(iic_base.iic_base):
    def __init__(self, port=0, addr=0x70):
        pass

    def gray_study(self): # 灰度学习
        pass

    def gray(self, port=None): # 灰度
        pass
    
    def color(self, port=None): # 颜色
        spass

    def black(self, port=None): # 黑线
        pass
```



## six_gray_sensor

```python
sgs = six_gry.six_gray_sensor()
```

### gray_study

> 灰度学习 （不会阻塞等待学习完成。时间大约为5s）

### gray

> 得到灰度值 0 - 255

- `port` 

  > 值为`None`时，以列表返回6路值；
  >
  > 值为 0~5时，返回其中一路的值

### color

> 得到识别的颜色；
>
> 红、黄、绿、青、蓝、紫

- `port` 

  > 值为`None`时，以列表返回6路值；
  >
  > 值为 0~5时，返回其中一路的值、
  >
  > <mark>颜色判断需要用 color.py 中的定义</mark>

### black

> 得到识别到的黑线

- `port` 

  > 值为`None`时，以列表返回6路值；
  >
  > 值为 0~5时，返回其中一路的值、
  >
  > 1 / 0 (或者用color.py 中的定义判断)



# OLED屏幕



<big>***文件：oled.py***</big>



```python
class oled(iic_base.iic_base):
    def __init__(self, port=0, addr=0x3c):
        pass
        
    def set_text(self, x, y, text, color=1):
        pass

    def clear_screen(self):
        pass
```



## oled

```python
display_oled = oled.oled()
```

### set_text

> 显示字符

- `x` : 屏幕的x坐标；0~120
- `y` : 屏幕的y坐标；0~5

- `text` : 显示的文本字符串
- `color` ：1 以白字显示；0 以黑字显示

### clear_screen

> 清屏



# 直流电机



<big>***文件：DC_motor.py***</big>



```python
M1
M2 
M3 
M4 

class motor():
    def __init__(self, port):
        pass

    def run(self, velocity): # -255 ~ 255
        pass


class motor_pair():
    def __init__(self, port1, port2):
       pass
        
    def move(self, velocity1, velocity2): # -255 ~ 255
        pass
```



## motor

```python
m1 = DC_motor.motor(DC_motor.M1)
```

### run

> 控制以多少的速度运行

- `velocity` : 以多少的速度运行；-255 ~ 255





## motor_pair

```python
motor = DC_motor.motor_pair(DC_motor.M1, DC_motor.M2)
```

### move

- `velocity1`  :  左电机以多少的速度运行；-255 ~ 255
- `velocity2`  :  右电机以多少的速度运行；-255 ~ 255





# 舵机



<big>***文件：servos.py***</big>



```python

S1 
S2 
S3 
S4 

class servos():
    def __init__(self, port):
        pass

    def angle(self, angle:int): # 设置角度 0 - 180
        pass
```



## servos

```python
ser = servos.servos(servos.S1)
```



### angle

> 设置舵机角度

- `angle` : 舵机角度。0~180





# 灯环



<big>***文件：light_ring.py***</big>



```python
P13P0
P14P1
P15P2

P7P8 
P9P12  
P10P16


class light_ring():
    def __init__(self, port):
        pass
    def light(self, light): # 设置亮度 0 - 255
        pass
    def color(self, color):
        pass
```





## light_ring

```python
lr = light_ring.light_ring(light_ring.P13P0)
```



### light

> 设置灯环亮度

- `light` : 亮度；0 ~ 255



### color

> 设置灯环颜色

- `color` 

  > - 可以为 如 （255， 0， 0）的元组作为形参
  > - 也可以使用 color.py 文件里定义好的颜色



# 超声波传感器



<big>***文件：ultrasonic.py***</big>



```python
P13P0 
P14P1
P15P2 

P7P8   
P9P12  
P10P16 

class ultrasonic_sensor:
    def __init__(self, port):
        pass
        
    def get(self): #cm
        pass
```



## ultrasonic_sensor

```python
ultr = ultrasonic.ultrasonic_sensor(ultrasonic.P13P0)
```



### get

> 得到测量的距离，单位为 mc



