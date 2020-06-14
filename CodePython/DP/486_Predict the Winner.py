class Pair:
    def __init__(self, fir=0, sec=0):
        self.fir = fir
        self.sec = sec

class Solution:
    def PredictTheWinner(self, nums):
        # 动态规划
        # 令dp[i,j].fir表示在nums[i:j]之间进行选择时，先手的获得最大分数
        # 则dp[i,j].sec表示在nums[i:j]之间进行选择时，后手的获得最大分数
        n = len(nums)
        if n<2:
            return True
        dp = [[Pair() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].fir = nums[i]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                left = nums[i]+dp[i+1][j].sec
                right = nums[j]+dp[i][j-1].sec
                if left>right:
                    dp[i][j].fir = left
                    dp[i][j].sec = dp[i+1][j].fir
                else:
                    dp[i][j].fir = right
                    dp[i][j].sec = dp[i][j-1].fir
        return dp[0][n-1].fir>=dp[0][n-1].sec

s = Solution()
# nums = [1,5,233,7]
nums = [1,1]
print(s.PredictTheWinner(nums))