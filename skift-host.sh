#!/bin/sh

variable="$(hostname)" 
echo 'Current host name:'$variable

MAC2="$(cat /sys/class/net/eth0/address | cut -c13-17)"
compare='RPI-'$MAC2
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
