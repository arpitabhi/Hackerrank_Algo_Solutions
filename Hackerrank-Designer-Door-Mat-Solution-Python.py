# Enter your code here. Read input from STDIN. Print output to STDOUT

# Author : Arpit Shukla
# Date : 26th May, 2020

# Hackerrank Designer Door Mat Solution Python

ls=list(map(int,input().split()))
n=ls[0]//2
m=ls[1]//2
t=1
# Solution 1 : Brute Force
'''
for i in range(1,n+1):
    print('-'*(m-(len('.|.'*t)//2)),end='')
    print('.|.'*t,end="")
    print('-'*(m-(len('.|.'*t)//2)))
    t+=2
k=(ls[1]-7)//2
print('-'*k+'WELCOME'+'-'*k)
for i in range(1,n+1):
    t-=2
    print('-'*(m-(len('.|.'*t)//2)),end='')
    print('.|.'*t,end="")
    print('-'*(m-(len('.|.'*t)//2)))
'''
# Solution 2 : Using Wrapper
t=1
for i in range(1,n+1):
    print(('.|.'*t).center(ls[1],'-'))
    t+=2
print('WELCOME'.center(ls[1],'-'))
for i in range(1,n+1):
    t-=2
    print(('.|.'*t).center(ls[1],'-'))
    

    
