#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#libraries
import random
import time
import os

#constants
SUITS = ["hearts","clubs","spades","diamonds"]
NUMBERS = {"2" : 2 , "3" : 3,"4" : 4,"5" : 5,"6" : 6,"7" : 7,"8" : 8,"9" : 9,"10" : 10,"J" : 10,"Q" : 10,"K" : 10,"A" : 1}

#variables
deck = [[],[]]
dealer_hand = [[],[]]
player_hand = [[],[]]
player_total = 0

#functions
def build_deck():
    for x in SUITS:
        for y in NUMBERS:
            deck[0].append(x)
            deck[1].append(y)

def delete_deck():
    global deck
    deck = [[],[]]

def check_hand():
    global player_hand
    global player_total
    player_total = 0

    for i in player_hand[1]:
        player_total += NUMBERS[i]

    if player_total > 21:
        delete_deck()
        build_deck()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You got too many points,try again\n")
        player_hand = [],[]
        time.sleep(3)
        return "over"

    if player_total == 21:
        delete_deck()
        build_deck()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You got 21, congrats\n")
        player_hand = [],[]
        time.sleep(3)
        return "perfect"

    else:
        return "good"

def player_deal():
    tile = random.randint(0,len(deck[0])-1)
    player_hand[0].append(deck[0][tile])
    player_hand[1].append(deck[1][tile])
    deck[0].pop(tile)
    deck[1].pop(tile)

    for i in range(0,len(player_hand[0])):
        print(i+1,":",player_hand[1][i],"of",player_hand[0][i])


def player_play_game(return_from_stand):
    ask_player = ""
    check_hand()

    if player_total > 21:
        return False

    while not ask_player:

        ask_player = input("Do you want to hit or stand? ( H / S )\n").upper().strip()

        if ask_player == "H":
            player_deal()
            player_play_game(True)
            check_hand()

        elif ask_player == "S":
            are_you_sure = input("Are you sure? ( Y / N )\n").upper().strip()

            if are_you_sure == "Y":
                continue

            elif are_you_sure == "N":
                return False

            else:
                print("Please try again")
                return are_you_sure

        else:
            print("Please try again")
            return ask_player

    if check_hand() == "perfect" or "over":
        delete_deck()
        build_deck()
        player_play_game(True)

#welcome_msg
print("---------------------------------")
print("-Welcome to tiles and turbulence-")
print("---------------------------------")

#main program
build_deck()
player_play_game(True)
