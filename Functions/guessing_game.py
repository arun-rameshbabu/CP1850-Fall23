# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:28:37 2023

@author: arun.rameshbabu
"""

import random

def title():
    print("Guess the Number!")

def random_number(low, high):
    number = random.randint(low, high)
    return number

def get_guess():
    user_guess = int(input("Your guess: "))
    return user_guess

def game():
    low = random.randint(1,3)
    high = random.randint(9,11)
    print("I'm thinking of a number from {} to {}\n".format(low, high))
    game_number = random_number(low, high)
    count = 1
    choice = 'y'
    while choice != 'n' :
        user_guess = get_guess()
        if user_guess > game_number:
            print("Too high")
            count += 1
        elif user_guess < game_number:
            print("Too low.")
            count += 1
        else:
            print("You guessed it in {} tries \n".format(count))
            choice = input("Would you like to play again? (y/n): ")

def main():
    title()
    game()
    print("\nBye!")


if __name__ == '__main__':
    main()


        
        
    