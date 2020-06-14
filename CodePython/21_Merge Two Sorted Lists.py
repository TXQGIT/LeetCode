#!/usr/bin/env python
from LinkList import *

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    dummyHead = ListNode(0)
    preNode = dummyHead
    while l1 and l2:
        if l1.val <= l2.val:
            preNode.next = l1
            l1 = l1.next
        else:
            preNode.next = l2
            l2 = l2.next
        preNode = preNode.next
    preNode.next = l1 if l1 else l2
    return dummyHead.next

# l1 = [1,2,4]
# l2 = [1,3,4]
l1 = []
if l1:
    print(True)
l2 = [1,3,4]
link1 = initLinkList_from_list(l1)
link2 = initLinkList_from_list(l2)
l = mergeTwoLists(link1, link2)
l.LinkWalk()