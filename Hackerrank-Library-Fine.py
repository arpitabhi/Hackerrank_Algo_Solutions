# -*- coding: utf-8 -*-
"""
Created on Fri May 15 05:20:21 2020

@author: arpit
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Solution 1:
    '''
    if y1>y2:
        return 10000
    elif y1==y2:
        if m1>m2:
            return (m1-m2)*500
        elif m1==m2:
            if d1>d2:
                return (d1-d1)*15
    else:
        return 0
    '''

    # Solution 2
    if y1>y2:
        return 10000

    if (y1==y2 and m1>m2):
        return (m1-m2)*500

    if (y1==y2 and m1==m2 and d1>d2):
        return (d1-d2)*15

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
	
#Library Fine Hackerrank Solution in Python


