# -*- coding: utf-8 -*-
"""
Created on Fri May 15 05:59:16 2020

@author: arpit
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    
    #Finding Unique Values in arr
    q=[]
    for i in arr:
        if i not in q:
            q.append(i)
    
    #Finding frequencies of elements of q in arr
    w=[]
    for i in q:
        e=0
        for j in arr:
            if i==j:
                e+=1
        w.append(e)

    # Making a list of Cummalative decresing frequencies of Elements of arr
    r=[]
    t=len(arr)
    y=len(q)
    for i in range(y):
        r.append(t)
        s=q.index(min(q))
        t=t-w[s]
        q.pop(s)
        w.pop(s)

    
    return r


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
	
#Cut the Stick Hackerrank Solution in Python
