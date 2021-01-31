#!/usr/bin/python3
from requests import get
def geo(ip):
	response = get('https://api.hackertarget.com/geoip/?q=' + ip).text
	print(response,"\n")
