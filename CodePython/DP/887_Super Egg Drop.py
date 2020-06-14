class Solution:
    def SuperEggDrop(self, K, N):
        #解法1
        #令dp[K,N]表示K个鸡蛋,N层楼时最坏情况下的最少尝试次数
        #dp[k,n] = min{ max[dp(k,n-i),    #在第i层楼扔鸡蛋，鸡蛋没碎
        #                   dp(k-1, i-1)] #在第i层楼扔鸡蛋，鸡蛋碎了
        #             } +1, where i=1,2,..,n  遍历每层楼，找最坏情况的最小次数
        # dp = [[0]*(N+1) for _ in range(K+1)]
        # for k in range(K+1):
        #     dp[k][0] = dp[k][1] = 1
        # for n in range(N+1):
        #     dp[0][n] = float('inf')
        #     dp[1][n] = n
        # for k in range(2, K+1):
        #     for n in range(2, N+1):
        #         res = float('inf')
        #         for i in range(1, N+1):
        #             res = min(res, max(dp[k][n-i], dp[k-1][i-1])+1)
        #         dp[k][n] = res
        # return dp[K][N]

        #解法2
        #令dp[k,m]表示K个鸡蛋,扔m次能判定的最高楼层数
        #dp[k,m] = dp[k,m-1]    #某次在某层扔鸡蛋（具体哪次和哪层不重要），鸡蛋没碎
        #         +dp[k-1,m-1]  #某次在某层扔鸡蛋（具体哪次和哪层不重要），鸡蛋碎了
        #         +1            #
        dp = [[0]*(N+1) for _ in range(K+1)]
        # for k in range(K+1):
        #     dp[k][0] = 0
        # for n in range(N+1):
        #     dp[0][n] = 0
        m = 0
        while dp[K][m]<N:
            m += 1
            for k in range(1, K+1):
                dp[k][m] = dp[k][m-1]+dp[k-1][m-1]+1
        return m

s = Solution()
K,N=4,2000
print(s.SuperEggDrop(K,N))