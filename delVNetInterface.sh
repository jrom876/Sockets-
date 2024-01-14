#!/bin/bash

sudo ip addr del 192.168.1.100/24 brd + dev $1 label $1:0
sudo ip link delete $1 type dummy
sudo rmmod dummy
ip a
