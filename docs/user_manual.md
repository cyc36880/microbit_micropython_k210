- 在microbit中，iic的端口（port）没有意义，为兼容考虑保留。使用时不用填写



本文假设读者拥有一定的python基础，对于python的基本使用不再解释。下面给出使用的基本示例供参考



示例：

```python
import server_motor # 导入库（文件名）

m1 = server_motor.motor(addr = server_motor.LIGHT_RED) # 创建设备对象

while True:
    m1.run(20) # 对象使用
```



# iic_base



<big>***文件：iic_base.py***</big>



```python
class iic_base:
    def is_ready(self): # 是否在线
        pass
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
GENERAL      # 通用地址
LIGHT_RED    # 红灯
LIGHT_GREEN  # 绿灯
LIGHT_BLUE   # 蓝灯
LIGHT_YELLOW # 黄灯

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
	def get_absolute_position(self): # 得到电机的绝对位置
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

> micro\:bit 下，必须给出电机的地址。默认地址无法使用



## motor

```python
m1 = server_motor.motor(addr = server_motor.LIGHT_RED)
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

### get_absolute_position

> 得到电机的绝对位置



## motor_pair

```python
motor = server_motor.motor_pair(addr1=server_motor.LIGHT_RED, addr2=server_motor.LIGHT_BLUE)
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



# 摇杆传感器



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
GUNSHOT        # 枪声
LASER          # 激光
MOTORCYCLE     # 摩托车
WARBEGIN       # 战争开始
COUNTDOWN      # 倒计时
PLAYRECORDING  # 播放录音

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



<big>***文件：six_gray.py***</big>



```python
class six_gray_sensor(iic_base.iic_base):
    def __init__(self, port=0, addr=0x70):
        pass

    def gray_study(self): # 灰度学习
        pass

    def gray(self, port=None): # 灰度
        pass
    
    def color(self, port=None): # 颜色
        pass

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

    def write_angle(self, angle:int): # 设置角度 0 - 180
        pass
```



## servos

```python
ser = servos.servos(servos.S1)
```



### write_angle

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

> 得到测量的距离，单位为 cm





# AI 相机



<big>***文件：ai_camera.py***</big>



```python
AI_CAMERA_SYS     # 系统
AI_CAMERA_COLOR   # 颜色获取
AI_CAMERA_PATCH   # 色块追踪
AI_CAMERA_TAG     # 标签识别
AI_CAMERA_LINE    # 线条识别
AI_CAMERA_20_CLASS# 20类物体识别
AI_CAMERA_QRCODE  # 二维码识别
AI_CAMERA_FACE_DE # 人脸检测
AI_CAMERA_FACE_RE # 人脸识别
AI_CAMERA_DEEP_LEARN # 深度学习
AI_CAMERA_CARD # 卡片识别


class ai_camera(iic_base.iic_base):
    def __init__(self, port=0, addr=0x24):
        pass
    def set_sys_mode(self, mode:int): # 设置系统模式
        pass
    def get_sys_mode(self): # 获取系统模式
        pass
    def get_color_rgb(self): # 获取颜色识别的RGB值
        pass
    def set_find_color(self, color):
        pass
    def face_study(self): # 人脸识别学习
        pass 
    def deep_learn_study(self): # 深度学习
         pass
    def get_qrcode_content(self): # 获取二维码信息
         pass
    def get_identify_num(self, features, total=0): # 得到识别的数量
         pass
    def get_identify_id(self, features, index=0): # 得到识别的ID
         pass
    def get_identify_rotation(self, features, index=0): # 得到识别的角度
         pass
    def get_identify_position(self, features, index=0): # 得到识别的位置
		pass
    def get_identify_confidence(self, features, id): # 得到识别的置信度
        pass
```



在调用对应的对象时，应先确定该功能是否有相关的数据，否则会返回0

## ai_camera

```python
aic = ai_camera.ai_camera()
```



### set_sys_mode

> 设置工作模式
>
> 取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD



### get_sys_mode

> 获取系统的工作模式



### get_color_rgb

> 得到颜色识别的rgb值
>
> 返回：（r， g， b）



### set_find_color

> 设置色块追踪的颜色
>
> 取值为 `color.py` 文件下的值，需要首先确定支持该颜色
>
> 目前 （红 绿 蓝 黄 黑 白）



### face_study

> 使人脸识别学习



### deep_learn_study

> 使深度学习



### get_qrcode_content

> 得到二维码识别的字符信息



### get_identify_num

> 得到识别到的数量

- `features` : 功能选择，取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD

- `total` ：默认为0，在人脸识别下，设置为1，返回检测到（非识别到）所有人脸的数量



### get_identify_id

> 得到被识别物体的id

- `features` : 功能选择，取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD
- `index` ：对于可以多物体识别，index用于选择第几个物体的id （0~3）



### get_identify_rotation

> 得到被识别物体的旋转角度
>
> 返回：0~359

- `features` : 功能选择，取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD

- `index` ：对于可以多物体识别，index用于选择第几个物体的id （0~3）



### get_identify_position

> 得到被识别物体的位置
>
> 返回 [x, y, w, h]

- `features` : 功能选择，取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD

- `index` ：对于可以多物体识别，index用于选择第几个物体的id （0~3）



### get_identify_confidence

> 得到被识别物体的置信度
>
> <mark>只有深度学习可以使用并读取到</mark>
>
> 返回：0~100

- `features` : 功能选择，取值：AI_CAMERA_COLOR ~ AI_CAMERA_CARD

- `id` ：选择哪个id的置信度 （0~3），不在范围内返回0

