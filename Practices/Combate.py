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
            "sword":35,
            #add defense
            "shield":35,
            "drink health potion":35,
            "run away":0
            }
    },
    "Mage":{
        "hp":75,
        "Defense":10,
        "hit chance":35,
        "actions":{
            #chance use coin
            "freeze":1,
            #damage
            "attack":65,
            "run away":0,
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
            "run away":0,
            "drink health potion":45
        }
    }
}


