#!/bin/bash

macadr="$(cat /sys/class/net/eth0/address)"
sudo sed -i "s/thismacaddress/$macadr/g" /etc/dhcp/dhcpd.conf


# now it should start the DHCP service
