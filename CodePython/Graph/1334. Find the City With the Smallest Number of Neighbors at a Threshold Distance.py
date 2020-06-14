class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        # 求所有结点对之间的最短路径：Floyd算法--动态规划算法
        # dp[i,j,k]表示v_i到v_j路径的中间结点在[0,k-1]中的最短路径
        def build_graph(n, edges):
            graph = [[float('inf')] * n for _ in range(n)]
            for u, v, w in edges:
                graph[u][v] = w
                graph[v][u] = w
            return graph

        import copy
        graph = build_graph(n, edges)
        pre_dp = copy.deepcopy(graph)
        dp = copy.deepcopy(graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(pre_dp[i][j], pre_dp[i][k] + pre_dp[k][j])
            pre_dp = copy.deepcopy(dp)
        candidate = [0] * n
        ans = []
        for v in range(n):
            for i in range(n):
                if v != i and dp[v][i] <= distanceThreshold:
                    candidate[v] += 1
            if candidate[v] > 0:
                ans.append([candidate[v], -1 * v])
        ans.sort()
        return abs(ans[0][1]) if len(ans) else None


s = Solution()

# n = 4
# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# dis = 4

n = 6
edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
dis = 417

print(s.findTheCity(n, edges, dis))
