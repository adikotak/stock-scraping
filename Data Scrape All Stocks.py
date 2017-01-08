import urllib
import re

symbolfile = open("tickers.txt")

symbolList = symbolfile.read()

symbolList2 = symbolList.split("\n")


i = 0

while i<len(symbolList2):
    url = "http://finance.yahoo.com/q?s=" +symbolList2[i]+ "&ql=1"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "The price of ", symbolList2[i], " is " ,price[0]
    i += 1



