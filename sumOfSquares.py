from functools import reduce

def sumOfSquares(N):

    def sum(x, y):
        return x + y

    def square(x):
        return x**2

    squareArray = list(map(square, list(range(N + 1))))
    
    return reduce(sum, squareArray)

