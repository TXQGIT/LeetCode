class Solution:
    def canCross(self, stones):
        #dp[i,j]表示上一步跳j步是否可以到达位置i
        #dp[i,j] = dp[i-j,j-1] or dp[i-j,j] or dp[i-1, j+1]
        import bisect
        def find_lt(nums, target):
            idx = bisect.bisect_left(nums, target)
            if idx==len(nums) or nums[idx]!=target:
                return -1
            else:
                return idx

        n = len(stones)
        if n==0:
            return False
        dp = [[False]*(n+1) for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            for j in range(1, i+1):
                pre_stone = stones[i]-j
                k = find_lt(stones, pre_stone)
                if k!=-1:
                    dp[i][j] = dp[i][j] or dp[k][j-1] or dp[k][j] or dp[k][j+1]
        for j in range(1,n+1):
            if dp[n-1][j]:
                return True
        return False

stones = [0,1,3,4,5,7,9,10,12]
s = Solution()
print(s.canCross(stones))