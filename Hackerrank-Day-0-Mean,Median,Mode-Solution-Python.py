# Enter your code here. Read input from STDIN. Print output to STDOUT

#Author : Arpit Shukla
#Date : 24th May, 2020

n=int(input())
elements=list(map(int,input().split()))
elements.sort()

if len(elements)!=0:
    average=sum(elements)/len(elements)
else:
    average=0

if len(elements)%2!=0:
    median=elements[(len(elements)-1)//2]
else:
    median=(elements[len(elements)//2]+elements[len(elements)//2-1])/2

uni=[]
for i in elements:
    if i not in uni:
        uni.append(i)
freq=[]
for j in uni:
    cout=0
    for k in elements:
        if j==k:
            cout+=1
    freq.append(cout)
mode=uni[freq.index(max(freq))]
print(average)
print(median)
print(mode)


