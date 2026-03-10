#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#libraries
import random
import time

#constants
SUITS = ["hearts","clubs","spades","diamonds",]
NUMBERS = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

#variables
deck = [[],[]]
dealer_hand = [""]
player_hand = [[],[]]

#functions

def build_deck():
    for x in SUITS:
        for y in NUMBERS:
            deck[0].append(x)
            deck[1].append(y)

def player_deal():
    card = random.randint(0,len(deck[0])-1)
    player_hand[0].append(deck[0][card])
    player_hand[1].append(deck[1][card])
    deck[0].pop(card)
    deck[1].pop(card)
    for i in range(0,len(player_hand[0])):
        print(i+1,":",player_hand[1][i],"of",player_hand[0][i])

def player_play_game():
    ask_player = ""
    while not ask_player:
        ask_player = input("Do you want to hit or stand? ( H / S )\n").upper().strip()
        if ask_player == "H":
            player_deal()
        elif ask_player == "S":
            are_you_sure = input("Are you sure? ( Y / N )\n").upper().strip()
            if are_you_sure == "Y":
                continue
            else:
                return ask_player
        else:
            print("Please try again")


#welcome_msg
print("---------------------------------")
print("_Welcome to tiles and turbulence_")
print("---------------------------------")

#main program
build_deck()
player_deal()
return_from_stand_fail = player_play_game()