#Author : Arpit Shukla
# Date : 21st May, 2020


if __name__ == '__main__':
    '''
    arr={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #arr.append([name,score])
        arr[name]=score

    #print(arr)

    dic1={}
    for i in range(len(arr)):
        dic1[arr[i][0]]=arr[i][1]
    x=sorted(dic1.values)
    print(x)
    
    #print(sorted(arr.values))

    x={k: v for k, v in sorted(arr.items(), key=lambda item: item[1])}
    print(x)

    '''
    # Akash Solution : 

    '''
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=[name,score]
        l.append(a)
    # print(l)
    l.sort(key=lambda a : a[1],reverse=True)
    # print(l)
    x=3
    k= l[-2]
    k=list(k)
    # print(k)
    while(l[-2][1]==l[-x][1]):
        #print(k)
        k.append(l[-x][0])
        k.append(l[-x][1])
        x+=1


    # print(k)
    x=k

    y=[]
    z=[]
    for i in range(0,len(x)-1,2):
        y.append(x[i])
        z.append(x[i+1])
        i+=1
    y.sort()
    for i in range(len(y)):
        print(y[i])
    #print(z[i])
    #k.sort(key=lambda k : k[0])
    # for i in range(len(k)+1):
    #     print(k[i])
    '''
    # Solution : Final One
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        #arr[name]=score
    #Sorting here 1. Score then with 2. Name Alphabetically
    arr.sort(key= lambda x : (x[1],x[0]))
    
    #Creating a list of Second Highest Score list 
    mini=arr[0][1]
    l1=[]
    sec_min=mini
    #Iterating over the Length of List

    for i in range(1,len(arr)):
        if arr[i][1]>mini:
            #Only when the Second Minimum is founf
            sec_min=arr[i][1]
            l1.append(arr[i])
            #Now appending all the Elements with Second Minimum Score
            for j in range(i+1,len(arr)):
                if arr[j][1]==sec_min:
                    l1.append(arr[j])
                else:
                    #Breaking the Second Loop
                    break
            #Breaking the First loop 
            break

        
    # Priting the Names of Second Minimum Score
    for i in range(len(l1)):
        print(l1[i][0])




