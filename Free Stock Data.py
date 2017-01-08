import urllib
import re
import json

symbolsList = open("tickersv2.txt").read()
symbolsList = symbolsList.split("\n")


for symbol in symbolsList:
    myfile = open("Daily Prices/" + symbol + ".csv", "w+")
    htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/" +symbol+ ":US")
    data = json.load(htmltext)
    datapoints = data["data_values"]
    myfile = open("Daily Prices/" + symbol + ".csv", "a+")
    for points in datapoints:
        myfile.write("Symbol: " + str(symbol) +", Price: "+ str(points[1]) +", Time: "+ str(points[0]) +"\n")
    myfile.close()

        #print "Stock: ",symbol, " Sold at: ",points[1], " at time: ", points[0]

