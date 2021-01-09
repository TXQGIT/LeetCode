from collections import defaultdict
from itertools import combinations

class Solution:
    def buildGraph(self, n, dependencies):
        graph = defaultdict(list)
        inDegree = [0]*n
        for tail, head in dependencies:
            graph[tail-1].append(head-1)
            inDegree[head-1] += 1
        return graph, inDegree

    def topolical(self, graph, inDegree, queue, k):
        size = min(k, len(queue))
        for i in range(size):
            node = queue.pop(0)
            for adj in graph[node]:
                inDegree[adj] -= 1
                if inDegree[adj]==0:
                    queue.append(adj)
        return inDegree, queue

    def dfs(self, graph, inDegree, queue, k, curCnt, ans):
        if len(queue)==0:
            ans[0] = min(curCnt, ans[0])
            return
        if len(queue)<=k:
            # 如果当前度为0的节点数小于等于k, 则只有1种选择
            inDegreeNew, queueNew = self.topolical(graph, inDegree[:], queue[:], k)
            self.dfs(graph, inDegreeNew, queueNew, k, curCnt+1, ans)
        else:
            # 如果当前度为0的节点数大于k, 则对每种选择对计算结果, 最后取最小
            candidates = list(combinations(queue,k))
            for i in range(len(candidates)):
                queueCand = list(candidates[i]) + list(set(queue)-set(candidates[i]))
                inDegreeNew, queueNew = self.topolical(graph, inDegree[:], queueCand[:], k)
                self.dfs(graph, inDegreeNew, queueNew, k, curCnt+1, ans)


    def minNumberOfSemesters(self, n, dependencies, k):
        graph, inDegree = self.buildGraph(n, dependencies)
        queue = []
        for i in range(n):
            if inDegree[i]==0:
                queue.append(i)
        ans = [float('inf')]
        self.dfs(graph, inDegree, queue, k, 0, ans)
        return ans[0]

solution = Solution()
# n = 4
# dependencies = [[2,1],[3,1],[1,4]]
# k = 2

# n = 5
# dependencies = [[2,1],[3,1],[4,1],[1,5]]
# k = 2

# n = 12
# dependencies = [[1,2],[1,3],[7,5],[7,6],[4,8],[8,9],[9,10],[10,11],[11,12]]
# k = 2

n = 15
dependencies = [[2,1]]
k = 4

print(solution.minNumberOfSemesters(n,dependencies,k))