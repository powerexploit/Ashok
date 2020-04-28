#!/usr/bin/python3
import sys
from requests import get
def httpheader(url):
	response = get('https://api.hackertarget.com/httpheaders/?q=' + url).text
	sys.stdout.write(response)