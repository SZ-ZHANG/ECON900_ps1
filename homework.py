import urllib.request
import os
import ssl
import re
from bs4 import BeautifulSoup as soup
import time
import datetime

os.chdir("/Users/shen/Desktop/Homework/html_files/")

unverified_context = ssl._create_unverified_context()
#responsetest = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame', context = unverified_context)
#https://boardgamegeek.com/browse/boardgame/page/2
#html_test = responsetest.read()
#soup_test = soup(html_test, "html.parser")
#currencies_table = soup_test.find("div", {"class":"infobox"})

#currencies_table2 = currencies_table.div
#currencies_table3 = currencies_table.find('a',{'title':"last page"})
#r1 = re.search("page/", currencies_table3).start()
#print(r1)

for x in range(607	,1062):
  x = x+1
  web_url = 'https://boardgamegeek.com/browse/boardgame/page/'
  f = open("Boardgamegeek" + str(x) + ".html", "wb")
  web_urlseq = web_url + str(x)	
  response = urllib.request.urlopen(web_urlseq, context = unverified_context)
  page_html = response.read()
  f.write(page_html)
  f.close()	
  time.sleep(60)




