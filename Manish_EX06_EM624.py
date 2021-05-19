#AUTHOR: Manish Narwal
#PROFESSOR: Dr. Carlo Lipizzi
#ASSIGNMENT: Exercise 06
#DATE: 11/3/2020

import pandas as pd
#To display maximum columns in output at a stretch
pd.set_option('display.max_columns', None)

#LOADING THE THREE DATASETS INTO PANDAS DATAFRAME AND PRINTING FIRST 3 ROWS OF EACH DATAFRAMES

#Load movies.dat file and set parser engine to python since c engine doesn't support these separators
movies_file=pd.read_csv("movies.dat",sep="::",names=['MovieID','Title','Genres'],engine='python')
print("The Movies data is:\n")
#Printing the first 3 rows of the dataframe
print(movies_file.head(3))
print("\n")

#Load users.dat file and set parser engine to python since c engine doesn't support these separators
users_file=pd.read_csv("users.dat",sep="::",names=['UserID','Gender','Age','Occupation','Zip-code'],engine='python')
print("The Users data is:\n")
#Printing the first 3 rows of the dataframe
print(users_file.head(3))
print("\n")

#Load ratings.dat file and set parser engine to python since c engine doesn't support these separators
ratings_file=pd.read_csv("ratings.dat",sep="::",names=['UserID','MovieID','Rating','Timestamp'],engine='python')
print("The ratings data is:\n")
#Printing the first 3 rows of the dataframe
print(ratings_file.head(3))
print("\n")


#MERGING THE THREE DATAFRAMES INTO ONE SINGLE DATAFRAME CALLED 'data'

#First merging users and ratings on column UserID to join on
data0=pd.merge(users_file,ratings_file,on='UserID')

#Final merging to get dataframe 'data' 
data=pd.merge(data0,movies_file,on="MovieID")


#PRINTING THE NUMBER OF RECORDS IN EACH OF THE FOUR DATAFRAME AND GIVING APPROPRIATE HEADINGS

#Number of records of movies.dat file
print("The number of records of movies_file is: ", len(movies_file))
print("\n")
#Number of records of users.dat file
print("The number of records of users_file is: ", len(users_file))
print("\n")
#Number of records of ratings.dat file
print("The number of records of ratings_file is: ", len(ratings_file))
print("\n")
#Number of records of newly merged dataframe 'data'
print("The number of records of data is: ", len(data))
print("\n")


#REPLACING INTEGERS IN THE 'Occupation' COLUMN AS STRINGS AND PRINTING THE LAST 3 ROWS OF THE UPDATED DATAFRAME 'data'


#Replacing the integers in the Occupation column with strings
data['Occupation'].replace({0:'Other/not specified',1:'academic/educator',2:'artist',3:'clerical/admin',4:'college/grad student',5:'customer service',6:'doctor/health care',7:'executive/managerial',8:'farmer',9:'homemaker',10:'K-12 Student',11:'lawyer',12:'programmer',13:'retired',14:'sales/marketing',15:'scientist',16:'self-employed',17:'technical/engineer',18:'tradesman/craftsman',19:'unemployed',20:'writer'},inplace=True)
print("The Last 3 rows of updated dataframe 'data' is:\n")
#Printing the Last 3 rows of the updated dataframe 'data'
print(data.tail(3))
print("\n")


#FINDING THE 5 OCCUPATIONS WHICH GIVES OUT HIGHEST RATINGS FOR MOVIES

print("The 5 occupation which gives highest ratings for movies are:\n")
#Grouping by Occupation and sorting by Ratings and then adding ratings of each occupation 
print(data[['Occupation', 'Rating']].groupby('Occupation').sum().sort_values(by='Rating', ascending=False).head())
