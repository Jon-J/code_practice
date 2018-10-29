#!/bin/python3
#Following link is for solution to this problem. This Solution is called difference array and prefix array
#https://www.youtube.com/watch?v=2BkYwUMkePY
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
        final_list[start-1] += value
        final_list[end] -= value
    
    t_sum, maxium = 0, 0
    
    for i in final_list:
        t_sum += i
        if t_sum > maxium:
            maxium = t_sum
    return maxium


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


