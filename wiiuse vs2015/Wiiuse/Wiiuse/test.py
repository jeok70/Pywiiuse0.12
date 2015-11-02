import pywiiusetest as wiiuse 
import time

if __name__=="__main__":
   # wiiuse.main()
   
   text_file = open("Output.txt", "w")
   text_file.write("time: %f" % time.time())
   text_file.close()