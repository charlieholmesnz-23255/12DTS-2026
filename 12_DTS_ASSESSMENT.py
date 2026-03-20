#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#libraries
import random
import time

#constants
SUITS = ["kiwis","pies","paua","gumboots"]
NUMBERS = {"A" : 1,"2" : 2 , "3" : 3,"4" : 4,"5" : 5,"6" : 6,"7" : 7,"8" : 8,"9" : 9,"10" : 10,"J" : 10,"Q" : 10,"K" : 10}

#variables
deck = [[],[]]
dealer_hand = [[],[]]
player_hand = [[],[]]
player_total = 0

#functions
def check_hand():
    global player_total
    player_total = 0
    for i in player_hand[1]:
        player_total += NUMBERS[i]
    if player_total > 21:
        print("Unfortunate, you got over 21! try again\n")
        delete_deck()
        build_deck()
        # time.sleep(3)
        return ask_player

    if player_total == 21:
        print("Nice job! You got 21!\n")
        delete_deck()
        build_deck()
        # time.sleep(3)
        return ask_player

def build_deck():
    for x in SUITS:
        for y in NUMBERS:
            deck[0].append(x)
            deck[1].append(y)

def delete_deck():
    global deck
    global player_hand
    player_hand = [[],[]]
    deck = [[],[]]

def player_deal():
    tile = random.randint(0,len(deck[0])-1)
    player_hand[0].append(deck[0][tile])
    player_hand[1].append(deck[1][tile])
    deck[0].pop(tile)
    deck[1].pop(tile)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Player hand:")
    for i in range(0,len(player_hand[0])):
        print(i+1,":",player_hand[1][i],"of",player_hand[0][i])

def player_play_game(return_from_stand):
    global ask_player
    ask_player = 0
    while not ask_player:
        check_hand()
        ask_player = input("Do you want to hit or stand? ( H / S )\n").upper().strip()
        check_hand()
        print(player_total)
        if ask_player == "H":
            player_deal()
            player_play_game(True)
        elif ask_player == "S":
            are_you_sure = input("Are you sure? ( Y / N )\n").upper().strip()
            if are_you_sure == "Y":
                dealer_ai()
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
def dealer_check_hand():
    global dealer_total
    dealer_total = 0
    for i in dealer_hand[1]:
        dealer_total += NUMBERS[i]

def dealer_ai():
    global dealer_total
    dealer_total = 0
    while dealer_total < 21:
        if deck[0] == None:
            print("EMPTY DECK!!!!!!!!!!!!!!!!")
        else:
            print(deck)
            tile = random.randint(0,len(deck[0])-1)
            player_hand[0].append(deck[0][tile])
            player_hand[1].append(deck[1][tile])
            deck[0].pop(tile)
            deck[1].pop(tile)

#welcome_msg
print("---------------------------------")
print("_Welcome to tiles and turbulence_")
print("---------------------------------")

#main program
build_deck()
player_play_game(True)