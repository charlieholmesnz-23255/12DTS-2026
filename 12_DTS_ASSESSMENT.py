#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#libraries
import random
import time

#constants
SUITS = ["hearts","clubs","spades","diamonds"]
NUMBERS = {"2" : 2 , "3" : 3,"4" : 4,"5" : 5,"6" : 6,"7" : 7,"8" : 8,"9" : 9,"10" : 10,"J" : 10,"Q" : 10,"K" : 10,"A" : 1}

#variables
deck = [[],[]]
dealer_hand = [[],[]]
player_hand = [[],[]]
player_total = 0

#functions

def check_hand():
    global player_total
    for i in player_hand[1]:
        player_total += NUMBERS[i]
def build_deck():
    for x in SUITS:
        for y in NUMBERS:
            deck[0].append(x)
            deck[1].append(y)

def player_deal():
    tile = random.randint(0,len(deck[0])-1)
    player_hand[0].append(deck[0][tile])
    player_hand[1].append(deck[1][tile])
    deck[0].pop(tile)
    deck[1].pop(tile)
    for i in range(0,len(player_hand[0])):
        print(i+1,":",player_hand[1][i],"of",player_hand[0][i])


def player_play_game(return_from_stand):
    global ask_player
    ask_player = ""
    while not ask_player:
        player_bust()
        ask_player = input("Do you want to hit or stand? ( H / S )\n").upper().strip()
        check_hand()
        print(player_total)
        if ask_player == "H":
            player_deal()
            player_play_game(True)
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
        player_unsure = player_play_game(False)
        if player_unsure != True:
            player_play_game(True)

def player_bust():
    global ask_player
    if player_total >= 21:
        ask_player = False

#welcome_msg
print("---------------------------------")
print("_Welcome to tiles and turbulence_")
print("---------------------------------")

#main program
build_deck()
player_deal()
player_play_game(True)