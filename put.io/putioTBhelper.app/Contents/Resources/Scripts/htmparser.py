#!/usr/bin/env python
import requests
import json
import StringIO
import sys

_input = sys.argv[1].lower().strip()
#print _input
nsearch = _input.replace(" ","_")

if nsearch[0:3] == "the":
	nsearch = nsearch[4:]

if nsearch[0:2] == "a_":
	nsearch = nsearch[2:]

n1st = nsearch[0:1]

if (n1st == "c") or (n1st == "b"):
	nsearch = nsearch[0:4]
#elif
	# nsearch = nsearch[0:5]
elif (n1st == "a") or (n1st == "d"):
	nsearch = nsearch[0:6]
elif (n1st == "i") or  (n1st == "l"):
	nsearch = nsearch[0:8]
else:
	nsearch = nsearch[0:5]

#print n1st
#print nsearch

url = "http://sg.media-imdb.com/suggests/" + n1st + "/" + nsearch + ".json"
#print url
r = requests.get(url)
t = r.text[(r.text.find("(")+1):-1]
#print t
#i = t.index('[')
j = json.loads(t)
# search for the exact name
for item in j[u'd']:
	iTitle = item.get('l')
	iID = item.get('id') 
	if iTitle.lower() == _input:
		print iID + " :: " + iTitle
		quit()
		
# if exact name not found return all list from imdb
for item in j[u'd']:
	iTitle = item.get('l')
	iID = item.get('id') 
	print iID + " :: " + iTitle





