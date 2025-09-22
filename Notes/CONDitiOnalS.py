#PS 1st Conditionals notes

import random

Guy = {
    "Guy hp" : 20,
    "player attack" : 2,
    "player damage" : 5,
    "player defense": 5,
}

Bad_guy = {
    "Bad guy hp" : 15,
    "Bad guy attack" : 3,
    "Bad guy damage" : 10,
    "Bad guy defense" : 2
}

chance_damage = random.randint(1,20)

if chance_damage == 20:
    print("You Got A CRIT! That means you roll for damage twice")
    damage_number = random.randint(1,8) + random.randint(1,8) + + Guy["player damage"]
    Bad_guy["Bad guy hp"] -= damage_number

elif chance_damage == 1:
    print("You got the CRITical failure! Now the Bad guy gets to attack you")
    damage_number = random.randint(1,12) + Bad_guy["Bad guy damage"]
    Guy["Guy hp"] -= (damage_number - Guy["player defense"])

elif chance_damage + Guy["player damage"] >= 12:
    print("You hit Roll for damage!")
    damage_number = random.randint(1,8) + Guy["player damage"]

    if damage_number > Bad_guy["Bad guy defense"]:
        print(f"You did {damage_number-Bad_guy['Bad guy defense']} damage")
        Bad_guy["Bad guy hp"] -= (damage_number-Bad_guy["Bad guy defense"])

    else:
        print("You did not get the bad guy")
    
else:
    print("You missed you are a failure")

print(Guy)
print(Bad_guy)

print("Your turn is over")

if True:
    chance_damage = random.randint(1,20) + Bad_guy["Bad guy attack"]
    