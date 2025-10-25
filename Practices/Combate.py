#PS 1st Combat program

import random

player_types = {
    "Melee":{
        "hp":175,
        "Defense":20,
        #use D20 + hit chance
        "hit chance":3,
        "actions":{
            "dagger":55,
            "sword":45,
            #add defense
            "shield":15,
            "drink health potion":35,
            "Give up":0
            }
    },
    "Mage":{
        "hp":75,
        "Defense":10,
        "hit chance":35,
        "actions":{
            #chance use coin
            "freeze":0,
            #damage
            "attack":65,
            "dagger":65,
            "Give up":0,
            #add health
            "drink health potion":20
        }
    },
    "Rogue":{
        "hp":125,
        "defense":30,
        #use D20
        "hit chance": 7,
        "actions":{
            "bow":20,
            "dagger":75,
            "Give up":0,
            "drink health potion":45
        }
    }
}

Monster_Boys = {
    "Blob":{
        "hp":30,
        #use D40 and add hit chance to it
        "hit chance":2,
        "Defense":0,
        "attack":15
        },
    "Strong Lizard":{
        "hp":85,
        "Defense":10,
        "hit chance":6,
        "attack":35
        },
    "Goblin":{
        "hp":50,
        "Defense":4,
        "hit chance":4,
        "attack":20
    },
    "Dragon":{
        "hp":300,
        "Defense":15,
        "hit chance":8,
        "attack":65
    }
}
Backup_Monster_Boys = {
    "Blob":{
        "hp":30,
        #use D40 and add hit chance to it
        "hit chance":2,
        "Defense":0,
        "attack":15
        },
    "Strong Lizard":{
        "hp":85,
        "Defense":10,
        "hit chance":6,
        "attack":35
        },
    "Goblin":{
        "hp":50,
        "Defense":4,
        "hit chance":4,
        "attack":20
    },
    "Dragon":{
        "hp":300,
        "Defense":15,
        "hit chance":8,
        "attack":65
    }
}
action = ""
Frozen_enemy = 0
Monsters = ["Blob", "Strong Lizard" , "Goblin" , "Dragon"]
Monster = random.choice(Monsters)

def Monster_turn(Monster_Choice , Player_Defense , Player_health):
    
    print(f" It is now {Monster_Choice}'s turn to go")
    hit_number = random.randint(1,41) + Monster_Boys[Monster]["hit chance"]
    
    if hit_number > Player_Defense:
        print(f"{Monster_Choice} hit you! chance: {hit_number}")
        Damage_given = random.randint(1,21) + Monster_Boys[Monster]["attack"]
        Player_health -= Damage_given
        print(f"{Monster_Choice} dealt {Damage_given} damage!")
        return Player_health
    else:
        print(f"{Monster_Choice} missed")


print("Welcome to the DnD-like battle simulator")

Player_name = input("please answer to following questions according to the instructrions \n What is your name or the name of your character? \n write here: ")

#keeps the game on
while True:
    #authorizes that the user puts in a valid input for their class
    while True:
      Chosen_Class = input("What Class would you like to be? (press the number asociated with your chosen class) \n 1) Melee - You have a lot of health and defense but a low hit chance \n 2) Mage you have low health and defense but high hit chance and attack power \n 3) Rogue - You have high defense and high hit chance").strip()
      
      Player_type = ""
    
      if Chosen_Class == "1":
        Player_type = player_types["Melee"]
        print(f"Your Stats are: {Player_type}")
        break
      elif Chosen_Class == "2":
        Player_type = player_types["Mage"]
        print(f"Your Stats are: {Player_type}")
        break
      elif Chosen_Class == "3":
        Player_type = player_types["Rogue"]
        print(f"Your Stats are: {Player_type}")
        break
      else:
        print("Invalid Number please try again")

    print("To win you must take out 10 monsters")
    print(f"Your Journey begins and you encounter a {Monster}")

    #starts journey
    contenders = ["Player","Monster"]
    Last_turn = random.choice(contenders)
    battles = 0
    playerhp = Player_type["hp"]
    while True:
        #starts battle
        while True:
            if Last_turn == "Player":
                #monster turn
                if Frozen_enemy <= 0:
                    Player_type["hp"] = Monster_turn(Monster, Player_type["Defense"], Player_type["hp"])
                    print("Monster turn is over")
                    Last_turn = "Monster"
                    print(f"You have {playerhp}hp left and {Monster} has {Monster_Boys[Monster]['hp']}")
                else:
                    print(f"It was {Monster}'s turn but it looks like they are frozen!")
            elif Last_turn == "Monster":
                 #player turn
                
                print("Its your turn! choose one of the following to do \n (Don't worry about the numbers)")
                
                #authorizes a valid move
                while True:
                    action = input(Player_type["actions"]).strip()
                    if action in Player_type["actions"]:
                        break
                    else:
                        print("put in a valid action. (Type in the exact action as it is written)")
                if action == "Give up":
                    print("coward")
                    break
                elif action == "drink health potion":
                    Player_type["hp"] += Player_type[action["drink health potion"]]
                    Last_turn = "Player"
                if Frozen_enemy > 0:
                    Frozen_enemy -= 1
                else:
                    #attacks
                    player_hit_chance = random.randint(1,21) + Player_type["hit chance"]
                    if player_hit_chance >= Monster_Boys[Monster]["Defense"]:
                        print(f"Attack Hit! Chance: {player_hit_chance}")
                        player_damage = random.randint(1,20) + Player_type["actions"][action]
                        if action == "dagger":
                            print(f"You used dagger and dealt {player_damage} damage!")
                            Monster_Boys[Monster]["hp"] -= player_damage
                            print(f"You have {Player_type['hp']} HP, and {Monster} has {Monster_Boys[Monster]['hp']} HP")
                            Last_turn = "Player"
                        elif action == "freeze":
                            frozen_chance = random.randint(1,10)
                            if frozen_chance >= 5 and Monster != "Dragon":
                                print("Enemy Frozen successfully for 2 turns")
                                Last_turn = "Monster"
                                Frozen_enemy += 2
                            else:
                                print("You rolled lower than a 5 or your enemy was a dragon.(You can't freeze them)")
                        elif action == "shield":
                            if Player_type["defense"] >= 45:
                                print("You can not get more defense")
                            else:
                                print("You Put up your shield to add 15 defense")
                                Player_type["Defense"] += Player_type["actions"[action]]
                        else:
                            if Player_type == "Melee":
                                player_damage = random.randint(1,16) + Player_type["sword"]
                            elif Player_type == "Rogue":
                                player_damage = random.randint(1,10) + Player_type["bow"]
                            elif Player_type == "Mage":
                                player_damage = random.randint(1,21) + Player_type["attack"]
                            print(f"You used {action} and dealt {player_damage}")
                    else:
                        print("You missed")
                        
    
            if Monster_Boys[Monster]["hp"] <= 0:
                print("you have defeated the monster Good job")
                battles += 1
                print(f"you won {battles} battles")
                break
            if playerhp <= 0:
                print(f"{Player_name} died")
                break
            if action == "Give up":
                break

        Monster_Boys = Backup_Monster_Boys.copy()
        #player death,flee or win
        
        if Player_type["hp"] <= 0:
            print(f"{Player_name} died")
            break
        elif battles == 10:
            print(f"Good job {Player_name} you have conquered 10 enemies! You Win!")
            break
        elif action == "Give up":
            break
            
        Monster = random.choice(Monsters)
  
    Play_again = input("Would you like to play again? \n (y/n) \n invalid inputs will result in the game running again")
    if Play_again == "n":
        print("See you later!")
        break
    else:
        print("playing again")
