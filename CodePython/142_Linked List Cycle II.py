# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        def getIntersect(head):
            slow = head
            fast = head
            count = 0
            while slow and fast:
                count += 1
                if count % 2:
                    fast = fast.next
                else:
                    fast = fast.next
                    slow = slow.next
                if slow == fast:
                    return slow
            return None

        if head is None:
            return None
        meet_node = getIntersect(head)
        if meet_node is None:
            return None
        p1 = head
        p2 = meet_node
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


head = p = ListNode(3)
p.next = c = ListNode(2)
c.next = ListNode(0)
c.next.next = ListNode(-4)
c.next.next.next = c
solution = Solution()
ans = solution.detectCycle(head)
