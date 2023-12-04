# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:43:05 2023

@author: arun.rameshbabu
"""

instructors = [["Arun", "Cool", "Top Class", "VW", 2020],
               ["Unhappy Guy", "Tardy", "Cancelled Class", "Audi", 2023],
               ["Mike", "Cool", "Good Class", "BMW", 2022]]

instructors[0][3]
instructor = ["Brad", "Good", "Okay Class", "Honda", 2022]
instructors.append(instructor)
print(instructors)

for instructor in instructors:
    for element in instructor:
        print(element, end = ' | ')
    print()