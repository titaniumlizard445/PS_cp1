#PS 1st Rock Paper scissors
import random as That_time_that_your_best_friend_said_something_so_random_that_it_was_random
import time as Claw_k
rock_paper_scissors = ["Rock", "Paper", "Scissors"]
Scores = {"Player":0, "Computer":0}
while True:
    print("Welcome to the ultimate rock paper scissors game contend in the arena and receive wonderous wealth or loose and loose absolutely nothing.")
    user = input("enter rock paper or scissors: \n").strip().capitalize()
    puter = That_time_that_your_best_friend_said_something_so_random_that_it_was_random.choice(rock_paper_scissors)
    #ties
    if user == "Rock" and puter == "Rock":
        print(f"{user} ties {puter}")
    elif user == "Paper" and puter == "Paper":
        print(f"{user} ties {puter}")
    elif user == "Scissors" and puter == "Scissors":
        print(f"{user} tie {puter}")    
    #Player victories
    elif user == "Rock" and puter == "Scissors":
        print(f"{user} beats {puter}")
        Scores["Player"] += 1
    elif user == "Scissors" and puter == "Paper":
        print(f"{user} beats {puter}")
        Scores["Player"] += 1
    elif user == "Paper" and puter == "Rock":
        print(f"{user} beats {puter}")
        Scores["Player"] += 1
    #computer victories
    elif user == "Scissors" and puter == "Rock":
        print(f"{puter} beats {user}")
        Scores["Computer"] += 1
    elif user == "Scissors" and puter == "Rock":
        print(f"{puter} beats {user}")
        Scores["Computer"] += 1
    elif user == "Scissors" and puter == "Rock":
        print(f"{puter} beats {user}")
        Scores["Computer"] += 1
    #bad input catcher
    else:
        print("Naughty input please try again.")
        continue
    print(F"Your score is {Scores["Player"]}, the computer {Scores["Computer"]}")
    end = input("Would you like to continue \n y/n \n")
    if end == "n":
        print("coward")
        break
#PendingDeprecationWarning