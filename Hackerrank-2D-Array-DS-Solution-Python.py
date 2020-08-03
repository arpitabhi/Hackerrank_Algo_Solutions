# Author : Arpit Shukla
# Date : 3rd Aug, 2020

# Hackerrank 2D Array - DS Solution Python


def hourglassSum(arr):
    l=[]
    for i in arr:
        for j in i:
            l.append(j)
    p=[]
    for i in range(22):
        if (i+1)%6==0 or (i+2)%6==0:
            pass
        else:
            x=l[i]+l[i+1]+l[i+2]+l[i+7]+l[i+12]+l[i+13]+l[i+14]
            p.append(x)
    #print(p)
    return max(p)