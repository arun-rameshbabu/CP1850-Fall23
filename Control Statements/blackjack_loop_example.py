# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:40:24 2023

@author: arun.rameshbabu
"""

print("BLACKJACK!")
print("Blackjack payout is 3:2")
print("Enter 'x' for bet to exit")

start_money = float(input("Starting money: \t"))
while (start_money > 0):
    bet_amt = input("\nBet amount: ")
    if bet_amt == 'x':
        break
    else:
        bet_amt = float(bet_amt)
        bwpl = input ("Blackjack, win, push, or lose? (b/w/p/l): ")
        if bwpl == 'b':
            start_money = start_money + (1.5 * bet_amt)
            print(f"Money: {start_money}")
        elif bwpl == 'w':
            start_money = start_money + bet_amt
            print(f"Money: {start_money}")
        elif bwpl == 'p':
            start_money = start_money
            print(f"Money: {start_money}")
        elif bwpl == 'l':
            start_money = start_money - bet_amt
            print(f"Money: {start_money}")

print("Bye!")
