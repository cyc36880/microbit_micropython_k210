import iic_base

font =\
(0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,
0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x0022d422,0x00000000,0x000002e0,
0x00018060,0x00afabea,0x00aed6ea,0x01991133,0x010556aa,0x00000060,0x000045c0,0x00003a20,0x00051140,0x00023880,0x00002200,0x00021080,0x00000100,0x00111110,0x0007462e,0x00087e40,0x000956b9,0x0005d629,
0x008fa54c,0x009ad6b7,0x008ada88,0x00119531,0x00aad6aa,0x0022b6a2,0x00000140,0x00002a00,0x0008a880,0x00052940,0x00022a20,0x0022d422,0x00e4d62e,0x000f14be,0x000556bf,0x0008c62e,0x0007463f,0x0008d6bf,
0x000094bf,0x00cac62e,0x000f909f,0x000047f1,0x0017c629,0x0008a89f,0x0008421f,0x01f1105f,0x01f4105f,0x0007462e,0x000114bf,0x000b6526,0x010514bf,0x0004d6b2,0x0010fc21,0x0007c20f,0x00744107,0x01f4111f,0x000d909b,
0x00117041,0x0008ceb9,0x0008c7e0,0x01041041,0x000fc620,0x00010440,0x01084210,0x00000820,0x010f4a4c,0x0004529f,0x00094a4c,0x000fd288,0x000956ae,0x000097c4,0x0007d6a2,0x000c109f,0x000003a0,0x0006c200,0x0008289f,
0x000841e0,0x01e1105e,0x000e085e,0x00064a4c,0x0002295e,0x000f2944,0x0001085c,0x00012a90,0x010a51e0,0x010f420e,0x00644106,0x01e8221e,0x00093192,0x00222292,0x00095b52,0x0008fc80,0x000003e0,0x000013f1,
0x00841080,0x0022d422)

_screen = [0]*1025
_ZOOM = 1

def cmd1(iic_handle, cmd):
    iic_handle.write_bytes([0, cmd % 256]) 

def cmd2(iic_handle, cmd1, cmd2):
    _buf = [0, cmd1, cmd2]
    iic_handle.write_bytes(_buf) 

def cmd3(iic_handle, cmd1, cmd2, cmd3):
    _buf = [0, cmd1, cmd2, cmd3]
    iic_handle.write_bytes(_buf)

def set_pos(iic_handle, col=0, page=0):
    cmd1(iic_handle, 0xb0 | page) # page number
    c = col * (1 + 1)
    cmd1(iic_handle, 0x00 | (c % 16)) # lower start column address
    cmd1(iic_handle, 0x10 | (c >> 4)) # upper start column address    

def clear_screen(iic_handle):
    for i in range(1024):
        _screen[i] = 0
    set_pos(iic_handle)
    _screen
    _screen[0] = 0x40
    iic_handle.write_bytes(_screen)

def showStringxy(iic_handle, x, y, s, color = 1):
    col = 0
    e = 0
    ind = 0
    for f in range(len(s)):
        e = font[ord(s[f])]
        for g in range(5):
            col = 0
            for h in range(5):
                if (e & (1 << (5 * g + h))):
                    col |= (1 << (h + 1))
            ind = (x + f) * 5 * (_ZOOM + 1) + y * 128 + g * (_ZOOM + 1) + 1
            if (color == 0):
                col = 255 - col
            _screen[ind] = col
            if (_ZOOM):
                _screen[ind + 1] = col
    set_pos(iic_handle, x * 5, y)
    ind0 = x * 5 * (_ZOOM + 1) + y * 128
    buf7 = _screen[ind0 : ind + 1]
    buf7[0] = 0x40
    iic_handle.write_bytes(buf7)



def _init(iic_handle):
    # 
    cmd1(iic_handle, 0xAE)       # SSD1306_DISPLAYOFF
    cmd1(iic_handle, 0xA4)       # SSD1306_DISPLAYALLON_RESUME
    cmd2(iic_handle, 0xD5, 0xF0) # SSD1306_SETDISPLAYCLOCKDIV
    cmd2(iic_handle, 0xA8, 0x3F) # SSD1306_SETMULTIPLEX
    cmd2(iic_handle, 0xD3, 0x00) # SSD1306_SETDISPLAYOFFSET
    cmd1(iic_handle, 0 | 0x0)    # line #SSD1306_SETSTARTLINE
    cmd2(iic_handle, 0x8D, 0x14) # SSD1306_CHARGEPUMP
    cmd2(iic_handle, 0x20, 0x00) # SSD1306_MEMORYMODE
    cmd3(iic_handle, 0x21, 0, 127) # SSD1306_COLUMNADDR
    cmd3(iic_handle, 0x22, 0, 63)  # SSD1306_PAGEADDR
    cmd1(iic_handle, 0xa0 | 0x1) # SSD1306_SEGREMAP
    cmd1(iic_handle, 0xc8)       # SSD1306_COMSCANDEC
    cmd2(iic_handle, 0xDA, 0x12) # SSD1306_SETCOMPINS
    cmd2(iic_handle, 0x81, 0xCF) # SSD1306_SETCONTRAST
    cmd2(iic_handle, 0xd9, 0xF1) # SSD1306_SETPRECHARGE
    cmd2(iic_handle, 0xDB, 0x40) # SSD1306_SETVCOMDETECT
    cmd1(iic_handle, 0xA6)       # SSD1306_NORMALDISPLAY
    cmd2(iic_handle, 0xD6, 1)    # zoom on
    cmd1(iic_handle, 0xAF)       # SSD1306_DISPLAYON
    clear_screen(iic_handle)

class oled(iic_base.iic_base):
    def __init__(self, port=0, addr=0x3c):
        self._handle = iic_base.iic_base(port, addr)
        super().__init__(port, addr)
        _init(self._handle)
        
    def set_text(self, x, y, text, color=1):
        showStringxy(self._handle, x, y, text, color)

    def clear_screen(self):
        clear_screen(self._handle)


        