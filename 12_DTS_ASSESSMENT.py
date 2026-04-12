#file_name: 12_DTS_ASSESSMENT.py
#author: Charlie Holmes
#start_date: 9/3/26

#____Libraries____
import random  # Used to pick random tiles from the deck
import time    # Used to add delays/pauses in the game
import sys     # Used to print the story_text() character by character


#____Constants____
# The four suits in this deck
SUITS = ["kiwis", "pies", "paua", "gumboots"]

# Each card name and its point value
NUMBERS = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}


#____Variables____
# The deck is stored as two lists: [suits, numbers]
deck = [[], []]

# The dealer's hand, same structure as the deck
dealer_hand = [[], []]

# The player's hand, same structure as the deck
player_hand = [[], []]

# Tracks the player's current total score
player_total = 0


#____Functions____

def check_hand():
    # Recalculates the player's total score from their current hand
    global player_total
    player_total = 0

    # Add up the value of every card in the player's hand
    for i in player_hand[1]:
        player_total += NUMBERS[i]

    # If the player went over 21, reset and restart their turn
    if player_total > 21:
        print("Unfortunate, you got over 21! try again\n")
        delete_deck()
        build_deck()
        time.sleep(3)
        return ask_player

    # If the player hit exactly 21, move on to the dealer's turn
    if player_total == 21:
        print("Nice job! You got 21!\n")
        time.sleep(3)
        dealer_ai()
        main_story()


def build_deck():
    # Builds a deck of “cards” by combining every suit with every card number
    for x in SUITS:
        for y in NUMBERS:
            deck[0].append(x)   # Add the suit
            deck[1].append(y)   # Add the matching card number


def delete_deck():
    # Resets the deck and player's hand back to empty lists
    global deck
    global player_hand
    player_hand = [[], []]
    deck = [[], []]


def player_deal():
    # Picks a random tile from the deck and adds it to the player's hand
    tile = random.randint(0, len(deck[0]) - 1)

    player_hand[0].append(deck[0][tile])   # Add the suit to player's hand
    player_hand[1].append(deck[1][tile])   # Add the card number to player's hand

    # Remove the dealt tile from the deck so it can't be picked again
    deck[0].pop(tile)
    deck[1].pop(tile)

    # Clear the screen with blank lines, then show the player's current hand
    print("\n" * 27)
    print("Player's hand:")
    for i in range(0, len(player_hand[0])):
        print(i + 1, ":", player_hand[1][i], "of", player_hand[0][i])


def player_play_game():
    # Runs the player's turn they can hit or stand
    global ask_player
    ask_player = 0

    while not ask_player:
        check_hand()

        # Ask the player what they want to do
        ask_player_string = input("Do you want to hit or stand? ( H / S )\n").upper().strip()
        ask_player = ask_player_string[:1]
        check_hand()

        if ask_player == "H":
            # Player chose to draw another tile
            player_deal()

        elif ask_player == "S":
            # Player chose to stop / confirm they are sure
            are_you_sure_string = input("Are you sure? ( Y / N )\n").upper().strip()
            are_you_sure = are_you_sure_string[:1]
            if are_you_sure == "Y":
                # Player confirmed, move to dealer's turn
                dealer_ai()
            elif are_you_sure == "N":
                # Player changed their mind, go back
                return False
            else:
                print("Please try again")
                return are_you_sure
        else:
            print("Please try again")

        # If the player was unsure, loop their turn again
        player_unsure = player_play_game()
        if player_unsure != True:
            player_play_game()


def dealer_check_hand():
    # Checks the dealer's total score from their current hand
    global dealer_total
    dealer_total = 0

    for i in dealer_hand[1]:
        dealer_total += NUMBERS[i]


def dealer_ai():
    # Runs the dealer's turn the dealer keeps drawing until they beat the player
    global dealer_total
    dealer_total = 0

    while dealer_total < player_total:
        # Pick a random tile and add it to the dealer's hand
        tile = random.randint(0, len(deck[0]) - 1)

        dealer_hand[0].append(deck[0][tile])
        dealer_hand[1].append(deck[1][tile])

        # Remove the tile from the deck
        deck[0].pop(tile)
        deck[1].pop(tile)

        # Update the dealer's total
        dealer_check_hand()

    # Print the dealer's final hand
    print("Kiwi's hand:")
    for i in range(0, len(dealer_hand[0])):
        print(i + 1, ":", dealer_hand[1][i], "of", dealer_hand[0][i])

    # Check who won and print message
    if player_total > dealer_total:
        print("Congrats! you got more than the Kiwi!\n You are onto the next section\n")
        finished_story()

    elif dealer_total > 21:
        # Dealer went bust / player wins
        print("Nice! The Kiwi went over 21 and you won!\n")
        finished_story()

    elif dealer_total == player_total:
        # It's a tie / reset and play again
        print("Wow! you got the same as the Kiwi!\n Unfortunately, you dont win or lose! play again.\n")
        delete_deck()
        build_deck()
        player_play_game()
        return True

    else:
        # Dealer scored higher / player loses, reset and play again
        print("Ah! Unfortunate, the Kiwi got more than you!\n play again\n")
        delete_deck()
        build_deck()
        player_play_game()
        return True


def story_text(text, delay=0.03):
    # Prints text one character at a time to create a slow text effect
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)   # Small pause between each character
    return ""


def main_story():
    # Runs the intro story before the card game begins
    player_pathway_loop = 0

    # Walks the player through the intro dialogue
    input(story_text("For every piece of dialogue in this story, press enter to continue\n"))
    input(story_text("It was a cold and stormy night, you wake up in a forest in a plane crash.\n"))
    input(story_text("You find yourself with no food, water, or sleeping device.\n"))
    input(story_text("Eventually you stumble through the woods and see a sign...\n"))
    input("'The Brooklyn windmill!'\n")
    input(story_text("*but how do i get there...* you ask yourself\n"))
    input(story_text("A small kiwi exits its nest and waddles towards you.\n"))
    input(story_text("As it creeps closer to examine you, you stay as still as possible to not frighten the creature\n"))
    input(story_text("'HELLO THERE MATE' The somehow talkative kiwi exclaims\n"))
    print(story_text("'Well how'd you get round here, this is Greenstone Grove, no one been round here since the mythical ages'\n"))

    # Let the player choose how they respond to the kiwi
    while player_pathway_loop == 0:
        player_pathway_string = input("CHOOSE YOUR NEXT WORDS:\n'What's the mythical ages?'\nor\n'You can talk?'\n( 1 or 2 )\n").strip().upper()
        player_pathway = player_pathway_string[:1]
        if player_pathway == "1":
            # Player asks about the mythical ages
            input(story_text("'Well back in about 2020, there was a thing called lockdown.' \nThe talkative kiwi says.\n"))
            input(story_text("'Whilst everyone was stuck in there houses us kiwis started to flourish and made our own land out the back of brooklyn called Greenstone Grove'\n"))
            input(story_text("'Well that's nice but how do i get back to the CBD? I'm kind of stuck out here without food or water.' You say \n"))
            input(story_text("'The food issue is not a problem out here, we have tiles and tiles of food and supplies, you might just have to play for it.'The kiwi says in a less welcoming tone.\n"))
            player_pathway_loop = 1   # Exit the choice loop

        elif player_pathway == "2":
            # Player asks how the kiwi can talk
            input(story_text("'Back in the mythical times of 2020 as everyone was in their houses we made this little place out here called Greenstone Grove,\n "))
            input(story_text("'Where we evolved past humans, but somehow kept the classic kiwi shape.'\n"))
            input(story_text("'Well how do I get back to the CBD already, I'm kinda starving and haven't learnt how to forage.' You say\n"))
            input(story_text("'To get back to the CBD I can't really help you with that, \nbut the food isn't an issue, we have tiles and tiles of food and supplies if needs be,\n 'You might just have to play for it.'The kiwi says in a less welcoming tone.\n"))
            player_pathway_loop = 1   # Exit the choice loop

        else:
            print("Please enter 1 or 2")
            continue


def finished_story():
    # Runs the ending story after the player wins the card game
    finished_story_loop = 0

    # Play out the closing dialogue
    input(story_text("'Well good game, you bested me, now to stick to my promise, you can keep all the food and supplies you played with.'\n"))
    input(story_text("'Just please promise you will come visit every now and then, we would love to know what the CBD is up to now'\n"))
    input(story_text("'Oh dont worry i'll come round every couple months and update you guys.' You say\n"))
    input(story_text("'Oh well that would be wonderful, I wish you well on your adventures and good game sir'\n"))
    input(story_text("'Unless you want to stay here and learn more about how we live down here?' The kiwi says with a hopeful tone.\n"))

    # Let the player choose their final ending
    while finished_story_loop == 0:
        player_final_choice_string = input("CHOOSE YOUR PATH:\n1:Stay with the Kiwis\nor\n2:Go back to the CBD\n( 1 or 2 )\n").strip().upper()
        player_final_choice = player_final_choice_string[:1]
        if player_final_choice == "1":
            # Player chooses to stay with the kiwis
            input(story_text("'Actually I think I might stay.'\n"))
            input(story_text("'Well that's great, I'll get your bed ready now.'\n"))
            finished_story_loop = 1   # Exit the choice loop
            que_final()

        elif player_final_choice == "2":
            # Player chooses to go back to the CBD
            input(story_text("'Well it was nice seeing you guys, I'll check back every now and then.'\n"))
            input(story_text("'Be sure that visit is soon!'\n"))
            finished_story_loop = 1   # Exit the choice loop
            que_final()

        else:
            print("Please enter 1 or 2")
            continue


def que_final():
    # Shows the "THANKS FOR PLAYING" screen and asks if the player wants to restart
    time.sleep(2)

    # Clear the screen with blank lines
    print("\n" * 31)
    time.sleep(0.5)

    # Print the big ASCII art "THANKS FOR PLAYING" banner
    print(r"""            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~                                                                  ~
            ~     _____ _   _    _    _   _ _  ______    _____ ___  ____       ~
            ~    |_   _| | | |  / \  | \ | | |/ / ___|  |  ___/ _ \|  _ \      ~
            ~      | | | |_| | / _ \ |  \| | ' /\___ \  | |_ | | | | |_) |     ~
            ~      | | |  _  |/ ___ \| |\  | . \ ___) | |  _|| |_| |  _ <      ~
            ~     _|_| |_| |_/_/ _ \_\_|_\_|_|\_\____/__|_|   \___/|_| \_\     ~
            ~    |  _ \| |      / \ \ \ / /_ _| \ | |/ ___|                     ~
            ~    | |_) | |     / _ \ \ V / | ||  \| | |  _                      ~
            ~    |  __/| |___ / ___ \| |  | || |\  | |_| |                     ~
            ~    |_|   |_____/_/   \_\_| |___|_| \_|\____|                     ~
            ~                                                                  ~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

    # Ask the player if they want to play again
    restart_loop = 1
    while restart_loop == 1:
        restart_string = input("WOULD YOU LIKE TO RESTART?(y / n)\n").strip().lower()
        restart = restart_string[:1]
        if restart == "y":
            main_game()   # Restart the game from the beginning
        if restart == "n":
            quit()        # Close the program
        else:
            restart_loop = 0
            continue


#____Welcome Message____
#Shows a message before starting the game
print("---------------------------------")
print("_Welcome to tiles and turbulence_")
print("---------------------------------")
time.sleep(3)
print("\n" * 16)
input("To play you must draw tiles one by one. But make sure you dont go over 21!\npress enter to continue")
input("To win you must get less than 22 points and beat out the opponent\npress enter to continue")
input("KEY:\nK , Q , J  = 10\nA = 1\n")


# --- Main Program ---
def main_game():
    # Entry point for the game — runs the story then starts the card game
    main_story()
    delete_deck()
    build_deck()
    player_play_game()

# Start the game
main_game()