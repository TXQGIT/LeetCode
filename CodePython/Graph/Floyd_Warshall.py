# 计算图中所有结点对之间的最短路径
# 使用邻接矩阵表示图
# 不同于单源最短路径问题使用贪心算法，这里使用动态规划算法求解
import copy

def build_graph(edges):
    nodes = set()
    for tail, head, weight, in edges:
        nodes.add(tail)
        nodes.add(head)
    nodes_num = len(nodes)
    graph = [[float('inf')]*nodes_num for _ in range(nodes_num)]
    for v in nodes:
        graph[v][v] = 0
    for tail, head, weight, in edges:
        graph[tail][head] = weight
    return graph


def Floyd_Warshall(edges):
    # dp[i,j,k]表示v_i到v_j路径中的中间结点(不含v_i和v_j)在[0,1,...,k]的最短路径权重
    # dp[i,j,0] = graph[i,j]
    # dp[i,j,k] = min(dp[i,j,k-1], dp[i,k,k-1]+dp[k,j,k-1]
    graph = build_graph(edges)
    nodes_nums = len(graph)
    print(graph)
    pre_dp = copy.deepcopy(graph)
    dp = copy.deepcopy(graph)
    for k in range(nodes_nums):
        for i in range(nodes_nums):
            for j in range(nodes_nums):
                dp[i][j] = min(pre_dp[i][j], pre_dp[i][k]+pre_dp[k][j])
        pre_dp = copy.deepcopy(dp)
    print(dp)
    return dp


if __name__ == '__main__':
    edges = [[0, 1, 3], [0, 2, 8], [0, 4, -4], [1, 3, 1], [1, 4, 7],
             [2, 1, 4], [3, 0, 2], [3, 2, -5], [4, 3, 6]]
    Floyd_Warshall(edges)