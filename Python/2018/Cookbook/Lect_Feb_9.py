# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:42:40 2018

@author: jpsabini
"""

s1 = u'The Zen of Python'
s2 = u'きたないのよりきれいな方がいい\n'
s3 = u'Python的禅宗'
'''
immutable objects can't change or be updated.
Sequential objects have math property like ordering
mutable objects can change
Hashable objects are unique and immutable usually

lists are mutable and sequential and contain anything
dicts are key:value pairs and have mutable or immutable 
          values but keys are immutable, hashable 
          and non sequential ( no ordering)
sets are mutable and contain unique i.e. Hashable, non sequential
        immutable objects (numbers,strings)
tuples are immutable objects and may contain anything.
strings are immutable so are numbers.

'''
# insertion you can't because  strings are immutable 

s4=s2[0:2]+s1[4:6]+s3[5:]
print(s4)

#how end works 
for char in s2:
    print(char, end='')
    
for char in s2:
    print(char)   
    
# how sep works
print(s1,s3, sep=' this is translated to this ')    

#-------------------- dictionary - key:value pairs -------------------------------------#

'''Dictionaries are a convenient way to store data for later retrieval 
by name (key). Keys must be unique, immutable objects,
 and are typically strings.  The values in a dictionary can be anything. 
 For many applications the values are simple types such 
 as integers and strings.'''
 
# mutable unordered nonsequential - key is hashable and immutable = value is anything
# creating dicts 

weights = {'Fred': 175, 'Anne': 120, 'Joe': 192}

weights['Fred']

weights['Fred']=176

weights['Yao']=194

weights

# the dict constructor 
heights={} 
heights = dict([('Joe',5.11), ('Ann',5.9),('Fred',6.2)]) 
heights

heights = { 'Joe':5.11, 'Ann':5.9,'Fred':6.2}

 

#----notice that these are views and not values ---#

heights.keys()
heights.values()

type(heights.values())
# type here produces an iterable called dict_values instead of the value type
# an iterable is a python object that allows a loop to be used on it


# keys and values iteration and extraction 
for k in heights: 
    print (k) # this will alway get the key 
    
for k in heights.keys():
    print(k)

#values
for i in heights.values(): 
    print (i)


heights = { 'Joe':5.11, 'Ann':5.9,'Fred':6.2}
# you are using values as a key which is
#  Bad because it isnt there..heights[5.11]
for i in heights.values(): 
    print (heights[i])

# this is correct 
for i in heights.values():
    print (i)
    
# correct 
for i in heights.keys(): 
    print( heights[i]) # not pythonic


# items are mapped to k,v a pair 
# at a time with items
for k,v in heights.items():
    print(k,v) 

# redundant very un-pythonic.
for k,v in heights.items():
    print(k,heights[k])
    
# Bad for a differnt reason. key is not iterable
# 
for k,v in heights.values():
    print(k,v)
    
for k,v in heights:
    print(k,v)

# therefore Items is important
## Methods and interesting stuff #

# the get with default.
heights = { 'Joe':5.11, 'Ann':5.9,'Fred':6.2}
heights.get("Fred")
#Check for Ying not in original
kk="Ying"
# get and the default message if key is not present
heights.get(kk," I don't know " + kk)
print(heights)
# popitems and pop will assign and remove.
popped=heights.popitem()
popped
heights
#reset
heights = { 'Joe':5.11, 'Ann':5.9,'Fred':6.2}


# POP method gets the value of Fred (key is required) and removes Fred 
# and Fred;'s value 6.2

value_of_fred =heights.pop("Fred")
print(heights)
# not there anymore
heights.pop("Fred") #KeyError

# we have values and we can redo
print(value_of_fred)

heights['Fred']=value_of_fred #put Fred together again
print(heights)

weights = {'Fred': 175, 'Ann': 120, 'Joe': 192}


len(weights)
new_weights= weights.fromkeys(heights,0)
new_weights



## Assignment 1 

states = {'Oregon':'OR',
          'Florida':'FL',
          'California':'CA',
          'New York':'NY',
          'Michigan': 'MI'
          }

cities = {'CA':'San Francisco',
          'MI':'Detroit',
          'FL':'Jacksonville'
          }

cities['NY']  = 'New York'
cities['OR']  = 'Portland'
cities

# print out each city name and full state name
for state_name in states.keys():
    state_abbr=states[state_name]
    print(cities[state_abbr],state_name)

## reversal logic create new_state
new_state={}    
for statename,state_abbr in states.items():
    print(statename,state_abbr)
    new_state[state_abbr]=statename
# new state is the reverse of state
cities
new_state
for state_abbr,city_name in cities.items():
    print(city_name, new_state[state_abbr], end='\n')
    

# you can have many differnet types in dicts as in lists.

d_multi={(1,2):'strings',"2":[0,1],"Jo":{"a":1,"b":2}}
# referencing d_multi
d_multi[(1,2)]
d_multi['Jo']['a']  



#Advanced not on exam .....dictionary comprehensions {key: value for (key, value) in iterable}

### zipping a two lists into pairs for dict
seq=zip(['john','Joe','jim','ann','frodo'],[1,2,3])
ddict={}
for k,v in seq:
    ddict[k]=v

print(ddict)



heights
ddict
for k,v in ddict.items():
    try:
        print(k,' is ', heights[k] , ' feet')
    except KeyError:
        print(" I don't know " + k)

        

# using a dictionary comprehension to create a dictionary with 
# English alphabet to integers
import string

dict_c= {k: v for (k, v) in zip(string.ascii_lowercase, range(1,27))} 
print(dict_c)




"---------------------------------------------"
''' SETS Sets  are nonsequential , mutable containers 
    made up of unique valued immutable objects . There are also
    immutable sets, called frozensets, but those won't be covered'''

A={'apples','pears','plums'}




{1,2,3,4,1,2,3,4,10,20,20,30}



# the SET constructor 

set("my dog, her dog His dog")

ints=set([1,2,3,4,1,2,3,4,10,20,20,30])
ints

A=set("my dog","her dog","His dog")        
#Takes only one object

A=set(["my dog","her dog","His dog"])
print(A)


# methods
len(A)

A.add("my fish")

len(A)

A.clear()
print(A)


A
A={1, 2, 3, 4, 5, 6}
B ={4, 5, 6, 7, 8, 9}

print(A.union(B))


print(A.intersection(B))

# set difference.
print(A-B)
print(A.difference(B))
# not symmetric
print(B-A)

print( A ^ B)
A.symmetric_difference(B)

# since sets are mutable but contain immutable unique objects 
# you cannot add a list or a mutable object to a set.
' LOOK at This'
BAD={1,[1,2],'a',{'a':5},(1,2)}
OK={(1,'a'),(1,'a')} # tuples are immutable and hashable

print(OK) # interesting

1 in A

# looping over sets.
for i in A:
    if i not in B:
        print(i)
        
for p in range(1,7):
    A.add(p)




'''ADVANCED not on exam Set comprehensions like lists and dicts.


    

B={p for p in range(4,10) } #This is an example of Set Comprehension

print(B)
{4, 5, 6, 7, 8, 9}


MORE ADVANCED 

It gets more interesting when the values in a dictionary are
 collections (lists, dicts, etc.) In this case, the value 
 (an empty list or dict) must be initialized the first time 
 a given key is used. While this is relatively easy to do manually, 
the defaultdict type automates and simplifies these kinds of operations.

A defaultdict works exactly like a normal dict, 
but it is initialized with a function (“default factory”) 
that takes no arguments and provides the default value 
for a nonexistent key.

A defaultdict will never raise a KeyError.
 Any key that does not exist gets the value returned 
 by the default factory.
'''

#




#---example ---- notice the list in default dict---
from collections import defaultdict

city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), 
             ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), 
             ('TX', 'Dallas'), 
             ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)

for state, cities in cities_by_state.items():
    print (state, ', '.join(cities) )
