from functools import reduce

def gauss(N):

    def sum(x, y):
        return x + y
    
    return reduce(sum, list(range(N + 1)))


