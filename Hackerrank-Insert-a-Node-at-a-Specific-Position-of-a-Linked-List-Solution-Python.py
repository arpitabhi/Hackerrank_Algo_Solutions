#Author : Arpit Shukla
#Date : 2nd September, 2020

# Hackerrank Insert a Node at a specific position of a Linked List Solution Python


def insertNodeAtPosition(head, data, position):
    
    q=SinglyLinkedListNode(data)

    W=head
    if head is None:
        head=q
        return head
    for i in range(position-1):
        W=W.next
    q.next=W.next
    W.next=q
    return head