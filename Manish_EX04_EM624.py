#AUTHOR: Manish Narwal
#PROFESSOR: Dr.Carlo Lipizzi
#ASSIGNMENT: EX 04

#Importing pandas(for concatenating)  and statistics(for mean and sum calculations)
import pandas as pd
import statistics

#Open Text file
file = open("citi_bike.txt","r")
#Create empty list
data = []
#Read each line
for line in file:
    parts = line.strip().split()
    data.append(parts)

#Open CSV file
file1 = open("citi_bike.csv","r")
data1 = []
for line in file1:
    parts1 = line.strip().split(',')
    data1.append(parts1)

#Function taking list generated above as input
def print_details(data1):
    # Creating a list to store daily miles travelled, pass purchases, top trips and date
    daily_miles = []
    two_four_pass = []
    max_trips = []
    dates = []
    #Accessing lines in lists of lists
    for item in data1:
        #To pick up the month of june(6th month)
        if item[0][0] == '6':
            #To add to the empty list with values from month of june of daily miles travelled
            daily_miles.append(float(item[3]))
            #To add to the empty list with values from month of june of pass purchases
            two_four_pass.append(int(item[7]))
            #To perform statistics(mean and sum) to get average daily miles travelled and pass purchases for the month
            average_daily_miles = statistics.mean(daily_miles)
            total_two_four_pass = sum(two_four_pass)
            dates.append(item[0])
            #To add to empty list of max_trips to calculate top 5 trips later
            max_trips.append(int(item[1]))
        #To pick up month from CSV file (month of January)
        elif item[0][0] == '1':
            daily_miles.append(float(item[3]))
            two_four_pass.append(int(item[7]))
            average_daily_miles = statistics.mean(daily_miles)
            total_two_four_pass = sum(two_four_pass)
            dates.append(item[0])
            max_trips.append(int(item[1]))
    
    
    print('\n')
    #Print first and last day using list indexes
    print("The following data is from {} to {}".format(dates[0],dates[-1]))
    print('\n')
    #Print average daily miles
    print("Average daily miles travelled: {0:.2f}".format(average_daily_miles))
    print('\n')
    #Print total number of pass purchased
    print("Total 24-Hour purchases for the month: {}".format(total_two_four_pass))
    print('\n')
    #Print top 5 trips of the month
    print("The top 5 trips are:")
    #Sort values in descending order so as to get top 5 values with highest number of trips
    max_trips.sort(reverse = True)
    for item in range(5):
        print(max_trips[item])
        
print_details(data)
print_details(data1)
#Merging text and CSV file

# Argument delim_whitespace to take into account any number of white space characters and header none because we don't have column names
file01=pd.read_csv("citi_bike.txt", delim_whitespace=True,header=None)
file02=pd.read_csv("citi_bike.csv",header=None)

#Concatenating two datasets, ignore index to True for axis to be labeled from 0
raw_file=pd.concat([file01,file02],ignore_index=True)

print(raw_file)
print("\n")

#Close files
file.close()
file1.close()

print("This is the end of the file processing")      