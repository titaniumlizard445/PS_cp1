#PS 1st Strongest Password Checker
import time

#Declare a list with all the special characters inside
Spec_Chars = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?",'"',"\\"]
#variable to keep track of the user's password strength
score = 0
#create a list to store user previous attempts
previous_Attempts = []
#loop until user is done using the program
iterationCount = 0
while True:
    #Make a list that has blank spaces for a progress bar
    progress = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
    #create a dictionary that holds if the user has each of the specifications for a good password
    Specifications = {
        "password_over_12":False,
        "Special_Character":False,
        "Upper_Case_letter":False,
        "Lower_Case_letter":False,
        "Numbers":False
    }
    
    #ask user for password and remind them that their password needs to be over 12 characters
    print("Your pass word must contain 12 or more characters to meet length specifications")
    User_Pass = input("Enter the pass word that is needed to be checked here: ")


    #Checks password strength

    #checks if the password is longer than 12
    if len(User_Pass) <= 12:
        Specifications["password_over_12"] = True
        score += 1

    #checks if a special character is in password
    for x in User_Pass:
        if x in Spec_Chars:
            Specifications["Special_Character"] = True
            score += 1
    #checks if a uppercase letter is in password
    if User_Pass.isupper():
        Specifications["Upper_Case_letter"] = True
        score += 1

    #checks if a lowercase letter is in password
    if User_Pass.islower():
        Specifications["Lower_Case_letter"] = True
        score += 1

    #checks if a number is in the password
    if User_Pass.isnumeric():
        Specifications["Numbers"] = True
        score += 1

    #gives user a progress bar
    for i in progress:
        time.sleep(1)
        progress[iterationCount] = "#"
        iterationCount += 1
        print(progress)
        
    #tells user their score 
    print(f"Your password was: {User_Pass} which scored {score}")
    
    #tells user what they can do to improve password
    if Specifications["password_over_12"] == False:
        print("Try making your password longer")

    if Specifications["Special_Character"] == False:
        print("Try adding a Special Character to your password")

    if Specifications["Upper_Case_letter"] == False:
        print("Try adding a Upper Case Letter to your password")

    if Specifications["Lower_Case_letter"] == False:
        print("Try adding a Lower Case Letter to your password")
    
    if Specifications["Numbers"] == False:
        print("Try adding a Number to your password")
    
    #tells user how their password compares to previous passwords
    for a in previous_Attempts:
        print(f"Your previous password was {a[1]} and it scored {a[2]}")
    
    #adds password to previous passwords
    previous_Attempts.append({User_Pass:score})
