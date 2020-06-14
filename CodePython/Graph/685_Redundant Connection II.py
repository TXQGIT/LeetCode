class Solution:
    def findRedundantDirectedConnection(self, edges):
        # 并查集求解
        # 分两步
        # 先求解[[2,1],[3,1],[4,2],[1,4]]场景
        #   依次遍历边(u,v), 设置parent[v] = u.
        #   由于冗余边的存在，会出现某个结点parent[v]有2个值
        #   而根结点parnet[r] = r.
        #   找到r,v, 将parnet[v]不等于v的结点u和v组成的边(u,v)返回
        # 再求解[[2,1],[1,3],[4,2],[1,4]]场景
        #   依次遍历输入的有向边(u,v), 如果u和v不属于同一个集合, 则union(u,v);
        #   否则说明u,v都已经加入树, (u,v)就是冗余边.

        # 并查集算法的3个固定方法
        def init(n):
            parent = [0] * n
            for i in range(n):
                parent[i] = i
            return parent

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        def is_one_connected_compenent(edges, e):
            for i in range(n):
                parent[i] = i
            count = n
            for tail, head in edges:
                if [tail, head] != e:
                    root_x = find(tail - 1)
                    root_y = find(head - 1)
                    if root_x != root_y:
                        count -= 1
                        parent[root_y]=root_x
            return count == 1

        n = len(edges)
        parent = init(n)
        # case1: 存在结点有2个父节点（自然就有根结点）
        two_parent_vertex = root_vertex = None
        two_parent_vertex_parent = []
        for tail, head in edges:
            if parent[head - 1] == head - 1:
                parent[head - 1] = tail - 1
            else:
                two_parent_vertex = head - 1
                two_parent_vertex_parent = [parent[head - 1], tail - 1]
        for v in range(n):
            if parent[v] == v:
                root_vertex = v
                break
        if root_vertex is not None:
            for p in two_parent_vertex_parent[::-1]:
                e = [p + 1, two_parent_vertex + 1]
                if is_one_connected_compenent(edges, e):
                    return e
        # case2：所有结点都有1个父结点（存在环）
        parent = init(n)
        for tail, head in edges:
            if find(tail - 1) != find(head - 1):
                union(tail - 1, head - 1)
            else:
                return [tail, head]


s = Solution()
# edges = [[1, 2], [1, 3], [2, 3]]
edges = [[2, 1], [3, 1], [4, 2], [1, 4]]
# edges = [[2, 1], [1, 3], [4, 2], [1, 4]]
print(s.findRedundantDirectedConnection(edges))
