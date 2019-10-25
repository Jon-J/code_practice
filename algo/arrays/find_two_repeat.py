#https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
import math
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def print_two_repeating_integers(arr):
    S = 0
    P = 1
    size = len(arr)
    n = size - 2

    for i in range(size):
        S += arr[i]
        P *= arr[i]

    S = S - n*(n+1)//2
    P = P//fact(n)

    D = math.sqrt((S*S) - (4*P))

    X = (D+S)//2
    Y = (S-D)//2

    print("X = {}, Y = {}".format(X, Y))

a = [2,3,5,3,4,1,6,5]
print_two_repeating_integers(a)

a = [2,2,5,3,4,1,6,1]
print_two_repeating_integers(a)
