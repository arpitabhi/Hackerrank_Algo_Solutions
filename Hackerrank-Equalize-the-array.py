#!/bin/python3
#Author : Arpit Shukla
#Date 17th May, 2020

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    r=[]
    for i in arr:
        if i not in r:
            r.append(i)
    t=[]

    for i in r:
        p=0
        for j in arr:
            if i==j:
                p+=1
        t.append(p)
    
    t.pop(t.index(max(t)))
    return sum(t)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
