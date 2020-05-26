# Author : Arpit Shukla
# Date : 27th May, 2020

#Hackerrank Itertools Combinations with Replacement Solution Python

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S=list(input().split())
S[1]=int(S[1])

def comb_with_replace(S,n):
    S=[S[i:i+1] for i in range(len(S))]
    S.sort()
    ls=list(combinations_with_replacement(S,n))
    t=[]
    for i in ls:
        u=""
        for j in i:
            u+=j
        t.append(u)
    t.sort()
    return t

for i in comb_with_replace(S[0],S[1]):
    print(i)
