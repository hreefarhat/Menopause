# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:22:37 2020

@author: hreef
"""



import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#structuring the data
df = pd.read_csv("../data/menopause.csv")
pd.set_option('display.max_rows',230)
pd.set_option('display.max_columns',29)
pd.set_option('display.max_colwidth',1000)

#Extracting the questions and manipulating it
df['Do you have any questions?']
text = str(df['Do you have any questions?'].unique())
print(text)
text= text.replace('NaN','no')
print(text)

#Conducting word frequency analysis


text=text.replace('training','train')
text=text.replace('will','')
text=text.replace('really','')
text=text.replace('know','')
text=text.replace('make','')
text=text.replace('want','')
text=text.replace('still','')
text=text.replace('going','')
text=text.replace('cycling','')
text=text.replace('way','')
text=text.replace('don','')
print(text)


for char in "-,.'\n?":
    text=text.replace(char,' ') 
text= text.lower()
print(text)
word_list= text.split()
print(word_list) #total 3532


#Initializing dictionary for word count
d={}

#counting number of words each time comes up in list 
for word in word_list:
    d[word]= d.get(word,0)+1    
d
#get highest to lowest sorted
word_freq = []
for key, value in d.items():
    word_freq.append((value,key))
word_freq

word_freq.sort(reverse=True)
print(word_freq)

########### WORD FREQUENCY IMAGE #########################

stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 50, stopwords = stopwords)
wc.generate(text)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()
