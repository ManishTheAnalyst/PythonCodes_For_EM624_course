# AUTHOR: Manish Narwal
# PROFESSOR: Dr.Carlo Lipizzi
#COURSE: EM-624
#ASSIGNMENT: EX-02


while True:
    # Prompt the user to enter price or done to exit program
    prompt_1=input("Enter price in cents or Done to exit: ")
    # uppercase('Done') or lowercase('done') if any one of them is true proceed
    if prompt_1=='done' or prompt_1=='Done':
        #Say goodbye when user exits program and break
        print("Good-bye!")
        break
    #'Strip' to accept negative numbers as 'isdigit' only accepts positive numbers
    elif prompt_1.strip('-').isdigit()== False:
        print(prompt_1,"is not an integer!")
    # If entered number is less than zero then it's a negative number
    elif int(prompt_1) < 0:
        print(prompt_1,"is not a positive number!")
    # To check whether the entered number is a multiple of 5
    elif int(prompt_1) % 5 != 0:
        print(prompt_1,"is not a multiple of 5 cents!")
    else:
        # Show the user their correct entry
        print("You entered",prompt_1,"cents")
        continue
