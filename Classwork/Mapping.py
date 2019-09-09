#
# Jason Wong
#
# Demo code


def double(x):
    '''Compute the double of its input'''
    return 2*x

evensUpToEight = list(map(double, list(range(5))))
''' map function maps each list of numbers to the double function'''
#[0, 2, 4, 6, 8]


def increment(x):
	'''Compute x+1'''
	return x+1

oddsUpToNine = list(map(increment, evensUpToEight))
#[1, 3, 5, 7, 9]


def oddify(x):
	'''compute the x-th odd (0-based)'''
	return 2*x + 1

list(map(oddify, list(range(5))))
#[1, 3, 5, 7, 9]


### Will not work because the function dbl is inside the other function evensUpToN
def evensUpToN(n):
    '''Produce a list of the first n even numbers'''

    def dbl(x):
        '''Compute the double of its input'''
        return 2*x

    return list(map(dbl, list(range(n))))

