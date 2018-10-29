#!/bin/python3
#https://www.hackerrank.com/challenges/crush/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    tmp = n+1
    final_list = [0] * tmp
    for each_qu in queries:
        start, end, value = each_qu
        for i in range(start,end+1):
            final_list[i] += value
    return max(final_list)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
