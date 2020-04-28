#!/usr/bin/python3
import sys
from requests import get
def nmap(domain):
	response = get('http://api.hackertarget.com/nmap/?q=' + domain).text
	sys.stdout.write(response)