from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")
	
os.chdir("/Users/shen/Desktop/Homework/html_files/")
#### In mac system, safari has its own webdriver
driver = webdriver.Safari()

for x in range(1066):
	#### Get index from 1 to 1066
	x = x+1
	#### Use the dynamic method to grab the HTML 
	driver.get("https://boardgamegeek.com/browse/boardgame/page/" +str(x)) 
	page_html = driver.page_source 

	#### Write the web into files and a 10 second stop between each collection
	f = open("Boardgamegeek" + str(x)+".html", "w") 
	f.write(page_html)
	f.close()
	time.sleep(10)

driver.close()