from collections import defaultdict

class TireNode:
    def __init__(self, val=None):
        self.val = val
        self.leaf = False
        self.children = defaultdict(list)


class Tire:
    def __init__(self):
        self.root = TireNode()

    def add(self, word):
        root = self.root
        for v in word:
            if v not in root.children:
                root.children[v] = TireNode(v)
            root = root.children[v]
        root.leaf = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        # 按单词长度排序,从最短的单词开始建立前缀树.
        # 后续的单词依次进行遍历和插入
        def search(root, word, cur_match):
            if len(word) == 0:
                return root == TireTree.root and cur_match>1
            cur_char = word[0]
            flag = False
            if cur_char in root.children:
                root = root.children[cur_char]
                if root.leaf:
                    flag = flag or search(TireTree.root, word[1:], cur_match+1)
                flag = flag or search(root, word[1:], cur_match)
            return flag

        words.sort(key=lambda x: len(x))
        TireTree = Tire()
        for word in words:
            TireTree.add(word)
        ans = []
        for word in words:
            if search(TireTree.root, word, 0):
                ans.append(word)
        return ans

# words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["cat", "dog", "catdog"]
s = Solution()
print(s.findAllConcatenatedWordsInADict(words))