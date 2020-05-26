#Author : Arpit Shukla
#Date : 27th May, 2020

#Hackerrank Itertools Permutation Solution Python

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s=list(input().split())
s[1]=int(s[1])

ls=list(permutations(s[0],s[1]))
sorte=[]
for i in range(len(ls)):
    t=""
    for j in ls[i]:
        t+=j
    #print(t)
    sorte.append(t)
sorte.sort()
for i in sorte:
    print(i)


