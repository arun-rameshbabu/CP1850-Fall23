# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:32:33 2023

@author: arun.rameshbabu
"""

import baseball_file_ops as bfo

POSITIONS = ['C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P'] 

def seperator():
    print(75*'*')

def title():
    print('\t\t\t\t\t\tBaseball Team Manager')
    
def menu():
    print('MENU OPTIONS')
    print('1 – Display lineup')
    print('2 – Add player')
    print('3 – Remove player')
    print('4 – Move player')
    print('5 – Edit player position')
    print('6 – Edit player stats')
    print('7 - Exit program\n')

def display_pos():
    print('POSITIONS')
    print('C, 1B, 2B, 3B, SS, LF, CF, RF, P')
    

def get_position():
    while True:
        position = input("Position: ").upper()
        if position in POSITIONS:
            return position
        else:
            print("Invalid position. Try again.")
            display_pos()


def get_at():
    while True:
        at_bats = int(input('At bats: '))
        if at_bats < 0 or at_bats > 600: # I chose 600 expecting a healthy career over 10 years
            print('Invalid entry. Please enter a value between 0 and 600')
        else:
            return at_bats


def get_hits(at_bats):
    while True:
        hits = int(input('Hits: '))
        if (hits < 0) or (hits > at_bats):
            print(f'Invalid entry. Please enter a value between 0 and {at_bats}')
        else:
            return hits

        

def add_player(players_list):
    name = input("Name: ")
    position = get_position()
    at_bats = get_at()
    hits = get_hits(at_bats)
    avg = hits / at_bats
    player = [name, position, at_bats, hits, avg]
    players_list.append(player)
    print(f'{name} was added. \n')
    

def display_players(players_list):
    if players_list == None:
        print("There are no players currently with us.")
    else:
        print("\tPlayer\t\tPOS\tAB\tH\tAVG")
        print('-------------------------------------------------------------')
        for i, player in enumerate(players_list, start=1):
            print('{}\t{}\t\t\t{}\t{}\t{}\t{}'.format(i, player[0][:3], player[1], player[2], player[3], player[4]))
        print()


def get_lineup_num(players_list, message):
    while True:
        number = int(input(message))
        if number < 1 or number > len(players_list):
            print('Invalid player number. Please select again.')
        else:
            return number
    

def move_player(players_list):
    #old_num = int(input("Current lineup number: ")) - 1
    #new_num = int(input('New lineup number: ')) - 1
    old_num = get_lineup_num(players_list, 'Current Lineup Number: ')
    print(f'{players_list[old_num-1][0]} was selected.')
    new_num = get_lineup_num(players_list, 'New Lineup Number: ')
    player = players_list.pop(old_num - 1)
    players_list.insert(new_num - 1, player)
    print(f'{player[0]} was moved.\n')


def edit_player_stats(players_list):
    number = get_lineup_num(players_list, 'Lineup Number: ')
    player = players_list[number - 1]
    print(f'You selected {player[0]} POS={player[1]} AB={player[2]} H={player[3]} AVG={player[4]}')
    at_bats = get_at()
    hits = get_hits(at_bats)
    player[2] = at_bats
    player[3] = hits
    player[4] = hits / at_bats
    print(f'{player[0]} was updated.\n')


def edit_player_pos(players_list):
    number = get_lineup_num(players_list, 'Lineup Number: ')
    player = players_list[number - 1]
    print(f'You selected {player[0]} POS={player[1]}')
    pos = get_position()
    player[1] = pos
    print(f'{player[0]} was updated.\n')


def delete_player(players_list):
    number = get_lineup_num(players_list, 'Player to delete (number): ')
    player = players_list.pop(number-1)
    print(f'{player[0]} was deleted.\n')


def main():
    # players = [['Joe', 'P', 10, 2, 0.200],
    #            ['Tom', 'SS', 11, 4, 0.364],
    #            ['Ben', '3B', 9, 3, 0.333]]
    players = bfo.read_file()
    seperator()
    title()
    menu()
    display_pos()
    seperator()
    
    while True:
        menu_option = int(input("Menu option: "))
        
        if menu_option == 1:
            display_players(players)
        elif menu_option == 2:
            add_player(players)
            bfo.write_file(players)
        elif menu_option == 3:
            delete_player(players)
            bfo.write_file(players)
        elif menu_option == 4:
            move_player(players)
            bfo.write_file(players)
        elif menu_option == 5:
            edit_player_pos(players)
            bfo.write_file(players)
        elif menu_option == 6:
            edit_player_stats(players)
            bfo.write_file(players)
        elif menu_option == 7:
            print("Bye!")
            break
        else:
            print('Not a valid option. Do better when you try again! \n')
            menu()
            

if __name__ == '__main__':
    main()
            