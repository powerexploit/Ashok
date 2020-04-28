#!/usr/bin/python3
import sys
from os import system
import webtech
def techno(url):
	obj = webtech.WebTech()
	results = obj.start_from_url(url, timeout=1)
	system('tput setaf 9')
	sys.stdout.write(results)