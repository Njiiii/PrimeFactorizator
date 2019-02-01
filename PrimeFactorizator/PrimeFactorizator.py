#Every positive whole number is possible to show as a addition between 2 or more prime numbers (for example 30 = 2 * 3 * 5).
#This program is designed to show that addition.

import math
import collections

#Prime factors of an integer goes to this list.
#Final output is made with this list.
factors = []



#Function to check if number given by user is a prime number.
def is_this_prime(n):

    if n >= 2:
        for x in range(2, int(n)):
            if not (n % x):
                return False
        else: 
            return True
    


#This function breaks down the integer given by user to prime numbers
def prime_factorization(x):

    for i in range(2, x):

        while is_this_prime(i) == True and x % i == 0:
            factors.append(i)
            x = x / i 
           
    #If x is a prime number, we only append x and an extra value 1 to factors
    if is_this_prime(x) == True:

        factors.append(x) 
        
        #This if-check makes sure that we append that extra 1 x given by user is a prime number
        #Otherwise this can lead to situations like 1234 = 2 * 1 * 617, where we don't need the extra 1
        if len(factors) == 1:
            factors.append(1)
            factors.sort()
      


#This function asks user to give a number.
def ask_for_input():

    a = int(input("Give a number, please: ")) 
    return a



#Now we need function to make the final output from factors list
def make_output(factors):

    d = {x:factors.count(x) for x in factors}

    #keys are the prime numbers in the factors list
    keys = []
    [keys.append(a) for a in d.keys()]

    #values are the number of duplicates in factors list
    values = []
    [values.append(b) for b in d.values()]

    #E.g. if factors had [5, 5, 5, 7, 7], then keys would be [5, 7] and values would be [3, 2]
    #We'll use keys and values to create the final output: 6125 = 5^3 * 7^2

    output = []
    #We put x^y into output only if y < 1
    #x^1 is always x so it's redundant info
    for i in range(len(keys)):
        if values[i] != 1:
            output.append(str(keys[i]) + "^" + str(values[i]))
        else:
            output.append(str(keys[i]))

    #As an extra flair, it's nice if we show output as a = b^c * d
    #So l is the same as the integer user gives in ask_for_input() and which is used in prime_factorization(x)
    l = 1
    for j in range(len(factors)):
        l = l * factors[j]

    print(str(l) + " = ", end = "")
    print(*output, sep = " * ")
     


#Finally we have the main-class that calls everything nicely in the right order
def pf_main():

    a = int(ask_for_input())

    if a > 1 and a <= 25000:
        
        prime_factorization(a)
        make_output(factors)
        
    
    if a > 25000:
        print("Anything over 25000 is too heavy to process")


    if a <= 1: 
        print("Negative integers, 0 and 1 are not allowed")



pf_main()
