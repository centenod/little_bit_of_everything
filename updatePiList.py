import csv
import os

def updatePiList(msg):

        fileEmpty = os.stat('piList.csv').st_size == 0

        with open('piList.csv','r') as readfile, open('piList.csv','a') as appendfile:
                fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
                r = csv.DictReader(readfile, fieldnames=fieldnames, dialect='excel-tab')
                w = csv.DictWriter(appendfile, fieldnames=fieldnames, dialect='excel-tab')
                k=0
                if fileEmpty:
                        w.writeheader()
#                       print('header')
                for row in r:
                        if 'RPI-' in msg[0] and msg[0] not in row['Hostname']:
#                               w.writerow({'Hostname' : msg[0], 'IP' : msg[1], 'Status' : msg[2], 'Countdown' :$
#                               w.writerow({'Hostname' : 'blank ppending'})
#                               quit
                                k=1
#                               print('k is 1 -> writing')
                        else:
#                               w.writerow({'Hostname' : 'blank not appending'})
                                k=0
#                               print('k is 1')
                if k==1:
                        w.writerow({'Hostname' : msg[0], 'IP' : msg[1], 'Status' : msg[2], 'Countdown' : msg[3], 'Last update' : msg[4]})
                        quit


        with open('piList.csv','r') as infile, open('out.csv','w') as outfile:
                fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
                r = csv.DictReader(infile, fieldnames=fieldnames, dialect='excel-tab')
                w = csv.DictWriter(outfile, fieldnames=fieldnames, dialect='excel-tab')
                for row in r:
                        if ('RPI-' in msg[0]) and (row['Hostname'] == msg[0]):
                                w.writerow({'Hostname' : msg[0], 'IP' : msg[1], 'Status' : msg[2], 'Countdown' : msg[3], 'Last update' : msg[4]})
                        else:
                                w.writerow(row)
        os.replace('out.csv','piList.csv')
