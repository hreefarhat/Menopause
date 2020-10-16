# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:43:19 2020

@author: hreef
"""

import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
df = pd.read_csv("../data/menopause.csv")


pd.set_option('display.max_rows',230)
pd.set_option('display.max_columns',29)
pd.set_option('display.max_colwidth',1000)
df['What are the symptoms?'].unique

df.loc[df['Are you in any of these life stages?'] == 'Irregular']
##################################################
#   ALL LIFE STAGES SYMPTOMS WORD FREQUENCY  
###################################################
symptoms = str(df['What are the symptoms?'])



for char in ",.'\n?":
    symptoms=symptoms.replace(char,' ') 
symptoms= symptoms.lower()
symptoms = symptoms.replace('nan','')
print(symptoms)
word_list= symptoms.split()
print(word_list)

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


stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 100, stopwords = stopwords)
wc.generate(symptoms)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()


##################################################
#IRREGULAR MENOPAUSE LIFESTAGE- SYMPTOMS FREQUENCY     
###################################################



df[['Are you in any of these life stages?','What are the symptoms?']]

df2 = pd.read_csv("symptoms.csv")

df2.columns
df2['Lifestages-Symptoms'].unique()

file = open('irregular.txt')
irregular=file.read()
print(irregular)   
irregular=irregular.replace('Irregularly menstruating','')
irregular=irregular.replace('issues','')
irregular=irregular.replace('heavy','')
print(irregular)

for char in ",.'\n?":
    irregular=irregular.replace(char,' ') 
irregular= irregular.lower()
word_list= irregular.split()
print(word_list)

d={}
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


stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 100, stopwords = stopwords)
wc.generate(irregular)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()


##################################################
#REGULAR MENOPAUSE LIFESTAGE- SYMPTOMS FREQUENCY     
###################################################


file = open('regular.txt')
regular=file.read()
print(regular)

for char in ",.'\n?":
    regular=regular.replace(char,' ') 
regular= regular.lower()
regular=regular.replace('regularly menstruating','')
word_list= regular.split()
print(word_list)

d={}
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


stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 100, stopwords = stopwords)
wc.generate(regular)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()

df2['Lifestages-Symptoms'].unique()


##################################################
#PERI MENOPAUSE LIFESTAGE- SYMPTOMS FREQUENCY     
###################################################


file = open('peri.txt')
peri=file.read()
print(peri) 
peri=peri.replace('Peri-menopause','')        
print(peri)

for char in ",.'\n?":
    peri=peri.replace(char,' ') 
peri= peri.lower()
word_list= peri.split()
print(word_list)

d={}
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


stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 100, stopwords = stopwords)
wc.generate(peri)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()


##################################################
#POST MENOPAUSE LIFESTAGE- SYMPTOMS FREQUENCY     
###################################################


file = open('post.txt')
post=file.read()
print(post) 
post=post.replace('Post-menopause','')
print(post)


for char in ",.'\n?":
    post=post.replace(char,' ') 
post= post.lower()
word_list= post.split()
print(word_list)

d={}
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


stopwords=set(STOPWORDS)
#Appearance related
wc = WordCloud(background_color="white", max_words = 100, stopwords = stopwords)
wc.generate(post)
plt.axis('off')
plt.imshow(wc, interpolation="bilinear")
plt.show()