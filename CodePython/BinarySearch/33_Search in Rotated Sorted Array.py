class Solution:
    def search(self, nums, target):
        #step1:确定左右边界
        #由于target可能不存在,因此right=len(nums)
        left, right = 0, len(nums)-1
        while left<right:
            #step3:根据分支逻辑确定mid取左中位数还是右中位数,依据是不陷入死循环
            mid = (left+right)>>1
            #step2:只写两个分支，并且先写容易识别分支(例外)
            #左分支有序，且target不在左分支的范围内
            if nums[left]<=nums[mid] and (nums[left]>target or nums[mid]<target):
                left = mid+1
            #左分支无序，且target不在左分支范围内
            elif nums[left]>nums[mid] and (nums[mid]<target<nums[left]):
                left = mid+1
            else:
                right = mid
        #step4:退出循环时left=right，根据具体问题做后处理
        if nums[left]!=target:
            return -1
        else:
            return left

nums, target = [1,2,3], 3
# nums, target = [3,1], 3
# nums, target = [4,5,6,7,0,1,2], 0
s = Solution()
print(s.search(nums, target))