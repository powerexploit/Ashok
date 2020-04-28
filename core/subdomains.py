#!/usr/bin/python3
import sys
from requests import get
def sub(domain):
	response = get('https://api.hackertarget.com/hostsearch/?q=' + domain).text
	print(response,"\n")