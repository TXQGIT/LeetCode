#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    while head!=None:
        print(head.val, end='')
        print('->', end='')
        head = head.next
    print('None')

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    reverse = None
    while head!=None:
        temp = head
        head = head.next
        temp.next = reverse
        reverse = temp
    return reverse

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = fast = head
    while slow!=None and fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next
    if fast!=None:
        slow = slow.next
        slow = reverseList(slow)
    else:
        slow = reverseList(slow)
    while slow!=None:
        if slow.val!=head.val:
            return False
        slow = slow.next
        head = head.next
    return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(1)
print_list(l1)

print(isPalindrome(l1))