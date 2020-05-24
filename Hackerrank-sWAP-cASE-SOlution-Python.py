# Author : Arpit Shukla
# Date : 24th May, 2020

# Hackerrank sWap cASE Solution Python

def swap_case(s):
    t=""
    for i in s:
        if i.isupper()==True:
            t+=i.lower()
        else:
            t+=i.upper()

    return t

if __name__ == '__main__':