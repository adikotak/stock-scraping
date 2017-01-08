import urllib
import re

symbolList = ["aapl", "spy", "tsla", "goog", "nflx", "amzn"]

i = 0

while i<len(symbolList):
    url = "http://finance.yahoo.com/q?s=" +symbolList[i]+ "&ql=1"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_' +symbolList[i]+ '">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "The price of ", symbolList[i], " is " ,price
    i += 1



