#PS space invaders thing
import time as Clock
import random as Random
string = ""
choices = (" ","O"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ")
while True:
    randomnum = Random.choice(choices)
    string+=randomnum
    print(string)
    Clock.sleep(0.1)
    