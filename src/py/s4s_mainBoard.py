# s4s_mainBoard.py
from microbit import *
import iic_base
import struct

class s4s_mainBoard(iic_base.iic_base):
    CHARGING_REG           = 0x00
    AMBIENT_LIGHT_REG      = 0x05
    RTC_REG                = 0x0A
    SERVO_REG              = 0x0F
    GYROSCOPE_REG          = 0x14
    VOICE_REG              = 0x1E
    ENCODER_MOTOR_REG      = [0x50, 0x5A, 0x64, 0x6E]
    ENCODER_MOTOR_PAIR_REG = 0x78

    def __init__(self, port=0, addr=0x0F):
        super().__init__(port, addr)
    
    def _ret_data_(self, data, port):
        if port is None:
            return data
        else:
            return data[port]
        
    # ---------------- 充电管理 ----------------
    def charging_get_state(self):
        """返回 (is_charging:bool, voltage:int 0~100)"""
        charging_voltage = self.read_reg(self.CHARGING_REG+0, 1)[0]
        return charging_voltage

    # ---------------- 氛围灯 ----------------
    def ambient_light_set_state(self, light=None, color=None):
        """
        light : 0~255 , None 表示保持
        color : (r,g,b) 或 None 表示保持
        """
        if light is not None:
            light = max(0, min(255, int(light)))
            self.write_reg(self.AMBIENT_LIGHT_REG, [light])
        if color is not None:
            if len(color) != 3:
                raise ValueError("color must be (r,g,b)")
            self.write_reg(self.AMBIENT_LIGHT_REG + 1, list(color))

    # ---------------- RTC ----------------
    def rtc_set_date(self, year, month, day):
        """year 0~99 , month 1~12 , day 1~31"""
        self.write_reg(self.RTC_REG+1, [0, month, day, year])

    def rtc_set_time(self, hour, minute, second):
        self.write_reg(self.RTC_REG, [hour, minute, second])

    def rtc_get_date(self, sel=None):
        buf = self.read_reg(self.RTC_REG+1, 4)
        return self._ret_data_( [buf[3], buf[1], buf[2], buf[0]], sel )   # year, month, day, week

    def rtc_get_time(self, sel=None):
        buf = self.read_reg(self.RTC_REG, 3)
        return self._ret_data_( [buf[0], buf[1], buf[2]], sel )           # hour, minute, second

    # ---------------- 舵机 ----------------
    def servo_set_angle(self, servo_id, angle):
        """servo_id 0/1 , angle 0~180"""
        if servo_id > 1:
            raise ValueError("servo_id only 0 or 1")
        self.write_reg(self.SERVO_REG + servo_id, [angle])

    # --------------- 连续舵机 ---------------
    def continuous_servo_set_speed(self, servo_id, speed):
        """speed -100~100"""
        if servo_id > 1:
            raise ValueError("servo_id only 0 or 1")
        self.write_reg(self.SERVO_REG + servo_id + 2, [struct.unpack('B', struct.pack('b', speed))[0]])

    # ---------------- 陀螺仪 ----------------
    def gyro_enable(self, en: bool):
        self.write_reg(self.GYROSCOPE_REG, [int(en)])

    def gyro_set_state(self, state):
        """0 空闲  1 开始校准  2 重置偏航角"""
        self.write_reg(self.GYROSCOPE_REG + 1, [state])

    def gyro_get_state(self):
        return self.read_reg(self.GYROSCOPE_REG + 1, 1)[0]

    def gyro_get_acc(self, sel=None):
        buf = self.read_reg(self.GYROSCOPE_REG + 2, 6)
        accX = struct.unpack('>h', bytes(buf[0:2]))[0]
        accY = struct.unpack('>h', bytes(buf[2:4]))[0]
        accZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        accX = accX if accX < 32768 else accX - 65536
        accY = accY if accY < 32768 else accY - 65536
        accZ = accZ if accZ < 32768 else accZ - 65536
        return self._ret_data_( [accX, accY, accZ], sel ) # accX, accY, accZ

    def gyro_get_gyro(self, sel=None):
        buf = self.read_reg(self.GYROSCOPE_REG + 3, 6)
        gyroX = struct.unpack('>h', bytes(buf[0:2]))[0]
        gyroY = struct.unpack('>h', bytes(buf[2:4]))[0]
        gyroZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        gyroX = gyroX if gyroX < 32768 else gyroX - 65536
        gyroY = gyroY if gyroY < 32768 else gyroY - 65536
        gyroZ = gyroZ if gyroZ < 32768 else gyroZ - 65536
        return self._ret_data_( [gyroX, gyroY, gyroZ], sel ) # gyroX, gyroY, gyroZ

    def gyro_get_angle(self, sel=None):
        buf = self.read_reg(self.GYROSCOPE_REG + 4, 6)
        angleX = struct.unpack('>h', bytes(buf[0:2]))[0]
        angleZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        angleY = struct.unpack('>h', bytes(buf[2:4]))[0]
        angleX = angleX if angleX < 32768 else angleX - 65536
        angleY = angleY if angleY < 32768 else angleY - 65536
        angleZ = angleZ if angleZ < 32768 else angleZ - 65536
        return self._ret_data_([angleX, angleY, angleZ], sel ) # angleX, angleY, angleZ

    def gyro_get_tilted(self):
        buf = self.read_reg(self.GYROSCOPE_REG + 5, 1)
        return buf[0]
    
    def gyro_get_orientation(self):
        buf = self.read_reg(self.GYROSCOPE_REG + 6, 1)
        return buf[0]

    # ---------------- 编码电机 ----------------
    def _motor_reg(self, motor_id):
        if motor_id > 3:
            raise ValueError("motor_id only 0~3")
        return self.ENCODER_MOTOR_REG[motor_id]

    def encoder_motor_get_angle(self, motor_id):
        buf = self.read_reg(self._motor_reg(motor_id) + 0, 4)
        return struct.unpack('>i', buf)[0]

    def encoder_motor_get_speed(self, motor_id):
        buf = self.read_reg(self._motor_reg(motor_id) + 1, 2)
        return struct.unpack('>h', buf)[0]
    
    def encoder_motor_get_power(self, motor_id):
        buf = self.read_reg(self._motor_reg(motor_id) + 2, 2)
        return struct.unpack('>h', buf)[0]
    
    def encoder_motor_reset_angle(self, motor_id):
        self.write_reg(self._motor_reg(motor_id) + 0, [0, 0, 0, 0])
    
    def encoder_motor_set_action(self, motor_id, action):
        self.write_reg(self._motor_reg(motor_id) + 3, [action])

    def encoder_motor_set_speed(self, motor_id, speed):
        """speed 0~..."""
        data = list(struct.unpack('BB', struct.pack('>h', int(speed))))
        self.write_reg(self._motor_reg(motor_id) + 4, data)

    def encoder_motor_set_power(self, motor_id, power):
        """power 0~100"""
        self.write_reg(self._motor_reg(motor_id) + 5, [power])

    def encoder_motor_set_ring(self, motor_id, ring):
        """ring 0~100"""
        data = list(struct.unpack('BB', struct.pack('>h', int(ring))))
        self.write_reg(self._motor_reg(motor_id) + 6, data)

    def encoder_motor_set_relative_angle(self, motor_id, angle):
        """angle 0~65535"""
        data = list(struct.unpack('BB', struct.pack('>h', int(angle))))
        self.write_reg(self._motor_reg(motor_id) + 7, data)

    def encoder_motor_set_run_time(self, motor_id, time):
        """time 0~65535"""
        data = list(struct.unpack('BB', struct.pack('>h', int(time))))
        self.write_reg(self._motor_reg(motor_id) + 8, data)


    # ---------------- 电机组 ----------------
    def encoder_motor_pair_set_action(self, action):
        self.write_reg(self.ENCODER_MOTOR_PAIR_REG+0, [action])
    
    def encoder_motor_pair_set_group(self, l_motor, r_motor):
        self.write_reg(self.ENCODER_MOTOR_PAIR_REG+1, [l_motor, r_motor])

    def encoder_motor_pair_set_run_speed(self, l_speed, r_speed):
        data1 = list(struct.unpack('BB', struct.pack('>h', int(l_speed))))
        data2 = list(struct.unpack('BB', struct.pack('>h', int(r_speed))))
        self.write_reg(self.ENCODER_MOTOR_PAIR_REG+2, data1+data2)

    def encoder_motor_pair_set_run_time(self, l_time):
        data = list(struct.unpack('BB', struct.pack('>h', int(l_time))))
        self.write_reg(self.ENCODER_MOTOR_PAIR_REG+3, data)

    # ------------------ 语音模块 -------------------------
    def voice_get_state(self):
        sleep(10)
        return self.read_reg(self.VOICE_REG, 1)[0]
