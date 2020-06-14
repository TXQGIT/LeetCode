class Solution:
    def firstMissingPositive(self, nums):
        # O(n)时间复杂度，O(1)空间复杂度
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return len(nums) + 1


s = Solution()
nums = [3, 4, -1, 1, 3, 5]
nums = [3, 4, 2, 1, 6, 5]
print(s.firstMissingPositive(nums))
