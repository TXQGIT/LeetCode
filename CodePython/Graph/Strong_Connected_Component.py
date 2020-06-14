
#将有向图分解为强连通分量《算法导论》22.5节
from collections import defaultdict

class Node:
    def __init__(self, value, color='white', enter_time=0, quit_time=0):
        self.val = value
        self.color = color
        self.d = enter_time
        self.f = quit_time


def build_graph_from_edge_pairs(edges):
    graph = defaultdict(list)
    for tail, head in edges:
        graph[tail].append(head)
    nodes = defaultdict()
    for i in range(len(graph)):
        nodes[i] = Node(i)
    return (graph, nodes)

def DFS_visit(graph, nodes, node, time):
    print(node.val, end='->')
    time[0] += 1
    node.d = time[0]
    node.color = 'gray'
    for adj_v in graph[node.val]:
        if nodes[adj_v].color == 'white':
            DFS_visit(graph, nodes, nodes[adj_v], time)
    time[0] += 1
    node.f = time[0]
    node.color = 'black'
    return time

def DFS(graph, nodes):
    for v in nodes.values():
        v.color = 'white'
    time = [0]
    for v in nodes.values():
        if v.color == 'white':
            print('one in:')
            DFS_visit(graph, nodes, v, time)
            print('\none out:')

def graph_transpose(graph):
    graph_t = defaultdict(list)
    for node in graph:
        for adj_v in graph[node]:
            graph_t[adj_v].append(node)
    return graph_t

def strongly_connected_component(graph, nodes):
    #step1:DFS计算每个节点的遍历完成时间
    DFS(graph, nodes)
    #step2:计算转置图
    graph_t = graph_transpose(graph)
    #step3:以step1的遍历完成时间，降序排列结点
    for v in nodes.values():
        v.color = 'white'
    nodes_for_walk = list(nodes.values())
    nodes_for_walk.sort(key = lambda x: x.f, reverse = True)
    #step4:对step3的结点序列依次在转置图graph_t上做DFS遍历
    for v in nodes_for_walk:
        if v.color == 'white':
            print('\nnext strongly_connected_component:')
            DFS_visit(graph_t, nodes, v, [0])

if __name__=="__main__":
    edges = [[0,1], [1,2], [2,3], [3,2], [3,7], [7,7], [1,5], [5,6], [6,7], [6,5], [1,4], [4,5], [4,0]]
    graph, nodes = build_graph_from_edge_pairs(edges)
    strongly_connected_component(graph, nodes)