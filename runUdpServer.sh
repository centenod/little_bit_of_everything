#!/bin/sh
# lunch  UDP client python program 

echo '\n'
dateRun="$(date)"
echo $dateRun '  Runned  /etc/Telenor/runudpclient.sh'

python3 /etc/Telenor/udpServer.py
