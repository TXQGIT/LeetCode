class Solution:
    def largestRectangleArea(self, heights):
        #方法1：以每个柱子为底边，计算和其他柱子组成的最大矩形面积
        maxSize = 0
        n = len(heights)
        for i in range(n):
            valid_height = heights[i]
            for j in range(i, n):
                valid_height = min(valid_height, heights[j])
                width = j-i+1
                maxSize = max(maxSize, valid_height*width)
        return maxSize

s = Solution()
h = [2,1,5,6,2,3]
print(s.largestRectangleArea(h))