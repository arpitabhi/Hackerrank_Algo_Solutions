# Author : Arpit Shukla
# Date : 24th May,2020

#Hackerrank Tuples Solution Python

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))