import socket
import time
from updatePiList import updatePiList

def Main():
        port = 5000

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('',port))

        print("Server started!")
        while True:
                data, addr = s.recvfrom(1024)
                data = data.decode('utf-8')

                address = str(addr)
                for char in address:
                        if char in "( )'":
                                address = address.replace(char,'')
                ts = time.asctime ( time.localtime(time.time()))
                status = (data + "," + address + "," + "Up" + "," + "3" + "," + ts)
                l = status.split(',')
                l.remove('5001')
                print(l)
                updatePiList(l)
        c.close()
	
if __name__ == '__main__':
        Main()
