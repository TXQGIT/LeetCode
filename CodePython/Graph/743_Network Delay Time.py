class Solution:
    def networkDelayTime(self, times, N, K):
        # 迪杰斯特拉算法
        # 求特定点到图中其他顶点的最短路径
        def buildGraph(edges, N):
            graph = {}
            for i in range(N):
                graph[i+1] = []
            for departure, destination, t in edges:
                graph[departure].append([destination, t])
            return graph

        def init_search(graph, K):
            search = {}  # 存储k到其余顶点的时间
            # 初始化
            for v in graph.keys():
                if v != K:
                    search[v] = float('inf')
            for des, t in graph[K]:
                search[des] = t
            return search

        def find_min(search):
            des = ''
            cur_min = float('inf')
            for v in search.keys():
                if search[v] <= cur_min:
                    cur_min = search[v]
                    des = v
            return (des, cur_min)

        graph = buildGraph(times, N)
        search = init_search(graph, K)
        dis = {}
        # 迪杰斯特拉算法一共要执行N-1轮
        for i in range(len(graph.keys())-1):
            (des, t) = find_min(search)
            dis[des] = t
            search.pop(des)
            for v in search.keys():
                for node, t in graph[des]:
                    if v == node and dis[des] + t < search[v]:
                        search[v] = dis[des] + t
        return -1 if max(dis.values()) == float('inf') else max(dis.values())

soluton = Solution()
# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2
# times = [[1,2,1]]
# N = 2
# K = 2
times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
N = 4
K = 1
print(soluton.networkDelayTime(times, N, K))