# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        leave_level = 0
        node = root
        while node:
            node = node.left
            leave_level += 1
        leave_count = 0
        stack = []
        level = 1
        while root or len(stack):
            while root:
                stack.append([root, level])
                root = root.left
                level += 1
            root, level = stack.pop()
            if root.left is None and root.right is None:
                if level==leave_level:
                    leave_count += 1
                else:
                    break
            root = root.right
            level += 1
        return 2**(leave_level-1)-1+leave_count

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
s = Solution()
print(s.countNodes(root))