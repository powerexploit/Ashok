#!/usr/bin/python3
from requests import get
def subnetlookup(cidr):
	response = get('https://api.hackertarget.com/subnetcalc/?q='+ cidr).text
	print(response)