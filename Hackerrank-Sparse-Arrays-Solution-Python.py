#Author : Arpit Shukla
#Date : 5th August, 2020

#Hackerrank-Sparse-Arrays-Solution-Python


def matchingStrings(strings, queries):
    freq=[]
    for i in queries:
        x=0
        for j in strings:
            if i==j:
                x+=1
        freq.append(x)
    return freq