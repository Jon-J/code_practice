#!/bin/python3
'''
# Problem statement: https://www.hackerrank.com/challenges/sparse-arrays
'''
import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    queries_dict = { i : 0 for i in queries}
    for i in strings:
        if i in queries_dict:
            queries_dict[i] +=1
            
    return_list = []
    for test in queries:
        if test in queries_dict:
            # print(queries_dict[test])
            return_list.append(queries_dict[test])
    return return_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

