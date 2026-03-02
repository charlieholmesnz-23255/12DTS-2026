
import random
import time

wild_pokemon = [
       {"Name":"Charmander","Type":"Fire","Level":1,"Health":random.randint(20,30),"Attack":["Fire swipe",random.randrange(3,6),"Incendiary",random.randrange(20,25)]},
       {"Name":"Bulbasoar","Type":"Grass","Level":1,"Health":random.randint(30,45),"Attack":["Branch fall",random.randrange(2,5),"Tree Trunk",random.randrange(30,35)]},
       {"Name":"Squirtle","Type":"Water","Level":1,"Health":random.randint(25,35),"Attack":["Splash",random.randrange(4,7),"Incendiary",random.randrange(15,20)]},
       {"Name":"Sylveon","Type":"Fairy","Level":1,"Health":random.randint(15,35)},"Attack":["Daze",random.randrange(3,4),"Sleepyhead",random.randrange(1,50)]},
       {"Name":"Gengar","Type":"Ghost","Level":1,"Health":random.randint(50,60)},
       {"Name":"Lucario","Type":"Fighting","Level":1,"Health":random.randint(40,50)},
       {"Name":"Rhydon","Type":"Rock","Level":1,"Health":random.randint(60,70)}
]

player_pokemon = [{"Name":"Ditto","Type":"Normal","Level":1,"Health":random.randint(5,10),"Attack":["Nothing",random.randrange(1,2),"More Nothing",random.randrange(10,20)]}]

def overworld_timer():
       timer = random.randint(1,5)
       print(timer)
       time.sleep(timer)
       print("Battle begins")
       battle()

def starting_pokemon():
       x = random.randint(0,2)
       pokemon = wild_pokemon[x]
       print(pokemon["Name"])
       print("It's a", pokemon["Type"], "pokemon")
       print("Level : ", pokemon["Level"])
       print("Health : ", pokemon["Health"],"\n")

def professor_oak():
       possible_player_picks = ["B","S","C"]
       player_picked = ""
       starting_pokemon()
       starting_pokemon()
       starting_pokemon()
       player_pokemon.append = input("Which pokemon would you like to choose as your first?\n (B or S or C)")
       while not player_picked:
              if player_pokemon not in possible_player_picks:
                     print("Try again\n")
                     continue
              else:
                     player_picked = player_pokemon

def battle():
       x = random.randint(0, len(wild_pokemon)-1)
       enemy_pokemon = wild_pokemon[x]
       own_pokemon = player_pokemon[0]
       player_pokemon_hp = own_pokemon["Health"]
       pokemon = wild_pokemon[x]
#show player
       print("Player pokemon:",own_pokemon["Name"])
       print("Player pokemon HP:",player_pokemon_hp)
#show enemy
       print("A wild", pokemon["Name"], "appeared")
       print("It's a", pokemon["Type"], "pokemon")
       print("Level : ", pokemon["Level"])
       print("Health : ", pokemon["Health"])

       while True:
              enemy_attack_randomiser = random.randrange(0,3,2)
              print("Random number for attack", enemy_attack_randomiser)
              print(enemy_pokemon["Name"], "attacks with", enemy_pokemon["Attack"][enemy_attack_randomiser], "for",enemy_attack_randomiser["Attack"][enemy_attack_randomiser + 1], "damage")
              player_pokemon_hp = player_pokemon_hp - enemy_pokemon["Attack"][enemy_attack_randomiser + ]
              print(player_pokemon["Name"], "has", player_pokemon_hp, "health ")
           overworld_timer()

battle()
