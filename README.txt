# little_bit_of_everything
little_bit_of_everything


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

* * * * * /bin/sh /etc/Telenor/runudpclient.sh
* * * * * /bin/sh //etc/Telenor/changehost.sh

