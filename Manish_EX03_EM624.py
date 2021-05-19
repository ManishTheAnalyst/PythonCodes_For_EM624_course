# AUTHOR: Manish Narwal
# PROFESSOR: Dr.Carlo Lipizzi
#COURSE: EM-624
#ASSIGNMENT: EX-03


# PART 1
# Open file from same directory
file = open('marketingdata.txt')
# Initialize counter to count NA values
counter_NA = 0
# Initialize counter to count number of lines in text file
counter = 0
# Initialize counter to count lines with no NA values
counter_print = 0

print("These are the first twenty lines in the file with no NA in it:")
for line in file:
    # Start counting total number of lines
    counter = counter + 1
    # If NA is detected in line then increment counter by 1
    if 'NA' in line:
        counter_NA = counter_NA + 1
    else:
        # If counter get first 20 lines with no NA values then it will stop printing
        if counter_print != 20:
            counter_print = counter_print + 1
            print(line)

print('\n')
# To calculate number of lines which are not NA
counter_notNA = counter - counter_NA
# To calculate percentage of lines which has no NA in it
answer = counter_notNA / counter * 100
print("PART 1: Marketing Data (text file):")
print("The file has",counter_notNA,"lines with no NA in it,that are",str(round(answer, 2)) + '%',"of the total")

# Close text file
file.close()


# PART 2

# Open the CSV file from same directory
df=open("NYC-CitiBike-2016.csv")

# Initialize counter to count total number of lines
countlines= 0
# Initialize counter to count lines with date 9/29/16
countgivendate = 0
for lines in df:
    # Start counting total lines
    countlines = countlines + 1
    # If date 9/29/16 is detected then increment counter countgivendate
    if "9/29/16"in lines:
        countgivendate = countgivendate + 1
# Percentage calculation
answer_part2 = countgivendate / countlines * 100

print('\n')
print("PART 2: NYC CitiBike (CSV file):")
print("The file has",countlines,"lines,of which",countgivendate,"are from 9/29/16. The lines from 9/29/16 are",str(round(answer_part2,2))+'%',"of the total lines")

# Close CSV file
df.close()

print('\n')
# To check whether which file is larger first file(text file) or second file(CSV file)
if counter>countlines:
    print("The first file is larger than the second one")
else:
    print("The first file is smaller than the second one")