import urllib
import re
import json

htmltext = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US")

data = json.load(htmltext)

print data["last_price"]

