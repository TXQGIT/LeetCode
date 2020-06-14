class Solution:
    def splitArray(self, nums, m):
        # dp[n][m]表示前n个数分m组的题解
        # dp[n][m] = min(max(sum(nums[i:n]), dp[i][m-1])), where 0<=i<n
        # n = len(nums)
        # dp = [[float('inf')] * m for _ in range(n)]
        #
        # dp[0][0] = nums[0]
        # for i in range(1, n):
        #     dp[i][0] = dp[i - 1][0] + nums[i]
        #
        # i,j的遍历顺序无关紧要，j在外层更加直观
        # for j in range(1, m):
        #     for i in range(1, n):
        #         tmp = float('inf')
        #         for k in range(i-1, -1, -1):
        #             if k>=j-1:
        #                 split_one = sum(nums[k+1:i+1])
        #                 tmp = min(tmp, max(split_one, dp[k][j - 1]))
        #             else:
        #                 break
        #         dp[i][j] = tmp
        # return dp[n-1][m-1]

        left = max(nums)
        right = sum(nums)
        while left<right:
            mid = (left+right)//2
            cnt = 1
            tmp = 0
            for v in nums:
                tmp += v
                if tmp>mid:
                    cnt += 1
                    tmp = v
            if cnt<m:
                right = mid-1
            else:
                left = mid
        return left

s = Solution()
nums = [7,2,5,10,8]
m = 2
print(s.splitArray(nums, m))