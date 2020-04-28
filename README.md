<h1 align="center">
  <br>
  <a href="https://github.com/ankitdobhal/Ashok"><img src="https://dev-to-uploads.s3.amazonaws.com/i/vbm48fw5v25qju2h8lr4.png" alt="Osint"></a>
  <br>
  Ashok
  <br>
</h1>

<h4 align="center">Osint Recon Swiss Army Knife</h4>

## Main Features
```python
[+] 1  - HTTP Header Checker

[+] 2  - Whois Lookup

[+] 3  - Dns Lookup

[+] 4  - Nslookup

[+] 5  - Banner Graber

[+] 6  - Github Information Extractor

[+] 7  - Nmap Scan

[+] 8  - Link Extractor 

[+] 9  - Subdomain Identifier

[+] 10 - Subnet Lookup 

[+] 11 - Cms/Technology Detector With Custom Headers

[+] 12 - Geoip Lookup
```

## Compatibility
Ashok is a Osint Recon Swiss Army Knife, It is still in a beta state so it it not compatible with windows .It will run with following configuration:

Operating Systems: Linux, Mac
Python Versions: Python3.5, Python 3.7

## Installation
Ashok is very simple to install with the following steps :

```
~> git clone https://github.com/ankitdobhal/Ashok
~> cd Ashok
~> pip3 install requirements.txt
~> python3 Ashok -h
```

## Usage

Ashok is a beginners friendly tool for beginners in penetration testing and Osint, it can be used with the following command and examples : 

**[+] Note : You can check whole help page of Ashok with the following command :**
**~> python3 Ashok.py -h**
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/uiiarf08z0dk0vk6vhp8.png)

**Here are some basic example to use Ashok for your Osint recon :**
```
1. HTTP Header Checker

~> python3 Ashok.py --headers domain_name
example : python3 Ashok.py --headers example.com
```

```
2. Whois Lookup

~> python3 Ashok.py --whois domain_name
example : python3 Ashok.py --whois example.com
```

```
3.Banner Graber
~> python3 Ashok.py --banner ip_address
example : python3 Ashok.py --banner 8.8.8.8
```

```
4. Github Information Extractor
~> python3 Ashok.py --username username_of_github_user
example : python3 Ashok.py --username Elliot
```

```
5. Cms/Technology Detector With Custom Headers
~> python3 Ashok.py --cms url_of_target
example : python3 Ashok.py --cms https://www.example.com
```

## Contribution & License
You can contribute in following ways:

- Report bugs
- Develop plugins
- Give suggestions to make it better
- Fix issues & submit a pull request
