#
# Jason Wong
#
# Map Reduce
#
# I pledge my honor that I have abided by the Stevens Honor System.


from functools import reduce

def maxString(s):
    def length(s):
        return [len(s), s]

    lengthofString = list(map(length, s))

    return reduce(max, lengthofString)[1]
