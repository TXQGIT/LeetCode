def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    #方案一：
    #先建立邻接表表示的有向图
    #然后进行DFS检测有向图是否存在环
    '''
    def make_graph(numCourses, prerequisites):
        Adj = [[] for i in range(numCourses)]
        for ele in prerequisites:
            TailNode = ele[1]
            HeadNode = ele[0]
            Adj[TailNode].append(HeadNode)
        return Adj
    
    def DFS(G_Adj, flag, Node):
        for ele in G_Adj[Node]:
            if flag[ele]==False:
                flag[ele] = True
                if DFS(G_Adj, flag, ele):
                    return True
                else:
                    flag[ele] = False
            else:
                return True
        return False
    
    G_Adj = make_graph(numCourses, prerequisites)
    for i in range(numCourses):
        flag = [False]*numCourses
        flag[i] = True
        hasCircle = DFS(G_Adj, flag, i)
        if hasCircle:
            return False
    return True
    '''

    #方案二: 建立邻接表表示有向图，表中每一行的第一列表示当前结点的入度，后面的列表示当前结点做连接的其他结点
    def make_graph(numCourses, prerequisites):
        Adj = [[0] for i in range(numCourses)]
        for ele in prerequisites:
            TailNode = ele[1]
            HeadNode = ele[0]
            Adj[HeadNode][0] += 1
            Adj[TailNode].append(HeadNode)
        return Adj
    
    def BFS(G_Adj, Node):
        for i in range(1, len(G_Adj[Node])):
            ele = G_Adj[Node][i]
            G_Adj[ele][0] -= 1
    
    G_Adj = make_graph(numCourses, prerequisites)
    visited = [False]*numCourses
    for j in range(numCourses):
        hasIndegree0 = False
        for i in range(numCourses):
            if not visited[i] and G_Adj[i][0]==0:
                hasIndegree0 = True
                visited[i] = True
                BFS(G_Adj, i)
                break
        if not hasIndegree0:
            return False
    return True

numCourses = 3
prerequisites = [[1,0],[2,0],[0,2]]
# numCourses = 3
# prerequisites = [[0,1],[0,2],[1,2]]
# numCourses = 2
# prerequisites = [[0,1]]
flag = canFinish(numCourses, prerequisites)
print(flag)