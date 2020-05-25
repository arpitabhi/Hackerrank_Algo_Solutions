# Author : Arpit Shukla
# Date : 26th May, 2020

# Hackerrank Text Wrap Solution Python

import textwrap

def wrap(string, max_width):
	# Solution 1 : Brute Force
	'''
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
	'''

    # Solution 2 : Using TextWrap Library
    text=textwrap.TextWrapper(width=max_width)
    text_List=text.wrap(string)
    s=""
    for i in range(len(text_List)):
        if i!=len(text_List)-1:
            s+=text_List[i]+'\n'
        else:
            s+=text_List[i]

    return s
    


    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)