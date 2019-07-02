from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pandas as pd
import time
import random

df = pd.read_csv("UrlList.csv")
browser = webdriver.Chrome('/home/raghu/Pictures/chromedriver') 

print(len(df))
for j in range(len(df)):
#for j in range(7,8):				# Only select 1st url from urlList 
	print("Testing started")
	browser.get(df.loc[j, "Url"])						#open website 
	print (df.loc[j, "Symbol"])							# Company Name from urlList.csv
	print("Testing 1")
	time.sleep(random.randint(5, 10))					#sleep time 5-10ms before it gets data from selenium
	print("Testing 2")
	browser.execute_script("window.scrollTo(0, 2000)")	#scroll window to 0-2000 through webdriver tool(selenium)
	print("Testing 3")
	time.sleep(random.randint(5, 10))					#sleep time 5-10ms after it gets data from selenium and process it
	print("Testing stop")
	alldata = []										#create list "alldata"
	allData = browser.find_elements_by_class_name("rht_content")	#adding values from browser whose class name is "rht_content"
	print(allData)
	
	comments = []										#create a list "comment"
	dates = []											#create a set "dates"
		    
	for i in allData:									#iterate data in allData
		comment = i.find_element_by_class_name("txt16gry")		#add comment from class name "txt16gry" from allData
		#print(comment)
		date = i.find_element_by_class_name("link13gry")		#add date from class name "link13gry" from allData
		#print(date)
		#print("\n")
		try:
			c = comment.find_element_by_tag_name('a')			#find element by tag name "a"(anchor tag) in "txt16gry" in "rht_content"
			comments.append(c.text)								# append text from c(anchor tag) in text format
			dates.append(date.text)								# append date from date in text format
		except:
			print ("No Recommendation.")
			continue

	print(comments)
	print(dates)

	#################
'''	df1 = []
	df1 = pd.DataFrame(df)
	df1.insert(loc=0, column='Company', value=df.loc[j, "Symbol"])
	df1.append(loc=1, column='Dates', value=dates)
	df1.append(loc=2, column='Comments', value=comments)
	#print (Result)
	#outfile = "Semi_structured.csv"
	opdf = pd.read_csv("Semi_structured.csv")
	opdf = 
	Result = pd.DataFrame(Result)
	Result.to_csv(outfile, index=None)
	print (Result)
'''
