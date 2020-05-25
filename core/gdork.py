#!/usr/bin/python3.7
import os
import time
from googlesearch import search
def dork(amount):
	gquery = input("[+] Enter THe Google Dork Query : ")
	os.system('tput setaf 6')
	print("[+] Google Dorking For Given Dorkquery")
	requ = 0
	counter = 0
	for results in search(gquery, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
		counter = counter+1
		print ("[+] ", counter, results)
		time.sleep(0.1)
		requ += 1
		if requ >= int(amount):
			break