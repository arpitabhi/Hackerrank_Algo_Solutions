#Author : Arpit Shukla
#Date : 26th May, 2020

# Hackerrank String Validation Solution Python

import re
if __name__ == '__main__':
    s = input()
    # Solution 1 : Brute Force
    '''
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
    '''
    # Solution 2: Using RegEx
    if re.search('[a-zA-Z0-9]',s):
        print("True")
    else:
        print("False")
    if re.search('[a-zA-Z]',s):
        print("True")
    else:
        print("False")
    if re.search('[0-9]',s):
        print("True")
    else:
        print("False")
    if re.search('[a-z]',s):
        print("True")
    else:
        print("False")
    if re.search('[A-Z]',s):
        print("True")
    else:
        print("False")
