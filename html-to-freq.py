#html-to-freq.py

import urllib.request, urllib.error, urllib.parse, obo, json

record = json.loads(body)

url = 'https://www.dhi.ac.uk/api/data/oldbailey_record_single?idkey=t17800628-33'

response = urllib.request.urlopen(url)

body = response.read().decode('UTF-8')

record = json.loads(body)

html = record['hits']['hits'][0]['_source']['html']

text = obo.stripTags(html).lower()
wordlist = obo.stripNonAlphaNum(text)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))