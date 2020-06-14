class Node:
    def __init__(self):
        self.is_leaf = False
        self.chiildren = {}

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node = self.root
            for w in word:
                if w not in node.chiildren:
                    node.chiildren[w] = Node()
                node = node.chiildren[w]
            node.is_leaf = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        def search_recurve(root, word, replaced):
            if len(word) == 0:
                if root.is_leaf and replaced:  #字符匹配到末尾，如果字典树有匹配的，且替换过字符了 hello和hello不满足题意
                    return True
                else:
                    return False
            cur = word[0]
            ans = False
            for v in root.chiildren.keys():  #对每个分支都进行匹配
                if cur==v:
                    ans = ans | search_recurve(root.chiildren[v], word[1:], replaced)
                else:
                    if not replaced:  #回溯
                        replaced = True
                        ans = ans | search_recurve(root.chiildren[v], word[1:], replaced)
                        replaced = False
                if ans:
                    break
            return ans
        return search_recurve(self.root, word, False)

# Your MagicDictionary object will be instantiated and called as such:
dict = ["hello","hallo","leetcode"]
obj = MagicDictionary()
obj.buildDict(dict)
print(obj.search("hello"))
print(obj.search("hhllo"))
print(obj.search("hell"))
print(obj.search("leetcoded"))

# dict = ["hello","hallo","leetcode","judge", "judgg"]
# obj = MagicDictionary()
# obj.buildDict(dict)
# print(obj.search("juggg"))