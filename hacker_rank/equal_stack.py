#!/bin/python3
#https://www.hackerrank.com/challenges/equal-stacks/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    l1, l2, l3 = 0, 0, 0
    for i in h1:
        l1 += i
    for i in h2:
        l2 += i
    for i in h3:
        l3 += i
    # print(l1,l2,l3)
    while l1 != 0 and l2 != 0 and l3 != 0 and ( l1 != l2 or l2 != l3):
        if max(l1, l2, l3) == l1:
            # print(" l1 = l1 - h1 {} - {}".format(l1, h1[0]))
            l1 = l1 - h1[0]
            h1.pop(0)
        elif max(l1, l2, l3) == l2:
            # print(" l2 = l2 - h2 {} - {}".format(l2, h2[0]))
            l2 = l2 - h2[0]
            h2.pop(0)
        else:
            # print(" l3 = l3 - h3 {} - {}".format(l3, h3[0]))
            l3 = l3 - h3[0]
            h3.pop(0)
    else:
        if l2 == l1 and l3 == l2:
            # print(l1,l2,l3)
            return l1
        else:
            return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

