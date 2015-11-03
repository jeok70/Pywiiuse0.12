import py_wiiuse as wiiuse

import sys
import time
import os
import ctypes

dll=ctypes.cdll.wiiuse

class Wiimote(object):
 def handle_event(wm):
  btn=wiiuse.pressed_button(wm)
  if btn != [] : print "Push ",btn
  if "Home" in btn : return False
  if wiiuse.is_just_pressed(wm[0], wiiuse.WIIMOTE_BUTTON_MINUS) :
      wiiuse.wiimote_motion_sesing(wm,0)
  if wiiuse.is_just_pressed(wm[0], wiiuse.WIIMOTE_BUTTON_PLUS) :
      wiiuse.wiimote_motion_sesing(wm,1)
  if wiiuse.is_just_pressed(wm[0], wiiuse.WIIMOTE_BUTTON_B) :
      wiiuse.wiimote_rumble(wm,1)
  if wiiuse.is_just_pressed(wm[0], wiiuse.WIIMOTE_BUTTON_UP) :
      wiiuse.wiimote_set_ir(wm,1)
  if wiiuse.is_just_pressed(wm[0], wiiuse.WIIMOTE_BUTTON_DOWN) :
      wiiuse.wiimote_set_ir(wm,0)
  return True 

 def check_event(wms, id):
  global dll
  if dll.wiiuse_poll(wms, wiiuse.MAX_WIIMOTES) :
    evt = wms[id][0].event
    if evt == wiiuse.WIIUSE_EVENT:
      return handle_event(wms[id])
  return True

 def main():
  id = 0
  wms = wiiuse.init_wiimote()
  while check_event(wms, id):
     if wiiuse.using_acc(wms[id]):
      
      print 'roll = %f pitch = %f yaw = %f' % (wms[id][0].orient.roll,wms[id][0].orient.pitch,wms[id][0].orient.yaw)
      print 'x= %f y = %f  z = %f' % (wms[id][0].gforce.x,wms[id][0].gforce.y,wms[id][0].gforce.z)
     if wms[id][0].exp.type == wiiuse.EXP_NUNCHUK:
      nc=wms[id][0].exp.u.nunchuk
      print "Nunchuk:",nc.js.ang, nc.js.mag,nc.orient.roll, nc.orient.pitch
     if wms[id][0].exp.type == wiiuse.EXP_CLASSIC:
      cc=wms[id][0].exp.u.classic
      print cc.l_shoulder, cc.r_shoulder
      print cc.ljs.ang, cc.ljs.mag,cc.rjs.ang,cc.rjs.mag

