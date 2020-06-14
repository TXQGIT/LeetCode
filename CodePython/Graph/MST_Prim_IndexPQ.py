# Prim算法求解最小生成树MST 《算法导论》23.2节
from Graph.MST_Prim import *
from Graph.MinIndexPQ import MinIndexPQ


def visit_idxPQ(dist_to, edge_to, edge, mark, pq):
    weight, tail, head = edge[0], edge[1], edge[2]
    if not mark[head] and dist_to[head] > weight:
        edge_to[head] = tail
        dist_to[head] = weight
        if pq.contains(head):
            pq.change(head, dist_to[head])
        else:
            pq.insert(head, dist_to[head])


def prim_mst_idxPQ(edges, start_node):
    graph = build_graph(edges)
    nodes_num = len(graph)
    # 初始化求解mst的结果集
    # dist_to表示以结点s为根节点生成mst时，每个结点接入mst时接入边的权重
    # edge_to表示以结点s为根节点生成mst时，每个结点接入mst时接入边的另一个结点
    dist_to, edge_to = initialize_single_source(nodes_num, start_node)
    # 标记每个结点是否已加入mst
    mark = [False] * nodes_num
    # 保存每次遍历时mst外结点与mst连接的最短边信息
    idx_pq = MinIndexPQ(nodes_num)
    idx_pq.insert(0, 0)
    mst = []
    while not idx_pq.is_empty():
        node = idx_pq.delMin() - 1
        mst.append([dist_to[node], node, edge_to[node]])
        mark[node] = True
        for e in graph[node]:
            visit_idxPQ(dist_to, edge_to, e, mark, idx_pq)
    print('mst in (weight, tail, head): ', mst[1:])


if __name__ == '__main__':
    edges = [[0, 1, 4], [1, 2, 8], [2, 3, 7], [3, 4, 9], [4, 5, 10], [5, 6, 2], [6, 7, 1], [7, 8, 7], [2, 8, 2],
             [6, 8, 6], [3, 5, 14], [2, 5, 4], [0, 7, 8], [1, 7, 11]]
    prim_mst(edges, 0)
    prim_mst_idxPQ(edges, 0)
