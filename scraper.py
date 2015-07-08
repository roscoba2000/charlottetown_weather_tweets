import scraperwiki
import requests

import time
import urllib
import re
import csv
import tweepy

HTML = urllib.urlopen("http://www.theguardian.pe.ca/Weather-Forecast").read()
HTML = re.search('<strong class="temperature">(.+?)</strong>', HTML, re.S)
Temperature = HTML.group(1)

TempTweet = "The temperature in Charlottetown is " + Temperature + " http://www.theguardian.pe.ca/Weather-Forecast"

auth = tweepy.OAuthHandler("FownCzUifldM8XrpRN70t9Rpr", "tKZQDS1tzbXen2jHkPMhrdBzagDt62LC3JgESm2K4s7QdMdu0n")
auth.set_access_token("9056452-PnygMdcxjnRohFEq2NmUeiSojgwIG9uEjyHJPyZMsQ", "zeAZBSf4VrbyewmrF5mbZV4GddW7y1FRgw4CATn8pG33r")
api = tweepy.API(auth)

# searchResult = api.search(geocode="43.6363,-79.353,500km", rpp="100")
api.update_status(status=TempTweet)
print TempTweet
