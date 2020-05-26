# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
S=list(input().split())
S[1]=int(S[1])

# Author : Arpit Shukla
# Date : 27th May, 2020

# Hackerrank Itertools Combination Solution Python

def comb(S,n):
    S=[S[i:i+1] for i in range(len(S))]
    S.sort()
    ls=list(combinations(S,n))
    t=[]
    for i in ls:
        u=""
        for j in i:
            u+=j
        t.append(u)
    t.sort()
    return t
b=[]
for i in range(1,S[1]+1):
    b.append(comb(S[0],i))
for i in b:
    for j in i:
        print(j)
