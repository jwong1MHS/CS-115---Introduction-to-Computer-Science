#
# Jason Wong
#
# Homework 09/09/19
#
# I pledge my honor that I have abided by the Stevens Honor System.


from math import factorial, sqrt
from functools import reduce
   

def sum(x, y):
    return x + y


# Compute arithmetic mean of a give list of numbers

def arithmetic_mean(m):
    return reduce(sum, m)/len(m)



# Compute the length or norm of a vector given a input of a list

def vector_length(v):
    def square(x):
        return x**2 

    return sqrt(reduce(sum, list(map(square,v))))



# Compute an approximation of the value of e (base of natural log) using Taylor 

def e(T):
    def reciprocal(r):
        return 1/factorial(r)
    
    return reduce(sum, list(map(reciprocal, list(range(T + 1)))))
