from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import os
import glob


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random
from nltk.corpus import wordnet
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import os
import glob

browser = webdriver.Chrome('/home/raghu/Pictures/chromedriver')
keyword = set()
lists = ['hold', 'Assets', 'At the money', 'Bear Market', 'Beta', 'Bid', 'Blue Chip Stock', 'Board Lot', 'Bonds:',
         'Book', 'Broker/Brokerage Firm', 'Bull Market', 'Business Day', 'Call Option', 'Close Price', 'Commodities',
         'Convertible Securities', 'Debentures', 'Defensive Stock', 'Delta', 'Derivatives', 'Diversification',
         'Dividend', 'Equity', 'Face value', 'Hedge', 'Income Stock', 'Index', 'Initial Public Offering',
         'Internet Trading', 'Limit Order', 'Limit Order', 'Limit Order', 'Mutual Fund', 'Odd Lot', 'One-sided Market',
         'Out-of-The-Money', 'Portfolio', 'Positions Limit', 'Pre-opening Session', 'Price Earnings Ratio',
         'Put Option', 'Risk', 'Securities', 'Strike Price', 'Stock Split', 'Thin Market', 'Trading session', 'Yield',
         'Buy', 'Sell', 'Short sell', 'Buy to cover', 'Revenues', 'Profits/Losses', 'Earnings per Share or EPS',
         'Moving averages', 'Resistance', 'Support', 'Breakouts/Breakdowns', 'Market valuation', 'Shares outstanding',
         'Float', 'Restricted shares', 'Unrestricted shares', 'Annual Report', 'Arbitrage', 'Averaging Down',
         'Bear Market', 'Beta', 'Blue Chip Stocks', 'Bourse', 'Bull Market', 'Broker', 'Bid', 'Close', 'Day Trading',
         'Dividend', 'Exchange', 'Execution', 'Haircut', 'High', 'Index', 'Leverage', 'Low', 'Margin', 'Moving Average',
         'Open', 'Order', 'Pink Sheet Stocks', 'Portfolio', 'Quote', 'Rally', 'Sector', 'Share Market', 'Short Selling',
         'Spread', 'Stock Symbol', 'Volatility', 'Volume', 'Yield']
for i in lists:
    keyword.add(i)

df = pd.read_csv("UrlList.csv")

RatingList = []

#for j in range(len(df)):
for j in range(1,2):
    try:
        browser.get(df.loc[j, "Url"])
        time.sleep(random.randint(5, 10))
        browser.execute_script("window.scrollTo(0, 2000)")
        time.sleep(random.randint(5, 10))
        alldata = []
        allData = browser.find_elements_by_class_name("rht_content")

        comments = []
        dates = []
        for i in allData:
            comment = i.find_element_by_class_name("txt16gry")
            date = i.find_element_by_class_name("link13gry")
            try:
                c = comment.find_element_by_tag_name('a')
                comments.append(c.text)
                dates.append(date.text)
            except:
                print ("No Recommendation.")
                continue

        Comments = []
        Dates = []
        for i in dates:
            if i.find("about") != -1 or i.find("Mar 8th") != -1:
                Dates.append(i)
        for i in range(len(Dates)):
            Comments.append(comments[i])
        print (df.loc[j, "Symbol"])
        print (len(Comments))

        keyword = set()
        print("oneone")
        lists = ['Agent', 'Ask/Offer', 'Assets', 'At the money', 'Bear Marke', 'Beta', 'Bid', 'Blue Chip Stock',
                 'Board Lot', 'Bonds:', 'Book', 'Broker/Brokerage Firm', 'Bull Market', 'Business Day', 'Call Option',
                 'Close Price', 'Commodities', 'Convertible Securities', 'Debentures', 'Defensive Stock', 'Delta',
                 'Derivatives', 'Diversification', 'Dividend', 'Equity', 'Face value', 'Hedge', 'Income Stock', 'Index',
                 'Initial Public Offering', 'Internet Trading', 'Limit Order', 'Limit Order', 'Limit Order',
                 'Mutual Fund', 'Odd Lot', 'One-sided Market', 'Out-of-The-Money', 'Portfolio', 'Positions Limit',
                 'Pre-opening Session', 'Price Earnings Ratio', 'Put Option', 'Risk', 'Securities', 'Strike Price',
                 'Stock Split', 'Thin Market', 'Trading session', 'Yield', 'Buy', 'Sell', 'Short sell', 'Buy to cover',
                 'Revenues', 'Profits/Losses', 'Earnings per Share or EPS', 'Moving averages', 'Resistance', 'Support',
                 'Breakouts/Breakdowns', 'Market valuation', 'Shares outstanding', 'Float', 'Restricted shares',
                 'Unrestricted shares', 'Annual Report', 'Arbitrage', 'Averaging Down', 'Bear Market', 'Beta',
                 'Blue Chip Stocks', 'Bourse', 'Bull Market', 'Broker', 'Bid', 'Close', 'Day Trading', 'Dividend',
                 'Exchange', 'Execution', 'Haircut', 'High', 'Index', 'Leverage', 'Low', 'Margin', 'Moving Average',
                 'Open', 'Order', 'Pink Sheet Stocks', 'Portfolio', 'Quote', 'Rally', 'Sector', 'Share Market',
                 'Short Selling', 'Spread', 'Stock Symbol', 'Volatility', 'Volume', 'Yield']
        print("onetwo")
        for i in lists:
            keyword.add(i)
        # keywords={'buy','sell','stock','price','share'}
        # comments=['It is good to buy','It is not good to buy',"Regretted buying this",'Good to sell']
        forms = set()
        print("onethree")

        for k in keyword:
            print("onefive1")
            for lemma in wnet.lemmas(k):
                print("onefive2")
                forms.add(lemma.name())

                for related_lemma in lemma.derivationally_related_forms():
                    forms.add(related_lemma.name())
                    print("onesix")
        print("onefour")
        rating = dict()
        SingleRating = []
        print("one")
        for comment in Comments:
            sentences = (sent_tokenize(comment))
            print("two")
            for sentence in sentences:
                for keyword in forms:
                    print("three")
                    if sentence.lower().find(keyword.lower()) != -1:
                        sid = SentimentIntensityAnalyzer()
                        ss = sid.polarity_scores(sentence)
                        if ss['pos'] > ss['neg']:
                            rating[keyword] = rating.get(keyword, 0) + 1
                        elif ss['neg'] > ss['pos']:
                            rating[keyword] = rating.get(keyword, 0) - 1
                print("four")
        SingleRating.append(df.loc[j, "Symbol"])
        SingleRating.append(rating)
        RatingList.append(SingleRating)
        print ("Single Rating"+SingleRating)

    except:
        print ("No Recommendation..")

BuyList = []
SellList = []
HoldList = []
NewRatingList = RatingList
for i in NewRatingList:
    Prediction = i[-1]
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

Lar = [len(HoldList), len(BuyList), len(SellList)]
maxlen = max(Lar)

for i in range(maxlen - len(BuyList)):
    BuyList.append("")
for i in range(maxlen - len(SellList)):
    SellList.append("")
for i in range(maxlen - len(HoldList)):
    HoldList.append("")

Result = []
Result = pd.DataFrame(Result)
Result.insert(loc=0, column='Buy', value=BuyList)
Result.insert(loc=1, column='Sell', value=SellList)
Result.insert(loc=2, column='Hold', value=HoldList)
print (Result)
outfile = "Result_final.csv"
Result = pd.DataFrame(Result)
Result.to_csv(outfile, index=None)
print (Result)
