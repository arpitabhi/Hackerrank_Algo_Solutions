#Author : Arpit Shukla
#Date : 27th May, 2020

# Hackerrank Alphabet Rangoli Solution Python

def print_rangoli(size):
    # your code goes here
    All="abcdefghijklmnopqrstuvwxyz"
    width=size*4-3
    string=""
    l_string=""
    r_string=""
    if size>1:
        for i in range(size-1,0,-1):
            string=l_string+"-"+All[i]+"-"+r_string
            print(string.center(width,"-"))
            l_string=string[:(len(string)+1)//2]
            r_string=string[(len(string)+1)//2-1:]
        string=l_string[1:]+"-a-"+r_string[:len(r_string)-1]
        print(string)
        for i in range(1,size):
            t=(len(string)-3)//2
            l_string=string[:t]
            if t-2>0:
                r_string=string[-(t-1):]
            else:
                r_string=""
            string=l_string+r_string
            print(string.center(width,"-"))
    else:
        print("a")


if __name__ == '__main__':