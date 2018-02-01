import socket
import time
#import netifaces as ni

def Main():
#       host =  ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']  #Wlan0 address
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('',port))
	
	print("Server started!")
	
	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
#               print('Message from:' + str(addr))
#               print('From user: ' + data)
		address = str(addr)
		for char in address:
			if char in "( )'":
				address = address.replace(char,'')
		ts = time.asctime ( time.localtime(time.time()))
		status = (data + "," + address + "," + "Up" + "," + "3" +','+ ts)
		l = status.split(',')
		l.remove('5001')
#               t = tuple(l)
		print(l)
#               print(t)
#                data = data.upper()
#                print('Sending: ' + data)
#                s.sendto(data.encode('utf-8'), addr)
	c.close()

if __name__ == '__main__':
        Main()

