class Solution:
    def maxNumber(self, nums1, nums2, k):
        # 从nums1中取保持相对顺序的i个数中的最大值，nums2中取保持相对顺序的k-i个数最大值
        # 将两组数拼接起来取最大拼接值，最后遍历i取最大值即可

        def pick(nums, i):
            if i == 0:
                return []
            stack = [nums[0]]  # 单调递增栈
            pop_count = len(nums) - i  # 单调栈最大可出栈次数
            for j in range(1, len(nums)):
                while stack and pop_count and stack[-1] < nums[j]:
                    pop_count -= 1
                    stack.pop()
                stack.append(nums[j])
            return stack[:i]

        def merge(nums1, nums2):
            ans = []
            n1, n2 = len(nums1), len(nums2)
            i1, i2 = 0, 0
            while i1 < n1 and i2 < n2:
                if nums1[i1] >= nums2[i2]:
                    ans.append(nums1[i1])
                    i1 += 1
                else:
                    ans.append(nums2[i2])
                    i2 += 1
            if i1 < n1:
                ans += nums1[i1:]
            if i2 < n2:
                ans += nums2[i2:]
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
nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 15
print(s.maxNumber(nums1, nums2, k))