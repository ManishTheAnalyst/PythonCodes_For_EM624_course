#AUTHOR: Manish Narwal
#PROFESSOR: Dr. Carlo Lipizzi
#ASSIGNMENT: EX-09
#DATE: 12/04/2020

#Importing all the necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Range of pages to iterate
pages = list(range(50))
#Empty list 
reviews_list=[]

#Going through each page of reviews and scrapping reviews and ratings
for page in pages:
    #URL of my favorite movie '12 Angry Men'
    URL='https://www.rottentomatoes.com/m/1000013_12_angry_men/reviews?type=&sort=&page={}'.format(page)
    body = requests.get(URL)
    soup = BeautifulSoup(body.text, 'html.parser')
    reviews=soup.find_all('div',{'class':'row review_table_row'})
    for item in reviews:
        rev={
        'review':item.find('div',{'class':'the_review'}).text.strip(),
         #Removing unnecessary texts before the ratings and extracting only the numerics or pure ratings    
        'rating':''.join(item.find('div',{'class':'small subtle review-link'}).text.split()).replace('FullReview|OriginalScore:','').replace('FullReview','').replace('OriginalScore:','')
            }
        #Creating list of lists
        reviews_list.append(rev)
        
#List to store review text
reviews=[]
#List to store ratings
ratings=[]
#Iterating through initial list of list and appending review and rating to respective lists
for item in reviews_list:
    reviews.append(item['review'])
    ratings.append(item['rating'])

#Converting in pandas dataframe so that it will make standardization easy
df=pd.DataFrame()
#Reviews column
df['Reviews'] = reviews
#Ratings column
df['Ratings']=ratings

#Filling missing values with NaN
df=df.replace('', np.NaN)
#Removing rows with NaN
df.dropna(inplace=True)

#Normalizing the ratings on scale of 1 to 5 with 1 being minimum and 5 maximum
df['Ratings']=df['Ratings'].replace('A','4.8')
df['Ratings']=df['Ratings'].replace('A+','5.0')
df['Ratings']=df['Ratings'].replace('B','4.3')
df['Ratings']=df['Ratings'].replace('B-','4.1')
df['Ratings']=df['Ratings'].replace('A-','4.6')
df['Ratings']=df['Ratings'].replace('4.5/5','4.5')
df['Ratings']=df['Ratings'].replace('5/5','5.0')
df['Ratings']=df['Ratings'].replace('4/5','4.0')
df['Ratings']=df['Ratings'].replace('10/10','5.0')
df['Ratings']=df['Ratings'].replace('4.0/4.0','5.0')
df['Ratings']=df['Ratings'].replace('82/100','4.1')
df['Ratings']=df['Ratings'].replace('84/100','4.2')
df['Ratings']=df['Ratings'].replace('4/4','5.0')
df['Ratings']=df['Ratings'].replace('9/10','4.5')
df['Ratings']=df['Ratings'].replace('92/100','4.6')
df['Ratings']=df['Ratings'].replace('3/4','3.75')
df['Ratings']=df['Ratings'].replace('3.5/4','4.37')

#Sorting dataframe from highest to lowest
df_final=df.sort_values(by='Ratings',ascending=False)

#Empty list to create list of lists of sorted and cleaned reviews and ratings
Final_list =[] 
for index, rows in df_final.iterrows(): 
    #Create list for the row 
    my_list =[rows.Reviews, rows.Ratings] 
      
    #Append the list to the final list 
    Final_list.append(my_list) 

#Top 5 Reviews in list
Top_5=Final_list[:5]
print("\n")
print("The Top 5 reviews of the list are:\n")
print(Top_5)

#Bottom 5 Reviews in list
Bot_5=Final_list[-5:]
print("\n")
print("The Bottom 5 reviews of the list are:\n")
print(Bot_5)
        
#Extracting top 5 reviews text for WordCloud
Top5_list =[] 
for index,rows in df_final.iterrows(): 
    #Create list for the current row 
    my_tp =[rows.Reviews] 
      
    #Append the list to the Top5 list 
    Top5_list.append(my_tp) 

Top5_list=Top5_list[:5]

#Extracting Bottom 5 reviews text for WordCloud
Bot5_list =[] 
for index, rows in df_final.iterrows(): 
    #Create list for the current row 
    my_tj =[rows.Reviews] 
      
    #Append the list to the Bot5 list 
    Bot5_list.append(my_tj) 

Bot5_list=Bot5_list[-5:]

#Stopwords file and converting it into list
with open("stopwords_en.txt","r") as file:
    stopwords_list=[f for l in file for f in l.split()]

#Empty list for getting cleaned texts of Top 5 Reviews
cleaned_Top5_list=[]


#Data Cleaning: Removing the Stopwords and Punctuations and eliminating small words
for word in Top5_list:
    for key in word:
        k1=key.strip()
        text1=''.join(k1)
        text_tokens1 = word_tokenize(text1)
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for t in text1:
            if t in punc:
                text1 = text1.replace(t, " ")
                word_T5=word_tokenize(text1.lower())
    for q in word_T5:
        T5_list=[]
        if q not in stopwords_list and len(q)>3:
            T5_list.append(q)
            cleaned_Top5_list.append(T5_list)

#Converting list of lists to list of strings            
res1 = [''.join(ele) for ele in cleaned_Top5_list]

#WordCloud of Top 5 Reviews

#Converting list to text
top5_string = ' '.join(res1)  

#Generating WordCloud of Top 5 Reviews
wc1 = WordCloud(width=1000,height=700,background_color='white',max_words=200).generate(top5_string)
wc1.to_file('top5_cloud.png')
plt.figure(figsize = (8, 8))
plt.imshow(wc1)
plt.axis('off')
plt.title("Top 5 Review of 12 Angry Men",fontsize=20)
plt.tight_layout(pad = 0)
plt.show()

#Empty list for getting cleaned text of Bottom 5 Reviews
cleaned_Bot5_list=[]

#Data Cleaning: Removing the Stopwords and Punctuations and eliminating small words
for word in Bot5_list:
    for key in word:
        k2=key.strip()
        text2=''.join(k2)
        text_tokens2 = word_tokenize(text2)
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for t in text2:
            if t in punc:
                text2 = text2.replace(t, " ")
                word_B5=word_tokenize(text2.lower())
    for q in word_B5:
        B5_list=[]
        if q not in stopwords_list and len(q)>3:
            B5_list.append(q)
            cleaned_Bot5_list.append(B5_list)

#Converting list of lists to list of strings 
res2 = [''.join(ele) for ele in cleaned_Bot5_list]

#WordCloud of Bottom 5 Reviews of 12 Angry Men

#Converting list to text
bot5_string = ' '.join(res2)

#Generating WordCloud of Bottom 5 Reviews
wc2 = WordCloud(width=1000,height=700,background_color='white',max_words=200).generate(bot5_string)
wc2.to_file('bot5_cloud.png')
plt.figure(figsize = (8, 8))
plt.imshow(wc2)
plt.axis('off')
plt.title("Bottom 5 Review of 12 Angry Men",fontsize=20)
plt.tight_layout(pad = 0)
plt.show()


