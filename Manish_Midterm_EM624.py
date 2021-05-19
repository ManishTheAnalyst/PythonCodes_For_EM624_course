#AUTHOR: Manish NArwal
#PROFESSOR: Dr.Carlo Lipizzi
#ASSIGNMENT: Mid-term


#SECTION 2: CODE CHECKING

#PROBLEM #6

#Issues with Code:
#1)If you run it straight away then it is printing output as list
#2)And even output is not proper because L is multiplied by 3 at end of program

#Reason: 
#1)Mutliplied by 3 at end of code
#2)The code does not convert list into string

#Changes made by me:
#1)Multiply letters by 3 within loop so that each letter is printed thrice (eg: If you enter 'Of' it will be printed 'OOOfff' and not 'OfOfOf')
#2)Convert list into string by using map method


N = input("Enter your characters: ")
L = []
for letters in N:
    letters.split()
    L.append(letters*3)
    #Convert list to string
    b="".join(map(str,L))
print (b)


#PROBLEM #7

#Issue with the code:
#1) The list was not sorted and hence out of top 3 the largest word appeared in the last
#2) The words were repeated hence not unique
#3)Minor error at last line of code where top3 was printed outside print parentheses

#Reason
#1) Reverse argument of sort was not set to True
#2) There was no condition to take only unique values in the top3

#Changes made by me:
#1)Reverse argument set to True so now the largest word will come first followed by 2nd and 3rd largest word
#2) I put a condition that if the word is not in top3 then only put word in top3 list. In this way only unique words will come
#3) Took top3 inside print parentheses

handle =open('word_list.csv','r')

top3 = ["","",""]

for line in handle:
    #For each line in the file, strip the input and put it into the word variable
    word = line.strip()
    
    #Compare the length of each incoming word to the length of each word in each position
    for i in range(0,3):
        #Sorts list in descending order
        top3.sort(key = len,reverse=True)
        if (len(word) > len(top3[i])):
            #To get only unique values
            if word not in top3:
                 top3[i] = word
                        
#Print the words
print ("\nThe 3 longest words are:",top3)


#PROBLEM #8



#What was wrong with the original code:
#1)When you enter any string of length 1 even just a space then it prints out 'True'
#2)'Y' is not a vowel
#3)Even for single special character it prints 'True'

#Reason: I think maybe its because of incorrect use of boolean operator 'OR' 

#Correction made by me:
#1) Made sure it catches special characters as Invalid input.
#2) Made proper use of boolean operator "OR"
#3) Made sure that irrespective of user entering vowels in upper or lower case the code prints 'True'
#4) I put a break at end to stop the loop


#Put all special characters as string
special_characters = "!@#$%^&*()-+~`_={}\|[]:;''<>,.?/"
#Upper and Lower case vowels
vow="aeiouAEIOU"


while True:
    #prompts and receives user input
    char = input('Please enter an alphabetical character:')
    if char.isdigit(): #checks if input is numerical
        print ('Invalid input.')
    else:
        #checks if input is more than one character
        if len(char) > 1:
            print ('Invalid input.')
        else:
            #Check for special character
            if char in special_characters:
                print('Invalid input.')
            else:
                #Accept vowel whether its lower case or upper case
                if char in vow:
                     print ('True')
                else:
                    print ('False')
    break               

#SECTION 3: Writing a Code

#PROBLEM #9


import operator
import itertools
import matplotlib.pyplot as plt
#Opening the stopwords file and converting it into flat list 
#Because every single word in stopwords_en became separate list
#So I made list of list into one single list so that problem becomes less complicated
with open("stopwords_en.txt","r") as file1:
    stopwords_list=[word for line in file1 for word in line.split()]

#Opening the ai_trends file and converting it into flat list as well
#Because every paragraph in ai_trends became separate list
#So I made list of list into one single list so that problem becomes less complicated    
with open("ai_trends.txt","r") as file2:
    #words in ai_trends needed to be converted to lower case because stopwords to be removed are lower case
    ai_list=[word.lower() for line in file2 for word in line.split()]

#If contents of ai_list is not found in stopwords_list then add it to final_list    
final_list = [i for i in ai_list if i not in stopwords_list]

#Create empty dictionary to put words as keys and number of occurrences as values
d=dict()

#Go through each word from final_list if the same word occurs again then increment else count of it will remain 1
for word in final_list:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
#Key is word and d[key] is value which is number of times that word has occured in final_list
for key in list(d.keys()):
    key,":",d[key]

#Initialize counter to count number of occurrences of words
count=0
#Loop through each values in dictionary 'd'
for val in d.values():
    count = count + val
#Average=count of words/total length of dictionary    
count=count/len(d)
print("The average occurrences of the words is:",count)
print("\n")    

#Empty list to get words
longest_word = []
#Sort dictionary in descending order and add to list
longest_word =sorted(d, key=len, reverse=True) 

#Print top 2 longest words
print("The longest 2 words are:",longest_word[0:2])
print("\n")  


#Empty list 'lister' to word length of each distinct word
lister = []
#Length of each distinct word is appended to "lister"
for words in d.keys():
    lister.append(len(words))

#Sum of word count in 'lister'
sum_words = sum(lister) 
#Average word length = sum of word lengths/length of list
avg_word_length = sum_words/len(lister)
print("The average word length is:",avg_word_length)
print("\n")


#Sorting dictionary in descending order
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))

#We are using itertools.islice to slice piece of iterable which is top 10 occurring word which we want to plot
graph_val = dict(itertools.islice(sorted_d.items(), 10)) 

#Adjust graph size
plt.figure(figsize = (10,6))
#title of bar plot
plt.title("Top 10 most frequent words",fontsize=25)
#Extracting keys for X-axis
keys = graph_val.keys()
#X-axis label
plt.xlabel("WORDS",fontsize=13)
#Extracting values for Y-axis
values = graph_val.values()
#Y-axis label
plt.ylabel("COUNT",fontsize=13)
#Plotting bar graph
plt.bar(keys, values)
#Keeping text of X-axis vertical
plt.xticks(rotation=90)


#PROBLEM #10


import pandas as pd

#Open CSV file in pandas structure
file=pd.read_csv("cars.csv")
file

#Printing first 3 rows of the dataset
print(file.head(3))
#Printing last 3 rows of the dataset
print(file.tail(3))

#Sorting average mileage in ascending order to get lowest 3 values
a=file.sort_values('average-mileage',ascending=True)

#Print top 3 values which are the lowest average mileage
print("The 3 cars with the lowest average-mileage are:")
print(a[['company','body-style','average-mileage']][0:3])
print("\n")

#Sorting average mileage in descending order to get highest 3 values
a=file.sort_values('average-mileage',ascending=False)
#Print top 3 values which are the highest average mileage
print("The 3 cars with the highest average-mileage are:")
print(a[['company','body-style','average-mileage']][0:3])                    