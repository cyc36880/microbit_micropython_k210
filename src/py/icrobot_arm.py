import iic_base
import time


class icr_arm(iic_base.iic_base):
    def __init__(self, port=0, addr=0x06):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)
    
    def open(self, isBlock=False):
        self._handle.write_bytes([1, 0, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self._handle.read_bytes(5)[0] == 0x0b:
                time.sleep_ms(10)

    def close(self, isBlock=False):
        self._handle.write_bytes([2, 0, 0, 0, 0])
        if isBlock:
            time.sleep_ms(10)
            while self._handle.read_bytes(5)[0] == 0x0b:
                time.sleep_ms(10)


