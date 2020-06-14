
def rob(nums):
    # DP
    # dp[i]:到第i家时能获得的最大收益,可能抢也可能不抢第i家
    # dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    # dp[0] = nums[0],
    # dp[1] = max(nums[0], nums[1])
    n = len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    dp = [0]*n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

if __name__ == '__main__':
	nums = [2,7,9,3,1]
	print(rob(nums))