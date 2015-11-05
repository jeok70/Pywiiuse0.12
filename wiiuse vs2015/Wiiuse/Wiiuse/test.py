import pywiiusetest as wiiuse 
import time

if __name__=="__main__":
   wm = wiiuse.Wiimote()
   wm.main()
   a = wm.x+wm.y+wm.z+wm.roll+wm.pitch
   print a
   text_file = open("Output.txt", "w")
   text_file.write("time: %f" % a)
   text_file.close()
