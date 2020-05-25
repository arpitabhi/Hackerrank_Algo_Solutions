#Author : Arpit Shukla
#Date : 26th May, 2020

# Hackerrank String Validation Solution Python

if __name__ == '__main__':
    s = input()
    an=ac=d=l=u=0
    for i in s:
        if i.isalnum():
            an+=1
        if i.isalpha():
            ac+=1
        if i.isdigit():
            d+=1
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
    #print(an,ac,d,l,u)
    if an>0:
        print("True")
    else:
        print("False")
    if ac>0:
        print("True")
    else:
        print("False")
    if d>0:
        print("True")
    else:
        print("False")
    if l>0:
        print("True")
    else:
        print("False")
    if u>0:
        print("True")
    else:
        print("False")
