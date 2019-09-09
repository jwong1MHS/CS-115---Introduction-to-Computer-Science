#
# A. Nicolosi
#
# 9/6/19
#
# Utility to convert a list of temperatures from ^F to ^C
# Also, compute simple stats
#

from functools import reduce

def toC(tempF):
    '''convert the given temperature from ^F to ^C'''
    return (10.0/18.0)*(tempF-32)

def toF(tempC):
    '''convert the given temperature from ^C to ^F'''
    return (18.0/10.0)*tempC+32

def listToC(l):
    '''convert a list of ^F temps into ^C'''
    return list(map(toC, l))

def tempStats(listF):
    '''convert a list of ^F temps into ^C and compute simple statistics'''

    def myMin(x,y):
        return x if x < y else y

    def myMax(x,y):
        return x if x > y \     # \ means continue
               else y
    
    listC = listToC(listF)
    minTemp = list(reduce(myMin, listC))
    maxTemp = list(reduce(myMax, listC))

    return [minTemp, maxTemp, listC]


