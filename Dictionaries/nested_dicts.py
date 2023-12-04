# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 09:26:35 2023

@author: arun.rameshbabu
"""

characters = {'Arun': {'Class': 'Knight', 'Weapon':'Lance', 'City':'Rivendale',
                       'HPPotions': 5, 'MPPotions': 10},
              'Yennifer': {'Class': 'Wizard', 'Weapon':'Dagger', 'City':'Allentown',
                           'HPPotions': 10, 'MPPotions':2, 'Unique_Skill':'Dark Magic'}}
weapon = characters['Arun']['Weapon']
characters['Arun']['Unique_Skill'] = 'Rolling Bash'
characters['Arun'].pop('Unique_Skill')
characters['Yennifer'].get('Weapon')
characters['Yennifer'].get('Armor', 'Cloth')
characters['Arun']['Regular_Skills'] = ['Bash', 'Taunt', 'Stab']
characters['Arun']['Regular_Skills']
characters['Arun']['Regular_Skills'][0]
