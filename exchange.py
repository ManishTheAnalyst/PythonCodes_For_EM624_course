# AUTHOR: Manish Narwal
# COURSE: EM-624
# PROFESSOR: Dr. Carlo Lipizzi
# ASSIGNMENT: EXERCISE 01

while True:
    # Prompt user to enter how many US Dollars does he/she want to exchange
    usd_val = input("How many US Dollars do you want to exchange: ")
    # Check if user has entered appropriate entry (only 'int')
    if usd_val.isdigit() == False:
        # If 'float' or 'str' tell the user it's wrong entry and continue the loop again
        print("\nSorry! Wrong Input. Please Try Again")
        continue
    else:
        # Prompt user to enter the name of currency they wish to convert into
        inr_val = input("\n Enter the name of currency you are converting dollars to: ")
        # Prompt the user to enter exchange rate (For e.g: 1 USD = 74 INR, so just enter 74)
        exchange_val = input("\n What is the exchange rate:")
        # Check if user has entered appropriate entry (only 'int')
        if exchange_val.isdigit() == False:
            # If 'float' or 'str' tell the user it's wrong entry and continue the loop again
            print("\nSorry! Wrong Input. Please Try Again")
            continue

        else:
            # Calculate and display the result
            print("\n You can exchange ", usd_val, "US dollars for", int(usd_val) * int(exchange_val), inr_val)
            break