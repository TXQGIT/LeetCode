class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 字典序算法：
        # step1:从右往左开始遍历，找到第一个a[i-1]<a[i]的数字.如果找不到那么表示当前序列已经是最大
        # 从i开始往往右遍历，找到大于a[i-1]的数字中最小值a[k]
        # 交换a[i-1]和a[k]
        # 将a[i]:a[n]升序排列
        # firstDescent = -1
        # for i in range(len(nums)-1, 0, -1):
        #     if nums[i-1]<nums[i]:
        #         firstDescent = i-1
        #         break
        # if firstDescent==-1:
        #     return nums.sort()
        # candidate = firstDescent
        # #由step1可知，firstDescent+1及其之后的数据都是降序排列的
        # for i in range(firstDescent+1, len(nums)):
        #     if nums[i]>nums[firstDescent]:
        #         candidate = i
        #     else:
        #         break
        # nums[firstDescent], nums[candidate] = nums[candidate], nums[firstDescent]
        # #交换之后，firstDescent+1及其之后的数据依然是降序排列的.所以升序排列只需要翻转即可
        # nums[firstDescent+1:] = nums[-1:firstDescent:-1]
        # return nums

        decre_idx = -1
        # 从右往左遍历, 找到首次出现元素值下降的元素位置decre_idx
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                decre_idx = i
                break
        if decre_idx == -1:
            return nums.sort()
        # 从decre_idx往右遍历, 找到最后1个比nums[decre_idx]大的元素
        # 将该元素和nums[decre_idx]交换
        candidate = decre_idx
        for i in range(decre_idx + 1, len(nums)):
            if nums[i] > nums[decre_idx]:
                candidate = i
            else:
                break
        nums[candidate], nums[decre_idx] = nums[decre_idx], nums[candidate]
        nums[decre_idx + 1:] = nums[-1:decre_idx:-1]
        return nums


s = Solution()
# nums = [8, 6, 9, 7, 5]
nums = [3,2,1]
print(s.nextPermutation(nums))
