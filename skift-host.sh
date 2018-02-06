#!/bin/sh

variable="$(hostname)" 
echo 'Current host name:'$variable


MAC1="$(cat /sys/class/net/eth0/address)"
echo 'MAC address: '$MAC1

MAC2="$(cat /sys/class/net/eth0/address | cut -c13-14)"
MAC3="$(cat /sys/class/net/eth0/address | cut -c16-17)"
compare='RPI-'$MAC2$MAC3
echo 'Desired hostname: '$compare




if [ $variable != $compare ]; then

        echo 'inside if'
        echo '-----task-----'
        echo '-----task-----'
        echo '-----task-----'
#       hostname 'NEWtry'                 #Change the HOSTNAME
#       reboot

#else
#echo 'outside'


fi
echo 'done'
