#Author : Arpit Shukla
#Date : 24th May, 2020
#Hackerrank List Solution Python

if __name__ == '__main__':
    N = int(input())
    ls=[]
    for i in range(N):
        ls.append(list(input().split()))
    #print(ls)
    ori=[]
    for i in ls:
        if i[0]=="insert":
            ori.insert(int(i[1]),int(i[2]))
        elif i[0]=="print":
            print(ori)
        elif i[0]=="remove":
            ori.remove(int(i[1]))
        elif i[0]=="append":
            ori.append(int(i[1]))
        elif i[0]=="sort":
            ori.sort()
        elif i[0]=="pop":
            ori.pop()
        elif i[0]=="reverse":
            ori.reverse()
    