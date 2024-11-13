# Password Authentication Program
# Alpha Version 1.0
# Coder: Emma Patneau
# Date: 2024-11-13
# Purpose: Ask user for password and loop until correct and then let 
# them into a college application portal to view their acceptance status'

# Set correct password and store to variable
set_password = "W1ldW0lv3$"

# Use while loop to ask for multiple inputs until correct
# Ask user for password and store to local variable
while True:
    for i in range(5):
        user_name = input("Enter username: ")
        user_pass = input("Enter password: ")

# Compare user password with set password
# if correct break from loop
# else keep asking
# output correct or incorrect before restarting loop
        if user_pass == set_password:
            break
        else:
            print("Incorrect Password or Username")
    print("You have entered the wrong password too many times please wait 5 minutes to try again")
    break

# When correct password input print statement welcoming user to university 
# application portal and let them view their application/acceptance status
if user_pass == set_password:
    print("-----------------------")
    print("")
    print("Welcome to Common App!")
    print("")
    print("-----------------------")
    print("Purdue University")
    print("Application Status: Accepted")
    print("")
    print("University of Illinois")
    print("Application Status: Submitted")
    print("")
    print("Georgia Tech")
    print("Application Status: Submitted")
    print("")
    print("The Ohio State University")
    print("Application Status: Deferred")
    print("")
    print("Stanford University")
    print("Application Status: Accepted")
    print("")