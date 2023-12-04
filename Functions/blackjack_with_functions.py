# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 10:03:56 2023

@author: arun.rameshbabu
"""

def print_title():
    return "BLACKJACK! \nBlackjack payout is 3:2\nEnter 'x' for bet to exit"

def start_money():
    start_mon = int(input("\nStarting money:\t"))
    if start_mon < 5:
        print("The minimum amount of starting money should be 5")
        start_mon = start_money()
    elif start_mon > 10000:
        print("The maximum amount of starting money should be 10000")
        start_mon = start_money()
    return start_mon

def bet_amount():
    bet_amt = input("\nBet amount: ")
    return bet_amt

def bwpl():
    import random
    num = random.randint(1, 100)
    if num > 95:
        return 'b'
    elif num > 58:
        return 'w'
    elif num > 49:
        return 'p'
    else:
        return 'l'

def main():
    print(print_title())
    start_mon = start_money()
    while (start_mon > 0):
        bet_amt = bet_amount()
        if bet_amt == 'x':
            return None
        elif float(bet_amt) < 5:
            print("The minimum bet should be 5")
        elif float(bet_amt) > 1000:
            print("The maximum bet should be 1000")
        elif float(bet_amt) > start_mon:
            print (" You do not have enough money for this bet. Try a lower number")
        else:
            bet_amt = float(bet_amt)
            bwpl_var = bwpl()
            if bwpl_var == 'b':
                start_mon = start_mon + (1.5 * bet_amt)
                print('You got a blackjack!.\nMoney: {:.1f}'.format(start_mon))
            elif (bwpl_var == 'w'):
                start_mon = start_mon + (1 * bet_amt)
                print('You won.\nMoney: {:.1f}'.format(start_mon))
            elif (bwpl_var == 'p'):
                start_mon = start_mon
                print('You pushed.\nMoney: {:.1f}'.format(start_mon))
            else:
                start_mon = start_mon - (1 * bet_amt)
                print('You lost.\nMoney: {:.1f}'.format(start_mon))
                
if __name__ == '__main__':
    main()
    print('Bye!')