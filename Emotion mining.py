# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:45:25 2021

@author: DELL
"""

#Emotion mining
#Importing the libraries
import matplotlib.pyplot as plt
import requests
import re
from bs4 import BeautifulSoup as bs
import nltk
import os


#Extracting the review
shoes_reviews = []
for i in range(1,30):
    shoes = []
    url = 'https://www.amazon.in/Puma-36970604-Mens-Running-Shoe/product-reviews/B08KJX1WZW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'+str(i)
response = requests.get(url)
soup=bs(response.content, 'html.parser')
reviews=soup.find_all("span", {"data-hook":"review-body"})
for i in range(len(reviews)):
    shoes.append(reviews[i].text)
    shoes_reviews = shoes_reviews+shoes

#Saving the extracted data
with open ('shoes.txt', "w", encoding='utf8') as output:
    output.write(str(shoes_reviews))

#Joining all the reviews into a single paragraph
shoes_rev_str = ' '.join(shoes_reviews)
shoes_rev_str

#Removing unwanted symbols
shoes_rev_str = re.sub("[^A-Za-z" "]+"," ",shoes_rev_str).lower()
shoes_rev_str = re.sub("[0-9" "]+"," ", shoes_rev_str)

#Splitting the words into individual strings
shoes_reviews_words = shoes_rev_str.split(" ")

#Removing the stopwords
from nltk.corpus import stopwords
stop_words=stopwords.words('english')

with open("C:\\Users\\DELL\\Desktop\\Seema Data Science\\Python codes\\Text Mining\\Assignment files\\stop.txt", "r") as sw:
    stopwords = sw.read()
    
shoes_reviews_words = [w for w in shoes_reviews_words if not w in stopwords]
shoes_rev_str = ' '.join(shoes_reviews_words)  
  
#Creating the wordcloud
from wordcloud import WordCloud
wordcloud_shoes=WordCloud(background_color="black", width=2000, height=1500).generate(shoes_rev_str)
plt.imshow(wordcloud_shoes)

#Extracting the positive words from wordcloud
with open("C:\\Users\\DELL\\Desktop\\Seema Data Science\\Python codes\\Text Mining\\Assignment files\\positive-words.txt",encoding='utf-8-sig') as pos:
    positive_words=pos.read().split('\n')
    positive_words=positive_words[36:]

shoes_positive = " ".join([w for w in shoes_reviews_words if w in positive_words])

#Positive wordcloud
wordcloud_positive=WordCloud(background_color="black", width=2000, height=1500).generate(shoes_positive)
plt.imshow(wordcloud_positive)

#Extracting the negative words from wordcloud
with open("C:\\Users\\DELL\\Desktop\\Seema Data Science\\Python codes\\Text Mining\\Assignment files\\negative-words.txt","r") as neg:
    negative_words=neg.read().split("\n")
    negative_words=negative_words[37:]
shoes_negative = " ".join([w for w in shoes_reviews_words if w in negative_words])

#Negative wordcloud
wordcloud_negative=WordCloud(background_color="black",width=2000,height=1500).generate(shoes_negative)
plt.imshow(wordcloud_negative)



















