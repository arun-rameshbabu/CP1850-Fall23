# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:57:07 2023

@author: arun.rameshbabu
"""

def test1(a, input2='Radio', z=5):
    """
    

    Parameters
    ----------
    a : List
        A list of elements.
    input2 : Str
        A string element.
    z : num
        A numeric element.

    Returns
    -------
    input_computed : str
        String + str(100).
    some_var : num
        A numeric object.

    """
    print(a)
    input_computed = input2 + str(100)
    some_var = z+z
    return input_computed, some_var

out1, out2 = test1(a=[2,3,4], input2='Name', z=6)
test1([2,3,4],'Name', 6)
list1 = [2,3,4]
str1 = 'Name'
int1 = 6
test1(list1, str1, int1)
test1(list1)

# nested loops
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for row in matrix:
    print(row)
    for num in row:
        print(num)
        
file_read_handle = open('C:/Users/arun.rameshbabu/Desktop/class_review.txt', 'r')
read_input = file_read_handle.read()
file_read_handle.close()

with open('C:/Users/arun.rameshbabu/Desktop/class_review.txt', 'r') as fh:
    print(fh.read())

file_write_handle = open('C:/Users/arun.rameshbabu/Desktop/class_review_w.txt', 'w')
file_write_handle.write(read_input)
file_write_handle.close()

with open('C:/Users/arun.rameshbabu/Desktop/class_review_ww.txt', 'w') as fwh:
    fwh.write(read_input)
    
def read_file(filename):
    with open(filename, 'r') as frh:
        print(frh.read())