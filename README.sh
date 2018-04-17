###################################################
#####     Full instalation of the nodes
##################################################


###### Steps to fully configure a node:

###### 1. Update and upgrade the OS.
$ sudo apt-get update && sudo apt-get upgrade -y

###### 2. Download the files from GitHub:
$ git clone git://github.com/Laassee/masterT /home/pi/

###### 3. Move the folder "telenor" and  Delete the folder downloaded from GitHub:
$ mv /home/pi/masterT/t* /home/pi/ && sudo rm -r /home/pi/masterT/

###### 4. Install applications and programs used:
$ sudo pip3 install netifaces 
$ sudo easy_install3 pip 
$ sudo apt-get install -y isc-dhcp-server 
$ sudo apt-get install -y nmap
###### 5. Edit the crontab file
(sudo crontab -l 2>/dev/null; echo "* * * * * /home/pi/telenor/runUdpClient.sh >> /home/pi/logRunUdpLog.log 2>&1")| sudo crontab -
(sudo crontab -l 2>/dev/null; echo "@reboot /home/pi/telenor/changeHost.sh >> /home/pi/logChangeHost.log 2>&1")| sudo crontab -
(sudo crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /home/pi/telenor/udpServer.py >> /home/pi/logRunUdpServer.log 2>&1")| sudo crontab -

###### 6. Give permissions to the files to write logs 
$ sudo chmod 777 /home/pi/telenor/changeHost.sh
$ sudo chmod 777 /home/pi/telenor/runUdpClient.sh
$ sudo chmod 777 /home/pi/telenor/udpServer.py
$ sudo chmod 777 /home/pi/telenor/updatePiList.py
$ sudo chmod 777 /home/pi/telenor/countDown.py

###### 7. Replace existing DHCP server configuration with custom from ./telenor/network 
$ sudo rm /etc/dhcp/dhcpd.conf && sudo cp /home/pi/telenor/network/custom_dhcpd.conf /etc/dhcp/dhcpd.conf 

###### 8. Update which inteface the DHCP service should work with (replace existing file): 
$ sudo rm /etc/default/isc-dhcp-server && sudo cp /home/pi/telenor/network/isc-dhcp-server /etc/default/isc-dhcp-server

https://sourceforge.net/projects/hexinject/files/hexinject-1.6/hexinject-1.6.tar.gz/download
https://sourceforge.net/projects/hexinject/files/latest/download?source=files
