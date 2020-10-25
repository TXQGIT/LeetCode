class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 从nums1中取保持相对顺序的i个数中的最大值，nums2中取保持相对顺序的k-i个数最大值
        # 将两组数拼接起来取最大拼接值，最后遍历i取最大值即可

        def pick(nums, k):
            stack = []
            drop = len(nums)-k
            for digit in nums:
                while drop and stack and stack[-1]<digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            return stack[:k]


        def merge(m1, m2):
            ans = []
            while m1 or m2:
                bigger = m1 if m1 > m2 else m2
                ans.append(bigger[0])
                bigger.pop(0)
            return ans

        res = [0] * k
        for i in range(0, k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, merge(pick(nums1, i), pick(nums2, k - i)))
        return res

s = Solution()
# nums1 = [3,4,6,5]
# nums2 = [9,1,2,5,8,3]
# k = 5
# nums1 = [2,5,6,4,4,0]
# nums2 = [7,3,8,0,6,5,7,6,2]
# k = 15
nums1 = [6,7]
nums2 = [6,0,4]
k = 5
print(s.maxNumber(nums1, nums2, k))