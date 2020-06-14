from collections import defaultdict
import heapq

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


def relax(dist_to, edge_to, edge, hash_map):
    weight, tail, head  = edge[0], edge[1], edge[2]
    # Dijkstra算法和Prim算法的核心差异所在
    if dist_to[head] > dist_to[tail] + weight:
        dist_to[head] = dist_to[tail] + weight
        edge_to[head] = tail
        hash_map[head] = [dist_to[head], head]


def dijkstra(edges, start_node):
    graph = build_graph(edges)
    nodes_num = len(graph)
    # 初始化结果集
    # dist_to表示结点s到每个结点v的当前最短路径权重
    # edge_to表示结点s到每个结点v的当前最短路径中结点v相连的上一个结点
    dist_to, edge_to = initialize_single_source(nodes_num, start_node)
    hash_map = defaultdict(list)
    hash_map[start_node] = [0.0, start_node]
    # Dijkstra算法的核心步骤.
    # 每轮对选择当前和源点s的距离最近的结点，然后对该结点的边进行松弛
    while hash_map:
        # 转换为优先队列
        min_heap = list(hash_map.values())
        heapq.heapify(min_heap)
        # 取当前和源点s距离最近的结点
        dist, node = heapq.heappop(min_heap)
        hash_map.pop(node)
        for e in graph[node]:
            relax(dist_to, edge_to, e, hash_map)
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
    edges = [[0, 1, 10], [0, 3, 5], [1, 2, 1], [1, 3, 2], [2, 4, 4],
             [3, 1, 3], [3, 2, 9], [3, 4, 2], [4, 0, 7], [4, 2, 6]]
    dijkstra(edges, 0)
