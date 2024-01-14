#!/bin/bash

read -p "Enter the new network interface name: " newName
echo "You entered $newName" 
## read -p "Enter the new IP Address: " newIP
## echo "You entered $newIP" 

## Start off by enabling the dummy kernel module with the following command
sudo modprobe dummy

## Now that the module has been loaded, we can create a new virtual interface. 
## Feel free to name yours however you want.
sudo ip link add $newName type dummy

## Verify that the link was added by executing the following command afterwards
ip link show $newName

## We have our virtual interface, but it’t not much use to us without an IP address or MAC address. 
## Let’s give the interface a MAC address with the following command. 
## Feel free to substitute any address you want to use, as ours is just a randomly generated one.
sudo ifconfig $newName hw wlan 192.168.1.100

## We can now add an alias to the interface and configure an it with an IP address. 
sudo ip addr add 192.168.1.100/24 brd + dev $newName label $newName:0

## Don’t forget to put the interface up, or it probably won’t be very useful. 
sudo ip link set dev $newName up

## You should now be able to use your virtual network interface for whatever you want. 
## You can see the full configuration by viewing the output of the ip a command. 
ip a
