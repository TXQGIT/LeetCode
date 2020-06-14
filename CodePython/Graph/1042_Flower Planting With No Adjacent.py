class Solution:
    def gardenNoAdj(self, N, paths):
        # g = AdjacencyMatrix()
        # g.init_graph(paths, N)
        # flowers = [None]*N
        # for i in range(N):
        #     candidate = list(range(1,5))
        #     for j in range(N):
        #         if g.matrix[i][j] and flowers[j]:
        #             candidate.pop(candidate.index(flowers[j]))
        #     flowers[i] = min(candidate)
        # return flowers

        #邻接表
        g = [[] for i in range(N)]
        flowers = [None] * N
        for path in paths:
            tail = path[0] - 1
            head = path[1] - 1
            g[tail].append(head)
            g[head].append(tail)
        for i in range(N):
            candidate = list(range(1,5))
            for node in g[i]:
                if flowers[node] in candidate:
                    candidate.remove(flowers[node])
            flowers[i] = min(candidate)
        return flowers

solution = Solution()
# N = 4
# paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
N = 5
paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]
output = solution.gardenNoAdj(N, paths)
print(output)