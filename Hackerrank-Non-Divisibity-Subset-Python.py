#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    #Solution 1: 
    '''
    q=[]
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            if (s[i]+s[j])%k!=0:
                q.append(s[i]+s[j])
              
    #w=[]
    #for i in q:
    #    if i not in w:
    #        w.append(i)
    #print(w)
    return len(q)
    '''
    #Solution 2:
    '''
    q=[]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if (s[i]+s[j])%k!=0:
                q.append(s[i])
                
    
    print(len(q))
    e=[]
    for i in q:
        if i not in e:
            e.append(i)
    print(e)

    d=[]
    for i in e:
        for j in s:
            if i==j:
                d.append(i)
    #print(w)
    return len(e)
    '''
    
    #Solution 3: 
    '''
    master=[]
    # making list of possible subsets

    for i in s:
        l=[i]
        r=s
        r.pop(r.index(i))
        for j in r:
            o=0
            for u in l:
                if (j+u)%k!=0:
                    o+=1
            if o==len(l):
                l.append(j)
        master.append(l)
    
    max1=0
    for i in master:
        if len(i)>max1:
            max1=len(i)
    return max1
    '''

    #Solution 4: 
    # creating a list of reminder frequency
    f=[0 for i in range(k)]

    for i in s:
        f[i%k]+=1
    # if the reminder is divisible by 2 ...that means if the frequency of that reminder 
    #increases it becomes divisible by k

    if k%2==0:
        f[k//2]=min(f[k//2],1)
    
    # Same is the case with reminder 0... One of the occurence of such number is not 
    # issue but frequency more than 1 leads to divisibility
    res=min(f[0],1)

    #now just add the maximum frequency out of i or k-i reminders
    
    for i in range(1,k//2+1):
        res+=max(f[i],f[k-i])

    return res
    

                    
        




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#Non Divisible Subset Hackerrank Solution in Python
