import os
import csv

# This program should be launch every minute
# What if the file is empty????
# it should do nothing
zero = "0"
one = "1"
two = "2"
three = "3"
down="DOWN"
with open('piList.csv','r',newline='') as infile, open('count.csv','w',newline='') as outfile:
        fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
        r = csv.DictReader(infile, fieldnames=fieldnames, dialect='excel-tab')
        w = csv.DictWriter(outfile, fieldnames=fieldnames, dialect='excel-tab')
        for row in r:
                if row['Countdown'] == two or row['Countdown'] == three:
                        temp_count= int(row['Countdown']) - 1
                        w.writerow({'Hostname' : row['Hostname'], 'IP' : row['IP'], 'Status' : row['Status'], 'Countdown' : temp_count, 'Last upda$

                elif row['Countdown'] == one:
                        temp_count= int(row['Countdown']) - 1
                        w.writerow({'Hostname' : row['Hostname'], 'IP' : row['IP'], 'Status' : down, 'Countdown' : temp_count , 'Last update' : ro$
                else:
                        w.writerow(row)
os.replace('count.csv','piList.csv')
