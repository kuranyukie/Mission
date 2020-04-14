#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 12:56:02 2018

@author: Yukie
"""

# in class 1
n = 0
while (n < 9):
    if n % 2 == 0:
        print("The count is:", n)
    n += 1
print("Good bye!")
    
# in class 2
for n in range(10):
    if n % 2 == 1:
        print(n)
        
# in class 3
def print_range():
    for num in range(5,21,5):
        print(num, end=' ')
print_range()