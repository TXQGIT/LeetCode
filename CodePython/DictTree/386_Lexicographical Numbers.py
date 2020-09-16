class Node:
    def __init__(self, val=None):
        self.val = val
        self.is_leaf = False
        self.children = {}


class Tire:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        node.is_leaf = True


class Solution:
    def lexicalOrder(self, n):
        # #方法1：构建前缀树，然后进行先序遍历
        # def num_split(v):
        #     ans = []
        #     while v:
        #         ans.append(v % 10)
        #         v = v // 10
        #     return ans[::-1]
        #
        # def preorder_walk(pre_level_val, root):
        #     children = sorted(list(root.children.keys()))
        #     for c in children:
        #         cur_val = pre_level_val * 10 + c
        #         ans.append(cur_val)
        #         preorder_walk(cur_val, root.children[c])
        #
        # prefix_tree = Tire()
        # for i in range(1, n + 1):
        #     prefix_tree.insert(num_split(i))
        # ans = []
        # preorder_walk(0, prefix_tree.root)
        # return ans

        #方法2:直接用DFS
        def dfs(n, cur):
            if cur>n:
                return
            ans.append(cur)
            for i in range(10):
                dfs(n, cur*10+i)
        ans = []
        for i in range(1,10):
            dfs(n,i)
        return ans


s = Solution()
n = 12
print(s.lexicalOrder(n))