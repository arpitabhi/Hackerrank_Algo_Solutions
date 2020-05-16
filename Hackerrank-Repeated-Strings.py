# -*- coding: utf-8 -*-
"""
Created on Sun May 17 02:30:00 2020

@author: arpit
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    # Solution 1
    '''
    if s!="a":
        s1=s[:(n%len(s))+1]
    else:
        s1=""

    t=0
    for i in s:
        if i=="a":
            t+=1
    y=0
    for i in s1:
        if i=="a":
            y+=1
    return ((n//len(s))*t+y)
    '''

    #Solution 2: Not passing because of space complexity and Memory Error
    '''
    if n%len(s)!=0:
        s=(n//len(s))*s+s[:n%len(s)]
        t=0
        for i in s:
            if i=="a":
                t+=1
        #print("ONE")
        return t
    else:
        y=0
        for i in s:
            if i=="a":
                y+=1
        #print("TWO")
        return y*n//len(s)
    '''

    # Solution 3 : The final Solution
    
    if n%len(s)!=0:
        s1=s[:n%len(s)]
        t=0
        for i in s:
            if i=="a":
                t+=1
        #print("ONE")
        d=0
        for i in s1:
            if i=="a":
                d+=1
        return t*(n//len(s))+d
    else:
        y=0
        for i in s:
            if i=="a":
                y+=1
        #print("TWO")
        return y*n//len(s)


    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
