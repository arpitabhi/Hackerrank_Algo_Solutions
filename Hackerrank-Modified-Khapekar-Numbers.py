#!/bin/python3
# Author : Arpit Shukla
# Date : 19th May, 2020

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):

    t=[]
    for i in range(p,q+1):
        a=str(i)
        b=str(i*i)
        d=len(b)-len(a)
        if len(b)>1:
            c=int(b[:d]) + int(b[d:])
        else:
            c=int(b)


        if c==i:
            t.append(i)
    if len(t)>0:
        print(*t)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

#Modified Khapekar Number Hackerrank Solution in Python
