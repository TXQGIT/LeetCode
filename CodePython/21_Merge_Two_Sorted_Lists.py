#!/usr/bin/env python 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1
    l3 = head = ListNode(None)
    while l1 and l2:
        if l1.val<=l2.val:
            l3.next = l1 #mae l1= 1->1->2->3->4->4->None
            l1 = l1.next
        else:
            l3.next = l2 ##mae l2= 1->2->3->4->4->None
            l2 = l2.next
        l3 = l3.next
    if l1:
        l3.next = l1
    if l2:
        l3.next = l2
    return head.next

def print_list(head):
    while head!=None:
        print(head.val, end='')
        print('->', end='')
        head = head.next
    print('None')

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print_list(l1)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print_list(l2)

result = mergeTwoLists(l1,l2)
print_list(l1)
print_list(l2)
print_list(result)