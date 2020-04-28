#!/usr/bin/python3
import requests as res
import json
def gitusers(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print("[+] Dumping Sensitive information from github")
	system('tput setaf 9')
	print("[+] Name : ", str(data['name']))
	print("[+] Location : ", str(data['location']))
	print("[+] Website : ", str(data['blog']))
	print("[+] Number of public github Repository : " ,str(data['public_repos']))
	print("[+] Number of public gist Repository : ",str(data['public_gists']))

def gitemails(username):
	try:
		response = res.get("https://api.github.com/users/%s/events/public" %(username))
		jsn = response.json()
		data = jsn[0]
		dump = data["payload"]["commits"][0]["author"]["email"]
		print("[+] Email data : ", dump)	
	except KeyError:
		system('tput setaf 12')
		print("[+] Aww Snap Unable to find out the email address!")