#!/usr/bin/env python

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def LinkWalk(self):
        curNode = self
        walkList = []
        while curNode:
            walkList.append(curNode.val)
            curNode = curNode.next
        print(walkList)


def initLinkList_from_list(nums):
    dummyHead = curNode = ListNode(0)
    for v in nums:
        curNode.next = ListNode(v)
        curNode = curNode.next
    return dummyHead.next

def appedLinkList(oriListNode, appListNode):
    while oriListNode.next:
        oriListNode = oriListNode.next
    oriListNode.next = appListNode