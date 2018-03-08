#!/usr/bin/python3
import pingparsing
import csv
import os.path
import os
import subprocess

from multiprocessing import Process
from subprocess import Popen, PIPE

########################################################################

# First let's get the process id for just running this script

current = os.getpid()
print ("\nCurrent process:", current)

########################################################################

# Now let's launch another process and get the id.

def run_ping():

    
    #Process= Popen('./home/pi/Desktop/inputsh.sh %s %s' % (str(test_num), str(var2)), shell=True)
    output = subprocess.Popen(['ping', '-c', '3', '-s', '500', '8.8.8.8'], stdout=subprocess.PIPE).communicate()[0]
    #Process= Popen(["./home/pi/Desktop/inputsh.sh %s %s" % (test_num, var2) ], stdin= PIPE, shell=True)
    
    outputToFile=output.decode('utf-8')
    print(outputToFile)
    print("Saving in data%i.txt" %i)
    with open('/home/pi/Desktop/ping/data%i.txt' %i, 'w') as f:
        f.write(outputToFile)
    print("PROCESS FINISH")




    with open("/home/pi/Desktop/ping/data%i.txt" %i,'r') as f, open("/home/pi/Desktop/ping/ResultsFile.txt", 'a') as apnd:
        fieldnames = ['packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
        w = csv.DictWriter(apnd, fieldnames=fieldnames, dialect='excel-tab')
        ping_parser.parse(f.read())
        w.writerow(ping_parser.as_dict())


#print("Call number %i:" %i)



ping_parser = pingparsing.PingParsing()
fileMissing = os.path.isfile("/home/pi/Desktop/ping/ResultsFile.txt")
with open("/home/pi/Desktop/ping/ResultsFile.txt", 'a') as apnd:
    fieldnames = ['packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
    w = csv.DictWriter(apnd, fieldnames=fieldnames, dialect='excel-tab')
    if not fileMissing:
        w.writeheader()



i=1
print("Call number 1")
p1= Process(target=run_ping)
p1.start()

i=i+1    
print("Call number 2")
p2= Process(target=run_ping)
p2.start()

i=i+1
print("Call number 3")
p3= Process(target=run_ping)
p3.start()

i=i+1
print("Call number 4")
p4= Process(target=run_ping)
p4.start()

i=i+1
print("Call number 5")
p5= Process(target=run_ping)
p5.start()

i=i+1
print("Call number 6")
p6= Process(target=run_ping)
p6.start()

i=i+1
print("Call number 7")
p7= Process(target=run_ping)
p7.start()

i=i+1
print("Call number 8")
p8= Process(target=run_ping)
p8.start()

i=i+1
print("Call number 9")
p9= Process(target=run_ping)
p9.start()

i=i+1
print("Call number 10")
p10= Process(target=run_ping)
p10.start()

i=i+1
print("Call number 11")
p11= Process(target=run_ping)
p11.start()

i=i+1
print("Call number 12")
p12= Process(target=run_ping)
p12.start()

i=i+1
print("Call number 13")
p13= Process(target=run_ping)
p13.start()

i=i+1
print("Call number 14")
p14= Process(target=run_ping)
p14.start()

i=i+1
print("Call number 15")
p15= Process(target=run_ping)
p15.start()

i=i+1
print("Call number 16")
p16= Process(target=run_ping)
p16.start()

i=i+1
print("Call number 17")
p17= Process(target=run_ping)
p17.start()

i=i+1
print("Call number 18")
p18= Process(target=run_ping)
p18.start()

i=i+1
print("Call number 19")
p19= Process(target=run_ping)
p19.start()

i=i+1    
print("Call number 20")
p20= Process(target=run_ping)
p20.start()

i=i+1    
print("Call number 21")
p21= Process(target=run_ping)
p21.start()

i=i+1    
print("Call number 22")
p22= Process(target=run_ping)
p22.start()

i=i+1    
print("Call number 23")
p23= Process(target=run_ping)
p23.start()

i=i+1    
print("Call number 24")
p24= Process(target=run_ping)
p24.start()

i=i+1    
print("Call number 25")
p25= Process(target=run_ping)
p25.start()


p1.join()
p2.join()
p3.join()
p4.join()
p5.join()
p6.join()
p7.join()
p8.join()
p9.join()
p10.join()
p11.join()
p12.join()
p13.join()
p14.join()
p15.join()
p16.join()
p17.join()
p18.join()
p19.join()
p20.join()
p21.join()
p22.join()
p23.join()
p24.join()
p25.join()


print("is it done?")

