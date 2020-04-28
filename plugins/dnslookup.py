#!/usr/bin/python3
import sys
from requests import get
def dnslookup(url):
	response = get('https://api.hackertarget.com/dnslookup/?q=' + url).text
	sys.stdout.write(response)