# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:13:26 2023

@author: arun.rameshbabu
"""

import random

def get_deck():
    deck=[]
    ranks=("Ace","2","3","4","5","6","7","8","9","10",
           "Jack","Queen","King")
    suits=("Clubs", "Diamonds", "Hearts", "Spades")
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank == "Jack" or rank == "Queen" or rank == "King":
                value = 10
            else:
                value = int(rank)
            card = [rank, suit, value]
            deck.append(card)
    
    return deck


def shuffle(deck_cards):
    random.shuffle(deck_cards)


def deal_card(deck_cards):
    card = deck_cards.pop()
    return card

def get_empty_hand():
    hand=[]
    return hand

def add_card(hand, card):
    hand.append(card)

def get_points(hand):
    points = 0
    aces = 0
    for card in hand:
        points += card[2]
        if card[0] == 'Ace':
            aces += 1
        
    if aces > 0 and points > 21:
        points = points - (aces * 10)
    if aces > 1 and points <= 11:
        points += 10
    return points
