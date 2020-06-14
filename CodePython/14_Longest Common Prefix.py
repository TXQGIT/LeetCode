class Node:
    def __init__(self, value=''):
        self.val = value
        self.is_leaf = False
        self.children = {}


class Tire:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node(w)
            node = node.children[w]
        node.is_leaf = True


class Solution:
    def longestCommonPrefix(self, strs):
        # 建立前缀树，从跟往下查直到第一个分叉点
        tire = Tire()
        for word in strs:
            tire.insert(word)
        ans = ''
        node = tire.root
        while node and not node.is_leaf:
            ch = list(node.children.keys())
            if len(ch) == 1:
                node = node.children[ch[0]]
                ans += node.val
            else:  # 出现分支
                break
        return ans

#strs = ["flower","flow","flight"]
#strs = ['a']
strs = ['', 'a']
solution = Solution()
print(solution.longestCommonPrefix(strs))