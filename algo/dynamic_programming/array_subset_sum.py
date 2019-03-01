#!/bin/python3

import math
import os
import random
import re
import sys


from itertools import chain, combinations
#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def subsetA(arr):
    # Write your code here
    max_sum = sum(arr)
    res_sum = 0
    res_list = []
    for i, combo in enumerate(powerset(arr), 1):
        curr_sum = sum(combo)
        diff = max_sum - curr_sum
        if curr_sum > diff:
            if (res_sum == 0 or curr_sum > res_sum) and ( len(res_list) == 0 or len(combo) <= len(res_list)):
                res_sum = curr_sum
                res_list = list(combo)
    return sorted(res_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

