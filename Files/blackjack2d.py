# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:34:45 2023

@author: arun.rameshbabu
"""

import cards
import blkjack_file_fxns as bff

def title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print("Enter 'x' for bet to exit")
    print()


def get_starting_money():
    while True:
        money = float(input("Amount: "))
        if money < 5 or money > 10000:
            print("Invalid amount. Must be atleast 5 to 10000")
        else:
            return money

def get_bet(start_money):
    while True:
        bet = input("Bet amount: ")
        print()
        
        if bet.lower() == 'x':
            return 'x'
        
        bet = float(bet)
        if bet < 5:
            print("The minimum bet is 5.")
        elif bet > 1000:
            print("The maximum bet is 1000")
        elif bet > start_money:
            print("You don't have enough money to make that bet.")
        else:
            return bet


def start_game():
    deck = cards.get_deck()
    cards.shuffle(deck)
    
    dealer_hand = cards.get_empty_hand()
    player_hand = cards.get_empty_hand()
    
    return deck, player_hand, dealer_hand


def display_hand(hand, title):
    print(title.upper())
    for card in hand:
        print(f"{card[0]} of {card[1]}")
    print()


def deal(deck, player_hand, dealer_hand):
    cards.add_card(player_hand, cards.deal_card(deck))
    cards.add_card(player_hand, cards.deal_card(deck))
    #cards.add_card(player_hand, cards.deal_card(deck))
    
    show_card = cards.deal_card(deck)
    cards.add_card(dealer_hand, show_card)
    
    display_hand([show_card], "DEALER'S SHOW CARD: ")
    display_hand(player_hand, "YOUR CARDS: ")
    print(f"Points: {cards.get_points(player_hand)}")

    
def player_turn(deck, player_hand):
    while True:
        choice = input("Hit or stand? (h/s): ")
        print()
        
        if choice == 'h':
            cards.add_card(player_hand, cards.deal_card(deck))
            display_hand(player_hand, "YOUR CARDS: ")
            
            if cards.get_points(player_hand) > 21:
                break
        elif choice == 's':
            break
        else:
            print("Not a valid choice. Please try again")


def dealer_turn(deck, player_hand, dealer_hand):
    if cards.get_points(player_hand) <= 21:
        while cards.get_points(dealer_hand) < 17:
            cards.add_card(dealer_hand, cards.deal_card(deck))
    display_hand(dealer_hand, "DEALER'S CARDS: ")


def play(deck, player_hand, dealer_hand):
    if cards.get_points(player_hand) == 21 and len(player_hand) == 2:
        return
    if cards.get_points(dealer_hand) == 21 and len(dealer_hand) == 2:
        return
    
    player_turn(deck, player_hand)
    dealer_turn(deck, player_hand, dealer_hand)
    

def det_outcome(player_hand, dealer_hand, money, bet):
    player_pts = cards.get_points(player_hand)
    dealer_pts = cards.get_points(dealer_hand)
    
    outcome = ""
    
    if player_pts > 21:
        outcome = "Sorry. You're busted. Loser!"
        money -= bet
    elif dealer_pts > 21:
        outcome = "Yay! The dealer busted. Great Job!"
        money +=bet
    else:
        if player_pts == 21 and len(player_hand) == 2:
            if dealer_pts == 21 and len(dealer_hand) == 2:
                outcome = "Dang it, dealer has a blackjack too. You push"
            else:
                outcome = "Blackjack. You win! Awesome!"
                money += bet * 1.5
        elif player_pts > dealer_pts:
            outcome = "Hooray! You win!"
            money += bet
        elif player_pts == dealer_pts:
            outcome = "Meh, you push"
        elif player_pts< dealer_pts:
            if dealer_pts == 21 and len(dealer_hand) == 2:
                outcome = "Dealer got a Blackjack! You are a loser"
            else:
                outcome = "Sorry, you lose"
            money -= bet
        else:
            outcome = "This should not happen"
    
    return money, outcome


def disp_outcome(player_hand, dealer_hand, money, outcome):
    print(f"YOUR POINTS: {cards.get_points(player_hand)}")
    print(f"DEALER'S POINTS: {cards.get_points(dealer_hand)}")
    print()
    print(outcome)
    print(f"Money: {money}\n")
    
    
def main():
    title()
    
    #money = get_starting_money()
    money = bff.read_money()
    print(f"Money: {money}")
    
    while True:
        bet = get_bet(money)
        if bet == 'x':
            break
        
        deck, player_hand, dealer_hand = start_game()
        deal(deck, player_hand, dealer_hand)
        play(deck, player_hand, dealer_hand)
        money, outcome = det_outcome(player_hand, dealer_hand, money, bet)
        disp_outcome(player_hand, dealer_hand, money, outcome)
        bff.write_money(money)
        if money <= 0:
            print("You are out of money.")
            buy = input("Would you like to buy more chips? (y/n): ")
            if buy.lower() == 'y':
                money = get_starting_money()
                print(f"Money: {money}")
                bff.write_money(money)
            else:
                break
    
    print("Bye!")


if __name__ == '__main__':
    main()
            