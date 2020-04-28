#!/usr/bin/python3
import sys
from requests import get
def nslookup(url):
	response = get('http://api.hackertarget.com/dnslookup/?q=' + url).text
	sys.stdout.write(response)