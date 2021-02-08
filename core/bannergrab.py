#!/usr/bin/python3
from requests import get
import json
def banner(ip):
	response = get('https://api.hackertarget.com/bannerlookup/?q=' + ip).text
	data = json.loads(response)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)