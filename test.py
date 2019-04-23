import urllib.request
import os
import ssl
import re
from bs4 import BeautifulSoup
import time
import datetime
from urllib.request import urlopen as uReq
import requests

unverified_context = ssl._create_unverified_context()

web_url = 'https://boardgamegeek.com/browse/boardgame/page/2'
response = requests.get(web_url)
#page_html = uClient.read()
#uClient.close()


#response = urllib.request.urlopen(web_url, context = unverified_context)


page_soup = BeautifulSoup(response.text, 'xml')


#response = urllib.request.urlopen(web_url, context = unverified_context)

#soup = BeautifulSoup(response, 'html.parser')

print(page_soup)