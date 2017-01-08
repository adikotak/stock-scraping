import urllib
import re
import json

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/GOOG:US")

data = json.load(htmltext)

datapoints = data["data_values"]

for points in datapoints:
    print points[1]

print "Total Price Count: ",len(datapoints)
