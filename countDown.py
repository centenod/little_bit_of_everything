import os
import csv

# This program should be launch every minute
# What if the file is empty????
# it should do nothing

	with open('piList.csv','r',newline='') as infile, open('count.csv','w',newline='') as outfile:
		fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
		r = csv.DictReader(infile, fieldnames=fieldnames, dialect='excel-tab')
		w = csv.DictWriter(outfile, fieldnames=fieldnames, dialect='excel-tab')
		for row in r:
			if row['Countdown'] >= 1:
				temp_count= int(row['Countdown']) - 1 
				w.writerow({'Hostname' : row['Hostname'], 'IP' : row['IP'], 'Status' : row['Status'], 'Countdown' : temp_count, 'Last update' : row['Last update']})

			elseif row['Hostname'] ==0:
				w.writerow({'Hostname' : row['Hostname'], 'IP' : row['IP'], 'Status' : "DOWN", 'Countdown' : temp_count, 'Last update' : row['Last update']})

			
	os.replace('count.csv','piList.csv')
