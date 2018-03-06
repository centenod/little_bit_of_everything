# little_bit_of_everything
little_bit_of_everything


###### Steps to fully configure a node:

###### 1. Update and upgrade the OS.
###### 2. Download the files from GitHub:
$ git clone git://github.com/Laassee/masterT /home/pi
###### 3. Move the folder "telenor" :
$ mv /home/pi/masterT/t* /home/pi/
###### 4. Delete the folder downloaded from GitHub:
$sudo rm -r /home/pi/masterT/
###### 5. Install applications and programs used:
$ sudo apt-get update && sudo apt-get upgrade -y
$ sudo pip3 install netifaces 
$ sudo easy_install3 pip 
$ sudo apt-get install -y isc-dhcp-server 
$ sudo apt-get install -y nmap

(sudo crontab -l 2>/dev/null; echo "* * * * * myscript")| sudo crontab - 
(sudo crontab -l ; echo "* * * * * myscript")| sudo crontab -


###### 7. Give permissions to the files to write logs 
$ sudo chmod 777 /home/pi/telenor/changeHost.sh
$ sudo chmod 777 /home/pi/telenor/runUdpClient.sh
$ sudo chmod 777 /home/pi/telenor/udpServer.py
$ sudo chmod 777 /home/pi/telenor/updatePiList.py
$ sudo chmod 777 /home/pi/telenor/countDown.py

###### Replace existing DHCP server configuration with custom from ./telenor/network 
$ sudo rm /etc/dhcp/dhcpd.conf && sudo cp /home/pi/telenor/network/custom_dhcpd.conf /etc/dhcp/dhcpd.conf 

###### Update which inteface the DHCP service should work with (replace existing file): 
$ sudo rm /etc/default/isc-dhcp-server && sudo cp /home/pi/telenor/network/isc-dhcp-server /etc/default/isc-dhcp-server







Downloading the files:


wget ______________path____________ ____location______________

also install:

sudo apt-get update
sudo apt-get upgrate
sudo pip3 install netifaces
sudo easy_install3 pip
sudo apt-get install -y isc-dhcp-server
sudo apt-get install -y nmap



for running the udp client file every minute with space of 5 seconds in bettew go to crontab and add the following line at the bottom of the file

$ crontab -e
add the following line at the bottom:


* * * * * /etc/Telenor/runudpclient.sh >> /etc/Telenor/logrunudpclient.log 2>&1
@reboot /etc/Telenor/changehost.sh >> /etc/Telenor/logChangehost.log 2>&1
@reboot /etc/Telenor/runudpserver.sh >> /etc/Telenor/logudpserver.log 2>&1


/etc/Telenor contains:
updClient.py
udpServer.py
updatePiList.py
piList.csv
runUdpClient.sh
runUdpServer.sh
changeHost.sh

pi@raspberrypi:/etc/Telenor $ sudo chown pi:pi /etc/Telenor
sudo chmod 777 "files that need permision"
