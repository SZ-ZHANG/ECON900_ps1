# ECON900_ps1
Problem set 1 for Econ 900

Three steps are needed for finishing this project. The first step is web scraping from www.boardgamegeek.com. Then parsed data from the HTML page. The last step is the analysis of the data set. 

## Files in the Repository

Homework_scraping.py is used to get the web structure from boardgamegreek.com.

Homework_parse.py gets the information from the scraped HTML page. 

DataClean.R cleans the data set.

Analysis.py is the python code for data analysis. 

html_files is the raw HTML files.

parsed_results contains the dataset I will use for the analysis.

Analysis_Report.pdf is the final report.

## Web Scraping

A normal web scraping method is not enough, because the webpage contains the dynamic elements. Variables name, ratings, and voter number are contained in the static element, but the price is in the dynamic element. selenium will be used.

Safari has its own webdriver, so I use safari webdriver instead of other web browsers. The total number of the scraping webpage is 1,066.

## Parsing Information

Following the requirement, several variables are collected. They are game name, average rating, greek rating,  game rank, number of voters and list price. 
 
## Analysis Results

Firstly, I use a small R program to clean the dataset. I put NA with all missing values. All the variables are transferred to the proper type for the analysis. Also, I group the gameRank based on quartile. A new variable is added. The cleaned data set has been uploaded in the folder parsed results.

Using python to do the machine learning analysis. An analysis report is included in the repository. 
