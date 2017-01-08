import urllib
import re

symbolfile = open("tickers.txt")

symbolList = symbolfile.read()

symbolList2 = symbolList.split("\n")

i = 0

while i<len(symbolList2):

    htmltext = urllib.urlopen("https://www.google.com/finance/getprices?q="+symbolList2[i]+"&i=10&p=25m&f=c&df=cpct&auto=1&ts=1407269107353&ei=tTjhU9CyHq-2iALkuIG4Bg").read()
    price =  htmltext.split()[len(htmltext.split())-1]
    print "The price of " ,symbolList2[i], " is ", price
    i += 1
    

