class Solution:
    def sortItems(self, n, m, group, beforeItems):
        from collections import defaultdict
        def create_visited(graph):
            visited = defaultdict(bool)
            for v in graph:
                visited[v] = False
            return visited

        def detect_cycle(adjacency):
            def dfs(i, adjacency, flags):
                if flags.get(i, 0) == -1: return True
                if flags.get(i, 0) == 1: return False
                flags[i] = 1
                for j in adjacency[i]:
                    if not dfs(j, adjacency, flags): return False
                flags[i] = -1
                return True

            flags = {}
            for v in adjacency:
                if not dfs(v, adjacency, flags):
                    return False
            return True

        def dfs(node, visited, ans, graph):
            visited[node] = True
            for v in graph[node]:
                if not visited[v]:
                    dfs(v, visited, ans, graph)
            ans.append(node)

        def toposort(graph):
            visited = create_visited(graph)
            ans = []
            for v in graph:
                if not visited[v]:
                    dfs(v, visited, ans, graph)
            return ans[::-1]

        def build_graph(nodes, edges):
            graph = {}
            for v in nodes:
                graph[v] = []
            for tail, head in edges:
                graph[tail].append(head)
            return graph

        # 生成组图和子图
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        group_nodes = set(group)
        group_edges = []
        item_nodes = defaultdict(list)
        item_edges = defaultdict(list)
        for i in range(n):
            item_nodes[group[i]].append(i)
            for pre in beforeItems[i]:
                if group[pre] != group[i]:  # 组间依赖
                    group_edges.append([group[pre], group[i]])
                else:  # 组内依赖
                    item_edges[group[i]].append([pre, i])

        group_graph = build_graph(group_nodes, group_edges)
        if not detect_cycle(group_graph):
            return []
        group_sort = toposort(group_graph)
        item_sorts = defaultdict(list)
        for g in group_nodes:
            item_graph = build_graph(item_nodes[g], item_edges[g])
            if not detect_cycle(item_graph):
                return []
            else:
                item_sorts[g] = toposort(item_graph)
        ans = []
        for g in group_sort:
            ans += item_sorts[g]
        return ans

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
before = [[],[6],[5],[6],[3,6],[],[],[]]
s = Solution()
print(s.sortItems(n,m,group, before))

