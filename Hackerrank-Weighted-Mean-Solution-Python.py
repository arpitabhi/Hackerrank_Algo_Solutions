# Enter your code here. Read input from STDIN. Print output to STDOUT

#Author : Arpit Shukla
#Date : 28th May, 2020

#Hackerrank Day 0: Weighted Mean Solution Python


n=int(input())
ele=list(map(int,input().split()))
weight = list(map(int,input().split()))

sum1=0
for i in range(len(ele)):
    sum1+=ele[i]*weight[i]
a=sum1/sum(weight)
print("%.1f" % a)