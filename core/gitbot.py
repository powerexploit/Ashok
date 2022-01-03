#!/usr/bin/python3
import os
import requests as res
import json
def gitusers(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print("[+] Dumping Sensitive information from github")
	os.system('tput setaf 9')
	print("[+] Name : ", str(data['name']))
	print("[+] Location : ", str(data['location']))
	print("[+] Website : ", str(data['blog']))
	print("[+] Number of public github Repository : " ,str(data['public_repos']))
	print("[+] Number of public gist Repository : ",str(data['public_gists']))

def gitemails(username):
	response = res.get("https://api.github.com/users/%s/events" %(username))
	expression=re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}',response.text)
	print("[+] Extracting Email data:\n", expression)
