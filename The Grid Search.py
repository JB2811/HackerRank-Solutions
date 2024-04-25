#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here
 R=len(G[0]); r=len(P[0])
 x=".".join(G)
 s=0
 if P[0] in x:
  while P[0] in x[s:]:
   l=x[s:].index(P[0])
   il=l
   f=1
   for i in range(1,len(P)):
    print(l,P[i],x[s+l+R:s+l+R+len(P[i])])
    if x[s+l+R+1:s+l+R+1+len(P[i])]!=P[i]:
     s=s+il+1
     f=0
     break
    else:
     l=l+R+1
   print(s,i)
   if(f):
    return "YES"
 return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
