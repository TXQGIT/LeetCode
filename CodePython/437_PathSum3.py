# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    def inorder(root, cur_path, cur_sum, sum, path):
        cur_path.append(root.val)
        cur_sum += root.val
        #is_leaf = root.left==None and root.right==None
        #if cur_sum==sum and is_leaf:
        if cur_sum==sum:
            path.append(cur_path[:])
        if root.left!=None:
            inorder(root.left, cur_path, cur_sum, sum, path)
        if root.right!=None:
            inorder(root.right, cur_path, cur_sum, sum, path)
        cur_path.pop()
        cur_sum -= root.val
    
    if root==None:
        return 0
    path = []
    stack = []
    node = root
    while len(stack) or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        inorder(node, [], 0, sum, path)
        node = node.right

    print(path)
    return len(path)

def tree_init():
    root = TreeNode(10)

    root.left = TreeNode(5)
    root.right = TreeNode(-3)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    return root

root = tree_init()
pathSum(root, 8)