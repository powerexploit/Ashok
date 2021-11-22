#!/usr/bin/python3
import json
from os import system
from Wappalyzer import Wappalyzer, WebPage
import warnings 
def techno(url):
	try:
		webpage = WebPage.new_from_url(url)
		warnings.simplefilter("ignore")
		wappalyzer = Wappalyzer.latest()
		tech = wappalyzer.analyze_with_versions_and_categories(webpage)
		data = json.dumps(tech, indent = 4)
		system('tput setaf 9')
		print(data)
	except:
		print("[+] Oops unable to connect..")
