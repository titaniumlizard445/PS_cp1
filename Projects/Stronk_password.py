#PS 1st Strongest Password Checker
import time

#Declare a list with all the special characters inside
Spec_Chars = ["!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}","|",";",":",",",".","<",">","?",'"',"\\"," "]

#loop until user is done using the program
while True:
    Number = False
    Length = False
    Upper = False
    Lower = False
    Special = False
    iterationCount = 0
    #Make a list that has blank spaces for a progress bar
    Progress_Bar = ["0","1","2","3","4","5"]
    #loading screen bar
    Loading_Screen = ["_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_"]
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
    
    score = 0
    
    #checks if the password is longer than 12
    if len(User_Pass) >= 12:
        Specifications["password_over_12"] = True
        Length = True

    #checks if a special character is in password on every character in the password
    for x in User_Pass:
        if x in Spec_Chars:
            Specifications["Special_Character"] = True
            Special = True
        #checks if a uppercase letter is in password

        if x.isupper():
            Specifications["Upper_Case_letter"] = True
            Upper = True
      #checks if a lowercase letter is in password
        if x.islower():
            Specifications["Lower_Case_letter"] = True
            Lower = True
        #checks if a number is in the password
        if x.isnumeric():
            Specifications["Numbers"] = True
            Number = True
    #counts up score
    if Number == True:
      score += 1
    if Lower == True:
      score += 1
    if Upper == True:
      score += 1
    if Special == True:
      score += 1
    if Length == True:
      score += 1
    #Gives the progress bar a score
    num = 0
    for b in Progress_Bar:
        if score == num:
            Progress_Bar[num] = "#"
        num += 1

    #gives user a Loading Screen
    for i in Loading_Screen:
        time.sleep(0.25)
        Loading_Screen[iterationCount] = "#"
        iterationCount += 1
        print(Loading_Screen)
        
    #tells user their score 
    print(f"Your password was: {User_Pass} which scored {score}")
    print(Progress_Bar)

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
    
    #Ask user if they are done with the program
    done = input("Are you done using this program? ")
    if done == "yes":
        break
