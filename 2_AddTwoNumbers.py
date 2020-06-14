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

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = l3 = ListNode(None)
    carry = 0  #进位
    while l1!=None and l2!=None:
        sum_cur = l1.val+l2.val+carry
        digit = int(sum_cur%10)
        carry = int(sum_cur/10)
        l3.next = ListNode(digit)
        l3 = l3.next
        l1 = l1.next
        l2 = l2.next
    while l1!=None:
        sum_cur = l1.val+carry
        digit = int(sum_cur%10)
        carry = int(sum_cur/10)
        l3.next = ListNode(digit)
        l3 = l3.next
        l1 = l1.next
    while l2!=None:
        sum_cur = l2.val+carry
        digit = int(sum_cur%10)
        carry = int(sum_cur/10)
        l3.next = ListNode(digit)
        l3 = l3.next
        l2 = l2.next
    if carry!=0:
        l3.next = ListNode(carry)
        l3 = l3.next
    return head.next

l1 = ListNode(9)
l1.next = ListNode(1)
l1.next.next = ListNode(6)
print_list(l1)

l2 = ListNode(0)
print_list(l2)

print_list(addTwoNumbers(l1, l2))
print_list(l1)