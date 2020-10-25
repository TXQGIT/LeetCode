class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        # 建图, 然后进行BFS遍历
        from collections import defaultdict

        def build_graph(edges):
            graph = defaultdict(set)
            for tail, head in edges:
                graph[tail].add(head)
            return graph

        red_graph = build_graph(red_edges)
        blue_graph = build_graph(blue_edges)
        dist = [[None] * 2 for _ in range(n)]
        dist[0] = [0, 0]
        now_red = [0]
        now_blue = [0]
        step = 0
        while now_red or now_blue:
            next_red = []
            next_blue = []
            step += 1
            for node in now_red:
                for v in blue_graph[node]:
                    if dist[v][0] is None:
                        dist[v][0] = step
                        next_blue.append(v)
            for node in now_blue:
                for v in red_graph[node]:
                    if dist[v][1] is None:
                        dist[v][1] = step
                        next_red.append(v)
            now_red = next_red
            now_blue = next_blue
        ans = []
        for i in range(n):
            if dist[i][0] is None and dist[i][1] is None:
                ans.append(-1)
            elif dist[i][0] is not None and dist[i][1] is not None:
                ans.append(min(dist[i][0], dist[i][1]))
            elif dist[i][0] is not None:
                ans.append(dist[i][0])
            else:
                ans.append(dist[i][1])
        return ans

n = 3
red_edges = [[0,1]]
blue_edges = [[1,2]]
s = Solution()
print(s.shortestAlternatingPaths(n,red_edges,blue_edges))