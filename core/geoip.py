#!/usr/bin/python3
import sys
from requests import get
def geo(ip):
	response = get('https://api.hackertarget.com/geoip/?q=' + ip).text
	sys.stdout.write(response)