#!/bin/bash


# dhcpStop.sh
# 
# 1.Stop the dhcp-Server 
# 2.Delete the static IP file from the system and replace it 
# with a empty file of a file that has dhcp configured for 
# the interfaces.
# 

#-------------------------stop the DHCP service

sudo systemctl stop isc-dhcp-server

#--------------------------Delete and copy the interface file
sudo cp 
sudo rm 






