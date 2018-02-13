#!/bin/sh
# lunch  UDP client python program 

echo '\n'
dateRun="$(date)"
echo $dateRun '  Runned  /etc/Telenor/runSdpSlient.sh'

sudo python3 /etc/Telenor/udpServer.py
