#!/bin/python3
#Author Arpit Shukla
#Date 14th May, 2020

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    count=0
    e=n
    while(e>0):
        t=e%10
        e=e//10
        if t==0:
            pass
        elif n%t==0:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
	
#Find Digits Hackerrank Solution in Python
