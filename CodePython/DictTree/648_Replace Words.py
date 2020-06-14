class Node:
    def __init__(self, value=None):
        self.val = value
        self.is_leaf = False
        self.children = {}


class Tire:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for w in word:
            if node.children.get(w, None) is None:
                node.children[w] = Node(w)
            node = node.children[w]
        node.is_leaf = True

    def search(self, word):
        node = self.root
        path = ''
        for w in word:
            if node.children.get(w, None) is None:
                return ''
            node = node.children[w]
            path += w
            if node.is_leaf:
                return path


class Solution:
    def replaceWords(self, dict, sentence):
        tire = Tire()
        for word in dict:
            tire.insert(word)
        list_sentence = sentence.split(' ')
        ans = []
        for word in list_sentence:
            cur = tire.search(word)
            if len(cur):
                ans.append(cur)
            else:
                ans.append(word)
        return ' '.join(ans)

dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
solution = Solution()
print(solution.replaceWords(dict, sentence))
