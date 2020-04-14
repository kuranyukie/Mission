#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:24:35 2018

@author: Yukie
"""



"""
Assume the availability of a function is_prime. 
Assume a variable n has been associated with positive integer. 
Write the statements needed to find out how many prime numbers 
(starting with 2 and going in increasing order with successively 
higher primes [2,3,5,7,11,13,17,19,23...]) can be added before exceeding n. 
Associate this number with the variable k.
"""

def is_prime(a):
	if a == 0 or a == 1:
		return False
	for i in range(2,a):
		if a % i == 0:
			return False
	return True

def test(n):
    sum = 0
    k = -1
    num = 2
    while sum <= n:
        if is_prime(num):
            sum += num
            k += 1
        num += 1
    return(k)

# print(test(1))

for i in range(20):
    print("test:", i, "result:", test(i))
    
"""
interest rate
"""

p = float(input("Enter current bank balance:"))
i = float(input("Enter interest rate:"))
t = float(input("Enter the amount of time that passes:"))

def calc(p,i,t):
	f = p * (1 + i) ** t
	return f

print(calc(p,i,t))