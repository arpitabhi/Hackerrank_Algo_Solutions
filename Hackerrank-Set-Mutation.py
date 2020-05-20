# Enter your code here. Read input from STDIN. Print output to STDOUT

# Author : Arpit Shukla
# Date : 19th May, 2020

n=int(input())
A=set(map(int,input().split()))
N=int(input())

for i in range(N):
    (p,q)=input().split()
    s1=set(map(int,input().split()))
    #print(s1)
    if p=="intersection_update":
        #print(A)

        A.intersection_update(s1)
        #print(A)
    elif p=="update":
        A.update(s1)
        #print(A)
    elif p=="symmetric_difference_update":
        A.symmetric_difference_update(s1)
        #print(A)
    else:
        A.difference_update(s1)
        #print(A)
print(sum(A))


