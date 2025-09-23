#PS 1st Logical Operators

score = 100

if score > 100:
    print(f"You did extrat credit... you did {score -100}% extra credit!")
elif score == 100:
    print("Your grade is perfect!")
else:
    print(f"Try harder you only have {score}.")
    
username = "not_hi"
password = "hi"

user = input("Enter your username: ")
pword = input("Enter your password:")

if not user or not pword:
    print("Please enter a valid input")
elif user == "Somebody" and pword == "BadPassword":
    pass
elif user == username and pword == password:
    print("Welcome Not_Hi")
elif user == username:
    print("Password incorrect")
else:
    print("Incorrect credentials")