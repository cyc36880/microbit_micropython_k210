import iic_base
from color import *
AI_CAMERA_SYS=0
AI_CAMERA_COLOR=1
AI_CAMERA_PATCH=2
AI_CAMERA_TAG=3
AI_CAMERA_LINE=4
AI_CAMERA_20_CLASS=5
AI_CAMERA_QRCODE=6
AI_CAMERA_FACE_ATTRIBUTE=7
AI_CAMERA_FACE_RE=8
AI_CAMERA_DEEP_LEARN=9
AI_CAMERA_CARD=10
AI_CAMERA_WIFI_SERVER=11
AI_CAMERA_SETTING = 12


register_addr = (0,15,30,45,60,75,90,105,120,135,150, 165, 180)
color_tab = {
    WHITE:6,
    BLACK:5,
    RED: 1,
    YELLOW: 4,
    GREEN: 2,
    BLUE  : 3,
}
patch_color_tab = {
    6: WHITE,
    5:BLACK,
    1:RED,
    4:YELLOW,
    2:GREEN,
    3:BLUE,
}

obj_sys = {}
obj_color = {}
obj_patch = {
    "num":0x01, 
    "id":0x00,
    "pos":0x02,
}
obj_tag = {
    "num":0x00,
    "target":
    {
        "base_addr":0x01,
        "info":
        {
            "id":0,
            "rot":1,
            "pos":3,
        }
    }
}
obj_line = {
    "num":0x00,
    "pos":0x01,
}
obj_20_class = {
    "num":0x00,
    "target":
    {
        "base_addr":0x01,
        "info":
        {
            "id":0,
            "pos":1,
        }
    }
}
obj_qrcode = {
    "num":0x00,
    "infolen":0x01,
    "pos":0x02,
    "addinfo":0x03,
}
obj_face_attr = {
    "num":0x00,
    "target":
    {
        "base_addr":0x01,
        "info":
        {
            "pos":0,
        }
    }
}
obj_face_re = {
    "num":0x01,
    "target":
    {
        "base_addr":0x02,
        "info":
        {
            "id":0,
            "pos":1,
        }
    }
}
obj_self_learn = {
    "num":0x01,
    "id":0x02,
    "confidence":0x03,
}
obj_card = {
    "num":0x00,
    "target":
    {
        "base_addr":0x01,
        "info":
        {
            "id":0,
            "pos":1,
        }
    }
}
obj_wifi_server = {}
obj_ur_image_det = {
    "num" : 0x03,
    "target":
    {
        "base_addr" : 0x04,
        "info":
        {
            "id"  : 0,
            "pos" : 1,
        }
    }
}
obj_ur_image_class = {
    "num":0x01,
    "id" :0x02,
}

sys_register = (obj_sys, obj_color, obj_patch, obj_tag, obj_line, obj_20_class, 
                obj_qrcode, obj_face_attr, obj_face_re, obj_self_learn, obj_card, 
                obj_wifi_server, obj_ur_image_det, obj_ur_image_class)
def uint16_to_int32(data):
    if data >= 0x8000:
        return data - 0x10000
    else:
        return data
def get_register_addr(index, offset):
    return register_addr[index] + offset
def get_info_size(info_handle):
    info_size=0
    for key in info_handle:
        if key == "id":
            if obj_tag["target"]["info"] == info_handle:
                info_size += 2
            else:
                info_size += 1
        elif key == "rot":
            info_size += 2
        elif key == "pos":
            info_size += 8
    return info_size
def position_disposal(pos):
    _data = [0]*4
    for i in range(4):
        _data[i] = uint16_to_int32((pos[i*2]<<8) | pos[i*2+1])
    return _data



class ai_camera(iic_base.iic_base):
    def __init__(self, port=0, addr=0x24):
        super().__init__(port, addr)
        self._handle = iic_base.iic_base(port, addr)

    def set_sys_mode(self, mode:int): # 设置系统模式
        if mode<1:
            return
        self._handle.write_reg(0, [mode-1])

    def get_sys_mode(self): # 获取系统模式
        return self._handle.read_reg(0, 1)[0]+1
    
    def get_color_rgb(self): # 获取颜色识别的RGB值
        rgb = self._handle.read_reg(15, 3)
        return (rgb[0], rgb[1], rgb[2])
        
    def set_find_color(self, color):
        color_id = 1
        if color not in color_tab:
            return
        color_id = color_tab[color]
        self._handle.write_reg(get_register_addr(AI_CAMERA_PATCH, 0x00), [color_id])
        
    def face_study(self): # 人脸识别学习
        self._handle.write_reg(get_register_addr(AI_CAMERA_FACE_RE, 0x06), [0x01])
        
    def deep_learn_study(self): # 深度学习
        self._handle.write_reg(get_register_addr(AI_CAMERA_DEEP_LEARN, 0x00), [0x01])
    
    def get_qrcode_content(self): # 获取二维码信息
        num = self._handle.read_reg(get_register_addr(AI_CAMERA_QRCODE, 0x01), 1)[0]
        str = self._handle.read_reg(get_register_addr(AI_CAMERA_QRCODE, 0x03), num)
        try:
            return str.decode('utf-8')
        except:
            if len(str) == 0:
                return ""
            return str

    def get_identify_num(self, features, total=0): # 得到识别的数量
        target_base_addr = get_register_addr(features, 0)
        if features == AI_CAMERA_FACE_RE:
            if total==1:
                return self._handle.read_reg(target_base_addr+0, 1)[0]
        target_func = sys_register[features]
        if "num" in target_func:
            _offset = target_func["num"]
            return self._handle.read_reg(target_base_addr + _offset, 1)[0]
        return 0
    
    def get_identify_face_attribute(self, index=0):
        target_base_addr = get_register_addr(AI_CAMERA_FACE_ATTRIBUTE, 5)
        data = self._handle.read_reg(target_base_addr+index, 4)
        return (data[1], data[2], data[3])

    
    def get_identify_id(self, features, index=0): # 得到识别的ID
        target_base_addr = get_register_addr(features, 0)
        target_func = sys_register[features]
        if "id" in target_func:
            _offset = target_func["id"]
            return self._handle.read_reg(target_base_addr + _offset, 1)[0]
        elif "target" in target_func:
            id_offset = target_func["target"]["base_addr"]
            if "id" in  target_func["target"]["info"]:
                _offset = target_func["target"]["info"]["id"]
                if features==AI_CAMERA_TAG:
                    read_val = self._handle.read_reg(target_base_addr + id_offset+index, get_info_size(target_func["target"]["info"]))
                    return (read_val[_offset]<<8) | read_val[_offset+1]
                else:
                    ret_id = self._handle.read_reg(target_base_addr + id_offset+index, get_info_size(target_func["target"]["info"]))[_offset]
                if features==AI_CAMERA_PATCH:
                    return color_tab[ret_id] if ret_id in color_tab else ret_id
                else:
                    return ret_id
            else:
                return 0
        else:
            return 0

    def get_identify_rotation(self, features, index=0): # 得到识别的角度
        rot = [0]*2
        target_base_addr = get_register_addr(features, 0)
        target_func = sys_register[features]
        if "rot" in target_func:
            _offset = target_func["rot"]
            rot = self._handle.read_reg(target_base_addr + _offset, 2)
        elif "target" in target_func:
            rot_offset = target_func["target"]["base_addr"]
            if "rot" in target_func["target"]["info"]:
                _offset = target_func["target"]["info"]["rot"]
                rot = self._handle.read_reg(target_base_addr + rot_offset+index*2, get_info_size(target_func["target"]["info"]))[_offset:_offset+2]
        return uint16_to_int32(rot[0]<<8 | (rot[1]))

    def get_identify_position(self, features, index=0): # 得到识别的位置
        pos = [0]*4
        target_base_addr = get_register_addr(features, 0)
        target_func = sys_register[features]
        if "pos" in target_func:
            _offset = target_func["pos"]
            pos = position_disposal(self._handle.read_reg(target_base_addr + _offset, 8))
        elif "target" in target_func:
            pos_offset = target_func["target"]["base_addr"]
            _offset = target_func["target"]["info"]["pos"]
            _pos = self._handle.read_reg(target_base_addr + pos_offset+index, get_info_size(target_func["target"]["info"]))
            pos = position_disposal(_pos[_offset:_offset+8])
        return pos
    
    def get_identify_confidence(self, features, id): # 得到识别的置信度
        if id > 3:
            return 0
        target_base_addr = get_register_addr(features, 0)
        target_func = sys_register[features]
        if "confidence" in target_func:
            _offset = target_func["confidence"]
            return self._handle.read_reg(target_base_addr + _offset, 4)[id]
        return 0
        
    def set_light_brightness(self, brightness):
        target_base_addr = get_register_addr(AI_CAMERA_SETTING, 0)
        self._handle.write_reg(target_base_addr, [brightness])
        return brightness
    
    def get_light_brightness(self):
        target_base_addr = get_register_addr(AI_CAMERA_SETTING, 0)
        return self._handle.read_reg(target_base_addr, 1)[0]
    
    def set_wifi_server_is_scan_qrcode(self, is_scan_qrcode:bool):
        target_base_addr = get_register_addr(AI_CAMERA_WIFI_SERVER, 3)
        self._handle.write_reg(target_base_addr, [0x01 if is_scan_qrcode else 0x00])
    
    def get_wifi_server_ssid_passward(self):
        ssid_addr = get_register_addr(AI_CAMERA_WIFI_SERVER, 0)
        password_addr = ssid_addr + 1
        ssid_len = self._handle.read_reg(ssid_addr, 1)[0]+1
        password_len = self._handle.read_reg(password_addr, 1)[0]+1
        ssid = bytes(self._handle.read_reg(ssid_addr, ssid_len)[1:]).decode('utf-8')
        password = bytes(self._handle.read_reg(password_addr, password_len)[1:]).decode('utf-8')
        return ssid, password

    def set_wifi_server_ssid_passward(self, ssid:str, password:str):
        ssid = ssid.encode('utf-8')
        password = password.encode('utf-8')
        ssid_list = [len(ssid)]
        password_list = [len(password)]
        for ch in ssid:
            ssid_list.append(ch)
        for ch in password:
            password_list.append(ch)
        target_base_addr = get_register_addr(AI_CAMERA_WIFI_SERVER, 0)
        self._handle.write_reg(target_base_addr + 0x00, ssid_list)
        self._handle.write_reg(target_base_addr + 0x01, password_list)
        self.set_wifi_server_is_scan_qrcode(0)

    def get_wifi_server_ip(self):
        target_base_addr = get_register_addr(AI_CAMERA_WIFI_SERVER, 2)
        len = self._handle.read_reg(target_base_addr, 1)[0]+1
        return bytes(self._handle.read_reg(target_base_addr, len)[1:]).decode('utf-8')

    # def set_image_detection_model_info(self, model_size:int, anchors:str, identify_num:int):
    #     target_base_addr = get_register_addr(AI_CAMERA_USER_IMAGE_DETECTION, 0)
    #     model_size_addr = target_base_addr+0
    #     anchors_addr = target_base_addr+1
    #     identify_num_addr = target_base_addr+2

    #     model_size_str = str(model_size)
    #     model_size_list = [len(model_size_str)]
    #     for ch in model_size_str:
    #         model_size_list.append(ord(ch))

    #     anchors_list = [len(anchors)]
    #     for ch in anchors:
    #         anchors_list.append(ord(ch))
    #     self._handle.write_reg(model_size_addr, model_size_list)
    #     self._handle.write_reg(anchors_addr, anchors_list)
    #     self._handle.write_reg(identify_num_addr, [identify_num])
    
    # def set_image_class_model_info(self, model_size:int):
    #     target_base_addr = get_register_addr(AI_CALERA_USER_IMAGE_CLASS, 0)
    #     model_size_addr = target_base_addr+0

    #     model_size_str = str(model_size)
    #     model_size_list = [len(model_size_str)]
    #     for ch in model_size_str:
    #         model_size_list.append(ord(ch))
    #     self._handle.write_reg(model_size_addr, model_size_list)

        

