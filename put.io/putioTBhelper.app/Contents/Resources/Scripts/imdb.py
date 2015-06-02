#!/usr/bin/env python
import requests
import json
import StringIO
import sys

_input = sys.argv[1].lower().strip()
nsearch = _input.replace(" ","+")
url = "http://www.omdbapi.com/?t=" + nsearch + "&r=json"
r = requests.get(url)
t = r.text
j = json.loads(t)
print j[u'imdbID'] + " :: " + j[u'Title']
quit()

