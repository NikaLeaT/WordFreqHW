# save-webpage.py

import urllib.request, urllib.error, urllib.parse, json

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

f = open('obo-t17800628-33.html', 'wb')
f.write(webContent)
f.close