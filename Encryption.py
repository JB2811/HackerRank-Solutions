#!/bin/python3

import math
import os
import random
import re
import sys
import math
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
 # Write your code here
 s="".join(s.split(" "))
 l=len(s)
 #r=math.floor(math.sqrt(l))
 c=math.ceil(math.sqrt(l))
 t=[]
 i=0
 while((i+c)<l):
  t.append(s[i:i+c])
  i+=c
 t.append(s[i:])
 r=len(t)
 res=[0 for i in range(r*c+r)]
 j=0
 for i in t:
  q=0
  for k in range(len(i)):
   res[j+k+q]=i[k]
   q+=r
  j+=1
 r=""
 for i in res:
  if(i==0):
   if(r[-1]!=" "):
    r+=" "
   continue
  r+=i
 return r.strip() 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
