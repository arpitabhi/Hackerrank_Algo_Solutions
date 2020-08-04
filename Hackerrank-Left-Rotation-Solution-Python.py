#Author : Arpit Shukla
#Date : 5th August, 2020

#Hackerrank Left Rotation Solution Python



#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    for i in range(d):
        b=a[0]
        a.pop(0)
        a.append(b)
    print(*a)