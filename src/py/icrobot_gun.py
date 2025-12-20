import iic_base
import time


class icr_gun(iic_base.iic_base):
    def __init__(self, port=0, addr=0x0B):
        super().__init__(port, addr)

    def fire(self, num=1, isBlock=True):
        self.write_bytes([1, num, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self.read_bytes(5)[0] != 0x0b:
                time.sleep_ms(10)
