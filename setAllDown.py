import os
import csv

# SET ALL TO DOWN

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
                if row['Countdown'] >= zero:
                        w.writerow({'Hostname' : row['Hostname'], 'IP' : row['IP'], 'Status' : down, 'Countdown' : zero , 'Last update' : row['Las$
                else:
                        w.writerow(row)
os.replace('count.csv','piList.csv')
