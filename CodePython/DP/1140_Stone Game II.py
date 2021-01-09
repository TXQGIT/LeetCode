class Solution:
    def stoneGameII(self, piles):
        # dp[i][m][0]表示在piles[i:]进行游戏且M=m时先手获得的最大石子数
        # dp[i][m][1]表示在piles[i:]进行游戏且M=m时后手获得的最大石子数
        # dp[i][m][0] = max( sum(piles[i:i+x]) + dp[i+k][max(m,x)][1]), x from 1 to 2m
        n = len(piles)
        dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
        # dp[n][m][0] = dp[n][m][1] = 0作为边界条件
        # dp[n-1][m][0] 恒等于 piles[n-1]
        for m in range(1, n + 1):
            dp[n - 1][m][0] = piles[n - 1]
        # 从倒数第二个石子堆往前遍历
        for i in range(n - 2, -1, -1):
            # m的取值超过n没有意义,所有限制m取值在[1,n]
            for m in range(n, 0, -1):
                # 记录dp[i][m]时先手的最优选择时前多堆,便于计算后手
                select_x = 1
                # 记录dp[i][m]时先手的最优选择时最大值
                select_max = 0
                # x的取值为1<=x<=2m, 同时还不能大于n
                for x in range(1, min(2*m+1, n + 1)):
                    # 计算在pile[i:]进行游戏且M=m,先手取前x堆石子时先手获得的最大石子数
                    cur_choice = sum(piles[i:min(i + x, n)]) + dp[min(i + x, n)][max(m, x)][1]
                    # 如果当前的选择更优,则记录当前的选择,便于计算后手能获得的最大石子数
                    if cur_choice > select_max:
                        select_max = cur_choice
                        select_x = x
                dp[i][m][0] = select_max
                dp[i][m][1] = dp[i + select_x][max(m, select_x)][0]
        return dp[0][1][0]

solution  = Solution()
piles = [2,7,9,4,4]
print(solution.stoneGameII(piles))
