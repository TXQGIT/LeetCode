import collections


# 求解欧拉路径/欧拉回路的两种算法

# Hierholzer算法
def hierholzer(graph, start):
    def dfs(node):
        while len(graph[node]):
            v = graph[node].pop()
            graph[v].remove(node)
            dfs(v)
        path.append(node)
    path = []
    dfs(start)
    return path[::-1]


def buildGraph(graph, edges):
    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)
    return


edges = [[0, 1], [0, 3], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]
graph = collections.defaultdict(set)
buildGraph(graph, edges)
EulerPath = hierholzer(graph, 0)
print(EulerPath)