import pdb
import os,time
import ctypes
from ctypes import c_char_p, c_int, c_ubyte, c_uint, c_ushort, c_float, c_short, c_void_p, c_char,c_ulonglong, c_ulong
from ctypes import CFUNCTYPE, Structure, POINTER, Union, byref


# led bit masks
WIIMOTE_LED_NONE=0x00
WIIMOTE_LED_1=0x10
WIIMOTE_LED_2=0x20
WIIMOTE_LED_3=0x40
WIIMOTE_LED_4=0x80

# button codes 
WIIMOTE_BUTTON_TWO=0x0001
WIIMOTE_BUTTON_ONE=0x0002
WIIMOTE_BUTTON_B=0x0004
WIIMOTE_BUTTON_A=0x0008
WIIMOTE_BUTTON_MINUS=0x0010
WIIMOTE_BUTTON_ZACCEL_BIT6=0x0020
WIIMOTE_BUTTON_ZACCEL_BIT7=0x0040
WIIMOTE_BUTTON_HOME=0x0080
WIIMOTE_BUTTON_LEFT=0x0100
WIIMOTE_BUTTON_RIGHT=0x0200
WIIMOTE_BUTTON_DOWN=0x0400
WIIMOTE_BUTTON_UP=0x0800
WIIMOTE_BUTTON_PLUS=0x1000
WIIMOTE_BUTTON_ZACCEL_BIT4=0x2000
WIIMOTE_BUTTON_ZACCEL_BIT5=0x4000
WIIMOTE_BUTTON_UNKNOWN=0x8000
WIIMOTE_BUTTON_ALL=0x1F9F

# nunchul button codes
NUNCHUK_BUTTON_Z=0x01
NUNCHUK_BUTTON_C=0x02
NUNCHUK_BUTTON_ALL=0x03

# classic controller button codes
CLASSIC_CTRL_BUTTON_UP=0x0001
CLASSIC_CTRL_BUTTON_LEFT=0x0002
CLASSIC_CTRL_BUTTON_ZR=0x0004
CLASSIC_CTRL_BUTTON_X=0x0008
CLASSIC_CTRL_BUTTON_A=0x0010
CLASSIC_CTRL_BUTTON_Y=0x0020
CLASSIC_CTRL_BUTTON_B=0x0040
CLASSIC_CTRL_BUTTON_ZL=0x0080
CLASSIC_CTRL_BUTTON_FULL_R=0x0200
CLASSIC_CTRL_BUTTON_PLUS=0x0400
CLASSIC_CTRL_BUTTON_HOME=0x0800
CLASSIC_CTRL_BUTTON_MINUS=0x1000
CLASSIC_CTRL_BUTTON_FULL_L=0x2000
CLASSIC_CTRL_BUTTON_DOWN=0x4000
CLASSIC_CTRL_BUTTON_RIGHT=0x8000
CLASSIC_CTRL_BUTTON_ALL=0xFEFF

# guitar hero 3 button code
GUITAR_HERO_3_BUTTON_STRUM_UP=0x0001
GUITAR_HERO_3_BUTTON_YELLOW=0x0008
GUITAR_HERO_3_BUTTON_GREEN=0x0010
GUITAR_HERO_3_BUTTON_BLUE=0x0020
GUITAR_HERO_3_BUTTON_RED=0x0040
GUITAR_HERO_3_BUTTON_ORANGE=0x0080
GUITAR_HERO_3_BUTTON_PLUS=0x0400
GUITAR_HERO_3_BUTTON_MINUS=0x1000
GUITAR_HERO_3_BUTTON_STRUM_DOWN=0x4000
GUITAR_HERO_3_BUTTON_ALL=0xFEFF


# wiimote option flags 
WIIUSE_SMOOTHING=0x01
WIIUSE_CONTINUOUS=0x02
WIIUSE_ORIENT_THRESH=0x04
WIIUSE_INIT_FLAGS=(WIIUSE_SMOOTHING | WIIUSE_ORIENT_THRESH)

WIIUSE_ORIENT_PRECISION=100.0


# expansion codes 
EXP_NONE=0
EXP_NUNCHUK=1
EXP_CLASSIC=2
EXP_GUITAR_HERO_3=3


# IR correction types 
#typedef enum ir_position_t {
#	WIIUSE_IR_ABOVE,
#	WIIUSE_IR_BELOW
#} ir_position_t;
# duplicate the wiiuse data structures

MAX_PAYLOAD=32
WIIUSE_NONE=0
WIIUSE_EVENT=1
WIIUSE_STATUS=2
WIIUSE_CONNECT=3
WIIUSE_DISCONNECT=4
WIIUSE_UNEXPECTED_DISCONNECT=5
WIIUSE_READ_DATA=6
WIIUSE_NUNCHUK_INSERTED=7
WIIUSE_NUNCHUK_REMOVED=8
WIIUSE_CLASSIC_CTRL_INSERTED=9
WIIUSE_CLASSIC_CTRL_REMOVED=10
WIIUSE_GUITAR_HERO_3_CTRL_INSERTED=11
WIIUSE_GUITAR_HERO_3_CTRL_REMOVED=12


class read_req(Structure):
    pass

read_req_p = POINTER(read_req)

read_req._fields_ = [('cb', c_void_p),
                ('buf', POINTER(c_ubyte)),
                ('addr', c_uint),
                ('size', c_ushort),
                ('wait', c_ushort),
                ('dirty', c_ubyte),
                ('next', read_req_p), 
                ]

class vec2b(Structure):
    _fields_ = [('x', c_ubyte),
                ('y', c_ubyte),
                ]

class vec3b(Structure):
    _fields_ = [('x', c_ubyte),
                ('y', c_ubyte),
                ('z', c_ubyte),
                ]

class vec3f(Structure):
    _fields_ = [('x', c_float),
                ('y', c_float),
                ('z', c_float),
                ]

class orient(Structure):
    _fields_ = [('roll', c_float),
                ('pitch', c_float),
                ('yaw', c_float),
                ('a_roll', c_float),
                ('a_pitch', c_float),
                ]

class gforce(Structure):
    _fields_ = [('x', c_float),
                ('y', c_float),
                ('z', c_float),
                ]

class accel(Structure):
    _fields_ = [('cal_zero', vec3b),
                ('cal_g', vec3b),
                ('st_roll', c_float),
                ('st_pitch', c_float),
                ('st_alpha', c_float),
                ]

class ir_dot(Structure):
    _fields_ = [('visible', c_ubyte),
                ('x', c_uint),
                ('y', c_uint),
                ('rx', c_short),
                ('ry', c_short),
                ('order', c_ubyte),
                ('size', c_ubyte),
                ]

class ir(Structure):
    _fields_ = [('dot', ir_dot*4),
                ('num_dots', c_ubyte),
                ('aspect', c_int),
                ('pos', c_int),
                ('vres', c_uint*2),
                ('offset', c_int*2),
                ('state', c_int),
                ('ax', c_int),
                ('ay', c_int),
                ('x', c_int),
                ('y', c_int),
                ('distance', c_float),
                ('z', c_float),
                ]

class joystick(Structure):
    _fields_ = [('max', vec2b),
                ('min', vec2b),
                ('center', vec2b),
                ('ang', c_float),
                ('mag', c_float),
                ]

class nunchuk(Structure):
    _fields_ = [('accel_calib', accel),
                ('js', joystick),
                ('flags', POINTER(c_int)),
                ('btns', c_ubyte),
                ('btns_held', c_ubyte),
                ('btns_released', c_ubyte),
                ('orient_threshold', c_float),
                ('accel_threshold', c_int),
                ('accel', vec3b),
                ('orient', orient),
                ('gforce', gforce),
                ]

class classic_ctrl(Structure):
    _fields_ = [('btns', c_short),
                ('btns_held', c_short),
                ('btns_released', c_short),
                ('r_shoulder', c_float),
                ('l_shoulder', c_float),
                ('ljs', joystick),
                ('rjs', joystick),
                ]

class guitar_hero_3(Structure):
    _fields_ = [('btns', c_short),
                ('btns_held', c_short),
                ('btns_released', c_short),
                ('whammy_bar', c_float),
                ('js', joystick),
                ]

class expansion_union(Union):
    _fields_ = [('nunchuk', nunchuk),
                ('classic', classic_ctrl),
                ('gh3',guitar_hero_3),
                ]

class expansion(Structure):
    _fields_ = [('type', c_int),
                ('u', expansion_union),
                ]

class wiimote_state(Structure):
    _fields_ = [('exp_ljs_ang', c_float),
                ('exp_rjs_ang', c_float),
                ('exp_ljs_mag', c_float),
                ('exp_rjs_mag', c_float),
                ('exp_btns', c_ushort),
                ('exp_orient', orient),
                ('exp_accel', vec3b),
                ('exp_r_shoulder', c_float),
                ('exp_l_shoulder', c_float),
                ('ir_ax', c_int),
                ('ir_ay', c_int),
                ('ir_distance', c_float),
                ('orient', orient),
                ('btns', c_ushort),
                ('accel', vec3b),
                ]

class wiimote(Structure):
    _fields_ = [('unid', c_int),
                ('dev_handle', c_void_p),
                ('hid_overlap', c_void_p*5),
                ('stack', c_int),
                ('timeout', c_int),
                ('normal_timeout', c_ubyte),
                ('exp_timeout', c_ubyte),
                ('state', c_int),
                ('leds', c_ubyte),
                ('battery_level', c_float),
                ('flags', c_int),
                ('handshake_state', c_ubyte),
                ('read_req', c_void_p),
                ('accel_calib', accel),
                ('exp', expansion),
                ('accel', vec3b),
                ('orient', orient),
                ('gforce', gforce),
                ('ir', ir),
                ('btns', c_ushort),
                ('btns_held', c_ushort),
                ('btns_release', c_ushort),
                ('orient_threshold', c_float),
                ('accel_threshold', c_int),
                ('lstate', wiimote_state),
                ('event', c_int),
                ('event_buf', c_ubyte*MAX_PAYLOAD),
                ]

wiimote_p = POINTER(wiimote)
wiimote_pp = POINTER(wiimote_p)

event_cb_t = CFUNCTYPE(None, wiimote_p)
read_cb_t = CFUNCTYPE(None, wiimote_p, POINTER(c_ubyte), c_ushort)
ctrl_status_cb_t = CFUNCTYPE(None, wiimote_p, c_int, c_int, c_int, POINTER(c_int), c_float)
dis_cb_t = CFUNCTYPE(None, wiimote_p)

dll=ctypes.cdll.wiiuse

MAX_WIIMOTES=5

# wiimote button codes
wiimote_buttons={'2':WIIMOTE_BUTTON_TWO,
		 '1':WIIMOTE_BUTTON_ONE,
		 'B':WIIMOTE_BUTTON_B,
		 'A':WIIMOTE_BUTTON_A,
		 'Minus':WIIMOTE_BUTTON_MINUS,
		 'ZA6':WIIMOTE_BUTTON_ZACCEL_BIT6,
		 'ZA7':WIIMOTE_BUTTON_ZACCEL_BIT7,
		 'Home':WIIMOTE_BUTTON_HOME,
		 'Left':WIIMOTE_BUTTON_LEFT,
		 'Right':WIIMOTE_BUTTON_RIGHT,
		 'Down':WIIMOTE_BUTTON_DOWN,
		 'Up':WIIMOTE_BUTTON_UP,
		 'Plus':WIIMOTE_BUTTON_PLUS,
		 'ZA4':WIIMOTE_BUTTON_ZACCEL_BIT4,
		 'ZB5':WIIMOTE_BUTTON_ZACCEL_BIT5,
		 'Unknown':WIIMOTE_BUTTON_UNKNOWN,
		 'All':WIIMOTE_BUTTON_ALL
		}
# nunchul button codes
nunchuk_buttons={'N:Z':NUNCHUK_BUTTON_Z,
		 'N:C':NUNCHUK_BUTTON_C,
		 'N:ALL':NUNCHUK_BUTTON_ALL
		}

# classic controller button codes
classic_buttons={'C:UP':CLASSIC_CTRL_BUTTON_UP,
		 'C:LEFT':CLASSIC_CTRL_BUTTON_LEFT,
		 'C:ZR':CLASSIC_CTRL_BUTTON_ZR,
		 'C:X':CLASSIC_CTRL_BUTTON_X,
		 'C:A':CLASSIC_CTRL_BUTTON_A,
		 'C:Y':CLASSIC_CTRL_BUTTON_Y,
		 'C:B':CLASSIC_CTRL_BUTTON_B,
		 'C:ZL':CLASSIC_CTRL_BUTTON_ZL,
		 'C:FULL_R':CLASSIC_CTRL_BUTTON_FULL_R,
		 'C:PLUS':CLASSIC_CTRL_BUTTON_PLUS,
		 'C:HOME':CLASSIC_CTRL_BUTTON_HOME,
		 'C:MINUS':CLASSIC_CTRL_BUTTON_MINUS,
		 'C:FULL_L':CLASSIC_CTRL_BUTTON_FULL_L,
		 'C:DOWN':CLASSIC_CTRL_BUTTON_DOWN,
		 'C:RIGHT':CLASSIC_CTRL_BUTTON_RIGHT,
		 'C:ALL':CLASSIC_CTRL_BUTTON_ALL
		}

# guitar hero 3 button code
guitar_buttons={'G:STRUM_UP':GUITAR_HERO_3_BUTTON_STRUM_UP,
		'G:YELLOW':GUITAR_HERO_3_BUTTON_YELLOW,
		'G:GREEN':GUITAR_HERO_3_BUTTON_GREEN,
		'G:BLUE':GUITAR_HERO_3_BUTTON_BLUE,
		'G:RED':GUITAR_HERO_3_BUTTON_RED,
		'G:ORANGE':GUITAR_HERO_3_BUTTON_ORANGE,
		'G:PLUS':GUITAR_HERO_3_BUTTON_PLUS,
		'G:MINUS':GUITAR_HERO_3_BUTTON_MINUS,
		'G:STRUM_DOWN':GUITAR_HERO_3_BUTTON_STRUM_DOWN,
		'G:ALL':GUITAR_HERO_3_BUTTON_ALL
		}


wiimote_leds=[WIIMOTE_LED_NONE,
   	      WIIMOTE_LED_1,
   	      WIIMOTE_LED_2,
   	      WIIMOTE_LED_3,
   	      WIIMOTE_LED_4
	     ]

WIIMOTE_DEFAULT_TIMEOUT=10
WIIMOTE_EXP_TIMEOUT=10

def wiimote_set_ir(wm,flag):
  dll.wiiuse_set_ir(wm,flag)

def wiimote_motion_sesing(wm,flag):
  dll.wiiuse_motion_sensing(wm,flag)

def wiimote_leds(wm, flag):
  dll.wiiuse_set_leds(wm, flag)

def wiimote_rumble(wm, n):
  for i in range(n):
    dll.wiiuse_rumble(wm,1)
    time.sleep(0.2)
    dll.wiiuse_rumble(wm,0)
    time.sleep(0.2)

def is_pressed(wm, id):
  return (wm.btns & id) == id

def is_hold(wm, id):
  return  (wm.btns_held & id) == id

def is_released(wm, id):
  return (wm.btns_released & id) == id

def is_just_pressed(wm, id):
  return is_pressed(wm, id) and (not is_hold(wm, id))

def is_set_leds(wm, id, num):
  return (wm[i].leds & wiimote_leds[num] == wiimote_leds[num])

def get_ir_sensitivity(wm):
  if   (wm[0].state & 0x0200) == 0x0200:	v=1
  elif (wm[0].state & 0x0400) == 0x0400:	v=2
  elif (wm[0].state & 0x0800) == 0x0800:	v=3
  elif (wm[0].state & 0x1000) == 0x1000: 	v=4
  elif (wm[0].state & 0x2000) == 0x2000: 	v=5
  else:						v=0
  return v




def using_acc(wm):
  return ((wm[0].state & 0x020) == 0x020)

def using_exp(wm):
  return ((wm[0].state & 0x040) == 0x040)

def using_ir(wm):
  return ((wm[0].state & 0x080) == 0x080)

def using_speaker(wm):
  return ((wm[0].state & 0x100) == 0x100)

def init_wiimote():
  global dll
  dll.wiiuse_init.restype=wiimote_pp
  wiimotes=dll.wiiuse_init(MAX_WIIMOTES)
  found=dll.wiiuse_find(wiimotes,MAX_WIIMOTES,5)
  if found > 0:
    print ("Find %d wiimotes"%(found))
  else:
    print "No wiimotes found"
    return
  connected=dll.wiiuse_connect(wiimotes, MAX_WIIMOTES)
  if connected :
    print "Connected to %d wiimotes (of %d found)"%(connected, found)
  else:
    print "Fail to connect"
    return
  for i in range(found):
    wiimote_leds(wiimotes[i], WIIMOTE_LED_1 << i)
    wiimote_rumble(wiimotes[0], 1)
  return wiimotes

def pressed_button(wm):
  res=[]
  for x in wiimote_buttons :
    if is_pressed(wm[0], wiimote_buttons[x]) : res.append(x)
  if wm[0].exp.type == EXP_NUNCHUK :
    for x in nunchuk_buttons :
      nc=wm[0].exp.u.nunchuk
      if is_pressed(nc, nunchuk_buttons[x]) : res.append(x)
  if wm[0].exp.type == EXP_CLASSIC :
    for x in classic_buttons :
      cc=wm[0].exp.u.classic
      if is_pressed(cc, classic_buttons[x]) : res.append(x)
  return res

def disconnect(wm, id):
  dll.wiiuse_disconnect(wm[id])

def cleaup(wm):
  dll.wiiuse_cleanup(wm, MAX_WIIMOTES)

