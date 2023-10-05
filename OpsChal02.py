#Script: 401 Ops challenge 2
#Author: Samuel Allan
#Date of last revision: 10/02/2023
#Purpose: 
#---------In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
#---------Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#---------Evaluate the response as either success or failure.
#---------Assign success or failure to a status variable.
#---------For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
#---------Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8
#---------The script must:
#---------Save the output to a text file as a log of events.
#---------Accept user input for target IP address.

#Import space:
import os
import time
import datetime

#Variables: 
