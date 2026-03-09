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
player_amount_input = ("")
possible_player_amounts = ("1","2","3","4","5")
player_amount = ()

#functions
def number_of_players():
    player_amount = ""
    while not player_amount:
        player_amount_input = input("How many players would you like at the table?\n1-5\n").strip()
        if player_amount_input not in possible_player_amounts:
            print("please enter a number\n1-5")
            continue
        else:
            player_amount = player_amount_input
    return player_amount

def build_deck():
    for x in SUITS:
        print("Adding:",x,"suit.")
        for y in NUMBERS:
            deck[0].append(x)
            deck[1].append(y)
            print("Card:",y,"of",x,"added")
        print("Done")

def player_deal():
    card = random.randint(0,len(deck[0])-1)
    player_hand[0].append(deck[0][card])
    player_hand[1].append(deck[1][card])
    deck[0].pop(card)
    deck[1].pop(card)

#welcome_msg
print("_________________________________")
print("_Welcome to tiles and turbulence_")
print("_________________________________")

#main program
build_deck()
player_deal()
print(player_hand)