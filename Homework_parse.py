import os
from bs4 import BeautifulSoup
import glob
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


cwd = os.getcwd()

print(cwd)

driver = webdriver.Safari()


driver.get("https://boardgamegeek.com/browse/boardgame/page/1")

html = driver.page_source

print(html)

#cwd = os.getcwd()
#print(cwd)
## command + d 
#if not os.path.exists("parsed_results"):
#	os.mkdir("parsed_results")

#one_file_name = "Boardgamegeek1.html"

#os. chdir("/Users/shen/Desktop/Homework/html_files")

#f = open(one_file_name, "r")
#soup = BeautifulSoup(f.read(), 'html.parser')
#f.close()

#table_All = soup.find_all("tr", {"id":"row_"})

#table_shop = soup.find_all("td", {"class":"collection_shop"})

#table_price = soup.find_all("tr")

#print(table_price)

#table_test = table_All[0]

#price = table_test.find("td",{"class":"collection_shop"})

#print(price.div)

#print(table_shop[0])
#print(price)





