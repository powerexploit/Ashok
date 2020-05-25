#!/usr/bin/python3.7
import requests as res
import json
from os import system
def waybackurl(url):
	rq = res.get('http://web.archive.org/cdx/search/cdx?url=%s&output=json' %(url)).text
	system('tput setaf 9 ')
	rt = res.get('http://web.archive.org/cdx/search/cdx?url=%s&showNumPages=true' %(url)).text
	result = json.loads(rq)
	dump = json.dumps(result,sort_keys=True,indent=4)
	print('[+] Number of pages of target websites : ',rt)
	print('[+] Dumping wayback-machine data for target url and saving in : "waybackurls-list.json" file')
	with open('waybackurls-list.json', 'w') as f:
		f.write(dump)

def waybackrobots(domain):
	rq = res.get('https://web.archive.org/cdx/search/cdx/?url=%s/robots.txt&output=json&fl=timestamp,original&filter=statuscode:200&collapse=digest&limit=10' %(domain))
	result = json.loads(rq.text)
	dump = json.dumps(result,sort_keys=True,indent=4)
	system('tput setaf 6')
	print('[+] Dumping robots url using wayback-machine and saving in : "waybackrobots-list.json" file')
	with open('waybackrobots-list.json','w') as f:
		f.write(dump)

def waybackjson(url):
	rq = res.get('http://web.archive.org/cdx/search/cdx?url=%s&output=json&limit=3&' %(url)).text
	data = json.loads(rq)
	dump = json.dumps(data,sort_keys=True,indent=4)
	system('tput setaf 3')
	print(dump)