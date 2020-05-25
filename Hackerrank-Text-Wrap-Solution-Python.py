# Author : Arpit Shukla
# Date : 26th May, 2020

# Hackerrank Text Wrap Solution Python

import textwrap

def wrap(string, max_width):
    p=len(string)//max_width
    j=0
    s=""
    for i in range(p):
        s+=string[j:j+max_width]
        j+=max_width
        if i!=p-1:
            s+='\n'

    q=len(string)%max_width
    if q!=0:
        s+='\n'+string[p*max_width:]
    return s
    


    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)