#!/usr/bin/python3
import os
import sys
import argparse
import json
import webtech
from requests import get
from core.nmap import nmap
from core.gitbot import gitusers,gitemails
from core.linkextractor import extract
from core.bannergrab import banner
from core.subdomains import sub
from core.geoip import geo
from core.wayback import waybackurl,waybackrobots,waybackjson
from core.gdork import dork
from plugins.dnslookup import dnslookup
from plugins.subnetlookup import subnetlookup
from plugins.httpheaders import httpheader
from plugins.techanalyzer import techno
os.system('tput setaf 9')
print("""


 ▄▄▄        ██████  ██░ ██  ▒█████   ██ ▄█▀
▒████▄    ▒██    ▒ ▓██░ ██▒▒██▒  ██▒ ██▄█▒ 
▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██░  ██▒▓███▄░ 
░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▒██   ██░▓██ █▄ 
 ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░ ████▓▒░▒██▒ █▄
 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▒ ▓▒
  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒ ▒░
  ░   ▒   ░  ░  ░   ░  ░░ ░░ ░ ░ ▒  ░ ░░ ░  > Recon Swiss Army Knife
      ░  ░      ░   ░  ░  ░    ░ ░  ░  ░      v1.1   
""")
os.system('tput setaf 6')
print("""
 Author  : Ankit Dobhal | Break||The||Code
 Github  : https://github.com/ankitdobhal
 Website : http://ankitdobhal.github.io/ 
 =========================================
	""")
os.system('tput setaf 3')
parser = argparse.ArgumentParser()
parser.add_argument('--headers',help='Httpheaders of target url')
parser.add_argument('--dns',help='Dnslookup of target domain')
parser.add_argument('--subdomain',help='Subdomain lookup of target domain')
parser.add_argument('--nmap',help='Nmapscan of target domain')
parser.add_argument('--username', help='Github username of target')
parser.add_argument('--cms', help='Cms detect with headers url of target')
parser.add_argument('--extract',help='Extract links from target url(https/http)')
parser.add_argument('--cidr',help='Cidr for subnetlookup of target')
parser.add_argument('--banner',help='Banner grabing of target ip address')
parser.add_argument('--geoip',help='GeoIP lookup of target ip address')
parser.add_argument('--wayback',help="Internet Archive Crawling of target domain")
parser.add_argument('--dorknumber',help="Google dorking results number")
args = parser.parse_args()

if args.headers:
	print("[+] Extracing http headers of target url")
	os.system('tput setaf 10')
	httpheader(args.headers)
	exit()

if args.nmap:
	print("[+] Port scanning of target domain")
	os.system('tput setaf 10')
	nmap(args.nmap)
	exit()

if args.username:
	gitusers(args.username)
	gitemails(args.username)
	exit()

if args.cms:
	print("[+] Detecting CMS with Identified Technologies and Custom Headers from target url")
	os.system('tput setaf 10')
	techno(args.cms)
	exit()

if args.cidr:
	os.system('tput setaf 10')
	subnetlookup(args.cidr)
	exit()

if args.banner:
	print("[+] Banner Grabing from target ip address")
	os.system('tput setaf 10')
	banner(args.banner)
	exit()

if args.dns:
	print("[+] DNS lookup of target domain")
	os.system('tput setaf 10')
	dnslookup(args.dns)
	exit()

if args.subdomain:
	print("[+] Subdomain lookup from target domain")
	os.system('tput setaf 7')
	sub(args.subdomain)
	exit()

if args.extract:
	print("[+] Extracting all hidden and visiable links from target url")
	os.system('tput setaf 10')
	extract(args.extract)
	exit()

if args.geoip:
	print("[+] Geoip lookup of target Ip address")
	os.system('tput setaf 10')
	geo(args.geoip)
	exit()

if args.wayback:
	print("[+] Dumping and Crawling Internet Archive Machine With Ashok")
	waybackurl(args.wayback)
	waybackrobots(args.wayback)
	waybackjson(args.wayback)
	exit()

if args.dorknumber:
	dork(args.dorknumber)
	exit()