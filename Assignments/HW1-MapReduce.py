############################################################
#
#  Jason Wong
#
#  CS115-B/C HW1 ~ Applications of Map & Reduce
#
#  Due : Sep. 20th, 2019
#
#  Pledge : I pledge that I have abided by the Stevens Honor System.
# 
############################################################


# All functions should be written using map/reduce.
# No loops, no recursion, or other built-in functions unless explicitly allowed.
# You are free to write helper functions, so long as the main functions work as intended.

from functools import reduce
from math import factorial, sqrt # this import is necessary to use sqrt and factorial.


def taylorApproxE(lastIter):
    def sum(x,y):
        return x + y
    
    def reciprocal(r):
        return 1/factorial(r)
    
    return reduce(sum, list(map(reciprocal, list(range(T + 1)))))


def vectorNorm(vect1):
    def sum(x,y):
        return x + y 
    
    def square(x):
        return x**2 

    return sqrt(reduce(sum, list(map(square,v))))


def arithMean(vect1):
    def sum(x,y):
        return x + y
    return reduce(sum, m)/len(m)



