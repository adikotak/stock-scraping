import urllib
import re

urls = ["http://google.com", "http://cnn.com", "http://facebook.com", "http://yahoo.com", "http://reddit.com", "http://nytimes.com"]

i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i<len(urls):
    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern, htmltext)
    print titles
    i += 1


    
