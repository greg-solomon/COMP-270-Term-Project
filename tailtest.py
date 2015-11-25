#!/usr/bin/python
import time

""" this script is meant to test the tail function from the main script. I did this by using the function to read the HTTP access_log file 
and repeatedly made requests to my server from my browser while the script was running """
def tail(file):
	file.seek(0,2)	
	while True:
		line = file.readline()
		if not line:
			time.sleep(1)
			continue
		yield line
		
if __name__ == "__main__":
	file = open("/var/log/httpd/access_log")
	lines = tail(file)
	for line in lines:
		print line
