#!/usr/bin/python3
import sys
from requests import get
def whois(url):
	response = get('http://api.hackertarget.com/whois/?q=' + url).text
	sys.stdout.write(response)