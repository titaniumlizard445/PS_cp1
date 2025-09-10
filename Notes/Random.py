#PS 1st Random Numbers
import random
import time

name = input("What is your character name?\n").strip().title()

# Generate Stat Options
stat1 = random.randint(1,6) + random.randint(1,6)
stat2 = random.randint(1,6) + random.randint(1,6)
stat3 = random.randint(1,6) + random.randint(1,6)
stat4 = random.randint(1,6) + random.randint(1,6)
stat5 = random.randint(1,6) + random.randint(1,6)
stat6 = random.randint(1,6) + random.randint(1,6)
stat7 = random.randint(1,6) + random.randint(1,6)

#Telling user the stat choices
print(f"Your stat options are: {stat1}, {stat2}, {stat3}, {stat4}, {stat5}, {stat6}, {stat7}")


# Set Stats
strength = int(input(f"Which stat do you want as your strength: \n")) +2



print(f"This is a random number from 0-1 {random.random()}")
print(random.randint(0,20))

print(time.time())