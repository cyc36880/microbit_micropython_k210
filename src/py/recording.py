import iic_base

GUNSHOT       = 1 # 枪声
LASER         = 2 # 激光
MOTORCYCLE    = 3 # 摩托车
WARBEGIN      = 4 # 战争开始
COUNTDOWN     = 5 # 倒计时
PLAYRECORDING = 6 # 播放录音

class recording(iic_base.iic_base):
    def __init__(self, port=0, addr=0x18):
        super().__init__(port, addr)

    def voice(self, index:int):
        self.write_bytes([index])