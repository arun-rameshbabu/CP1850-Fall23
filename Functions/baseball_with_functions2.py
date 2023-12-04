# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:42:38 2023

@author: arun.rameshbabu
"""

def seperator(character = '='):
    """
    Creates a seperator

    Parameters
    ----------
    character : string
        Seperator character.

    Returns
    -------
    String
        A line with seperators.

    """
    return 50*character


def title(default = 'Baseball Team Manager') -> str:
    """
    

    Parameters
    ----------
    default : TYPE, optional
        DESCRIPTION. The default is 'Baseball Team Manager'.

    Returns
    -------
    default : TYPE
        DESCRIPTION.

    """
    return default

def menu_display():
    """
    

    Returns
    -------
    str
        DESCRIPTION.

    """
    return "MENU OPTIONS\n 1 - Calculate batting average\n 2 - Exit program"

def batting_avg(hits: int, at_hits: int) -> float:
    """
    

    Parameters
    ----------
    hits : TYPE
        DESCRIPTION.
    at_hits : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return hits/at_hits


def main():
    print(seperator())
    print(title())
    print(menu_display())
    print(seperator())
    option = input("Menu option: ")
    while (option != '2'):
        if option =='1':
            print('Calculate batting average...')
            at_bats = int(input('Official number of at bats: '))
            hits = int(input('Number of hits: '))
            avg = batting_avg(hits=hits, at_hits=at_bats)
            print("Batting average: {:.3f}".format(avg))
            option = input('\nMenu option: ')
        else:
            print('Not a valid option. Please try again.')
            option = input('\nMenu option: ')
    print("Bye!")

if __name__ == '__main__':
    main()
    """
    For test, checking the following combinations 
    1, 4, 0.25
    2, 4, 0.50
    3, 4, 0.75
    4, 4, 1
    """