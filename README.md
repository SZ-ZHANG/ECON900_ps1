# ECON900_ps1
Problem set 1 for Econ 900

There are three parts in this repository. The first parts contain the web scraping for www.boardgamegeek.com. The second part contains the parsed results from the HTML page. The third part contains the analysis results of the data set. 

## Web Scraping

Simply get next tagA normal web scraping method is not enough, because the webpage contains the dynamic elements. Variables name, ratings, and voter number are included in the static element, but the price is in the dynamic element. selenium will be used.

Safari has its own webdriver, so I use safari webdriver instead of other web browsers. The total number of the scraping webpage is 1,066.

## Parsing Information

Following the requirement, several variables are collected. They are game name, average rating, greek rating,  game rank, number of voters and list price. 
 
