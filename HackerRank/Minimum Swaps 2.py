#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    cnt = 0
    for i in range(len(arr)):
            while 1:
                if arr[i] != i+1:
                    a = arr[i]
                    arr[i], arr[a-1] = arr[a-1], arr[i]
                    cnt += 1
                else:
                    break
    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()              
