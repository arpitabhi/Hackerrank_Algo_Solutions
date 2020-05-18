# Enter your code here. Read input from STDIN. Print output to STDOUT



a=int(input())

# for creating a list of input numbers
#set is required for symmteric_difference calculations
eng=set(list(input().split()))

b=int(input())
fren=list(input().split())

# Here the Symmetric Difference is use that is (a U b) - (a inter b)
c=eng.symmetric_difference(fren)
print(len(c))
