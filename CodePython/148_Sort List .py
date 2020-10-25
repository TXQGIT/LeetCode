# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeList(self, h1, h2):
        dummyNode = ListNode()
        curNode = dummyNode
        while h1 and h2:
            if h1.val<= h2.val:
                curNode.next = h1
                h1 = h1.next
                curNode = curNode.next
            else:
                curNode.next = h2
                h2 = h2.next
                curNode = curNode.next
        if h1:
            curNode.next = h1
        if h2:
            curNode.next = h2
        return dummyNode.next

    def sortList(self, head):
        # 采用归并排序
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        h1 = self.sortList(head)
        h2 = self.sortList(mid)
        head = self.mergeList(h1, h2)
        return head

s = Solution()
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
a = s.sortList(head)