import time
import urllib
import re
import csv
import tweepy

HTML = urllib.urlopen("http://www.theguardian.pe.ca/Weather-Forecast").read()
HTML = re.search('<strong class="temperature">(.+?)</strong>', HTML, re.S)
Temperature = HTML.group(1)

TempTweet = "The temperature in Charlottetown is " + Temperature + " http://www.theguardian.pe.ca/Weather-Forecast"

auth = tweepy.OAuthHandler("o5NHBNd94C8MHOwKfmRW6Am36", "J2va7YswmudkDXC3CuXdjN6WjAlZYnyQUTdYTiZqcGd1Dqmgpj")
auth.set_access_token("3351764193-OJibbL4vL61nnzeKEf9EJEx0gOf5v0pxBfmQGJG", "FlkMDrcAi1iTgE94CppjiwVoZNMXpKiSTYAfJbXQ4Iime")
api = tweepy.API(auth)

# searchResult = api.search(geocode="43.6363,-79.353,500km", rpp="100")
api.update_status(status=TempTweet)
print TempTweet
