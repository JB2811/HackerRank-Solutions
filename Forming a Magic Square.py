#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
from math import inf
#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.

def is_magic_square(lst):
 a=[[0 for i in range(3)] for j in range(3)]
 for i in range(3):
  for j in range(3):
   a[i][j]=lst[3*i+j]
 
 s=sum(a[0])
 for i in range(1,3): 
  tmp=sum(a[i])
  if tmp !=s:
   return False
     
 for j in range(3):
  tmp=sum(a[i][j] for i in range(3))
  if tmp!=s:
   return False
     
 tmp=sum(a[i][i] for i in range(3))
 if tmp != s:
  return False
     
 tmp=sum(a[2-i][i] for i in range(3))
 if tmp!=s:
  return False
     
 return True
 
def find_magic_squares():
 magic_squares=[]
 l=list(range(1,10))
 
 for s in permutations(l):
  if is_magic_square(s):
   magic_squares.append(s)
 return magic_squares
 
def cost(a,b):
 return sum(abs(a[i]-b[i]) for i in range(9))
 
def formingMagicSquare(s):
 s=s[0]+s[1]+s[2]
 min_cost=inf
 magic_squares=find_magic_squares()
 for i in range(len(magic_squares)):
  min_cost=min(min_cost,cost(s,magic_squares[i]))
 return min_cost
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
