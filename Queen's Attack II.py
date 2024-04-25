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
    # Directions: [up, down, right, left, up-right, up-left, down-right, down-left]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    # Initialize counts for each direction
    counts = [n - r_q, r_q - 1, n - c_q, c_q - 1, min(n - r_q, n - c_q), min(n - r_q, c_q - 1),
              min(r_q - 1, n - c_q), min(r_q - 1, c_q - 1)]
    
    # Update counts based on obstacles
    for obstacle in obstacles:
        r, c = obstacle
        dr = r - r_q
        dc = c - c_q
        
        # Check if obstacle is in the same row or column
        if r == r_q:
            if c > c_q:
                counts[2] = min(counts[2], dc - 1)
            else:
                counts[3] = min(counts[3], -dc - 1)
        elif c == c_q:
            if r > r_q:
                counts[0] = min(counts[0], dr - 1)
            else:
                counts[1] = min(counts[1], -dr - 1)
        # Check if obstacle is in diagonal direction
        elif abs(dr) == abs(dc):
            if dr > 0:
                if dc > 0:
                    counts[4] = min(counts[4], dr - 1)
                else:
                    counts[5] = min(counts[5], dr - 1)
            else:
                if dc > 0:
                    counts[6] = min(counts[6], -dr - 1)
                else:
                    counts[7] = min(counts[7], -dr - 1)

    return sum(counts)

    
     
    
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
