import os
import csv


def updatePiList(msg):

	fileMissing = os.path.isfile('piList.csv')

	with open('piList.csv','a') as appendfile:
		fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
		w = csv.DictWriter(appendfile, fieldnames=fieldnames, dialect='excel-tab')
		#WRITING THE HEADERS IN THE .CSV-FILE IF THE FILE IS EMPTY
		if not fileMissing:
			w.writeheader()

	with open('piList.csv','r',newline='') as readfile, open('piList.csv','a',newline='') as appendfile:
		fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
		r = csv.DictReader(readfile, fieldnames=fieldnames, dialect='excel-tab')
		w = csv.DictWriter(appendfile, fieldnames=fieldnames, dialect='excel-tab')
		k=0
		for row in r: 
		#IF NO CURRENT ENTRY IN THE .CSV-FILE -> APPEND THEN STOP SCRIPT UNTIL NEXT ENTRY
			if 'RPI-' in msg[0] and msg[0] in row['Hostname']:
				k=0
				break
			else:
				k=1
		if 'RPI-' in msg[0] and k==1:
			w.writerow({'Hostname' : msg[0], 'IP' : msg[1], 'Status' : msg[2], 'Countdown' : msg[3], 'Last update' : msg[4]})

			quit


	with open('piList.csv','r',newline='') as infile, open('out.csv','w',newline='') as outfile:
		fieldnames = ['Hostname', 'IP', 'Status', 'Countdown','Last update']
		r = csv.DictReader(infile, fieldnames=fieldnames, dialect='excel-tab')
		w = csv.DictWriter(outfile, fieldnames=fieldnames, dialect='excel-tab')
		for row in r:
			#lOOKING FOR MATCHING "HOSTNAME" FOR EVERY LINE. 
			#IF MATCH IS FOUND, UPDATE THE WHOLE LINE WITH NEW INFO, IF NOT, USE OLD LINE
			if ('RPI-' in msg[0]) and (row['Hostname'] == msg[0]):
				w.writerow({'Hostname' : msg[0], 'IP' : msg[1], 'Status' : msg[2], 'Countdown' : msg[3], 'Last update' : msg[4]})
			else:
				w.writerow(row)
	os.replace('out.csv','piList.csv')
