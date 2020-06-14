class Solution:
    def lengthOfLIS(self, nums):
        # O(nlgn)的动态规划
        # tail[i]表示递增序列长为i的序列的末尾元素
        def binarySearch(nums, left, right, target):
            while left<=right:
                mid = left+(right-left)//2
                if nums[mid] == target:
                    return [mid, mid]
                if nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return [min(left, right), max(left,right)]

        if len(nums)==0:
            return 0
        tail = [nums[0]]
        for i in range(1, len(nums)):
            [l, r] = binarySearch(tail, 0, len(tail)-1, nums[i])
            if r< len(tail):
                tail[r] = nums[i]
            else:
                tail.append(nums[i])
        return len(tail)

a = Solution()
nums = [10,9,2,5,3,7,101,18]
a.lengthOfLIS(nums)