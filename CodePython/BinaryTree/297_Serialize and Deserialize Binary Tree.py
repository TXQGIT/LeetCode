# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # 方法1：先序遍历
        # def rserialize(root, string):
        #     if root is None:
        #         string += 'None,'
        #     else:
        #         string += str(root.val)+','
        #         string = rserialize(root.left, string)
        #         string = rserialize(root.right, string)
        #     return string
        # string = ''
        # return rserialize(root, string)

        # 先序遍历, 并且在遍历序列中保留每个叶子节点的None值
        res = []
        queue = []
        while root or queue:
            while root:
                res.append(str(root.val))
                queue.append(root)
                root = root.left
            res.append('None')
            root = queue.pop()
            root = root.right
        ans = ','.join(res)
        return ans


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        #方法1：从先序遍历中恢复
        # def rdeserialize(data):
        #     if data[0]=='None':
        #         data.pop(0)
        #         return None
        #     root = TreeNode(data[0])
        #     data.pop(0)
        #     root.left = rdeserialize(data)
        #     root.right = rdeserialize(data)
        #     return root

        def rdeserialize(data):
            if len(data)==0:
                return None
            val = data.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = rdeserialize(data)
            root.right = rdeserialize(data)
            return root

        if len(data)==0:
            return None
        data = data.split(',')
        root = rdeserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
ans = codec.deserialize(codec.serialize(None))