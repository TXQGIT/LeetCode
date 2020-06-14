# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        left = dummy.next
        mid = slow.next
        right = mid.next
        slow.next = None
        mid.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root

s = Solution()
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
print(s.sortedListToBST(head))