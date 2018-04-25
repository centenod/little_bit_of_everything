#!/bin/bash

#dateRun="$(date)"
#echo $dateRun '  Runned  /etc/Telenor/runudpclient.sh'

#echo "Positional parameter"
#echo '$0 =  ' $0
#echo '$1 =  ' $1
#echo '$2 =  ' $2
#echo '$3 =  ' $3
#echo '$4 =  ' $4

#echo "You start with $# positional parameters"

targetIP='10.168.74.115'
interface='wlan0'
interval=0.5
count=10
size=1000
multiplicator=10
while [ "$1" != "" ]; do
    case $1 in
        -t | --target )		shift
                                targetIP=$1
#				echo $interface
                                ;;
        -I | --Interface )	shift
                                interface=$1
#				echo $interface
                                ;;
        -i | --interval )	shift
				interval=$1
#				echo $interval
                                ;;
        -c | --count )		shift
				count=$1
#				echo $count
                                ;;
        -s | --size )		shift
				size=$1
#				echo $size
                                ;;
        -m | --multiplicator )	shift
				multiplicator=$1
                                ;;
        * )
                                exit 1
    esac
    shift
done




delay=0
declare -a packets=(55 40 30 25 20 10 5)
declare -a sizes=(200 400 800 1600 3200 3200 6400)


#clear
for number in 0 1 2 3 4 5 6
do


#(sleep $delay && sudo ping $targetIP -i $interval -I $interface -c $count -s $size)

size=$((${sizes[$number]}*$multiplicator))
delay=$(($number*2))
#echo 'sleep '$delay '&& sudo ping '$targetIP' -i '$interval' -I '$interface' -c '${packets[number]}' -s '$size
(sleep $delay && sudo ping $targetIP -i $interval -I $interface -c ${packets[number]} -s $size &> /dev/null) &

done
exit 0

