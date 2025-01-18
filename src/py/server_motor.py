import iic_base
import time

servo_command_map = (
    (0x01, 0x01),
    (0x01, 0x02),
    (0x03, 0x03),
    (0x04, 0x04),
    (0x05, 0x05),
    
    (0x11, 0x06),
    (0x12, 0x07),
    (0x13, 0x08),
    (0x14, 0x09)
);

class motor_base(iic_base.iic_base):
    def __init__(self, port, addr):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)
        
    def _send_command(self, data:list): # 三个数据
        velocity = data[1]
        data[2] = int(data[2])
        velocity = int(velocity)
        velocity //= 2
        velocity = -50 if velocity<-50 else 50 if velocity > 50 else velocity
        send_data = [data[0]&0xff, velocity&0xff, (data[2]>>8)&0xff, data[2]&0xff]
        self._handle.write_bytes(send_data)
        
    def _get_data(self):
        data = self._handle.read_bytes(6)
        ret_data = [data[0], (data[1]<<8)|data[2], (data[3]<<8)|data[4], data[5]]
        return ret_data
        
    def is_end_run(self):
        data = self._get_data()
        cmd = data[3]
        if cmd==0x01 or cmd==0x06:
            return 1
        if cmd==0x00 or cmd==0x0B or cmd==0x0a:
            return 1
        return 0


# 控制单个电机
class motor(iic_base.iic_base):
    def __init__(self, port=0, addr=0x50):
        self._handle = motor_base(port, addr)
        super().__init__(port, addr)
        
    def run(self, velocity:int): # 以多少的速度运行电机
        self._handle._send_command([0x01, velocity, 0])
        
    def run_for_time(self, velocity, duration, isBlock=True): # 以多少的速度运行多长时间
        if 0 < duration < 0.1:
            duration = 0.1
        duration *= 10
        self._handle._send_command([0x02, velocity, duration])
        if isBlock:
            time.sleep_ms(10)
            while not self._handle.is_end_run():
                pass
    
    def run_to_absolute_position(self, velocity, position, isBlock=True):# 以多少的速度运行到绝对位置
        self._handle._send_command([0x03, velocity, position])
        if isBlock:
            time.sleep_ms(10)
            while not self._handle.is_end_run():
                pass
    
    def run_to_relative_position(self, velocity, position, isBlock=True):# 以多少的速度运行到相对位置
        self._handle._send_command([0x04, velocity, position])
        if isBlock:
            time.sleep_ms(10)
            while not self._handle.is_end_run():
                pass

    
    
# 电机对，控制两个电机
class motor_pair():
    def __init__(self, port1=0, port2=0, addr1:int=0xff, addr2:int=0xff):
        self._handle_left  = motor(port1, addr1)
        self._handle_right = motor(port2, addr2)
        
    def move(self, velocity1, velocity2):
        self._handle_left.run(-velocity1)
        self._handle_right.run(velocity2)

    def move_for_time(self, velocity1, velocity2, duration):# 双电机以多少的速度转动多长时间
        self._handle_left.run_for_time(-velocity1, duration, False)
        self._handle_right.run_for_time(velocity2, duration, True)
        while not self._handle_left._handle.is_end_run():
            pass
            
    def move_to_relative_position(self, velocity1, velocity2, position):# 双电机以多少的速度移动相对位置
        self._handle_left.run_to_relative_position(velocity1, -position, False)
        self._handle_right.run_to_relative_position(velocity2, position, True)
        while not self._handle_left._handle.is_end_run():
            pass
        

        

        