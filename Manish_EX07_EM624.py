#AUTHOR: Manish Narwal
#PROFESSOR: Dr. Carlo Lipizzi
#ASSIGNMENT: EX-07
#DATE: 11/10/2020

#Import all the necessary libraries
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Opening the pro file,con file and stopword file and put it in a list
with open("pro_ marijuana_raw.txt","r") as file1:
    pro_list=[word.lower() for line in file1 for word in line.split()]
    
with open("con_ marijuana_raw.txt","r") as file2:
    con_list=[word.lower() for line in file2 for word in line.split()]
    
with open("stopwords_en.txt","r") as file3:
    stopwords_list=[word for line in file3 for word in line.split()]

#Removing contents of stopwords file from pro file
pro_final_list = [i for i in pro_list if i not in stopwords_list]
#Removing contents of stopwords file from con file
con_final_list = [i for i in con_list if i not in stopwords_list]


#Preparing the list of elements which are not needed or can tamper with analysis
char_list=['€','!','%','"',':',';','?','@','#','$','(',')','[',']','<','>','{','}','&','1','2','3','4','5','6','7','8','9','0',',','.','-',"'re","'ve","'s","'t","'ll","'d"]
#If these elements are present in the characters of the pro and con file then do not include those characters and make sure the length of characters is above 3
pro = [i for i in pro_final_list if all(ch not in i for ch in char_list) and len(i)>3]
con = [i for i in con_final_list if all(ch not in i for ch in char_list) and len(i)>3]

#Repitative irrelevant words to be removed
rep_words=['marijuana','seven','year','years','just','according','able','knowing','told','likely','billion','said','need','went','following','using','include','legal','legalizing','going','drew','users','used','says','people','states','united','washington']
pro1=[i for i in pro if i not in rep_words]
con1=[i for i in con if i not in rep_words]


#Sentiment analysis using vader library for PRO
analyzer = SentimentIntensityAnalyzer()
#Convert list to string as vader needs string as input(SOURCE: Classwork Module:sentiment.py)
clean_text_str = ' '.join(pro1)
#Polarity scores to get sentiment metrics from text
vad_sentiment = analyzer.polarity_scores(clean_text_str)

#Sentiment analyzer setup
pos = vad_sentiment ['pos']
neg = vad_sentiment ['neg']
neu = vad_sentiment ['neu']

print("\n")
print ('\nThe following is the distribution of the sentiment for the cleaned PRO text file :\n')
print ('\nThe pro text file was rated', '{:.1%}'.format(pos),"Positive")
print ('\nThe pro text file was rated', '{:.1%}'.format(neg),"Negative")
print ('\nThe pro text file was rated', '{:.1%}'.format(neu), "Neutral")


#Sentiment analysis using vader library for CON

clean_text_str1 = ' '.join(con1)
vad_sentiment1 = analyzer.polarity_scores(clean_text_str1)

pos1 = vad_sentiment1 ['pos']
neg1 = vad_sentiment1 ['neg']
neu1 = vad_sentiment1 ['neu']

print("\n")
print ('\nThe following is the distribution of the sentiment for the cleaned CON text file :\n')
print ('\nThe con text was rated', '{:.1%}'.format(pos1),"Positive")
print ('\nThe con text was rated', '{:.1%}'.format(neg1),"Negative")
print ('\nThe con text was rated', '{:.1%}'.format(neu1), "Neutral")


#EXTRACTING BIGRAMS (SOURCE: Classwork modules: text_processing_samples.py)
#Taking the string PRO file
text_pro=clean_text_str
#Extracting tokens from the string text
tokens = nltk.word_tokenize(text_pro)

#Calculation of the 5 most frequent words
freqdist = nltk.FreqDist(tokens).most_common(5)
print("\n")
print ('\nThe 5 most frequent words in the PRO text file are:',freqdist)
#Extracting and printing bigrams
bigram_pro = list(nltk.bigrams(tokens))
print("\n")
print ('\nThe following are the bigrams extracted from the cleaned PRO text:\n')
print (bigram_pro)


#EXTRACTING BIGRAMS FOR CON FILE
text_con=clean_text_str1
tokens1 = nltk.word_tokenize(text_con)

freqdist1 = nltk.FreqDist(tokens1).most_common(5)
print("\n")
print ('\nThe 5 most frequent words in the CON text file are:',freqdist1)
bigram_con = list(nltk.bigrams(tokens1))
print("\n")
print ('\nThe following are the bigrams extracted from the cleaned PRO text:\n')
print (bigram_con)


#WORDCLOUD FOR PRO FILE

#Activating figure
plt.figure(figsize = (8, 8))
print("\nThe following is the Wordcloud for PRO file(1st) and CON file(2nd):",)
#Setting parameters for wordcloud
wc_pro=WordCloud(width=1000,height=700,background_color='white',max_words=100).generate(clean_text_str)
#Display
plt.imshow(wc_pro)
#Should not show x and y axis
plt.axis("off") 
#Plot title
plt.title("The PRO file word cloud",fontsize=20)
#Adjusting figure area
plt.tight_layout(pad = 0)


#WORDCLOUD FOR CON FILE
plt.figure(figsize = (8, 8))
wc_con=WordCloud(width=1000,height=700,background_color='white',max_words=100).generate(clean_text_str1)
plt.imshow(wc_con)
plt.axis("off") 
plt.title("The CON file word cloud",fontsize=20)
plt.tight_layout(pad = 0)

