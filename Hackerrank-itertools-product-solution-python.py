# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Arpit Shukla
# Date : 27th May, 2020

# Hackerrank itertools product solution python


from itertools import product

def cartproduct(A,B):
    ls=sorted(list(product(A,B)))
    print(*ls)
    

A=list(map(int,input().split()))
B=list(map(int,input().split()))

cartproduct(A,B)