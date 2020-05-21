#Author : Arpit Shukla
#Date : 22st May,2020

regex_pattern = "[,.]"	# Do not delete 'r'.
#Solution 2
'''
x=str(input())
ls=[]
start=0
end=0
for i in range(len(x)):
    if (x[i]=="," or x[i]==".") and start==0:
        ls.append(x[start:i])
        start=i+1
    elif x[i]=="," or x[i]==".":
        ls.append(x[start:i])
        start=i+1
    elif i==len(x)-1:
        ls.append(x[start:i+1])
for i in ls:
    print(i)

'''
import re
print("\n".join(re.split(regex_pattern, input())))