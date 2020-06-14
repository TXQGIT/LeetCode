class Solution:
    def numIslands(self, grid):
        # # 并查集算法
        # # 对1进行合并，最后分几组就有几个岛
        # def init(nums):
        #     return list(range(nums))
        #
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])
        #     return parent[x]
        #
        # def union(x, y):
        #     root_x = find(x)
        #     root_y = find(y)
        #     if root_x != root_y:
        #         parent[root_x] = root_y
        #
        # def pos(i, j):
        #     return i * cols + j
        #
        # if len(grid) == 0:
        #     return 0
        # rows = len(grid)
        # cols = len(grid[0])
        # parent = init(rows * cols)
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1':
        #             if i + 1 < rows and grid[i + 1][j] == '1':
        #                 union(pos(i, j), pos(i + 1, j))
        #             if j + 1 < cols and grid[i][j + 1] == '1':
        #                 union(pos(i, j), pos(i, j + 1))
        # root_set = set()
        # ans = 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1':
        #             root_set.add(find(pos(i,j)))
        # return len(root_set)

        # DFS算法
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i > rows - 1 or j > cols - 1 or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(grid, i, j)
        return ans


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
s = Solution()
print(s.numIslands(grid))
