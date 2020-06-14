# Kruskal算法求解最小生成树MST 《算法导论》23.2节
# 使用并查集实现Kruskal算法

# 并查集的三个标准函数
def make_set(n):
    return list(range(n))


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_x] = root_y


# Kruskal算法
def mst_kruskal(edges):
    # 计算有多少个节点
    nodes = set()
    for tail, head, weight in edges:
        nodes.add(tail)
        nodes.add(head)
    nodes_count = len(nodes)
    mst = []
    # 初始化并查集
    parent = make_set(nodes_count)
    # 将图的边按权重升序排列
    edges.sort(key=lambda x: x[2], reverse=False)
    # 依次对每条边进行遍历处理
    # 对每条边(u,v)检查两短点是否属于同一集合。
    # 如果是则跳过（否则会形成环）；如果不是，则加入mst，并将两短点合并在1个集合内
    for tail, head, weight in edges:
        if find(parent, tail) != find(parent, head):
            mst.append([tail, head, weight])
            union(parent, tail, head)
    print(mst)


if __name__ == '__main__':
    edges = [[0, 1, 4], [1, 2, 8], [2, 3, 7], [3, 4, 9], [4, 5, 10], [5, 6, 2], [6, 7, 1], [7, 8, 7], [2, 8, 2],
             [6, 8, 6], [3, 5, 14], [2, 5, 4], [0, 7, 8], [1, 7, 11]]
    mst_kruskal(edges)
