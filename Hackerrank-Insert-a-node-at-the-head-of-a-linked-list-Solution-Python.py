#Author : Arpit Shukla
#Date : 2nd September, 2020

# Hackerrank Insert a node at the head of a linked list Solution Python

def insertNodeAtHead(llist, data):
    # Write your code here
    q=SinglyLinkedListNode(data)

    q.next=llist
    return q