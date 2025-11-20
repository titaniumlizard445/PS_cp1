#PS space invaders thing
import time as Clock
import random as Random
string = ""
choices = (" ","*"," "," "," "," "," "," ","."," "," "," "," "," ","|"," "," "," "," ")
while True:
    for x in range(0,100):
        randomnum = Random.choice(choices)
        string+=randomnum
    print(string)
    Clock.sleep(0.01)
    string=""
    