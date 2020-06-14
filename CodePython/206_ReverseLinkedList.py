#!/usr/bin/env python 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = head
    reverse = None
    while cur:
        temp = cur
        cur = cur.next
        temp.next = reverse
        reverse = temp
    return reverse

def print_list(head):
    while head!=None:
        print(head.val, end='')
        print('->', end='')
        head = head.next
    print('None')

one = ListNode(3)
two = ListNode(1)
three = ListNode(2)
one.next = two
two.next = three

print_list(one)  #3->1->2->None

result = reverseList(one)

print_list(one)  #3->None
print_list(result)