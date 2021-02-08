#!/usr/bin/python3
from requests import get
def sub(domain):
	response = get('https://api.hackertarget.com/hostsearch/?q=' + domain).text
	print(response,"\n")