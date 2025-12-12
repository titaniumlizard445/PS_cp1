#PS 1st The Adventure of John Jonathan Johnson

#Libraries
import random
import time

#Var

player_stats = {
    "Name":"John Jonathan Johnson",
    "Strength":4,
    "Intelligence":2,
    "Defense":1,
    "Money":0,
    "Health Points":125,
    "Slots Unlocked":3,
    "Max Health":125
    }
player_inventory = ["Chopsticks"]

enemies_stats={
    "Rat Burrower":{
        "Strength":5,
        "HP":50,
        "Boss":False
    },
    "Rat Soldier":{
        "Strength":7,
        "HP":100,
        "Boss":False
    },
    "Rat Archer":{
        "Strength":4,
        "HP":80,
        "Boss":False
    },
    "Rat Spartan":{
        "Strength":8,
        "HP":120,
        "Boss":False
    }
}

boss_stats = {
    "Rat Dictator":{
        "Strength":15,
        "HP":250,
        "Boss":True
    },
    "George":{
        "Strength":20,
        "HP":300,
        "Boss":True
    }
}



enemies = ["Rat Burrower", "Rat Soldier", "Rat Archer", "Rat Spartan"]
village_shops = {
    "Wellville":{
        "Heal":{
            "price":25,
            "description":"The doctors of Wellville heal you to max health",
            "stock":9999999
        }
    },
    "Chemisville":{
        "Tome of Damage":{
            "price":50,
            "description":"Increases your Strength when it is in your inventory",
            "stock":3
        },
        "Tome of Max Health":{
            "price":40,
            "descripton":"Increases your defense when it is in your inventory",
            "stock":3
        },
        "Tome of Defense":{
            "price":20,
            "description":"Increases your defense while in inventory",
            "stock":3
        }
    },
    "Gobapdular":{
        "Useless Hay":{
            "price":10,
            "description":"A bundle of a farmer's finest wheat",
            "stock":10
        }
    },
    "Kraftville":{
        "Iron ingot":{
            "price":15,
            "description":"A refined metal straight from kraftsville caves",
            "stock":10
        }
    },
    "Bovisad":{
        "Brisket":{
            "price":60,
            "description":"Increases your max health by 25hp permanently",
            "stock":8},
        "Pork":{
            "price":30,
            "description":"You gain 50hp",
            "stock":15
        }
    },
    "Kingdomsville":{
        "Not Available":{
            "price":0,
            "description":"King Timmy is to lazy to make merchants sell anything",
            "stock":0
        }
    },
    "Escargot":{
        "Longer chopstick":{
            "price":50,
            "description":"Weapon: is stronger than default chopsticks but is otherwise useless",
            "stock":1
        },
        "Chainsaw":{
            "price":100,
            "description":"Weapon: Highest damage output in game"
        }
    },
    "Litteratious":{
        "Send mail":{
            "price":10,
            "description":"You can write a letter to anyone and you will receive a reply instantly (note:does not contribute to the story in any way shape or form)",
            "stock":9999999999
        }
    }
}

chestlootsystem = {
    #There is repeats of the same items for skewing chance
    "normal items":["Money","Pork","Money","Money","Money","Brisket"],
    "Secret Chest loot":["Money","John's Axe","Pork","Money","Intelligence","Intelligence","Intelligence","Intelligence","Intelligence","Money","Money","Intelligence"]
}

freed_villages = []

resetdictionary= {
    "player stats":{
        "Name":"John Jonathan Johnson",
        "Strength":4,
        "Intelligence":2,
        "Money":0,
        "Health Points":125,
        "Slots Unlocked":3,
        "Max Health":125
    },
    "player default inventory":["Chopsticks"],
    "Village Shops":{
        "Wellville":{
            "Heal":{
                "price":25,
                "description":"The doctors of Wellville heal you to max health",
                "stock":9999999
            }
        },
        "Chemisville":{
            "Tome of Damage":{
                "price":50,
                "description":"Increases your Strength when it is in your inventory",
                "stock":3
            },
            "Tome of Max Health":{
                "price":40,
                "descripton":"Increases your defense when it is in your inventory",
                "stock":3
            },
            "Tome of Defense":{
                "price":20,
                "description":"Increases your defense while in inventory",
                "stock":3
            }
        },
        "Gobapdular":{
            "Useless Hay":{
                "price":10,
                "description":"A bundle of a farmer's finest wheat",
                "stock":10
            }
        },
        "Kraftville":{
            "Iron ingot":{
                "price":15,
                "description":"A refined metal straight from kraftsville caves",
                "stock":10
            }
        },
        "Bovisad":{
            "Brisket":{
                "price":60,
                "description":"Increases your max health by 25hp permanently",
                "stock":8},
            "Pork":{
                "price":30,
                "description":"You gain 50hp",
                "stock":15
            }
        },
        "Kingdomsville":{
            "Not Available":{
                "price":0,
                "description":"King Timmy is to lazy to make merchants sell anything",
                "stock":0
            }
        },
        "Escargot":{
            "Longer Chopsticks":{
                "price":50,
                "description":"Weapon: is slightly stronger than default chopsticks but is otherwise useless",
                "stock":1
            }
        },
        "Litteratious":{
            "Send mail":{
                "price":10,
                "description":"You can write a letter to anyone and you will receive a reply instantly (note:does not contribute to the story in any way shape or form)",
                "stock":9999999999
            }
        }
    }
}
Weapons = ["Chopsticks","Axe","Longer Chopsticks","Bow"]
weaponstats = {
    "Chopsticks":{
        "damagemult":1
    },
    "Axe":{
        "damagemult":2
    },
    "Longer Chopsticks":{
        "damagemult":1.25
    },
    "Bow":{
        "damagemult":1.5
    }
}

consumables = ["Brisket","Pork"]
name = ""

start_time = 0
end_time = 0

total_defeated = 0

#Village Name : Codes: reward/puzzle
secret_codes = {}

#score board contains names, points and times
scoreboard = {}

enemies_defeated = 0
bosses_defeated = 0
chest = []
#funct

def PlayerTurn(pstats,pinventory,weaponstats,weapons,consumables,estats):
    print("It is now your turn to attack!")
    usableitems = [""]
    for x in pinventory:
        if x in weapons:
            usableitems = usableitems.append(x)
        elif x in consumables:
            usableitems = usableitems.append(x)
    item = input(f"choose an item to use {usableitems}").strip()
    if item in pinventory:
        if item in weapons:
            hit_chance = random.randint(1,20)
            if hit_chance >= 6:
                print("Attack hit! rolling damage...")
                damage = random.randint(1,10) * pstats["Strength"] * weaponstats[item]["damagemult"]
                estats["HP"] -= damage
                print(f"You did {damage} damage!\nThe Foe is at {estats["HP"]}")
            else:
                print("You missed")
        elif item in consumables:
            if item == "Brisket":
                pstats["Max Health"] += 25
                pstats["Health Points"] += 25
                pinventory.remove("Brisket")
            elif item == "Pork":
                if pstats["Health Points"] >= pstats["Max Health"] or pstats["Health Points"] <= 0:
                    print("You cannot heal, You have Max health")
                else:
                    pstats["Health Points"] += 20
                    pinventory.remove("Pork")
            else:
                print("Item functionality not added yet")
        else:
            print("Error item not found")
    else:
        print("pick a weapon that you have in your inventory")
    return pstats, estats, pinventory

def MonsterTurn(estats,pstats,edefeat):
    print("It is now the foe's turn to attack!")
    hit_chance = random.randint(1,20)
    if hit_chance >= 8:
        print("Attack hit! rolling damage...")
        damage = random.randint(1,10) * estats["Strength"] * edefeat * 0.1
        pstats["HP"] -= damage
        print(f"The enemy did {damage} damage!\nYou are at {pstats["HP"]}")
    else:
        print("The Foe missed missed")
    if estats["Health Points"] <=0:
        edefeat +=1
    return pstats, estats, edefeat

def BossTurn(bstats,pstats,bdefeat):
    print("It is now the bosses turn to attack!")
    hit_chance = random.randint(1,20)
    if hit_chance >= 6:
        print("Attack hit! rolling damage...")
        damage = random.randint(1,10) * bstats["Strength"]
        pstats["HP"] -= damage
        print(f"The Boss did {damage} damage!\nYou are at {pstats["HP"]}")
    else:
        print("The Foe missed missed")
    if bstats["Health Points"] <=0:
        bdefeat +=1
    return pstats, bstats, bdefeat

def ItemDropSystem(items,pstats,pinventory,loottype):
    if loottype == "Normal":
        randomitem = random.choice(items["normal items"])
    elif loottype == "Secret":
        randomitem = random.random.choice(items["Secret Chest loot"])
    if randomitem == "Money":
        randommoney = random.randint(1,50)
        pstats["Money"] += randommoney
    elif randomitem == "Intelligence":
            randomintel = random.randint(1,40)
            pstats["Intelligence"] += randomintel    
    elif len(pinventory) < pstats["Slots Unlocked"]:
        if randomitem == "Pork" or randomitem == "Brisket" or randomitem == "John's Axe":
            pinventory = pinventory.append(randomitem)
        else:
            print("random item generator failed")
    else:
        print(f"You have a filled inventory, You may not hold anymore items. (items slots {pstats["Slots Unlocked"]})")

def OpenInventory(pinventory):
    print(f"Your inventory consists of {pinventory}")

def CombatSystem(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat,bdefeat,items):
    player_loss = False
    Enemydestroyed = edefeat
    bossdestroyed = bdefeat
    while not player_loss and Enemydestroyed == edefeat and bossdestroyed == bdefeat:
        if estats["Boss"]:
            pstats, estats, pinventory = PlayerTurn(pstats,pinventory,weaponstats,weapons,consumables,estats)
            if pstats["HP"] <= 0:
                player_loss = True
                continue
            if bossdestroyed < bdefeat:
                bdefeat += 1
                continue
            time.sleep(5)
            pstats, estats, bdefeat = BossTurn(estats,pstats,bdefeat)
            if pstats["HP"] <= 0:
                player_loss = True
                continue
            if bossdestroyed < bdefeat:
                bdefeat += 1
                continue
            time.sleep(5)
        else:
            pstats, estats, pinventory = PlayerTurn(pstats,pinventory,weaponstats,weapons,consumables,estats)
            if pstats["HP"] <= 0:
                player_loss = True
                continue
            if Enemydestroyed < edefeat:
                edefeat+=1
                continue
            time.sleep(5)
            pstats, estats, edefeat = MonsterTurn(estats,pstats,edefeat)
            if pstats["HP"] <= 0:
                player_loss = True
                continue
            if Enemydestroyed < edefeat:
                edefeat += 1
                continue
            time.sleep(5)
    if player_loss == False:
        pinventory = pinventory.append(ItemDropSystem(items,pstats,pinventory,"Normal"))
    return pstats, pinventory, bdefeat, edefeat, player_loss

def Rest():
    print("John slept and remained unproductive the whole night")

def FreeVillage(pstats,pinventory,weaponstats,weapons,consumables,edefeat,bdefeat,items,monsters,estats):
    win_counter = 0
    pre_ded_enemies = edefeat
    while win_counter < 3:
        enemychosen = random.choice(monsters)
        estats = estats[enemychosen]
        print(f"You are going to fight a {enemychosen} it has {estats["HP"]}Health and has {estats["Strength"]} points of strength")
        pstats, pinventory, bdefeat,edefeat,player_loss = CombatSystem(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat,bdefeat,items)
        if player_loss == True:
            print("You Lose, (death during Enemy rush)")
            break
        elif edefeat > pre_ded_enemies:
            win_counter += 1
            pre_ded_enemies = edefeat
    if player_loss == False:
        print("You have inspired the prisoners in rat prison to break out and free the village! \nGood Job!\n")
    return pstats, pinventory,edefeat,player_loss

#take in dictionary for items and village be accessed
def UseShop(shop_dict,village,pstats,pinventory):
    shopping = True
    while shopping:
        if len(pinventory) >= pstats["Slots Unlocked"]:
            print("Your inventory is full go back home to empty it and then you can shop.")
        else:
            print(f"SHOP KEEPER: Hello and Welcome to my Store, We have a nice selection of items for you to pick out today. \n ")
            for item in shop_dict[village]:
                print(f"{item.key()} Price: {item["price"]}$. Brief description: {item["description"]}. Stock: {item["stock"]}")
            itemwanted = input("SHOP KEEPER: What would you like? (type \"leave\" if you want to stop shopping) \n Enter valid shop item here: ").strip()
            if itemwanted == "leave":
                shopping == False
                continue
            elif itemwanted in shop_dict[village]:
                if shop_dict[village][itemwanted]["stock"] > 0:
                    if pstats["Money"] >= shop_dict[village][itemwanted]["price"]:
                        if village == "Litteratious":
                            mail = input("Write a letter here: ").strip()
                            print("You receive a reply")
                            mailchoices = ["Thank you for the letter, we really needed that information. Good luck on your adventure! -Dev","Thank you for the letter, I did not need you to explain your life story or anything of the such, Save the world faster! -Dev","Why did you send mail? Do you think these rats are a Joke? Stop doing useless actions its not worth it. -Dev"]
                            print(random.choice(mailchoices))
                        else:
                            pinventory = pinventory.append(itemwanted)
                            pstats["Money"] -= shop_dict[village][itemwanted]["price"]
                            shop_dict[village]["stock"] -= 1
                            print(f"SHOP KEEPER: Thank you for your purchase of a {itemwanted}")
                    else:
                        print("You are too poor to afford this item")
                else:
                    print("Sorry this item is out of stock")
            else:
                print("Invalid input, please type the item exactly as it is written")
                
        leave = input("Would you like to leave the store? (y/n)\nEnter Response here: ").strip()
        if leave == "y":
            shopping == False
        elif leave == "n":
            print("You may continue shoping")
        else:
            print("You entered an invalid input")
    return pstats, pinventory, shop_dict
def Credits():
    print("Lead Developer: PS \n Other Developer: PS \n designer: PS \n Small ideas: eb partners \n Pseudocode: PS \n Thank you for playing this PS production")

def JohnsHouse(pstats,pinventory,chest):
    visiting = True
    while visiting:
        print("Welcome to John's House you can rest (R), empty your inventory into a chest (EI), Take an item from the chest (TI), eat a Brisket (B), look at your stats (S) or leave (L) (input to capital letters in paranthesis for the action you would like to choose)")
        Action = input("Enter Action here: ").strip()
        if Action == "R":
            Rest()
        elif Action == "EI":
            print("Put a item(s) in the chest")
            using_chest= True
            while using_chest:
                item_to_move = input(f"What item would you like to move to your chest? (items in your inventory: {pinventory}) \n Enter item name here: ").strip()
                if item_to_move in pinventory:
                    chest = chest.append(item_to_move)
                    pinventory.remove(item_to_move)
                    print("Item successfully moved")
                else:
                    print("This item does not exist or you don't have one in your inventory")
                stop = input("Would you like to stop emptying items into the chest? \n Enter y/n here: ").strip()
                if stop == "y":
                    using_chest = False
                else:
                    print("Continue your buisness.")
        elif Action == "TI":
            print("Take item(s) from the chest")
            using_chest = True
            while using_chest:
                if pinventory < pstats["Slots Unlocked"]:
                    item_to_move = input(f"What item would you like to move to your inventory (item in the chest: {chest})").strip()
                    if item_to_move in chest:
                        pinventory = pinventory.append(item_to_move)
                        chest.remove(item_to_move)
                        print("Item successfully moved")
                    else:
                        print("Invalid item or chosen item is not in chest")
                else:
                    print("You have too many item in your inventory")
                    using_chest = False
                stop = input("Would you like to stop emptying items into the chest? \n Enter y/n here: ").strip()
                if stop == "y":
                    using_chest = False
                else:
                    print("Continue your buisness.")
        elif Action == "B":
            if "Brisket" in pinventory:
                pstats["Max Health"]
                pstats["Health Points"] = pstats["Max Health"]
                print("You savor the brisket to the last bite. (Max health increased and HP is at max now)")
                time.sleep(5)
            else:
                print("You have no Brisket :(")
        elif Action == "S":
            print(f"Player Stats:{pstats}")
            print("Yes his name is John Jonathan Johnson :)")
        elif Action == "L":
            print("You leave John's house")
            visiting = False
        else:
            print("Invalid input please read the instructions")
            time.sleep(5)
    return pstats, pinventory, chest
#(parameters) take in name and dictionary with info and villages defeated
def DefaultVillage(free_village,shop_dict,village,pinventory,pstats,weaponstats,weapons,consumables,edefeat,bdefeat,items,monsters,estats):
    visiting = True
    while visiting:
        print(f"Welcome to {village}")
        if village not in free_village:
            print("This village has not become free of rat power yet \n You must free it. (defeat 3 monsters)")
            pstats, pinventory,edefeat,player_loss = FreeVillage(pstats,pinventory,weaponstats,weapons,consumables,edefeat,bdefeat,items,monsters,estats)
            if player_loss == False:
                print("You may now use access shops and other village activities")
                free_village = free_village.append(village)
            if player_loss == True:
                break
        else:
            print("You may use the shop or leave the village (\"Shop\",\"Leave\")")
            Action = input("Enter choice here: ").strip()
            if Action == "Shop":
                pstats, pinventory, shop_dict = UseShop(shop_dict,village,pstats,pinventory)
            elif Action == "Leave":
                print("You run out of the village and onto the main path.")
                break
    return pstats, pinventory, shop_dict, edefeat, player_loss, free_village
def BastilliaFortuica(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat,bdefeat,items):
    print("You enter the fort and see a shadowy figure in the distance. It is wearing something pointy on its head. As it walks closer you notice that it is wearing red robes. It comes under the torchlight, Its the King of the Rats!")
    estats = estats["Rat Dictator"]
    pstats, pinventory, bdefeat, edefeat, player_loss = CombatSystem(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat,bdefeat,items)
    if player_loss == True:
        print("You have failed to conquer the rat King and he lives on and conquers the rest of the world.")
    else:
        print(f"You have successfully defeated the rat king. As you journey further into the Fort, you see a familiar shape, but at the sight of you it runs off very quickly down a nearby corridoor. \n \nYou Chase after it left, right, down some stairs until it stops. \n \nIt turns to face you. You see that it is wearing a dirty, brown trenchcoat and fedora. In a muffled voice it says,\"Your time has come dear friend my rat kingdom will take over the world and no one will stop me!\"\n \nYou realize that this is your friend George, \n \n\"Why would you do this George?\" You ask him. George does not respond. You must defeat George to save the world.")
        bdefeat += 1
        pstats, pinventory, bdefeat, edefeat, player_loss = CombatSystem(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat,bdefeat,items)
        if player_loss == True:
            print("You have failed to conquer the George and he lives on and conquers the rest of the world and reign in absolute as an autoritarian.")
        else:
            print("George wobbles side to side, Fallse onto his face, and rats come scurrying out of all the crevices in the trenchcoat and fedora.")
            print("You win! and have restored peace to all the surrounding villages and saved the world.")
            player_win = True
            bdefeat +=1
    return pstats, pinventory, bdefeat, edefeat, player_loss, player_win
def TutorialIntroduction():
    print("Here is a brief summary of what you can do in the game: \n \nYou will adventure to 9 different villages, defeating monsters and tyrants along the way. Make sure your inputs are exactly as the instructions have told you to format them. If there is no instructions then just write one of the options.")


village_choices = ["W","C","G","KR","B","KG","E","L"]
village_chosen = ""
#gameloop
while True:
    print(f"Welcome to possibly the greatest text based adventure game you will see today \nIf you care about your score: \nthere are three stats that will be recorded on the scoreboard \n1)Your Time \n2)The Number of Enemies you Defeated \n3)Your Intelligence stat \n \n Now the game can begin \n")
    village_chosen = ""
    Name = input("What is your name? \nEnter your name here: ").strip()
    start_time = time.time()
    end_time = 0.0
    game_time = 0.0
    endgame = False
    player_loss = False
    village_shops = resetdictionary["Village Shops"]
    player_stats = resetdictionary["player stats"]
    player_inventory = ["Chopsticks"]
    player_win = False
    #game
    while True:
        print(f"John was a humble woodcutter who lived alone in a weather-beaten log cabin deep in the heart of the vast Greenwood Forest. The nearest village lay fifty miles away—far enough that John could go months without seeing another human soul, which suited him fine.\n \nHe had his trees, his fireplace, and his meals eaten with his trusty pair of chopsticks—a habit picked up from the rare Asian merchants who wandered close enough for trade. His only friend in the world was George—a wandering tinkerer who visited every few months with stories, odd inventions, and a warm smile that John secretly treasured. \n \n The Day Everything ChangedOne crisp autumn morning, John marched into the woods carrying his well-used axe, ready to split logs for winter. But fate had other plans. A horse's frantic gallop broke the forest silence. A messenger—mud-stained, wide-eyed—rode up and thrust a rolled parchment into John's hands. \n \n “The eight villages to the south have fallen! Invaded by mutant rats—thousands of them! And… and your friend George was taken.”\n \n The messenger fled almost immediately, as if the forest itself were unsafe. John's heart pounded with panic and anger. George—the one person who cared about him—captured by rats? The thought didn't make sense. But before John could process the message, he heard chittering behind him. He spun around. \n \nToo late. A swarm of grotesque, oversized rats leapt from the underbrush, their eyes glowing with eerie green light. They rushed him like a furry tidal wave, squeaking with unnatural coordination. John swung his axe wildly—but they overwhelmed him. He felt tiny claws on his arms, his legs, his shoulders. In seconds they wrenched the axe from his grip and vanished into the forest with it, carrying the iron-headed tool like a trophy. John was left panting, weaponless, and furious.")
        TutorialIntroduction()
        endgame == False
        while not endgame:
            print(f"Villages: John’s House (JH), Wellville (W), Chemisville (C), Gobapdular (G), Kraftville (KR), Bovisad (B), Kingdomsville (KG), Escargot (E), Litteratious (L), Bastillia Fortuica (You cannot enter unless all other villages have been explored) (BF)\nChoose a village (or John's House) to explore!")
            choice = input("Enter Choice here: ").strip()
            if choice == "JH":
                player_stats, player_inventory, chest = JohnsHouse(player_stats,player_inventory,chest)
            elif choice == "BF":
                if len(freed_villages) == 8:
                    player_stats, player_inventory, bosses_defeat, enemies_defeat, player_loss, player_win = BastilliaFortuica(player_stats,player_inventory,weaponstats,Weapons,consumables,boss_stats,enemies_defeated,bosses_defeated,chestlootsystem,enemies)
            elif choice in village_choices:
                if choice == "W":
                    village_chosen = "Wellville"
                elif choice == "C":
                    village_chosen = "Chemisville"
                elif choice == "G":
                    village_chosen = "Gobapdular"
                elif choice == "KR":
                    village_chosen = "Kraftville"
                elif choice == "B":
                    village_chosen = "Bovisad"
                elif choice == "KG":
                    village_chosen = "Kingdomsville"
                elif choice == "E":
                    village_chosen = "Escargot"
                elif choice == "L":
                    village_chosen = "Litteratious"
                else:
                    print("Village Error ocurred")
                player_stats, player_inventory, village_shops, enemies_defeated, player_loss,freed_villages = DefaultVillage(freed_villages,village_shops,village_chosen,player_inventory,player_stats,weaponstats,Weapons,consumables,enemies_defeated,bosses_defeated,chestlootsystem,enemies,enemies_stats)
            else:
                print("Invalid input please try again")
                continue
            if player_loss == True:
                print("You Lose")
                game_time = "Did not finish"
                break
            if player_win == True:
                print("GG")
                end_time = time.time()
                break
        #scoreboard
        if isinstance(end_time,int):
            game_time = end_time - start_time
        scoreboard.append({Name:{"Time":str(game_time)+" seconds","Enemies defeated":enemies_defeated,"Intelligence":player_stats["Intelligence"]}})
        print("Scoreboard:")
        counter = 0
        for x in scoreboard:
            print(scoreboard[counter])
            counter += 1
        play_again = input(f"Would you like to play again? y/n \n Type here: ").strip()
        if play_again == "n":
            print("Thank you for playing")
            break
    break


