class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict

        def build_graph(wordList):
            graph = defaultdict(set)
            visited = defaultdict(bool)
            for w in wordList:
                for i in range(len(w)):
                    partten_w = list(w)
                    partten_w[i] = '*'
                    partten_w = ''.join(partten_w)
                    graph[w].add(partten_w)
                    graph[partten_w].add(w)
                    visited[w] = False
                    visited[partten_w] = False
            return graph, visited

        def dfs(vertex, path, cur_path):
            visited[vertex] = True
            if vertex == endWord:
                path.append(cur_path[:])
                return
            if visited[endWord]:
                return
            for adj in graph[vertex]:
                if not visited[adj]:
                    cur_path.append(adj)
                    dfs(adj, path, cur_path)
                    cur_path.pop()

        if endWord not in wordList:
            return []
        graph, visited = build_graph([beginWord] + wordList)
        path = []
        dfs(beginWord, path, [beginWord])
        path = path[0]
        ans = []
        for v in path:
            if '*' not in v:
                ans.append(v)
        return ans


s = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
beginWord = "hot"
endWord = "dog"
wordList =["hot","dog"]
print(s.findLadders(beginWord, endWord, wordList))
