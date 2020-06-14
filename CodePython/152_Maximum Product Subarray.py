
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp_max[i]: 以nums[i]结尾的子序列的最大乘积
    #dp_min[i]: 以nums[i]结尾的子序列的最小乘积
    if len(nums)==0:
        return 0
    dp_max = [0]*len(nums)
    dp_min = [0]*len(nums)
    dp_max[0] = dp_min[0] = nums[0]
    ans = max(nums[0],0)
    for i in range(1,len(nums)):
        dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
        ans = max(ans, dp_max[i])
    return ans

if __name__ == '__main__':
	nums = [2,3,-2,4]
	print(nums, ':', maxProduct(nums))

	nums = [-2,0,-4]
	print(nums, ':', maxProduct(nums))

	nums = [2,-3,2,-4]
	print(nums, ':', maxProduct(nums))

	nums = [2,-5,-2,-4,3]
	print(nums, ':', maxProduct(nums))