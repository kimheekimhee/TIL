#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    num_1 = 0
    num_2 = 0
    answer = 0
    for i in range(n):
        # print(i) # 0 1 2
        print(arr[i][i]) # 00 11 22
        num_1 += arr[i][i]
        print(arr[i][-1-i]) # 0-1 1-2 2-3
        num_2 += arr[i][-1-i]
    print(num_1, num_2) 
    answer = num_1-num_2
    if answer < 0:
        answer = -answer
    return answer

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()