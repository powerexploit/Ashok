#!/usr/bin/python3
import sys
from requests import get
def extract(url):
	response = get('https://api.hackertarget.com/pagelinks/?q=' + url).text
	sys.stdout.write(response)