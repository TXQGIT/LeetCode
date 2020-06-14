class Solution:
    def findTargetSumWays(self, nums, S):
        #dp[i,j]前i个数组合成目标为j的组合数
        #dp[i,j] = dp[i-1,j-nums[i]]+dp[i-1, j+nums[i]]
        # dp[i, j-nums[i]] += dp[i-1, j]
        # dp[i, j+nums[i]] += dp[i-1, j]
        sum_nums = sum(nums)
        if sum_nums<abs(S):
            return 0
        dp = [0]*(2*sum_nums+1)
        dp[sum_nums] = 1
        for i in range(len(nums)):
            pre = dp[:]
            v = nums[i]
            dp = [0]*(2*sum_nums+1)
            for j in range(-sum_nums, sum_nums+1):
                if j+sum_nums-v>=0:
                    dp[j+sum_nums] += pre[j+sum_nums-v]
                if j+sum_nums+v<=2*sum_nums:
                    dp[j+sum_nums] += pre[j+sum_nums+v]
        return dp[sum_nums+S]

nums =[1,1,1,1,1]
S = 4
solution = Solution()
print(solution.findTargetSumWays(nums, S))