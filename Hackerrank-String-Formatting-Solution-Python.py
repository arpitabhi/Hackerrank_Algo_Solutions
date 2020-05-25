# Author : Arpit Shukla
# Date : 26th May, 2020

#Hackerrank String Formatting Solution Python

def print_formatted(number):
    # your code goes here
    
    #u=len('{} {} {} {}'.format(number,oct(number)[2:],hex(number)[2:],bin(number)[2:]))
    #print(u)
    r=len('{}'.format(bin(number)[2:]))

    #t=textwrap.TextWrapper(r)
    for i in range(1,number+1):
        print(('{}'.format(i)).rjust(r," "),end=" ")
        print(('{}'.format(oct(i)))[2:].rjust(r," "),end=" ")
        print((('{}'.format(hex(i)))[2:].upper()).rjust(r," "),end=" ")
        print(('{}'.format(bin(i)))[2:].rjust(r," "))
        

if __name__ == '__main__':