import os
from bs4 import BeautifulSoup
import glob
import pandas as pd

if not os.path.exists("parsed_results"):
	os.mkdir("parsed_results")

os.chdir("/Users/shen/Desktop/Homework/")

#os.chdir("/Users/shen/Desktop/Homework/html_files")


df = pd.DataFrame()


for one_file_name in glob.glob("html_files/*.html"):

	print("parsing"+ one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()

	
	table_All = soup.find_all("tr", {"id":"row_"})

	#print(table_All)

	for r in table_All:
		#print(r.find('div',{"id":"results_objectname1"}).find('a').text)

		collection_name = r.find("td", {"class":"collection_objectname"}).find('a').text
		
		collection_rank = r.find('td',{"class":"collection_rank"}).text

		collection_rating = r.find("td",{"class":"collection_bggrating"}).text

		collection_avg_rating = r.find("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).text


		collection_voters = r.find("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).findNext("td",{"class":"collection_bggrating"}).text

		#print(r.find("td",{"class":"collection_shop"}).find("div",{"class":"aad"}).find('div').find('div').text)

		collection_price=r.find("td",{"class": "collection_shop"}).find("div", {"class": "aad"})

		# Simply get next tag Or we can search key word List price to collect data
		if collection_price is None:
			continue
		else:
			collection_Listprice = collection_price.next_element.next_element.next_element.next_element
			
			#print(collection_Listprice)

		#collection_Listprice = r.find("td",{"class":"collection_shop"}).find("div",{"class":"aad"}).find('div').find('div').text


		df = df.append({
				'GameName':collection_name,
				'GameRank':collection_rank,
				'GeekRating':collection_rating,
				'AvgRating':collection_avg_rating,
				'NumVoters': collection_voters,
				'ListPrice': collection_Listprice,
			
				} ,ignore_index=True)



#os.chdir("/Users/shen/Desktop/Homework/parsed_results/")

df.to_csv("parsed_results/BoardGameGeek.csv")

#print(type(collection_Listprice))

#table_shop = soup.find_all("td", {"class":"collection_shop"})

#table_price = soup.find_all("tr")

#print(table_price)

#table_test = table_All[0]

#price = table_test.find("td",{"class":"collection_shop"})

#print(price.div)

#print(table_shop[0])
#print(price)





