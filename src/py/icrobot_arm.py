import iic_base
import time


class icr_arm(iic_base.iic_base):
    def __init__(self, port=0, addr=0x06):
        super().__init__(port, addr)
    
    def open(self, isBlock=False):
        self.write_bytes([1, 0, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self.read_bytes(5)[0] == 0x0b:
                time.sleep_ms(10)

    def close(self, isBlock=False):
        self.write_bytes([2, 0, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self.read_bytes(5)[0] == 0x0b:
                time.sleep_ms(10)


