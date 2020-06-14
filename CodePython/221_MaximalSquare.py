def maximalSquare(matrix):
    # #dp[i][j]:以matrix[i][j]为右下角的满足题意的最大正方形边长
    # if len(matrix)==0 or len(matrix[0])==0:
    #     return 0
    # rows = len(matrix)
    # cols = len(matrix[0])
    # dp = [[0]*cols for i in range(rows)]
    # cur_max = 0
    # for r in range(rows):
    #     for c in range(cols):
    #         if matrix[r][c]=='1':
    #             top  = dp[r-1][c] if r>0 else 0
    #             left = dp[r][c-1] if c>0 else 0
    #             tl = dp[r-1][c-1] if r>0 and c>0 else 0
    #             dp[r][c] = min(top,left,tl)+1
    #             cur_max = max(cur_max,dp[r][c])
    # print(dp)
    # return cur_max**2
    # #return max(max(dp))**2  #!!!注意: cur_max != max(max(dp)),
    #                          #         max(dp)等价于max(dp[0],dp[1],..)其计算流程是先比较所有dp[i]中dp[i][0],选dp[i][0]最大的dp[i]返回
    #                          #         如果dp[i][0]相等，就比较dp[i][1]，依次类推
    #                          #         所以max(dp)并不是想象中的返回每一行或者每一列的最大值
    #                          #         这也导致max(max(dp))的结果并不是dp所有元素的最大值
    #                          #         例如：dp = [[3,1],[1,100],[2,-2]], max(dp)=[3,1] 而不是【3,100】

    rows = len(matrix)
    cols = len(matrix[0])
    dp_prev = [0]+list(map(int, matrix[0]))
    dp_cur = [0] * (cols + 1)
    max_edge = max(dp_prev)
    for i in range(1, rows):
        for j in range(1, cols + 1):
            if matrix[i][j - 1] == '1':
                dp_cur[j] = min(dp_cur[j - 1], dp_prev[j - 1], dp_prev[j]) + 1
            else:
                dp_cur[j] = 0
        dp_prev = dp_cur[:]
        max_edge = max(max_edge, max(dp_cur))
    return max_edge ** 2

# matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))