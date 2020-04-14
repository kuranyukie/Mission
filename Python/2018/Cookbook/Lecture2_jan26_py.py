# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:39:01 2018
 Most of the code here is on the slides.
 Some of the code is not. You can study that as well.
 There may be typos. Let me know
 

@author: jpsabini
"""
# GAddis Chapter 3  cont'd #
# Booleans return True or False 

''' >, <, >=,  <=, != , and, or, == (comparison) '''
''' Logicals and,not , or '''
# If you run this you get True or False
2 < 3, 3>=4 
#How to use modulus operation, getting even numbers 
n=17
n%2 == 0
n=10
n%2 == 0

''' If ( boolean) : elif (boolean) : else: '''

if (n%2 != 0):
    print(n ,'is odd') 
    

if (n%2 == 0):
    print(n, 'is even')


''' indentation 4 spaces for each  BLOCK
 blankspaces  are not tabs and they are meaningful !!!
 like so 
 if (x=y):
     Statement 1
     Statement 2
     ...
     Statement n
 elif (x >y):
     Statement n+1
     Statement n+2
     ...
 elif ( ):
     etc..
     
 else:
    Statement M
    Statement M+1 
     
  page 119 Figure 3-6 is very important to understand.'''

x= 5
if x <4:
    y=x*2
    print(x) # will not Print x
"--------------------------------------"    

if x < 4:
    y=x*2
print(x)  #will print 5 try print(x,y) 


"--------------------------------------"

''' the else: '''

if (n%2 != 0):
    print(n ,'is odd')  # 4 spaces
else: 
    print(n, 'is even')

"-------------------------------------"
# example of loan qualification using input  

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

# Determine whether the customer qualifies. The order of the decision is 
# determined by the imporance of the criteria. But you could invert
# the logic if you are logical :).
if salary >= min_salary:
    if years_on_job >= min_years:
        print('You qualify for the loan.')
    else:
        print('You must have been employed', \
              'for at least', min_years, \
              'years to qualify.')
else:
    print('You must earn at least $', \
          format(min_salary, ',.2f'), \
          ' per year to qualify.', sep='')
    
"------------------------------------"
   
# An alternative decision
    
if years_on_job >= min_years:
    if salary >= min_salary:
        print('You qualify for the loan.')
    else:
          print('You must earn at least $', \
          format(min_salary, ',.2f'), \
          ' per year to qualify.', sep='')
    
else:
        print('You must have been employed', \
              'for at least', min_years, \
              'years to qualify.')
        
"----------------------------------"

''' Strings and relational operators 
This program compare strings with the < operator.'''

# Get two names from the user.
# This program compare strings with the < operator.
# Get two names from the user.
# Display the names in alphabetical order.
    
name1 = input('Enter a name (last name first): ')
name2 = input('Enter another name (last name first): ')
print('Here are the names, listed alphabetically.')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
    
"-----------------------------------"

    
#Logical operators. 15 ####
    
havePlums=True
pickedRecipe=False

if havePlums or pickedRecipe:
    print('Let\'s makea pie!')
else:
    print("Somethng is missing")
    
if havePlums and pickedRecipe:
    print('Let\'s makea pie!')
else:
    print("Somethng is missing")

"------------------------------------"

### Testing mutex series of conditions slide 25
budget = float(input( 'budget please   '))
if budget == 0.0:
    print('the best things in life are free')
elif budget < 5.0:
    print('buy bubble tea')
elif budget <= 10.0:
    print('buy chocolate mousse') 
elif budget <= 15.0:
    print('buy lillies')
elif budget <= 20:
    print('buy a poster')
else:
    print("Cucumbers are in season")
    
"-----------------------------------------"
''' if : elif : else:    '''
 # Excersize  3.3 slide 27
age = int(input( ' Enter the age :' ))
if age <= 1:
    print('It\'s an infant') 
elif age > 1 and age < 13 :
    print('Child')
elif age > 13 and age <20 :
    print('Teenager')
else:
    print('Adult')

"----------------------------------------"

# another Way to do the program which is a bit cleaner.
    
age = int(input( ' Enter the age :' ))
if age <= 1:
    print('It\'s an infant')
elif age < 13 :                  # when age < 1 is false
    print('Child')
elif  age < 20 :
    print('Teenager')
else:
    print('Adult')

# try it with >= 

"---------------------------------------"
  
''' Loops While , for Gaddis Chapter 4'''

''' ALways Always Always set a counter 
    before entering the while. 
    IN GENERAL it is wise to intialize
    all variables before using them.'''
    
count = 0 
while ( count < 9):
    print ('the count is:', count)
    count=count + 1

print('See Ya!')

"------------------------------------"

#infinite loop 34  Hit Control C in the IPython Console ###
count = 0
while ( count < 9):
    print ('the count is:', count)
count=count + 1  
''' THIS count Statement is OUTDENTED i.e. not in the 
    scope of the of the while block. SO it will 
    never be executed. Hence count will always be set to 0 '''
print('See Ya!')

"------------------------------------"

''' Assignment Wite in class and submit '''
# slide 35 

# double the count 
count = 0
while ( count < 9):
    print ('the count is:', count)
    count +=2

print('good bye!')

"-------------------------------------"
### The even numbers are printed out.
count = 0
while ( count < 9):
    if count%2 ==0:
        print ('the count is:', count)
    count +=1  #<- because of math : 1 + odd is even .

print('good bye!')
"--------------------------------------"  

# Altering the count within the loop from an input
count = 0
while ( count < 9):
    count =int(input(' the new count ENTER HERE '))
    print ('the count is:', count)
    count=count + 1

print('See Ya!')

"------------FOR LOOP --------------------------"

# the for loop is a finite loop it will always do one pass

for x in ["a","b","c"]:
    print(x)

"-----------------------------------------------"
' Assignment slide 47 '
for x in [0,1,2,3,4,5,6,7,8,9]:
    if (x%2!=0) :
        print( x,'is an odd value')
"-----------------------------------------------"  
      
# range function slide 45
for x in range(5):
    print(x)

for x in range(-10,10):
    print(x)  
    
for x in range(-1,-10,-2):
    print(x)   
"-----------------------------------------------"


type(range(5))
range(5)
list(range(1,50)) # genrates a list 1 to 50
        
"--------------------------------------"
        
''' Functions Gaddis Chatpter 5'''

# 51###
     
'''Simple concept y= f(x) Where f has certain rules. Remeber we 
   we wrote and tested if the num is even or odd 
   let's make it a function it uses return statement
   at the end'''
   
def is_Odd(n):   
    if (n%2 != 0):
        #return(print(n ,'is odd') ) # 4 spaces
        return(True)
    else: 
        #return(print(n, 'is even'))
        return(False)

n=101
is_Odd(n)
"-------------------------------------------------"
#Now we can use the is_Odd funtion as a boolean because 
#it returns a boolean  constant: True or False 
if ( is_Odd(n)) :
    print('gee I am odd')
else: 
    print('I am not odd')
"----------------------------------------------"
       
## 68 Parameters 
# I used the "string{varable 0 } , {varible 1} ".format (x,y) 
# in this example you can look it up.

def main():
    value=99.99
    zippee=0.
    print('Initially in main the value is  ',value)
    zippee = change_me(value) #assign
    print('Back in main program the value is STILL = {0} \
          BUT zippee is {1} '.format(value, zippee ))
    
def change_me(my_arg):
    print('We entered the change value function and the my_arg parameter is :  ',my_arg)
    arg =my_arg + 101
    print('We set the value of arg returned  ', arg)
    return(arg) # using return "sets" the name of the change_me to "hold" the returned value

#invoke main() 
main()
"----------------------------------------------"




# two ways to tell if the functions are defined
type(main)
main
change_me 

"-----------------------------------------------------"

#slide 71 writing your own 
def main():
    green_apples = int(input('Enter No of green apples: '))
    red_apples = int(input(' Enternumber of red apples: '))
    
    total_apples =sum(green_apples,red_apples)
    
    print( ' we have a total of ' , total_apples, ' apples' )

def sum(green=0,red=0):
    return(red+green)
    
main()

"------------------------------------------"
### import libraries.
## when the library is large and we don't want to load all of it 
## we can load a part of it , if we know the library well.

import math
pow(2,10)

''' use the (period/dot) . selector to view all of the 
    math functions contained in math package'''
math.cos(3.14159)

cos(0)
import random       
random.randint(0,10) 

''' That's it for now '''      
   
