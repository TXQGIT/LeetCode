# 加权有向无环图的单源最短路径算法
# 可能存在负向边，所以不能有Dijkstr算法
# 使用Bellman-Ford算法时间复杂度为O(VE)
# 存在时间复杂度为O(V+E)的算法计算加权有向无环图的单源最短路径

from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    nodes = set()
    for tail, head, weight in edges:
        graph[tail].append([weight, tail, head])
        nodes.add(tail)
        nodes.add(head)
    return graph, nodes


def topological_sorting(graph, nodes):
    def DFS_VISIT(v):
        pre.append(v)
        visited[v] = True
        for weight, tail, head in graph[v]:
            if not visited[head]:
                DFS_VISIT(head)
        post.append(v)
    nodes_num = len(nodes)
    pre = []
    post = []
    visited = [False]*nodes_num
    for v in range(nodes_num):
        if not visited[v]:
            DFS_VISIT(v)
    return post[::-1]


def initialize_single_source(nodes_num, start_node):
    dist_to = [float('inf')] * nodes_num
    edge_to = [None] * nodes_num
    dist_to[start_node] = 0.0
    edge_to[start_node] = start_node
    return dist_to, edge_to


def relax(dist_to, edge_to, edge):
    weight, tail, head = edge[0], edge[1], edge[2]
    if dist_to[head] > dist_to[tail] + weight:
        dist_to[head] = dist_to[tail] + weight
        edge_to[head] = tail


def Shortest_Path_of_Weighted_DAG(edges, start_node):
    graph, nodes = build_graph(edges)
    nodes_num = len(nodes)
    # 获取有向无环图的拓扑排序
    topological_sort = topological_sorting(graph, nodes)
    # 初始化为求解最短路径的结果集
    dist_to, edge_to = initialize_single_source(nodes_num, start_node)
    # Shortest_Path_of_Weighted_DAG算法的核心步骤.
    # 按照拓扑排序的结点顺序，依次对每个结点的边进行松弛
    for v in topological_sort:
        for e in graph[v]:
            relax(dist_to, edge_to, e)
    # 输出源点s到每个结点的最短路径
    for v in range(nodes_num):
        cur_node = v
        path = []
        while v != start_node:
            path.append(v)
            v = edge_to[v]
        path.append(v)
        print('node:', cur_node, 'dist:', dist_to[cur_node], 'path:', path[::-1])
    return True


if __name__ == '__main__':
    edges = [[0, 1, 5], [0, 3, 3], [1, 2, 6], [1, 3, 2], [2, 4, -1], [2, 5, 1],
             [3, 2, 7], [3, 4, 4], [3, 5, 2], [4, 5, -2]]
    Shortest_Path_of_Weighted_DAG(edges, 0)