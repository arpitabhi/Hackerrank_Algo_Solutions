#Author : Arpit Shukla
#Date : 5th August 2020

#Hackerrank Dynamic Array Python Solution


def dynamicArray(n, queries):
    # Write your code here
    seqlist=[]
    x=0
    final=[]
    for i in range(n):
        seqlist.append([])
    for i in queries:
        if i[0]==1:
            b=((i[1]^x)%n)
            sec=i[2]
            seqlist[b].append(sec)
        elif i[0]==2:
            b=((i[1]^x)%n)
            sec=i[2]%len(seqlist[b])
            x=seqlist[b][sec]
            final.append(x)

    return final