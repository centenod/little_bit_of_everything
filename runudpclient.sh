#!/bin/sh
# lunch  UDP client python program 12 times in a
# minute once every 5 secondsc/path/to/task

dateRun="$(date)"
echo $dateRun '  Runned  /etc/Telenor/runudpclient.sh'

(sleep 9 && python3 /etc/Telenor/udpClient.py) &
(sleep 18 && python3 /etc/Telenor/udpClient.py) &
(sleep 26 && python3 /etc/Telenor/udpClient.py) &
(sleep 34 && python3 /etc/Telenor/udpClient.py) &
(sleep 41 && python3 /etc/Telenor/udpClient.py) &
(sleep 48 && python3 /etc/Telenor/udpClient.py) &
(sleep 54 && python3 /etc/Telenor/udpClient.py) &

exit 0
