#PS 1st User Sign In

import time as Clock
import random as Random

UserUnlock = False

Users = ["ParkerSwenson" , "Dirk" , "Bracken" , "Elijah" , "Liam", "PaxtonHall", "Watch", "ElementsOfTechnology", "Veritasium", "Water"]

UserPasswords = {
    "ParkerSwenson" : "Uc@s1$TP3ri0d",
    "Dirk" : "676767",
    "Bracken" : "Fred",
    "Elijah" : "G@rry",
    "Liam" : "I_L1k3_C0d3",
    "PaxtonHall" : "P@k1$tan-rUlZ",
    "Watch":"H3@dPh0n35",
    "ElementsOfTechnology":"Tf2IzB3$t",
    "Veritasium" : "@n3leM3Nt0FTruth",
    "Water" : "H2O"
}

Timeout = Random.randint(1,4)



while True:
    NameInput = input("Input Username Here:  ").strip()

    if NameInput in Users:
        UserUnlock = True
        PasswordInput = input("Input Password Here: ").strip()

        if PasswordInput == UserPasswords[NameInput]:
            print("Log in Success")
            print(f"Welcome, {NameInput}")
            break
        else:
            print("Invalid Password")
            if Timeout == 1:
                print("Please wait 10 seconds before trying again")
                Clock.sleep(10)
            elif Timeout == 2:
                print("Please wait 20 seconds before trying again")
                Clock.sleep(20)
            elif Timeout == 3:
                print("Please wait 30 seconds before trying again")
                Clock.sleep(30)
            elif Timeout == 4:
                print("Please wait 60 seconds before trying again")
                Clock.sleep(60)
    else:
        print("invalid Username")
        if Timeout == 1:
            print("Please wait 10 seconds before trying again")
            Clock.sleep(10)
        elif Timeout == 2:
            print("Please wait 20 seconds before trying again")
            Clock.sleep(20)
        elif Timeout == 3:
            print("Please wait 30 seconds before trying again")
            Clock.sleep(30)
        elif Timeout == 4:
            print("Please wait 60 seconds before trying again")
            Clock.sleep(60)