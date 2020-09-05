#Author : Arpit Shukla
# Date : 6th Sep, 2020

# Hackerrank Print in Reverse Solution Python


def reversePrint(head):
    if head is None:
        return
    else:
        reversePrint(head.next)
        print(head.data)