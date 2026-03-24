#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#libraries
import random
import time
import sys


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
        time.sleep(3)
        return ask_player

    if player_total == 21:
        print("Nice job! You got 21!\n")
        time.sleep(3)
        dealer_ai()

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
    while dealer_total < player_total:
        tile = random.randint(0,len(deck[0])-1)
        dealer_hand[0].append(deck[0][tile])
        dealer_hand[1].append(deck[1][tile])
        deck[0].pop(tile)
        deck[1].pop(tile)
        dealer_check_hand()
    print("Dealer hand:")
    for i in range(0,len(dealer_hand[0])):
        print(i+1,":",dealer_hand[1][i],"of",dealer_hand[0][i])
    if dealer_total > 21:
        print("Nice! The dealer went over 21 and you won!\n")
        player_play_game(True)
    elif dealer_total > player_total:
        print("Congrats! you got more than the dealer!\n You are onto the next section\n")
        player_play_game(False)
        return False
    if dealer_total == player_total:
        print("Wow! you got the same as the dealer!\n Unfortunately, you dont win or lose! play again.\n")
        player_play_game(True)
        return True
    else:
        print("Ah! Unfortunate, the dealer got more than you!\n play again\n")
        player_play_game(True)
        return True

def story_text(text, delay = 0.0000003):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    return ""

def main_story():
    player_pathway_loop = 0
    input(story_text("For every piece of dialogue in this story, press enter to continue\n"))
    input(story_text("It was a cold and stormy night, you wake up in a forest in a plane crash.\n"))
    input(story_text("You find yourself with no food, water, or sleeping device.\n"))
    input(story_text("Eventually you stumble through the woods and see a sign...\n"))
    input("'The Brooklyn windmill!'\n")
    input(story_text("*but how do i get there...* you ask yourself\n"))
    input(story_text("A small kiwi exits its nest and waddles towards you.\n"))
    input(story_text("As it creeps closer to examine you, you stay as still as possible to not frighten the creature\n"))
    input(story_text("'HELLO THERE MATE' The somehow talkitive kiwi exclaims\n"))
    print(story_text("'Well how'd you get round here, this is Greenstone Grove, no one been round here since the mythical ages'\n"))
    while player_pathway_loop == 0:
        player_pathway = input("CHOOSE YOUR NEXT WORDS:\n'What's the mythical ages?'\nor\n'You can talk?'\n( 1 or 2 )\n").strip().upper()
        if player_pathway == "1":
            input(story_text("'Well back in about 2020, there was a thing called lockdown.' \nThe talkitive kiwi says.\n"))
            input(story_text("'Whilst everyone was stuck in there houses us kiwis started to flourish and made our own land out the back of brooklyn called Greenstone Grove'\n"))
            input(story_text("'Well that's nice but how do i get back to the CBD? I'm kind of stuck out here without food or water.' You say \n"))
            input(story_text("'The food issue is not a problem out here, we have tiles and tiles of food and supplies, you might just have to play for it.'The kiwi says in a less welcoming tone.\n"))
            player_pathway_loop = 1
        if player_pathway == "2":
            input(story_text("'Back in the mythical times of 2020 as everyone was in their houses we made this little place out here called Greenstone Grove,\n "))
            input(story_text("Where we evolved past humans, but somehow kept the classic kiwi shape.'\n"))
            input(story_text("'Well how do I get back to the CBD already, I'm kinda starving and haven't learn't how to forage.' You say\n"))
            input(story_text("'To get back to the CBD I can't really help you with that, \nbut the food isn't an issue, we have tiles and tiles of food and supplies if needs be,\n 'You might just have to play for it.'The kiwi says in a less welcoming tone.\n"))
            player_pathway_loop = 1
        else:
            print("Please enter 1 or 2")
            return player_pathway
    build_deck()
    player_play_game(True)

#welcome_msg
print("---------------------------------")
print("_Welcome to tiles and turbulence_")
print("---------------------------------")
time.sleep(3)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
input("To play you must draw tiles one by one. But make sure you dont go over 21!\npress enter to continue")
input("To win you must get less than 22 points and beat out the opponent\npress enter to continue")
input("KEY:\nK , Q , J  = 10\nA = 1\n")

#main program
main_story()