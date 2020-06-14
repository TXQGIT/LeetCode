# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    if root==None:
        return ''
    queue = [root]
    val = [str(root.val)]
    while len(queue):
        root = queue.pop(0)
        if root.left:
            queue.append(root.left)
            val.append(str(root.left.val))
        else:
            val.append('null')
        if root.right:
            queue.append(root.right)
            val.append(str(root.right.val))
        else:
            val.append('null')
    while val[-1]=='null':
        val.pop()
    return ' '.join(val)
        
    

def deserialize(data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    vals = data.split()
    n = len(vals)
    if n==0:
        return None
    root = TreeNode(int(vals[0]))
    
    def func(root, idx):
        l_idx = 2*idx+1
        r_idx = 2*idx+2
        if l_idx<n:
            l_val = vals[l_idx]
            if l_val!='null':
                root.left = TreeNode(int(l_val))
                func(root.left, l_idx)
        if r_idx<n:
            r_val = vals[r_idx]
            if r_val!='null':
                root.right = TreeNode(int(r_val))
                func(root.right, r_idx)
    
    func(root,0)
    return root

data = '5 2 3 null null 2 4 3 1'
root = deserialize(data)
s_data = serialize(root)
print(s_data)