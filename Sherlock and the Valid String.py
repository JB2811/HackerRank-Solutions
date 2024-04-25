#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
 # Write your code here
 d=[]
 e=set(s)
 for i in e:
  d.append(s.count(i))
 t=d[0]
 i=0
 c=1
 while(i<2 and i<len(d)):
  if(c<d.count(d[i])):
   t=d[i]
   c=d.count(t)
  i+=1
 print(d,t,c,sum(d))
 if(len(set(d))<=2):
  if(c==len(d) or sum(d)==((t*(c+1))+1) or sum(d)==((t*c)+1)):
   return "YES"
  else:
   return "NO"
 else:
  return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
