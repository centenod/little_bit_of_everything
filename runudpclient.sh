#!/bin/sh
# lunch  UDP client python program 12 times in a
# minute once every 5 secondsc/path/to/task

(sleep 9 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 18 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 26 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 34 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 41 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 48 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
(sleep 54 && python3 /home/pi/Desktop/ServerClient/udpClient.py) &
