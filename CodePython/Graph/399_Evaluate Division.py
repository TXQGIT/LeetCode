class Solution:
    def calcEquation(self, equations, values, queries):
        # 建立有向带权图，然后DFS
        from collections import defaultdict
        def build_graph(edges, values):
            graph = defaultdict(list)
            for i in range(len(equations)):
                [head, tail] = equations[i]
                v = values[i]
                graph[head].append((tail, v))
                graph[tail].append((head, 1 / v))
            return graph

        def dfs(graph, node, cur_path):
            visited[node] = True
            if visited[tail]:
                ans.append(cur_path)
                return
            for (v, e) in graph[node]:
                if not visited[v] and not visited[tail]:
                    dfs(graph, v, cur_path * e)

        ans = []
        graph = build_graph(equations, values)
        for (head, tail) in queries:
            if head in graph.keys() and tail in graph.keys():
                visited = defaultdict(bool)
                for v in graph.keys():
                    visited[v] = False
                dfs(graph, head, 1.0)
                if not visited[tail]:
                    ans.append(-1.0)
            else:
                ans.append(-1.0)
        return ans

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
s=Solution()
print(s.calcEquation(equations, values, queries))
