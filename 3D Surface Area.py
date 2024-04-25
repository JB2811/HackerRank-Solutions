#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    totalArea=0
    for i in range(len(A)):
        for j in range(len(A[i])):
            temp=A[i][j]*6  #each vertical cuboidA[i][j] height
            temp -= (A[i][j]-1)*2 if A[i][j]>1 else 0
            temp -= min(A[i-1][j] if i-1 >= 0 else 0, A[i][j])
            temp -= min(A[i][j+1] if j+1 < len(A[i]) else 0, A[i][j])
            temp -= min(A[i+1][j] if i+1 < len(A) else 0, A[i][j])
            temp -= min(A[i][j-1] if j-1 >= 0 else 0, A[i][j])
            totalArea+=temp
    return totalArea
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
