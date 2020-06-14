# Prim算法求解最小生成树MST 《算法导论》23.2节
from collections import defaultdict
import heapq

def lazy_prim_mst(edges):
    # 遍历不在mst中的结点
    def visit(graph, node):
        #将当前节点标记为最小生成树的结点
        market[node] = True
        for weight, tail, head in graph[node]:
            #对当前结点的领接点，如果没有领接点不在最小生成树内，则把边加到候选边的最小优先队列中
            if not market[head]:
                heapq.heappush(min_heap_edge, (weight, tail, head))
        return None

    graph = build_graph(edges)
    nodes_count = len(graph)

    # 最小生成树的表
    mst = []
    # 标记图的结点是不是已加入最小生成树
    market = [False]*nodes_count
    # 生成mst的候选边的最小优先队列
    min_heap_edge = []

    #初始化mst根节点
    visit(graph, 0)
    while min_heap_edge:
        # 从候选边中取最短边
        edge = heapq.heappop(min_heap_edge)
        weight, tail, head = edge[0], edge[1], edge[2]
        # 如果该边的两个顶点都已经在mst中，则跳过
        if market[tail] and market[head]:
            continue
        # 否则该边是有效边，加入到mst中
        mst.append(edge)
        # 该边肯定是连接mst树内顶点和树外顶点的边
        # 那个顶点不在mst内，就要对该顶点visit
        if not market[tail]:
            visit(graph, tail)
        if not market[head]:
            visit(graph, head)
    print('mst in (weight, tail, head): ', mst)


def build_graph(edges):
    graph = defaultdict(list)
    for tail, head, weight in edges:
        graph[tail].append([weight, tail, head])
        graph[head].append([weight, head, tail])
    return graph


def initialize_single_source(nodes_num, start_node):
    dist_to = [float('inf')] * nodes_num
    edge_to = [None] * nodes_num
    dist_to[start_node] = 0.0
    edge_to[start_node] = start_node
    return dist_to, edge_to


def visit(dist_to, edge_to, edge, mark, hash_map):
    weight, tail, head  = edge[0], edge[1], edge[2]
    if not mark[head] and dist_to[head] > weight:
        dist_to[head] = weight
        edge_to[head] = tail
        hash_map[head] = [weight, head]


def prim_mst(edges, start_node):
    # 由边生成无向图
    graph = build_graph(edges)
    nodes_num = len(graph)
    # 初始化求解mst的结果集
    # dist_to表示以结点s为根节点生成mst时，每个结点接入mst时接入边的权重
    # edge_to表示以结点s为根节点生成mst时，每个结点接入mst时接入边的另一个结点
    dist_to, edge_to = initialize_single_source(nodes_num, start_node)
    # 标记每个结点是否已加入mst
    mark = [False]*nodes_num
    # 保存每次遍历时mst外结点与mst连接的最短边信息
    hash_map = defaultdict(list)
    hash_map[start_node] = [0.0, start_node]
    mst = []
    while hash_map:
        # 转换为优先队列
        min_heap = list(hash_map.values())
        heapq.heapify(min_heap)
        # 取当前和mst连接距离最近的结点
        dist, node = heapq.heappop(min_heap)
        mst.append([dist_to[node], node, edge_to[node]])
        mark[node] = True
        hash_map.pop(node)
        # 根据新加入mst的结点信息更新其他未加入mst的候选结点信息
        for e in graph[node]:
            visit(dist_to, edge_to, e, mark, hash_map)
    print('mst in (weight, tail, head): ', mst[1:])


if __name__ == '__main__':
    edges = [[0, 1, 4], [1, 2, 8], [2, 3, 7], [3, 4, 9], [4, 5, 10], [5, 6, 2], [6, 7, 1], [7, 8, 7], [2, 8, 2],
             [6, 8, 6], [3, 5, 14], [2, 5, 4], [0, 7, 8], [1, 7, 11]]
    lazy_prim_mst(edges)
    prim_mst(edges, 0)