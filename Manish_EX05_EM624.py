#AUTHOR: Manish Narwal
#PROFESSOR: Dr.Carlo Lipizzi
#ASSIGNMENT: EXERCISE 05
#DATE: 10/20/2020

import matplotlib.pyplot as plt
import numpy as np

#Creating a list with six elements initialized at zero
counts = [0, 0, 0, 0, 0, 0]

#Defining function
def get_index(parts):
    #Male and Lower class and increment it in counts[0]
    if parts[1] == '1' and (parts[0] == '1' or parts[0] == '2' or parts[0] == '3'):
        counts[0] = counts[0] + 1
    #Male and Middle class and increment it in counts[1]    
    elif parts[1] == '1' and (parts[0] == '4' or parts[0] == '5' or parts[0] == '6'):
        counts[1] = counts[1] + 1
    #Male and Upper class and increment it in counts[2]      
    elif parts[1] == '1' and (parts[0] == '7' or parts[0] == '8' or parts[0] == '9'):
        counts[2] = counts[2] + 1
    #Female and Lower class and increment it in counts[3]      
    elif parts[1] == '2' and (parts[0] == '1' or parts[0] == '2' or parts[0] == '3'):
        counts[3] = counts[3] + 1
    #Female and Middle class and increment it in counts[4]      
    elif parts[1] == '2' and (parts[0] == '4' or parts[0] == '5' or parts[0] == '6'):
        counts[4] = counts[4] + 1
    #Female and Upper class and increment it in counts[5]      
    else:
        counts[5] = counts[5] + 1

#Open text file
with open("marketingdata.txt", 'r') as file:
    #Read each line of a file
    for line in file:
        #Focus on lines with no NA
        if "NA" not in line:
            #Strip white space and create list
            parts = line.strip().split()
            #Call function
            index = get_index(parts)

#Printing the results of gender and social group
print("Who is at the mall?")
print("\n")
print("Lower Income Males:", counts[0], "    Lower Income Females:", counts[3], "    Total Lower Income:",
      counts[0] + counts[3])
print("\n")
print("Middle Income Males:", counts[1], "   Middle Income Females:", counts[4], "   Total Middle Income:",
      counts[1] + counts[4])
print("\n")
print("Upper Income Males:", counts[2], "   Upper Income Females:", counts[5], "    Total Upper Income:",
      counts[2] + counts[5])

#Preparation for pie chart because we need to combine male and female from each social group
Lower_Income=counts[0]+counts[3]
Middle_Income=counts[1]+counts[4]
Upper_Income=counts[2]+counts[5]
#Labels for both charts as list
bar_names=['Lower Class Men','Lower Class Women','Middle Class Men','Middle Class Women','Upper Class Men','Upper Class Women']
pie_names=['Lower Income','Middle Income','Upper Income']
#Values to be filled in pie chart
pie_values=[Lower_Income,Middle_Income,Upper_Income]
#To adjust graph size
plt.figure(figsize=(15,10))
#On left
plt.subplot(221)
#X and Y axis of bar plot
plt.bar([0,1,2,3,4,5],counts)
#Label Y axis
plt.ylabel('Count')
#Set tick locations and labels on Y-axis and labels to be kept at 90 to avoid overlapping
plt.xticks([0,1,2,3,4,5],bar_names,rotation='vertical')
#range of values to be shown on Y-axis
y_ticks=np.arange(0,1500,200)
plt.yticks(y_ticks)
#Title to bar graph
plt.title("Bar chart of men and women at mall according to their social class")
#On Right
plt.subplot(222)
#Plotting and labelling pie chart and calculating percentages of each social class
plt.pie(pie_values,labels=pie_names,autopct='%1.1f%%')
#Keeping Aspect Ratio intact
plt.axis('equal')
#Title to pie chart
plt.title("Pie chart of people according to thier social class")
#Display
plt.show()
#Close the file
file.close()