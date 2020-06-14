class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        from collections import defaultdict
        def dfs(vertex, path):
            visited[vertex] = True
            path.append(vertex)
            for adj in graph[vertex]:
                if not visited[adj]:
                    begin_idx = len(path)
                    dfs(adj, path)
                    end_idx = len(path)
                    if len(apple_vertex.intersection(set(path[begin_idx:end_idx]))) == 0:
                        path[begin_idx:end_idx] = []
                    else:
                        path.append(vertex)

        def build_graph(edges):
            graph = defaultdict(set)
            for u, v in edges:
                graph[u].add(v)
                graph[v].add(u)
            return graph

        apple_vertex = [i for i in range(n) if hasApple[i]]
        apple_vertex = set(apple_vertex)
        graph = build_graph(edges)
        path = []
        visited = [False] * n
        dfs(0, path)
        return len(path) - 1

s = Solution()
n = 5
edges = [[0,1],[0,2],[1,3],[0,4]]
hasApple = [False,False,False,True,False]
print(s.minTime(n, edges, hasApple))

