#AUTHOR: Manish Narwal
#PROFESSOR: Dr.Carlo Lipizzi
#ASSIGNMENT: Exercise 08
#DATE: 11/18/2020

#Importing all the necessary libraries
import requests 
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize 
import re
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA
import pandas as pd
from collections import Counter
from nltk.tokenize.treebank import TreebankWordDetokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Get the content from BBC news
body = requests.get('https://www.bbc.com/news')
soup = BeautifulSoup(body.content,'html.parser')

#Create empty list to store headlines
empty=[]

#Extracting headlines of the web page with the help of the source code of the website
for headlines in soup.find_all("h3"):
    #Each word should be lower case
    words=headlines.string.lower()
    #Append to empty list
    empty.append(words)

#Open stopwords text file and convert it to list    
with open("stopwords_en.txt","r") as file:
    stopwords_list=[word for line in file for word in line.split()]  
    
#Tokenize each string of the list
tokenized_list = [word_tokenize(i) for i in empty]     

#Removing Punctuations
regex=re.compile('[%s]'%re.escape(string.punctuation))

#Creating two new lists and performing operations so that our end product remains lists of lists
new_list=[]
#SOURCE:https://stackoverflow.com/questions/45764050/use-re-sub-to-replace-replace-variable-that-is-regex-with-a-string
for i in tokenized_list:
    b_list=[]
    for token in i:
        #Replacing unicode strings
        new_token=regex.sub(u'',token)
        if not new_token==u'':
            b_list.append(new_token)
    
    new_list.append(b_list)

#Removing Stopwords    
cleaned_list=[]

for key in new_list:
    top_list=[]
    for word in key:
        #Remove stopwords and length of words should be greater than 3
        if word not in stopwords_list and len(word)>3:
            top_list.append(word)
            
    cleaned_list.append(top_list)      

#Removing Numerics using isdigit
good_list=[]

for key in cleaned_list:
    bad_list=[]
    for things in key:
        if things.isdigit()== False:
            bad_list.append(things)
    good_list.append(bad_list)      

#List of Irrelevant words which can create anomaly in analysis    
useless_words=['doing','87yearold','gets','news','keeping','kept','touch','buying','world','remaining','actually']

#Removing Irrelevant words
tk_list=[]

for item in good_list:
    grd_list=[]
    for ele in item:
        if ele not in useless_words:
            grd_list.append(ele)
    tk_list.append(grd_list) 

#Raw headlines to enter into our dataframe and perform sentiment analysis    
res = [' '.join(ele) for ele in new_list]    

#Sentiment Intensity Analyzer
sia=SIA()
data=[]
for f in res:
    #Get polarity score
    result=sia.polarity_scores(f)
    #Create a new column headline
    result['headline']=f
    data.append(result)
#Make it into pandas dataframe    
df=pd.DataFrame.from_records(data)
#Order the column
df=df[['headline','pos','neu','neg','compound']]
#Keep one similar headline and drop others
df.drop_duplicates(subset = "headline", keep = 'first', inplace = True)
#Sorting in Ascending Order to Get Top 3 Lowest Sentiment
digi_dat=df.sort_values(by=['compound'])
print("\n")
print("\nThe following are the 3 headlines with the Lowest sentiment:\n")
print(digi_dat.head(3))

#Sorting in Descending Order to Get Top 3 Highest Sentiment
digi_dat2=df.sort_values(by=['compound'],ascending=False)
print("\n")
print("\nThe following are the 3 headlines with the Highest sentiment:\n")
print(digi_dat2.head(3))

#Cleaned Strings of headines in a list
listB=[]
for word in tk_list:
    listA=TreebankWordDetokenizer().detokenize(word)
    listB.append(listA)

#Create Bigrams
res1 = [i for j in listB for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]

#Empty list to keep Bigrams occuring more than 2 times
bigram_words=[]
#Empty list to keep rest of the single words
single_words=[]
#Count the bigrams
counts = Counter(res1)
#Addresing the key and count of bigram
for bg, count in counts.most_common():
    #If bigram occurs more than 2 times then put underscore and append to list
    if count > 2:
        bigram_words.append('_'.join(bg))
    else:
        #Get rest bigrams in single words
        for word in bg:
            single_words.append(word)

#Merge both the list
final_list=bigram_words+single_words

#Converting list to string for wordcloud
all_words_string = ' '.join(final_list)    
#Generate Wordcloud
wc = WordCloud(width=1000,height=700,background_color='white',max_words=100).generate(all_words_string)
wc.to_file('Pro_cloud.png')
plt.figure(figsize = (8, 8))
plt.imshow(wc)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#Sentiment Analysis
#Sum of Positive Column
Positive=df['pos'].sum()


Negative=df['neg'].sum()


Neutral=df['neu'].sum()

#values and labels in the list
x = ['Positive','Negative','Neutral']

y = [Positive, Negative,Neutral]

list_x = [i for i, _ in enumerate(x)]

plt.figure(figsize = (8, 8))
plt.bar(list_x, y, color='red')
plt.xlabel("TYPE OF EMOTIONS")
plt.ylabel("COUNT")
plt.title("Sentiment Analysis of the URL")
plt.xticks(list_x, x)
plt.show()
