#!/bin/python3
#Author : Arpit Shukla
# Date : 15th May, 2020

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    
    i,j=int(math.sqrt(a)),int(math.sqrt(b))
    if i!=j:
        mid=j-i-1
    else:
        if i*i==a:
            return 1
        else:
            return 0
    print(a,i,b,j,mid)
    if i*i==a:
        mid+=1
    
    if j*j<=b:
        mid+=1
    return mid
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

#Sherlock and Squares Hackerrank Solution in Python
