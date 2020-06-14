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

        # 方法2：中序遍历
        def rserialize(root, string):
            if root is None:
                string += 'None,'
            else:
                string = rserialize(root.left, string)
                string += str(root.val) + ','
                string = rserialize(root.right, string)
            return string

        string = ''
        return rserialize(root, string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # 方法1：从先序遍历中恢复
        # def rdeserialize(data):
        #     if data[0]=='None':
        #         data.pop(0)
        #         return None
        #     root = TreeNode(data[0])
        #     data.pop(0)
        #     root.left = rdeserialize(data)
        #     root.right = rdeserialize(data)
        #     return root

        # 方法2：从中序遍历中恢复
        def rdeserialize(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            left = TreeNode(data[0])
            data.pop(0)

            left = rdeserialize(data)
            root = TreeNode(data[0])
            data.pop(0)
            right = rdeserialize(data)
            root.left = left
            root.right = right
            return root

        data = data.split(',')
        data.pop(0)
        root = rdeserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
codec = Codec()
codec.deserialize(codec.serialize(root))