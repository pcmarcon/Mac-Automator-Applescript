#!/usr/bin/python
# coding: utf-8
# vim: ts=4: expandtab
import sys
import requests
import json
import StringIO

_putiourl = sys.argv[1]
_putiotoken =  sys.argv[2]

print _putiourl
print _putiotoken

url = "https://put.io/v2/files/"+_putiourl[-9:]+"?token="+_putiotoken
print url
quit()

r = requests.get(url)
print r
t = r.text
print t
# i = t.index('[')
j = json.loads(t)
for item in j[u'd']:
    print item.get('l')

quit()


