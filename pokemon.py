
import random

wild_pokemon = [
       {"Name":"Charmander","Type":"Fire","Level":random.randint(1,3),"Health":random.randint(20,30)},
       {"Name":"Bulbasoar","Type":"Grass","Level":random.randint(1,3),"Health":random.randint(30,45)},
       {"Name":"Squirtle","Type":"Water","Level":random.randint(1,3),"Health":random.randint(25,35)},
       {"Name":"Sylveon","Type":"Fairy","Level":random.randint(1,3),"Health":random.randint(15,35)},
       {"Name":"Gengar","Type":"Ghost","Level":random.randint(1,3),"Health":random.randint(50,60)},
       {"Name":"Lucario","Type":"Fighting","Level":random.randint(1,3),"Health":random.randint(40,50)},
       {"Name":"Rhydon","Type":"Rock","Level":random.randint(1,3),"Health":random.randint(60,70)}
]

def battle():
       x = random.randint(0,2)
       pokemon = wild_pokemon[x]
       print("A wild", pokemon["Name"], "appeared")
       print("It's a", pokemon["Type"], "pokemon")
       print("Level : ", pokemon["Level"])
       print("Health : ", pokemon["Health"])

battle()