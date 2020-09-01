#Author : Arpit Shukla
#Date : 2nd September, 2020

# Hackerrank Delete a Node Solution Python

def deleteNode(head, position):
    if head is None:
        return head
    temp=head
    if position ==0:
        t=head.next
        head=None
        return t
    for i in range(position):
        prev=temp
        temp=temp.next
    prev.next=temp.next
    temp=None
    return head