#!/bin/python3
#Author : Arpit Shukla
# Date 14th May,2020

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    #Solution 1 : Recursion
    '''
    if n==1:
        return 1
    else:
        return n*extraLongFactorials(n-1)
    '''

    #Solution 2 : Loops
    t=1
    for i in range(1,n+1):
        t=t*i
    print(t)
    #return t



if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
