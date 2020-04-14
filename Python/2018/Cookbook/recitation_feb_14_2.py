# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 18:57:27 2018

@author: jpsabini

A Review of the material 2 - 9


"""
'''You should know about how the special escape sequences work.
The sequences are here and in your book. And aboout scope.

# ABOUT the [] NOTATION which has people confused
  if the Bracket is on the right side A=[mylist of stuff]
   of an assignment then you are defining a list 
  For strings : string[an index-range] selects a substring
  
  For dictionaries D[key] selects a value belonging to the key
  
  For tuple TT[index-range  ] selects tuple(s) of TT
  
  SET objects DONOT have a [] referencing operation
  

 
https://en.wikipedia.org/wiki/Escape_sequences_in_C#endnote_Note3
You will need to know \t an \n and \' \\ and \"
'''


# precedence of operators.



1+2+3*4/4 # division is higher precedence than +
1+2+(3+4)/4 # parenthesis forces the 3+4 to be added BEFORE Division
2**2**2-1 # here the evaluation is 2 to the 4th then -1

#mixures teaser
True + False # this shows you that True is equivalesnt to 1
2>=True

2>= False

#figure this out The expression in parenthesis is evaluated first
y=10;x=15;z=20
y < z and not(x < y or z > x)
x < y or z > x

# Chapter Elementary strings and lists
# the continuation of a line
'The escape sequences \t( tab ) \n (newline) \ (blank) \\ Stuff to know '

# what does this do? \\ will force python NOT to evaluate the next \ 
print('The path is D:\\nabini\\test.')
#instead of 
print('The path is D:\nabini\test.') # notice the newlines and tabs

# astr Demos the \n \t detection with string methods like endswith etc     
astr='\nab\ncad\t\t\n'
astr
astr.endswith('\n')
astr.startswith('\n')
astr.find('\n')
# important what is the difference between find and index
astr.find('\t')
astr.index('a')
# what happens if the char is not in the string???
astr.index('s')
astr.find('s') # you get a V

astr.lstrip('\n')
astr.rstrip('\n')
astr.strip('\n')
astr.find('\n')   # WHY IS THIS 0? DID lstrip not remove it ?
astr              # Remember about making a string copy
aaa_astr=astr.lstrip('\n')  # assign a new string
aaa_astr # see there is no linefeed char at the beginning on the  left.

"substring" # A substring is a string which is usu contained 
##in a larger string but not necessarily 
astr='123456'
astr.find("345") # it returns the index of the first character it matches.


# DONOT FORGET you can't do this 
astr[2]='5'

# This program demonstrates several string testing methods.

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string:')
    
    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# Call the main function.
main();



#--------------------------------------------------#

## Some loopy things.
#What will be displayed after the following code is executed?
for num in range(0, 50, 5):
    print('before num:', num)
    num += num
    print('after num:', num)
    print('\n')
print(num)
    
#a.	100
#b.	90
#c.	0 5 10 15 20
#d.	0 10 20 30 40 50 60 70 80 90


# no 0f iterations in 2 nested loops.
count=0
for x in range(1,4):
    print(x)
    for y in range(100,106):
        print(y)
        count+=1
print(count)

''' functions...Scope and  arguments and named arguments.
We covered scope of a variable.
Scope is defined as the availability of the variable. In other words,
it's lifetime. Variables defined within a function are
local to that function. So two functions with locally defined 
variables y and y are independent.

When a block ends, all variables defined in
that block cease to exist and are not available to other
modules. Example

def my_function1(x):
    y=x  # scope of y is local to the my_function

def other_function(x):
    y=x
    
even though x may assign the same value, the two y's are hidden from each other.
They have a different scope. They are defined in different 
functions.

# global variables are those variable that are in scopr of the main
function and they are availble to all functions which are in
the main function. Globals can be referenced in the functions

    
t'''


#Non value returning and value returning.

#	In a value-returning function, the value of the
# expression that follows the keyword __ will be 
# sent back to the part of the program that called 
# the function.

# This program demonstrates what happens when you
# change the value of a parameter without a return

' arg is local to the scope of change_me() '

def main():
    value = 99
    print('The value is', value)
    change_me(value) 
    # the program returns to thispoint from the change_me()
    try:
        print('Back in main the value is{} and arg is {}'.format( value, arg))
    except NameError:
        print( 'arg is no longer in the scope of main, so it isno longer available ')


def change_me(arg):
    print('I am in chage_me changing the value.from arg =',arg)
    arg = 0
    print('I am about to leave change_me where the value is', arg)

# Call the main  function.

main()

#--------------------------#
# This program demonstrates a function that accepts
# two arguments.

def main():
    print('The sum of 12 and 45 is')
    x,y,name=12,45,'James'  # python's multiple oneline assignment
    show_sum(x,y, name)

# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2,name):
    result = num1 + num2
    
    print('the name and result are '+name, result)

# Call the main function.
main()
#----------------------------------------#

' now pass the arguments by naming or assigning to the arguments ' 
 
def main():
    
    
    show_sum(num2=10,name='Faustus  ',num1=17)
    
    #show_sum(num2=0)
    #show_sum(0)
# The show_sum function accepts two arguments
# and displays their sum.
def show_sum(num1, num2=1000,name=''):
    result = num1 + num2
    
    print('the name and result are '+  name + str( result))
# Call the main function.
main()
'----------------------------------------'
def main():
    print(show_sum(num2=1,num1=2))
    #show_sum(0)
    res,name=show_sum(num2=10,name='Faustus  ',num1=17)
    print('the name and result are '+  name + str( res))

# The show_sum function accepts two arguments but now thay are names and
# inparticular num2 and name have default values .
def show_sum(num1, num2=1000,name=''): 
    result = num1 + num2
    return(result,name)
    

# Call the main function.
main()

'=============== i/o exceptions ch 6==============================='

# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0
    
    try:
        # Open the sales_datxxxa.txt file.
        num=0
        numlist=list()
        while(num!=999):
            num=float(input('input number or input 999 to stop  '))
            if num !=999:
                numlist.append(num)
        # Read the values from the file and
        # accumulate them.
        for num in numlist:
            amount = float(num)
            total += amount
        # Print the total.
        print(format(total, ',.2f'))
        #infile.close()
    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except TypeError:
        print('An error occured.')
    
    except NameError:
        print(' I forgot to delete the close file line')
    else:
        print('The else statment is done because no exceptions ', total)
        
    finally:
        # Close the file.
        
        print('finally is done whether there is an exception or not')

# Call the main function.
main()
'----------------chapter 7 -lists ---------------------'
'''
1.You should know that lists after name assignment may be the same thing for 
different names. Lists are containers for mutable objects.

2. You should know remove() index() replace()
3. you should know that the string.split()
   produces a list. 
   
4. Tuples are containers for both mutable and immutable 
objects but tuple members are not mutable, they are sequetial 
t[1] comes before t[2]
and non unique'''
' lists and strings work together '
# many string methods like split produce lists

' lists and methods that generate them '
list('abcd') # different from
['abcd']
l=[]
l[0]="amy" # this is the wrong way to insret to a list
l.append("a") # the right way
print(l)
# 
# split and other methods produce lists.
bigstring='amy william colin didi'
# assign to string
string_list=bigstring.split(' ') # split on blank
string_list

line_el2=[1,2,3,4,5,6]
line_el2
line_el2.append('999')

line_el2
line_el2.remove(2)
line_el2

del(line_el2[3:5])  # removes all elements whose index is from 3 to 4 
# remeber that the last index is not counted. 

print(line_el2)


### Difference between Value Error and Type Error 
1+'a' # wrong type

int('1.3') # wrong value



#----tuples

tt=(["A","B","C",1,2,3],1.3,2,3,3,3,4,"pookie",(1,2,3))
tt[0][5]=100
tt[1]=100
tt[0].append(100)
"pookie" in tt
tt.index("pookie")



'======== Strings 8 ========================'
''' String index is like lists the LAST index in a 
slice is not counted. If the slice index goes beyond the 
string contents , the you get the whole string.
'''
string="Funnily"
len(string)
string[0:6]

string[0:7]
print(string[0:])
# string constructor str()
A=str("3.14159")
print(type(A),A)

''' There are many string methods. Put a dot after
the string variable and you will obtain a selection 
of methods that are available.'''

" A.splitlines , A.count , A.split()"



q = 459
p = 0.098

#Strings and print concatenated items 
#convert numbers to string types
print(q, p, p * q)
print(str(q) + " " + str(p) + " " + str(p * q))

''' Dictionary values can contain anythng, but keys are 
special indexes so they are unordered, immutable,hashable( unique),
'''
A=dict()
A['fooof'][1]
key colon value comma
A={"a":1,"b":2,"c":3,"fooof":[1,2,"oh"],"myset1":{1,2,3,1}}

A["bo"]="myvalue"
print(A)   #notice there is no order.
A.items()
print(A)

del(A['myset1'])
print(A)
A.popitem() # popitem takes no arguments 

A.pop('fooof') # pop takes one argument

A.get('a')
A.get('fooof', 'it\'s been poped')

"a" is in A
"a" in A


'Sets'
l=[1,1,1] # list can contain same values
st={1,2,1,2,1,2,4} # the values are unique
st2={4,5,6} # another set 

st.intersection(st2)
st[0]  # NO NO Indexing on sets.


ttt=(1,)  # a tuple is defined with a comma

