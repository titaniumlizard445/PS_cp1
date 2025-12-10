#PS 1st The Adventure of John Jonathan Johnson

#Libraries
import random
import time

#Var

player_stats = {
    "Strength":4,
    "Intelligence":2,
    "Defense":1,
    "Money":0,
    "Health Points":125,
    "Slots Unlocked":3,
    "Max Health":125
    }
player_inventory = ["Chopsticks","",""]

enemies_stats={
    "Rat Burrower":{
        "Strength":5,
        "HP":50
    },
    "Rat Soldier":{
        "Strength":7,
        "HP":100
    },
    "Rat Archer":{
        "Strength":4,
        "HP":80
    },
    "Rat Spartan":{
        "Strength":8,
        "HP":120
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
            "Price":10,
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
    "items":["Money","John's Axe","Pork","Money","Intelligence","Intelligence","Intelligence","Intelligence","Intelligence","Money","Money","Intelligence"]
}

freed_villages = []

resetdictionary= {
    "player stats":{
        "Strength":4,
        "Intelligence":2,
        "Money":0,
        "Health Points":125,
        "Slots Unlocked":3,
        "Max Health":125
    },
    "player default inventory":["Chopsticks","",""],
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
                "Price":10,
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
weapons = ["Chopsticks","Axe","Longer Chopsticks","Bow"]
weaponstats = {
    "Chopsticks":{
        "Damagemult":1
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

enemystats = {}
#funct

def PlayerTurn(pstats,pinventory,weaponstats,weapons,consumables,estats):
    print("It is now your turn to attack!")
    usableitems = []
    for x in pinventory:
        if x in weapons or x in consumables:
            usableitems.append(x)
    item = input(f"choose an item to use {usableitems}")
    if item in pinventory:
        if item in weapons:
            hit_chance = random.randint(1,20)
            if hit_chance >= 6:
                print("Attack hit! rolling damage...")
                damage = random.randint(1,10) * pstats["Strength"] * weaponstats[item]["damgagemult"]
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
        damage = random.randint(1,10) * estats["Strength"]
        pstats["HP"] -= damage
        print(f"The enemy did {damage} damage!\nYou are at {pstats["HP"]}")
    else:
        print("The Foe missed missed")
    if estats["Health Points"] <=0:
        edefeat +=1
    return pstats, estats, edefeat

def BossTurn():
    print("Insert stuff here")

def ItemDropSystem():
    print("Insert stuff here")

def OpenInventory():
    print("Insert stuff here")

def CombatSystem(pstats,pinventory,weaponstats,weapons,consumables,estats,edefeat):
    player_loss = False
    Enemydestroyed = edefeat
    while not player_loss and Enemydestroyed == edefeat:
        pstats, estats, pinventory = PlayerTurn(pstats,pinventory,weaponstats,weapons,consumables,estats)
        pstats, estats, edefeat = MonsterTurn(estats,pstats,edefeat)

def Chestsystem():
    print("Insert stuff here")

def Rest():
    print("John slept and remained unproductive the whole night")

def FreeVillage():
    print("Put combat function with for x3 and other stuff")

#take in dictionary for items and village be accessed
def UseShop():
    print("Insert stuff here")

def Credits():
    print("Insert cool stuff here")

def JohnsHouse():
    print("Insert stuff here")

#(parameters) take in name and dictionary with info and villages defeated
def DefaultVillage():
    print("Insert stuff here")

def BastilliaFortuica():
    print("Insert stuff here")

def TutorialIntroduction():
    print("Insert stuff here")

#gameloop
while True:
    print(f"Welcome to possibly the greatest text based adventure game you will see today \nIf you care about your score: \nthere are three stats that will be recordeed on the scoreboard \n1)Your Time \n2)The Number of Enemies you Defeated \n3)Your Intelligence stat \n")
    
    #game
    while True:
        print(f"John was a humble woodcutter who lived alone in a weather-beaten log cabin deep in the heart of the vast Greenwood Forest. The nearest village lay fifty miles away—far enough that John could go months without seeing another human soul, which suited him fine.\n \nHe had his trees, his fireplace, and his meals eaten with his trusty pair of chopsticks—a habit picked up from the rare Asian merchants who wandered close enough for trade. His only friend in the world was George—a wandering tinkerer who visited every few months with stories, odd inventions, and a warm smile that John secretly treasured. \n \n The Day Everything ChangedOne crisp autumn morning, John marched into the woods carrying his well-used axe, ready to split logs for winter. But fate had other plans. A horse's frantic gallop broke the forest silence. A messenger—mud-stained, wide-eyed—rode up and thrust a rolled parchment into John's hands. \n \n “The eight villages to the south have fallen! Invaded by mutant rats—thousands of them! And… and your friend George was taken.”\n \n The messenger fled almost immediately, as if the forest itself were unsafe. John's heart pounded with panic and anger. George—the one person who cared about him—captured by rats? The thought didn't make sense. But before John could process the message, he heard chittering behind him. He spun around. \n \nToo late. A swarm of grotesque, oversized rats leapt from the underbrush, their eyes glowing with eerie green light. They rushed him like a furry tidal wave, squeaking with unnatural coordination. John swung his axe wildly—but they overwhelmed him. He felt tiny claws on his arms, his legs, his shoulders. In seconds they wrenched the axe from his grip and vanished into the forest with it, carrying the iron-headed tool like a trophy. John was left panting, weaponless, and furious.")
        break
    break


#scoreboard



