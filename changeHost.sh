#!/bin/bash

dateRun="$(date)"
echo $dateRun '  Runned  /etc/Telenor/changeHost.sh'

actual="$(hostname)"
#echo 'Current host name:  '$actual

MAC1="$(cat /sys/class/net/eth0/address)"

#echo 'MAC address: '$MAC1
MAC2="$(cat /sys/class/net/eth0/address | cut -c13-14)"
MAC3="$(cat /sys/class/net/eth0/address | cut -c16-17)"
desired='RPI-'$MAC2$MAC3
#echo 'Desired hostname: '$desired

if [ $actual != $desired ]; then

#       echo 'inside if'
#       echo '-----task-----'
#       echo '-----task-----'
#       echo '-----task-----'
#       sed -i "s/$actual/$desired/g" /etc/hosts
#       sed -i "s/$actual/$desired/g" /etc/hostname
        echo '    changed from '$actual' to '$desired
        echo '    if is working well , just uncomment the  commands in /etc/Tel$
#       reboot

fi

#echo 'Done'




