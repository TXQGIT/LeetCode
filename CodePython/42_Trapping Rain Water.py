class Solution:
    def trap(self, height):
        #找每个柱子上方可积多少水
        #对每个柱子，分别找左右两边的最大高度，其中小值觉得该柱子可积多少水
        n = len(height)
        left_max = [height[0]]
        for i in range(1,n):
            left_max.append(max(height[i], left_max[i-1]))
        right_max = [0]*n
        right_max[n-1] = height[n-1]
        for i in reversed(range(n-1)):
            right_max[i] = max(height[i], right_max[i+1])
        ans = 0
        for i in range(1,n-1):
            bar = min(left_max[i], right_max[i])
            ans += bar-height[i]
        return ans

solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(height))