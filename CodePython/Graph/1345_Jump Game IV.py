class Solution:
    def minJumps(self, arr) -> int:
        from collections import defaultdict

        def build_graph(edges):
            graph = defaultdict(set)
            for u, v in edges:
                graph[u].add(v)
                graph[v].add(u)
            return graph

        def create_edges(arr):
            n = len(arr)
            edges = []
            hash_map = defaultdict(list)
            for i in range(n):
                if i+1<n:
                    edges.append([i, i + 1])
                for j in hash_map[arr[i]]:
                    edges.append([j, i])
                hash_map[arr[i]].append(i)
            return edges

        def bfs(graph, n):
            visited = [False] * n
            queue = [0]
            visited[0] = True
            step = 0
            while queue:
                cur_lvl = len(queue)
                step += 1
                while cur_lvl:
                    v = queue.pop(0)
                    cur_lvl -= 1
                    for adj in graph[v]:
                        if adj == n - 1:
                            return step
                        if not visited[adj]:
                            queue.append(adj)
            return step

        edges = create_edges(arr)
        graph = build_graph(edges)
        return bfs(graph, len(arr))

s = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(s.minJumps(arr))