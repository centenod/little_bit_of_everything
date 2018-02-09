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

* * * * * /etc/Telenor/runudpclient.sh >> /etc/Telenor/losrunudpclient.log 2>&1     #log when the program was runned
#0-59/15 * * * *  /etc/Telenor/changehost.sh >> /etc/Telenor/logChangehost.log 2>&1 #It will log everytime it runs
@reboot python3 /etc/Telenor/udpServer.py >> /etc/Telenor/logudpServer.log          #It will log absolutly every broadcast a R-PI sends


