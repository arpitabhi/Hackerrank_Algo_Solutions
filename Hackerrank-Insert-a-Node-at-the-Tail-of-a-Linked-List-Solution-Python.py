#Author : Arpit Shukla
#Date : 2nd September, 2020

# Hackerrank Insert a Node at the Tail of a Linked List Solution Python


def insertNodeAtTail(head, data):
    q=SinglyLinkedListNode(data)
    
    if head is None:
        head=q
        return head

    d=head
    while (d.next):
        d=d.next
    d.next=q
    return head