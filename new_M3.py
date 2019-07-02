from nltk.corpus import wordnet as wnet
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import pandas as pd
import ast
import os

df = pd.read_csv("UrlList.csv")
raw_semi = pd.read_csv("Semi_structured.csv")


lists = ['hold', 'Assets', 'At the money', 'Bear Market', 'Beta', 'Bid', 'Blue Chip Stock', 'Board Lot', 'Bonds:','Book', 'Broker/Brokerage Firm', 'Bull Market', 'Business Day', 'Call Option', 'Close Price', 'Commodities','Convertible Securities', 'Debentures', 'Defensive Stock', 'Delta', 'Derivatives', 'Diversification', 'Dividend', 'Equity', 'Face value', 'Hedge', 'Income Stock', 'Index', 'Initial Public Offering', 'Internet Trading', 'Limit Order', 'Limit Order', 'Limit Order', 'Mutual Fund', 'Odd Lot', 'One-sided Market', 'Out-of-The-Money', 'Portfolio', 'Positions Limit', 'Pre-opening Session', 'Price Earnings Ratio','Put Option', 'Risk', 'Securities', 'Strike Price', 'Stock Split', 'Thin Market', 'Trading session', 'Yield','Buy', 'Sell', 'Short sell', 'Buy to cover', 'Revenues', 'Profits/Losses', 'Earnings per Share or EPS','Moving averages', 'Resistance', 'Support', 'Breakouts/Breakdowns', 'Market valuation', 'Shares outstanding', 'Float', 'Restricted shares', 'Unrestricted shares', 'Annual Report', 'Arbitrage', 'Averaging Down','Bear Market', 'Beta', 'Blue Chip Stocks', 'Bourse', 'Bull Market', 'Broker', 'Bid', 'Close', 'Day Trading','Dividend', 'Exchange', 'Execution', 'Haircut', 'High', 'Index', 'Leverage', 'Low', 'Margin', 'Moving Average','Open', 'Order', 'Pink Sheet Stocks', 'Portfolio', 'Quote', 'Rally', 'Sector', 'Share Market', 'Short Selling','Spread', 'Stock Symbol', 'Volatility', 'Volume', 'Yield']

keyword = set() # Set dont accepts duplicates values
RatingList = []						#creating a list called RatingList

'''
k = raw_semi.loc[0, "Comments"]
print(k)
print(type(k),"\n")


s = []
s = ast.literal_eval(k)
print(s, "\n", type(s))
'''

for l in lists:
	keyword.add(l)

forms =set()

#print("lists",lists,"\n\nkeyword",keyword,"\n\nforms",forms)

#print(len(df))

for j in range(len(raw_semi)):				# Only select 1st url from urlList 
#for j in range(0,1):				# Only select 1st url from urlList 
	for k in keyword:
		#print(k)
		for lemma in wnet.lemmas(k):
			#print(lemma," ",lemma.name())
			forms.add(lemma.name())
			for related_lemma in lemma.derivationally_related_forms():
				#print(related_lemma, related_lemma.name())
				forms.add(related_lemma.name())
			#print("\n")
		#print("\n")

	#print(forms)
	#Comments = ['27-MAY-19 to 31-MAY-19 // ACC is looking weak on charts as a weekly positional sell only if it starts to trade below 1631 !!', '27-MAY-19 to 31-MAY-19 -- ACC If it moves below 1631 then we can go short for a T 5 delivery based selling purpose ...', 'Great knowledge and experience. See our description for a great risk reward ratio.and earn everyday @ whzap 844 five four 92O five 6', '27-MAY-19 to 31-MAY-19 // ACC is looking strong on charts as a weekly positional buy only if it starts to trade above 1744 !!', 'Expert advice in all segment trading with proper safety and reall time followups in market @wzzupp 844 five four 92O five 6', '27-MAY-19 to 31-MAY-19 -- ACC If it moves above 1744 then we can go long for a T 5 delivery based buying purpose ...', 'right time to trade with us ..... we make multiple profit ride with KD advisory .... if you want to be in profit ..... don`t miss his daily level .... for more ... nine five six 89140 three nine']
	
	#Comments = ['🔼🔼 - BUMPER NEWS !! Intraday,Options, Commodity and Future calls For Free 👉👉 cutt.us/4qF8w 👈👈', '03-JUNE-19 to 07-JUNE-19 // ACC is looking strong on charts as a weekly positional buy only if it starts to trade above 1747 !!', '03-JUNE-19 to 07-JUNE-19 -- ACC If it moves above 1747 then we can go long for a T 5 delivery based buying purpose ...', '1780 .when it will come. we have 2 lots 1740CE. can I hold or do average.', 'we have sold ACC at 1626 in the morning in our free teelle graamm channeell - ASKINVESTMENTACADEMY....booked full profit at 1600 and got a profit of 7k', 'again pair trading: buy ACC around 1597 and sell UltraTech cem around 4580. for 20000 profit per lot', 'Acc stock will rise above 1780 and therefore will be a good stock to invest.', 'market recovering i strongly believe it will close 1625... buy and buy', 'any chance of buying now.. .still gng down... what is happening', '03-JUNE-19 to 07-JUNE-19 -- ACC If it moves below 1648 then we can go short for a T 5 delivery based selling purpose ...']
	#Dates = ['about 2 hrs 26 mins ago', 'about 5 hrs 30 mins ago', 'about 19 hrs 48 mins ago', 'about 7 hrs 8 mins ago', 'about 7 hrs 37 mins ago', 'about 10 hrs 25 mins ago', 'about 23 hrs 48 mins ago']

	Comments = []
	Dates = []
	Comments_str = raw_semi.loc[j, "Comments"]
	print(Comments_str)
	print(type(Comments_str))
	Comments = []
	Comments = ast.literal_eval(Comments_str)
	Dates = raw_semi.loc[j,"Dates"]

	
	rating = dict()										# creating a dictonary called "rating"
	SingleRating = []									# creating a list called SingleRating
	#Format for SingleRating List ['Company_name',dictionary of keyword found in comments and their corresponding scores/ratings]

#	j=0

	for comment in Comments:											
		sentences = (sent_tokenize(comment))			#tokenize(1 token = sentence) Comment
		#print("two")
		for sentence in sentences:
			for keyword in forms:
				#print("three")
				if sentence.lower().find(keyword.lower()) != -1:
					sid = SentimentIntensityAnalyzer()
					ss = sid.polarity_scores(sentence)
					if ss['pos'] > ss['neg']:
						rating[keyword] = rating.get(keyword, 0) + 1
					elif ss['neg'] > ss['pos']:
						rating[keyword] = rating.get(keyword, 0) - 1
			#print("four")
#	print("rating ",rating,"\n")
#	print("\n",j,raw_semi.loc[j, "Company"],"\n")
	SingleRating.append(raw_semi.loc[j, "Company"])
	SingleRating.append(rating)					#dictionary of ratings of fetured keyword(already defind) for single Company
	RatingList.append(SingleRating)				#dictionary of ratings of all companies
	print ("Single Rating ",SingleRating)
	print("RatingList ",RatingList)
	
	# RatingList
	# 
###################

BuyList = []
SellList = []
HoldList = []
NewRatingList = RatingList

for i in NewRatingList:	#Select one company from List and predict by checking 'buy','sell','hold' present in list if those keyword present increse pos/neg/hold values
    Prediction = i[-1]	#['comapny_name',{keyword,values}] 	select only dictionary
    #print(i[-1])
    #print(i)
    #print(" \nPrediction Items\n\t ",Prediction.items())
    pos = 0
    neg = 0
    hold = 0
    for key, value in Prediction.items():
        if key.lower() == 'buy' or key.lower() == 'buying':
            pos+=value
        if key.lower() == 'sell' or key.lower() == 'risk':
            neg+=value
        if key.lower() == 'hold':
            hold+=value
    if pos > neg and pos > hold:
        BuyList.append(i[-2])
    elif neg > pos and neg > hold:
        SellList.append(i[-2])
    elif hold > pos and hold > neg:
        HoldList.append(i[-2])
    #print(pos)
    #print(neg)
    #print(hold)
	

Lar = [len(HoldList), len(BuyList), len(SellList)]
print(Lar)
maxlen = max(Lar)
print(Lar,"\n",maxlen)
for i in range(maxlen - len(BuyList)):
    BuyList.append("")
for i in range(maxlen - len(SellList)):
    SellList.append("")
for i in range(maxlen - len(HoldList)):
    HoldList.append("")

print("\n BuyList ",BuyList)
print("\n HoldList ",HoldList)
print("\n SellList ",SellList)
Result = []
Result = pd.DataFrame(Result)
Result.insert(loc=0, column='Buy', value=BuyList)
Result.insert(loc=1, column='Sell', value=SellList)
Result.insert(loc=2, column='Hold', value=HoldList)
#print (Result)
outfile = "Result_final.csv"
Result = pd.DataFrame(Result)
Result.to_csv(outfile, index=None)
print (Result)


os.system('python UI2.py')
