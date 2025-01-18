import iic_base

font = [0] * 128

font[0] = 0x0022d422
font[1] = 0x0022d422
font[2] = 0x0022d422
font[3] = 0x0022d422
font[4] = 0x0022d422
font[5] = 0x0022d422
font[6] = 0x0022d422
font[7] = 0x0022d422
font[8] = 0x0022d422
font[9] = 0x0022d422
font[10] = 0x0022d422
font[11] = 0x0022d422
font[12] = 0x0022d422
font[13] = 0x0022d422
font[14] = 0x0022d422
font[15] = 0x0022d422
font[16] = 0x0022d422
font[17] = 0x0022d422
font[18] = 0x0022d422
font[19] = 0x0022d422
font[20] = 0x0022d422
font[21] = 0x0022d422
font[22] = 0x0022d422
font[23] = 0x0022d422
font[24] = 0x0022d422
font[25] = 0x0022d422
font[26] = 0x0022d422
font[27] = 0x0022d422
font[28] = 0x0022d422
font[29] = 0x0022d422
font[30] = 0x0022d422
font[31] = 0x0022d422
font[32] = 0x00000000
font[33] = 0x000002e0
font[34] = 0x00018060
font[35] = 0x00afabea
font[36] = 0x00aed6ea
font[37] = 0x01991133
font[38] = 0x010556aa
font[39] = 0x00000060
font[40] = 0x000045c0
font[41] = 0x00003a20
font[42] = 0x00051140
font[43] = 0x00023880
font[44] = 0x00002200
font[45] = 0x00021080
font[46] = 0x00000100
font[47] = 0x00111110
font[48] = 0x0007462e
font[49] = 0x00087e40
font[50] = 0x000956b9
font[51] = 0x0005d629
font[52] = 0x008fa54c
font[53] = 0x009ad6b7
font[54] = 0x008ada88
font[55] = 0x00119531
font[56] = 0x00aad6aa
font[57] = 0x0022b6a2
font[58] = 0x00000140
font[59] = 0x00002a00
font[60] = 0x0008a880
font[61] = 0x00052940
font[62] = 0x00022a20
font[63] = 0x0022d422
font[64] = 0x00e4d62e
font[65] = 0x000f14be
font[66] = 0x000556bf
font[67] = 0x0008c62e
font[68] = 0x0007463f
font[69] = 0x0008d6bf
font[70] = 0x000094bf
font[71] = 0x00cac62e
font[72] = 0x000f909f
font[73] = 0x000047f1
font[74] = 0x0017c629
font[75] = 0x0008a89f
font[76] = 0x0008421f
font[77] = 0x01f1105f
font[78] = 0x01f4105f
font[79] = 0x0007462e
font[80] = 0x000114bf
font[81] = 0x000b6526
font[82] = 0x010514bf
font[83] = 0x0004d6b2
font[84] = 0x0010fc21
font[85] = 0x0007c20f
font[86] = 0x00744107
font[87] = 0x01f4111f
font[88] = 0x000d909b
font[89] = 0x00117041
font[90] = 0x0008ceb9
font[91] = 0x0008c7e0
font[92] = 0x01041041
font[93] = 0x000fc620
font[94] = 0x00010440
font[95] = 0x01084210
font[96] = 0x00000820
font[97] = 0x010f4a4c
font[98] = 0x0004529f
font[99] = 0x00094a4c
font[100] = 0x000fd288
font[101] = 0x000956ae
font[102] = 0x000097c4
font[103] = 0x0007d6a2
font[104] = 0x000c109f
font[105] = 0x000003a0
font[106] = 0x0006c200
font[107] = 0x0008289f
font[108] = 0x000841e0
font[109] = 0x01e1105e
font[110] = 0x000e085e
font[111] = 0x00064a4c
font[112] = 0x0002295e
font[113] = 0x000f2944
font[114] = 0x0001085c
font[115] = 0x00012a90
font[116] = 0x010a51e0
font[117] = 0x010f420e
font[118] = 0x00644106
font[119] = 0x01e8221e
font[120] = 0x00093192
font[121] = 0x00222292
font[122] = 0x00095b52
font[123] = 0x0008fc80
font[124] = 0x000003e0
font[125] = 0x000013f1
font[126] = 0x00841080
font[127] = 0x0022d422

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


        