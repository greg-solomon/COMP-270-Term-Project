#!/usr/bin/python
import time,subprocess,os
from re import *

def tail(file):	# reads from beginning of file and waits at the end to return lines as they are generated
	file.seek(0,2)	
	while True:
		line = file.readline()
		if not line:
			time.sleep(60)
			continue
		yield line
		
def block(ip):	# creates an ip.block file for a shell script to use to block an ip and keeps a list of all ip's that have been blcoked by the script in ip.blocked

	# sanitize IP from ['xxx.xxx.xxx.xxx'] to xxx.xxx.xxx.xxx
	for char in "[']":
		ip = ip.replace(char,"")
	
	# check if the ip.blocked file already exists
	if os.path.exists("ip.blocked"):
		blocked = open("ip.blocked","r")
		
		
		if ip in blocked.read():
			blocked.close()
			return
		else:
			block = open("ip.block","w")
			blocked.close() 
			blocked = open("ip.blocked","a")
			blocked.write(ip+"\n")
			block.write(ip)
			
			
			blocked.close()
			block.close()
			
			# block ip and delete ip.block file
			subprocess.call(['./block.sh'])
			os.remove("ip.block")
	else:
	#	ip.blocked doesn't exist so we start it
	# 	ip.block is still necessary because the bash script is looking for ip.block
		blocked = open("ip.blocked","w")
		blocked.write(ip+"\n")
		
		block = open("ip.block", "w")
		block.write(ip)
		
		blocked.close()
		block.close()
		
		subprocess.call(['./block.sh'])
		os.remove("ip.block")
		
		
	
if __name__ == "__main__":
	f = open("/var/log/secure","r")

	catalog = {}
	lines = tail(f)
	
	for line in lines:
		if search(r"Invalid user",line):
			ip = findall(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', line)
			ip = str(ip)
			if ip in catalog.keys():
				catalog[ip] += 1
				if catalog[ip] > 3:
					block(ip)
			else:
				catalog[ip] = 0
