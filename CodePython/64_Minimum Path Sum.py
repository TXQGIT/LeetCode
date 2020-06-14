#!/usr/bin/env python

def minPathSum(grid):
    # dp[i,j]到达(i,j)处的路径长
    import numpy as np
    m = len(grid)
    n = len(grid[0])
    dp = np.zeros([m, n], dtype=int)
    for i in range(0, m):
        for j in range(0, n):
            if i==0 and j==0:
                dp[0,0] = grid[0][0]
            elif i==0 and j!=0:
                dp[i,j] = dp[i, j - 1] + grid[i][j]
            elif i!=0 and j==0:
                dp[i, j] = dp[i-1, j] + grid[i][j]
            else:
                dp[i, j] = min(dp[i - 1, j], dp[i, j - 1]) + grid[i][j]
    return dp[m - 1, n - 1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(minPathSum(grid))