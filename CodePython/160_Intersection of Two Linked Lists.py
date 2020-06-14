#!/usr/bin/env python
from LinkList import *

def getIntersectionNode(headA, headB):
    p1, p2 = headA, headB
    while p1 != p2:
        # 结束条件(1.找到交点，p1和p2都位于交点. 2.没有交点，p1,p2都把headA,headB遍历完且同时到达None)
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    return p1

if __name__=='__main__':
    l1 = [4,1]
    l2 = [5,0,1]
    l3 = [8,3,5]
    link1 = initLinkList_from_list(l1)
    link2 = initLinkList_from_list(l2)
    link3 = initLinkList_from_list(l3)
    appedLinkList(link1, link3)
    appedLinkList(link2, link3)
    l = getIntersectionNode(link1, link2)
    print(l)