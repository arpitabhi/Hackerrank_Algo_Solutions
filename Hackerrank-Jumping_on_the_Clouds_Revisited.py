#!/bin/python3
#Author : Arpit Shukla


=======
#Date : 14th May, 2020


import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    #Solution 1
    '''
    thun=jump=i=0
    while True:
        jump+=1
        i=(i+k)%len(c)
        if c[i]==1:
            thun+=1
        elif i==0:
            break
    return 100-jump-(thun*2)
    '''
    #Solution 2
    '''
    e=100
    i=0
    while (i+k)%len(c)!=0:
        if c[(i+k)%len(c)]==1:
            e=e-3
        else:
            e=e-1
        i=(i+k)%len(c)
    return e
    '''

    #Solution 3
    E=99
    i=k%len(c)
    if c[i]==1:
        E-=2
    while i!=0:
        E-=1
        i=(i+k)%len(c)
        if c[i]==1:
            E-=2
    return E


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
	
#Jumping on the clouds Revisited Hackerrank Solution in Python
