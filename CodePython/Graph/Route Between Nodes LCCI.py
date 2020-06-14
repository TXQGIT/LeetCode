class Solution:
    def findWhetherExistsPath(self, n, graph, start, target):
        from collections import defaultdict

        def dfs(v):
            visited[v] = True
            for adj in graph_adj[v]:
                if not visited[adj]:
                    print(v, '->', adj)
                    dfs(adj)
            return None

        def build_graph(edges):
            graph = defaultdict(list)
            for tail, head in edges:
                graph[tail].append(head)
            return graph

        graph_adj = build_graph(graph)
        visited = [False] * n
        dfs(start)
        return True if visited[target] else False

n = 12
edges = [[0, 1], [1, 2], [1, 3], [1, 10], [1, 11], [1, 4], [2, 4], [2, 6], [2, 9], [2, 10], [2, 4], [2, 5], [2, 10], [3, 7], [3, 7], [4, 5], [4, 11], [4, 11], [4, 10], [5, 7], [5, 10], [6, 8], [7, 11], [8, 10]]
start = 2
target = 3
s = Solution()
print(s.findWhetherExistsPath(n, edges, start, target))