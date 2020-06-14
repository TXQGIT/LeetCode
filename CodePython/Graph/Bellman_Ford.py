# 单源最短路径算法Bellman-Ford算法
# 适用范围：边可以为负权边，但图中不能存在源点s可到达的负向权重环
# 时间复杂度O(VE)

from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(list)
    for tail, head, weight in edges:
        graph[tail].append([weight, tail, head])
    return graph


def initialize_single_source(nodes_num, start_node):
    dist_to = [float('inf')] * nodes_num
    edge_to = [None] * nodes_num
    dist_to[start_node] = 0.0
    edge_to[start_node] = start_node
    return dist_to, edge_to


def relax(dist_to, edge_to, edge):
    tail, head, weight = edge[0], edge[1], edge[2]
    if dist_to[head] > dist_to[tail] + weight:
        dist_to[head] = dist_to[tail] + weight
        edge_to[head] = tail


def Bellman_Ford(edges, start_node):
    graph = build_graph(edges)
    nodes_num = len(graph)
    dist_to, edge_to = initialize_single_source(nodes_num, start_node)
    # Bellman-Ford算法的核心步骤.
    # 每轮对所有边进行松弛，共松弛nodes_num-1轮
    for i in range(nodes_num - 1):
        for e in edges:
            relax(dist_to, edge_to, e)
    # 检测是否存在从源点可到达的负权重环
    for tail, head, weight in edges:
        if dist_to[head] > dist_to[tail] + weight:
            print('存在从源点可到达的负权重环')
            return False
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
    edges = [[0, 1, 6], [0, 3, 7], [1, 2, 5], [1, 3, 8], [1, 4, -4],
             [2, 1, -2], [3, 2, -3], [3, 4, 9], [4, 0, 2], [4, 2, 7]]
    Bellman_Ford(edges, 0)