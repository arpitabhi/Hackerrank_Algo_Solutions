#Author : Arpit Shukla
# Date :  24th May, 2020

#Hackerrank Mutation Solution Python

def mutate_string(string, position, character):
    t=string[:position]+character+string[position+1:]
    return t

if __name__ == '__main__':