# COMP-270-Term-Project
A python file that parses the secure log file in real time and blocks crackers after they have made multiple login attempts. Includes file used to test the tail() function in the main script. 

This script blocks IP's by writing the perpetrator's IP to an ip.block file and executes a shell script that creates iptables rules to block outgoing and incoming traffic from that IP.
