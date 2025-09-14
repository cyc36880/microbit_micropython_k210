import iic_base
import time


class icr_gun(iic_base.iic_base):
    def __init__(self, port=0, addr=0x0B):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)

    def fire(self, num=1, isBlock=True):
        self._handle.write_bytes([1, num, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self._handle.read_bytes(5)[0] != 0x0b:
                time.sleep_ms(10)
