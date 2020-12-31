#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a troll is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")


def valid_input(prompt):
    while True:
        response = input(prompt).lower()
        if '1' == response:
            break
        elif '2' == response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def play_choice(prompt):
    while True:
        response = input(prompt).lower()
        if 'y' in response:
            break
        elif 'n' in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def win():
    print_pause("As the " + enemy + " moves to attack,"
                " you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you"
                " brace yourself for the attack.")
    print_pause("But the " + enemy + " takes one look at your shiny new toy"
                " and runs away!")
    print_pause("You have rid the town of the " + enemy + "."
                " You are victorious!")
    type = play_choice("Would you like to play again? (y/n)")
    if type == 'y':
        print_pause("Excellent! Restarting the game ...")
        items = []
        play_game(items)
    elif type == 'n':
        print_pause("Thanks for playing! See you next time")


def run():
    print_pause("You run back into the field. Luckily,"
                " you don't seem to have been followed.")
    play_game(items)


def defeat():
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the " + enemy)
    print_pause("You have been defeated!")
    type = play_choice("Would you like to play again? (y/n)")
    if type == 'y':
        print_pause("Excellent! Restarting the game ...")
        items = []
        play_game(items)
    elif type == 'n':
        print_pause("Thanks for playing! See you next time.")


def door(items):
    if "sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out steps"
                    " a " + enemy + ".")
        print_pause("Eep! This is the " + enemy + "'s house!")
        print_pause("The " + enemy + " attacks you!")
        choice = valid_input("Would you like to (1) fight or (2) run away?")
        if choice == '1':
            win()
        elif choice == '2':
            run()
    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out steps"
                    " a " + enemy + ".")
        print_pause("Eep! This is the " + enemy + "'s house!")
        print_pause("The " + enemy + " attacks you!")
        print_pause("You feel a bit under-prepared for this,"
                    " with only having a tiny dagger.")
        choice = valid_input("Would you like to (1) fight or (2) run away?")
        if choice == '1':
            defeat()
        elif choice == '2':
            run()


def cave(items):
    if 'sword' in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause(" It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        play_game(items)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    " take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")
        play_game(items)


def play_game(items):
    global enemy
    enemy = random.choice(['troll', 'pirate'])
    print_pause("Enter 1 to knock on the door of the house.")
    choice = valid_input("Enter 2 to peer into the cave.\n"
                         "What would you like to do?")
    if choice == '1':
        door(items)
    elif choice == '2':
        cave(items)


if __name__ == "__main__":
    items = []
    intro()
    play_game(items)


# In[ ]:




