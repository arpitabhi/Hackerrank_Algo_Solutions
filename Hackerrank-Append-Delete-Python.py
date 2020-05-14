#!/bin/python3
#Author : Arpit Shukla
#Date : 14th May, 2020

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):

    # Solution 1
    '''
    if s==t and k==(2*len(s)+1):
        return "Yes"
    else:
        if len(s)>len(t):
            i=0
            while i<len(t):
                if s[i]!=t[i]:
                    
                    break
                i+=1
            if (len(s)-i)==0:
                if len(s)+len(t)-2*i+1==k:
                    return "Yes"
                else:
                    return "No"
            else:
                if len(s)+len(t)-2*i==k:
                    return "Yes"
                else:
                    return "No"
        else:
            i=0
            r=0
            while i<len(s):
                if s[i]!=t[i]:
                    r=i
                    break
                i+=1
            if len(s)-i==0:
                if len(s)+len(t)-2*r+1==k:
                    return "Yes"
                else:
                    return "No"
            else:
                if len(s)+len(t)-2*r==k:
                    return "Yes"
                else:
                    return "No"


    '''
    #Solution 2:
    '''
    i=0
    while i<min(len(s),len(t)):

        if s[i]!=t[i]:
            break
        i+=1
    f=len(s)+len(t)-2*i
    
    if s==t:
        f=len(t)*2+1
    elif i==min(len(s),len(t)):
        f=abs(len(s)-len(t))
    
    print(f)
    if f==k:
        return "Yes"
    else:
        return "No"
    '''

    #Solution 3

    if ((len(s) + len(t)+1)<= k): 
        return "Yes"
  
    # finding common length of both string 
    u = 0
    for i in range(0, min(len(s), len(t))): 
        if (s[i] == t[i]): 
            u += 1
        else: 
            break
  
    # Case A (ii)- 
    if k//(len(s)+len(t)-(2*i))>0:
        return "Yes"
    '''
    if ((k - len(s) - len(t) + 2 *commonLength) % 2 == 0): 
        return "Yes"
    '''
  
    # Case B- 
    return "No"





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
