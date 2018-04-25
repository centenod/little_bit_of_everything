#!/usr/bin/python3
import time
import os
import numpy as np
import datetime
from multiprocessing import Process
import sys, getopt

#print(" ========================================================================================================= ")
#current = os.getpid()
#print ("Current process:", current)
#now_time= datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
#print(now_time)
#print(" ========================================================================================================= ")

def run_ping(targetIP, multi):
   #print("first ping")
   #os.system('(sleep 1 && ping 8.8.8. -i 0.2 -I wlan0 -c 1 -s 2000) &')
   os.system('(bash Traffic_Ping.sh -t %s -I wlan0 -i 0.5 -c 2 -m %s) &' %(targetIP, multi))
   #print("(bash TrafficPing.sh -t %s  -I wlan0 -i 0.5 -c 2 -m %s) &" %(targetIP, multi))
   #os.system('ping %s -c %s' %(targetIP, multi))
   time.sleep(25)
   #print("second ping")
   #os.system('(sleep %d && ping 8.8.8.8 -i 0.2 -I wlan0 -c 100 -s 2000) &' %(delay+1 ))
   os.system('(bash Traffic_Ping.sh -t %s -I wlan0 -i 0.5 -c 2 -m %s) &' %(targetIP, multi))
   time.sleep(25)

def main(argv):
   inputfile = ''
   outputfile = ''
   targetIP = '10.168.74.115'
   interface = 'wlan0'
   interval = '0.5'
   count = '10'
   size = '1000'
   multi= 10



   try:
      opts, args = getopt.getopt(argv,"ht:m:",["target=","multi="])
   except getopt.GetoptError:
      print ('ERROR, syntesis should be writen like:')
      print ('test.py -tar <targetIP> -m <outputfile>')
      print ('test.py -target <targetIP> -multi <multiplicator>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('Usage:')
         print ('test.py -t <targetIP> -m <outputfile>')
         print ('test.py -target <targetIP> -multi <multiplicator>')
         sys.exit()
      elif opt in ("-t", "--target"):
         targetIP = arg
      elif opt in ("-m", "--multi"):
         multi =str(arg)
   print ('TargetIP =', targetIP)
   print ('Multiplicator =', multi)


   p = []
   j = 0
   parall_procc=1
   for i in range(0,parall_procc):
#      print('Call number '+ str(j))
      pro = Process(target=run_ping(targetIP, multi))
      p.append(pro)
      p[j].start()
      time.sleep(1)
      p[j].join()
      j += 1

#   print(" ========================================================================================================= ")
#   now_time= datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
#   print(now_time)
#   print("  SCRIPT FINISHED")
#   print(" ========================================================================================================= ")

if __name__ == "__main__":
   main(sys.argv[1:])
