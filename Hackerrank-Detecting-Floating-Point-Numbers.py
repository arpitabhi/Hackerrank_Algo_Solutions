# Enter your code here. Read input from STDIN. Print output to STDOUT

# Author : Arpit Shukla
# Date : 21st, May,2020
# Detecting Floating point Numbers Hackerrank Solution Python


N=int(input())
num=[]
for i in range(N):
    t=str(input())
    num.append(t)


for i in num:
    if i[0]=="+" or i[0]=="-":
        i=i[1:]
    if "." in i:
        print(i.replace(".","",1).isdigit())
    else:
        print("False")


