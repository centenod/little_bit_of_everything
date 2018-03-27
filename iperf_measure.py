#!/usr/bin/python3
import pingparsing
import csv
import os.path
import os
import subprocess
import shutil
import datetime

from multiprocessing import Process
from subprocess import Popen, PIPE, call

########################################################################

# First let's get the process id for just running this script
print(" ========================================================================================================= ")
current = os.getpid()
print ("Current process:", current)
now_time= datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
print(now_time)
print(" ========================================================================================================= ")


########################################################################



def run_iperf():

    output = subprocess.Popen(['iperf' ,'-c', '169.254.4.26', '-p', '9001', '-t', '50', '-P', '5'],
                              stdout=subprocess.PIPE).communicate()[0]
    #Process= Popen(["./home/pi/Desktop/inputsh.sh %s %s" % (test_num, var2) ], stdin= PIPE, shell=True)
    
    outputToFile=output.decode('utf-8')
    print(outputToFile)
    
    
    print("Saving in data%i.txt" %i)
    with open('/home/pi/Desktop/Iperf/Data/data%i.txt' %i, 'w') as f:
        f.write(outputToFile)
    print("PROCESS FINISH")




##    with open("/home/pi/Desktop/ping/Data/data%i.txt" %i,'r') as f, open("/home/pi/Desktop/ping/Data/ResultsFile.csv", 'a') as apnd:
##        fieldnames = ['packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
##        w = csv.DictWriter(apnd, fieldnames=fieldnames, dialect='excel-tab')
##        ping_parser.parse(f.read())
##        w.writerow(ping_parser.as_dict())

shutil.rmtree('/home/pi/Desktop/Iperf/Data')
os.mkdir('/home/pi/Desktop/Iperf/Data')

##ping_parser = pingparsing.PingParsing()
fileMissing = os.path.isfile("/home/pi/Desktop/ping/Data/ResultsFile.csv")


with open("/home/pi/Desktop/Iperf/Data/ResultsFile.csv", 'a') as apnd:
    fieldnames = ['packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
    w = csv.DictWriter(apnd, fieldnames=fieldnames, dialect='excel-tab')
    if not fileMissing:
        w.writeheader()



p = []
j = 0
parallel_procc= 100
for i in range(0,parallel_procc):
    print('Call number '+ str(j))
    pro = Process(target=run_iperf)
    p.append(pro)
    p[j].start()
    j += 1
j = 0

for i in range(0,parallel_procc):
    p[j].join()
    j+=1

        

##    
##fileMissing = os.path.isfile('/home/pi/Desktop/ping/Average.csv')
##with open('/home/pi/Desktop/ping/Average.csv','a',newline='') as appendfile:
##    #fieldnamesA = ['Time_Stamp','packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
##    fieldnamesA = ['Time_Stamp','destination', 'packet_transmit', 'packet_receive', 'packet_loss_count', 'packet_loss_rate', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_min', 'rtt_avg', 'rtt_max', 'rtt_mdev']
##    w = csv.DictWriter(appendfile, fieldnames=fieldnamesA, dialect='excel-tab')
##    
##    if not fileMissing:
##        w.writeheader()
##    
##    
##
##packet_loss_rate =[]
##rtt_mdev =[]
##packet_loss_count =[]
##packet_duplicate_rate =[]
##packet_duplicate_count =[]
##rtt_avg =[]
##destination =[]
##packet_receive =[]
##rtt_min =[]
##packet_transmit =[]
##rtt_max =[]


##with open('/home/pi/Desktop/ping/Data/ResultsFile.csv') as readfile, open('/home/pi/Desktop/ping/Average.csv','a',newline='') as appendfile:
####    fieldnames = ['Time_Stamp','packet_loss_rate', 'rtt_mdev', 'packet_loss_count', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_avg', 'destination', 'packet_receive', 'rtt_min', 'packet_transmit', 'rtt_max']
##    fieldnames = ['Time_Stamp','destination', 'packet_transmit', 'packet_receive', 'packet_loss_count', 'packet_loss_rate', 'packet_duplicate_rate', 'packet_duplicate_count', 'rtt_min', 'rtt_avg', 'rtt_max', 'rtt_mdev']
##    reader = csv.DictReader(readfile, dialect='excel-tab')
##    writer = csv.DictWriter(appendfile, fieldnames=fieldnames, dialect='excel-tab')
##    for row in reader:
##        packet_loss_rate.append(float(row['packet_loss_rate']))
##        rtt_mdev.append(float(row['rtt_mdev']))
##        packet_loss_count.append(float(row['packet_loss_count']))
##        packet_duplicate_rate.append(float(row['packet_duplicate_rate']))
##        packet_duplicate_count.append(float(row['packet_duplicate_count']))
##        rtt_avg.append(float(row['rtt_avg']))
##        destination =row['destination']
##        packet_receive.append(float(row['packet_receive']))
##        rtt_min.append(float(row['rtt_min']))
##        packet_transmit.append(float(row['packet_transmit']))
##        rtt_max.append(float(row['rtt_max']))
##    
##    average_packet_loss_rate = sum(packet_loss_rate)/ len(packet_loss_rate)
##    average_rtt_mdev = sum(rtt_mdev)/ len(rtt_mdev)
##    average_packet_loss_count = sum(packet_loss_count)
##    average_packet_duplicate_rate =sum(packet_duplicate_rate)/len(packet_duplicate_rate)
##    average_packet_duplicate_count =sum(packet_duplicate_count)/len(packet_duplicate_count)
##    average_rtt_avg =sum(rtt_avg)/len(rtt_avg)
##    #average_destination =sum(destination)/len(destination)
##    average_packet_receive =sum(packet_receive)
##    average_rtt_min =sum(rtt_min)/len(rtt_min)
##    average_packet_transmit =sum(packet_transmit)/len(packet_transmit)
##    average_rtt_max =sum(rtt_max)/len(rtt_max)
##        
##    now_time= datetime.datetime.now().strftime("%Y:%m:%d %H:%M:%S")
##    writer.writerow({'Time_Stamp': now_time,
##                     'packet_loss_rate': average_packet_loss_rate,
##                     'packet_loss_count': average_packet_loss_count,
##                     'packet_duplicate_rate': average_packet_duplicate_rate,
##                     'packet_duplicate_count':average_packet_duplicate_count,
##                     'rtt_avg': average_rtt_avg,
##                     'destination': destination,
##                     'packet_receive': average_packet_receive,
##                     'rtt_min': average_rtt_min ,
##                     'packet_transmit': average_packet_transmit ,
##                     'rtt_max': average_rtt_max,
##                     'rtt_mdev': average_rtt_mdev,})
##    
##




print(" ========================================================================================================= ")
print("  SCRIPT FINISHED")
print("  SCRIPT FINISHED")
print("  SCRIPT FINISHED")
print(" ========================================================================================================= ")
