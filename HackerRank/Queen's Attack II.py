#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    moves = [(1,0),(1,1),(-1,0),(-1,-1),(0,1),(0,-1)]
    ans = 0
    print(obstacles)
    
    for y,x in moves:
        new_c_q, new_r_q = r_q + y, c_q + x
        print(new_c_q, new_r_q)
        while new_c_q >=0 and new_r_q >=0 and new_c_q<n and new_r_q<k:
            if (new_c_q,new_r_q) in obstacles:
                break
            ans += 1
            new_c_q, new_r_q = new_c_q+y, new_r_q+x 
    
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
