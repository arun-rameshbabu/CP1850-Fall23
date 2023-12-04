# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 08:35:12 2023

@author: arun.rameshbabu
"""
def get_password():
    while True:
        passwrd = input("Enter password:\t")
        if len(passwrd) < 8:
            print("Password must be 8 characters or more")
        else:
            conditions = {'decimal': 0, 'uppercase':0}
            for c in passwrd:
                if c.isdecimal():
                    conditions['decimal'] += 1
                elif c.isupper():
                    conditions['uppercase'] += 1
            if (conditions['decimal'] > 0) and (conditions['uppercase'] > 0):
                return passwrd
            else:
                print("Password must be 8 characters or more \nwith at least one digit and one uppercase letter.")


def get_name():
    while True:
        name = input("Enter full name:\t")
        if len(name.split()) > 1:
            password = get_password()
            print(f"Hi {name.split()[0]}, thanks for creating an account")
            return name, password
        else:
            print("You must enter your full name")
            
if __name__=='__main__':
    user_name, user_password = get_name()