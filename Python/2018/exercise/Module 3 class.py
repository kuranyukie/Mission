#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:17:05 2018

@author: Yukie
"""

test_file = open('Module3test.txt', 'w')
test_file.write("The first line\n")
test_file.write("The second line\n")
test_file.close()

a = open('Module3test.txt', 'a')
a.write("add a new line")
a.close()

infile = open('Module3test.txt', 'r')
for line in infile:
    print(line)
    if line.endswith('\n'):
        line = line.rstrip('\n')
infile.close()


# inclass assignment

flowers = ["rose", "poppy", "lotus"]
count = 0
while (count<len(flowers)):
    print(flowers[count])
    count += 1
    
# create list
flower1 = ['red', 'blue', 'yellow', 'red', 'green']
flower2 = [x for x in flower1 if x != "red"]
print(flower2)

# ch6 ex6.2 51360
    
ini = open('numbers.txt', 'w')
ini.write("9\n7\n5\n18\n13\n2\n22\n16")
ini.close()

ipt = open('numbers.txt', 'r')

line = ipt.readline()
maxv = 0
runsum = 0

while line != '':
    print("line:", line)
    if int(line) > maxv:
        runsum += int(line)
        print("runsum", runsum)
        maxv = int(line)
        print("maxv:", maxv)
    line = ipt.readline()

ipt.close()

# ch6.4 51364 solution 1

x, y, z = 'ud8a', '10','b'   
x, y, z = '10', '8','2'   

errors = []

try:
    x = int(x)
except:
    errors.append("x")
    
try:
    y = int(y)
except:
    errors.append("y")
    
try:
    z = int(z)
except:
    errors.append("z")

if len(errors) == 0:
    print(x+y+z)    
else:
    final_list = ['bad value(s) in:'] + errors
    for i in final_list:
        print(i, end=' ')
        
# ch6.4 51364 solution 2

x, y, z = 'ud8a', '10','b'
# x, y, z = '10','8','2'      

errors = []
sum = 0

for var in 'xyz':
    try :
        num = int(eval(var))
        sum += num
    except:
        errors.append(var)

if len(errors) == 0:
    print(sum)
else:
    final_list = ['bad value(s) in:'] + sorted(errors, key=str.lower)
    print(*final_list)
    
# Ch6.5 71434

count = int(input("Enter number of players:"))

info = []

for i in range(count):
    name = input("Enter name of player number " + str(i+1) + ":")
    score = input("Enter score of player number " + str(i+1) + ":")
    info.append(name)
    info.append(score)

opt = open("golf.txt", "w")
for i in info:
    opt.write(i+"\n")

opt.close()

ipt = open("golf.txt", "r")

line = ipt.readline()
count = 1

while line != '':
    if count % 3 == 1:
        print("Name:" + line.strip("\n"))
        line = ipt.readline()
    elif count % 3 == 2:
        print("Score:" + line.strip("\n"))
        line = ipt.readline()
    else:
        print()
    count += 1

ipt.close()

# ch7.2 51280

list1 = [1,2,3,4,4,4,4]
list1 = [1,2,3]

has_dups = False
check_list = []
for i in list1:
    if i not in check_list:
        check_list.append(i)
    else:
        has_dups = True
        break
    
print(has_dups)

# Ch7.5 51289 solution 1

m,n = 2,20

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return (fibonacci(n-1)+fibonacci(n-2))

fib = []
i = 0
tested = 0

while tested <= n:
    tested = fibonacci(i)
    if tested >= m and tested <= n:
        fib.append(tested)
    i += 1
        
print(fib)		

# Ch7.5 51289 solution 2

m,n = 4,20

fib1 = [0,1,1]
fib  = []

for i in fib1: # first append initial fib1
    if i >= m and i <= n:
        fib.append(i)

tested = 2 # start to test with 1+1=2
while tested <= n:
    fib1.append(tested) # add the newest tested into fib1 to ensure line 209 will work
    if tested >= m: # only add tested into fib when >= m
        fib.append(tested)
    tested = fib1[-1] + fib1[-2] # updated tested and a new while loop will execute

print(fib)
        
for i in  range(0,10,-1):
    print(i)
