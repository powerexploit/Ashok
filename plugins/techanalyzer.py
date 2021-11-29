#!/usr/bin/python3
import json
from os import system
from Wappalyzer import Wappalyzer, WebPage
import warnings 
import time
def techno(url):
	start = time.time()
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

	end = time.time()
	print(f"\n[+] Total Execution Time: {end - start} seconds\n\n")
