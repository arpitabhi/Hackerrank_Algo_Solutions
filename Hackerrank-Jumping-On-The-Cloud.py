#!/bin/python3
# Author : Arpit Shukla
# Date : 17th May,2020

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    #Solution 1 : High Space complexity
    '''
    d=f=0
    while d+1<len(c):
        if d+2<len(c):
            if c[d+2]==0:
                d+=2
        else:
            d+=1
        f+=1
    return f
    '''
    # Solution 2: 
    d=f=0
    while d+1<len(c):
        if d+2<len(c) and c[d+2]==0:
            d+=2
        else:
            d+=1
        f+=1
    return f

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
