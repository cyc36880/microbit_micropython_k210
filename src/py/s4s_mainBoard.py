# s4s_mainBoard.py
import iic_base
import struct

class s4s_mainBoard(iic_base.iic_base):
    CHARGING_REG        = 0x00
    AMBIENT_LIGHT_REG   = 0x05
    RTC_REG             = 0x0A
    SERVO_REG           = 0x0F
    GYROSCOPE_REG       = 0x14
    VOICE_REG           = 0x1E
    ENCODER_MOTOR_REG   = [0x50, 0x5A, 0x64, 0x6E]

    def __init__(self, port=0, addr=0x05):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)

    # ---------------- 充电管理 ----------------
    def charging_get_state(self):
        """返回 (is_charging:bool, voltage:int 0~100)"""
        is_charging = self._handle.read_reg(self.CHARGING_REG+0, 1)[0]
        charging_voltage = self._handle.read_reg(self.CHARGING_REG+1, 1)[0]
        return is_charging, charging_voltage

    # ---------------- 氛围灯 ----------------
    def ambient_light_set_state(self, light=None, color=None):
        """
        light : 0~255 , None 表示保持
        color : (r,g,b) 或 None 表示保持
        """
        if light is not None:
            light = max(0, min(255, int(light)))
            self._handle.write_reg(self.AMBIENT_LIGHT_REG, [light])
        if color is not None:
            if len(color) != 3:
                raise ValueError("color must be (r,g,b)")
            self._handle.write_reg(self.AMBIENT_LIGHT_REG + 1, list(color))

    # ---------------- RTC ----------------
    def rtc_set_date(self, year, month, day):
        """year 0~99 , month 1~12 , day 1~31"""
        self._handle.write_reg(self.RTC_REG+1, [0, month, day, year])

    def rtc_set_time(self, hour, minute, second):
        self._handle.write_reg(self.RTC_REG, [hour, minute, second])

    def rtc_get_date(self):
        buf = self._handle.read_reg(self.RTC_REG+1, 4)
        return buf[3], buf[1], buf[2], buf[0]   # year, month, day, week

    def rtc_get_time(self):
        buf = self._handle.read_reg(self.RTC_REG, 3)
        return buf[0], buf[1], buf[2]           # hour, minute, second

    # ---------------- 舵机 ----------------
    def servo_set_angle(self, servo_id, angle):
        """servo_id 0/1 , angle 0~180"""
        if servo_id > 1:
            raise ValueError("servo_id only 0 or 1")
        self._handle.write_reg(self.SERVO_REG + servo_id, [angle])

    # ---------------- 陀螺仪 ----------------
    def gyro_enable(self, en: bool):
        self._handle.write_reg(self.GYROSCOPE_REG, [int(en)])

    def gyro_set_state(self, state):
        """0 空闲  1 开始校准  2 重置偏航角"""
        self._handle.write_reg(self.GYROSCOPE_REG + 1, [state])

    def gyro_get_state(self):
        return self._handle.read_reg(self.GYROSCOPE_REG + 1, 1)[0]

    def gyro_get_acc(self):
        buf = self._handle.read_reg(self.GYROSCOPE_REG + 2, 6)
        accX = struct.unpack('>h', bytes(buf[0:2]))[0]
        accY = struct.unpack('>h', bytes(buf[2:4]))[0]
        accZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        accX = accX if accX < 32768 else accX - 65536
        accY = accY if accY < 32768 else accY - 65536
        accZ = accZ if accZ < 32768 else accZ - 65536
        return accX, accY, accZ # accX, accY, accZ

    def gyro_get_gyro(self):
        buf = self._handle.read_reg(self.GYROSCOPE_REG + 4, 6)
        gyroX = struct.unpack('>h', bytes(buf[0:2]))[0]
        gyroY = struct.unpack('>h', bytes(buf[2:4]))[0]
        gyroZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        gyroX = gyroX if gyroX < 32768 else gyroX - 65536
        gyroY = gyroY if gyroY < 32768 else gyroY - 65536
        gyroZ = gyroZ if gyroZ < 32768 else gyroZ - 65536
        return gyroX, gyroY, gyroZ # gyroX, gyroY, gyroZ

    def gyro_get_angle(self):
        buf = self._handle.read_reg(self.GYROSCOPE_REG + 6, 6)
        angleX = struct.unpack('>h', bytes(buf[0:2]))[0]
        angleZ = struct.unpack('>h', bytes(buf[4:6]))[0]
        angleY = struct.unpack('>h', bytes(buf[2:4]))[0]
        angleX = angleX if angleX < 32768 else angleX - 65536
        angleY = angleY if angleY < 32768 else angleY - 65536
        angleZ = angleZ if angleZ < 32768 else angleZ - 65536
        return angleX, angleY, angleZ # angleX, angleY, angleZ

    # ---------------- 编码电机 ----------------
    def _motor_reg(self, motor_id):
        if motor_id > 3:
            raise ValueError("motor_id only 0~3")
        return self.ENCODER_MOTOR_REG[motor_id]

    def encoder_motor_set_mode(self, motor_id, mode):
        """mode: 0 直流  1 位置环  2 速度环"""
        self.write_bytes(self._motor_reg(motor_id), [mode])

    def encoder_motor_set_power(self, motor_id, power):
        """power -1000~1000"""
        data = list(struct.unpack('BB', struct.pack('>h', int(power))))
        self.write_bytes(self._motor_reg(motor_id) + 1, data)

    def encoder_motor_set_position(self, motor_id, position):
        """position int32"""
        data = list(struct.unpack('BBBB', struct.pack('>i', int(position))))
        self.write_bytes(self._motor_reg(motor_id) + 2, data)

    def encoder_motor_get_position(self, motor_id):
        buf = self.read_bytes(self._motor_reg(motor_id) + 3, 4)
        return struct.unpack('>i', buf)[0]

    def encoder_motor_set_position_pid(self, motor_id, kp, ki, kd):
        data = [int(kp) & 0xFF, int(ki) & 0xFF, int(kd) & 0xFF]
        self.write_bytes(self._motor_reg(motor_id) + 4, data)

    def encoder_motor_set_velocity_pid(self, motor_id, kp, ki, kd):
        data = [int(kp) & 0xFF, int(ki) & 0xFF, int(kd) & 0xFF]
        self.write_bytes(self._motor_reg(motor_id) + 5, data)
        