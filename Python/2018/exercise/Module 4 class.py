#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:30:19 2018

@author: Yukie
"""

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
        }
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
        }

# add two cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out each city and full state name

for state, state_abbr in states.items():
    print(cities[state_abbr], state)
    
# ======================================================

# zip
seq = zip(['a','b','c'], [1,2,3])
ddict = {}
for k,v in seq:
    ddict[k] = v
print(ddict)

# create a mapping quickly
import string
dict_c = {k:v for (k,v) in zip(string.ascii_lowercase, range(1,27))}
print(dict_c)
a = list(dict_c.keys())
a.sort()
print(a)

dict1 = {k:v for (k,v) in zip(list1, list2)}

# dictionary comprehension
premier_province = {v:k for k,v in province_premier.items()} # reverse key and values

# set comprehension
B= {p for p in range(4,10)}
print(B, type(B))

# reverse a string
strr = 'abcd'
str1 = strr[::-1]
print(str1)
str1.reverse() # illegal

# ======================================================

n = 5
triangulars = []
for i in range(1,(n+1)):
    triangulars.append(sum(range(1,i+1)))
print(triangulars)

# ======================================================

# dict update
regional_capitals = {}
regional_capitals.update(state_capitals)
regional_capitals.update(provincial_capitals)

# 51304

desired_weight, weights = 4, set([1, 2, 4, 5])
desired_weight, weights = 13, set([1, 3, 15])
minabs = 100
for i in weights:
	if (desired_weight - i < minabs) and (desired_weight >= i):
		minabs = desired_weight - i
		actual_weight = i
weights.remove(actual_weight)
print(actual_weight, weights)

# 71413

sent = 'hello. my name is Joe. what is your name?'
cap = True
new = ''
for i in sent:
    if cap == True and i != ' ':
        new += i.upper()
        cap = False
        continue
    if i == ' ':
        new += i
        continue
    if cap == False:
        if i in ['.', '!', '?']:
            cap = True
        new += i
	
print(new)

# ======================================================

total = 5
num = 0

try:
    ave = total / num
except ZeroDivisionError:
    print('have a nice day')
except ValueError:
    print('negative')
    
# ======================================================


# using a lambda to get a even list
list1 = [2,3,4,5,6,7,8,9,10,11,12]
result = list(filter(lambda x: x % 2 == 0, list1))
print(result)
