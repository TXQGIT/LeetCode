#!/usr/bin/env python
def findUnsortedSubarray(nums):
	# 方法1：对每个i, 判断nums[i]与nums[j](i<j<n)的关系
	# 如果nums[j]<nums[i],那两者都不在正确位置上，记录当前的边界
	# left = len(nums)
	# right = 0
	# for i in range(len(nums)-1):
	#     for j in range(i+1, len(nums)):
	#         if nums[j]<nums[i]:
	#             left = min(left, i)
	#             right = max(right, j)
	# return 0 if right-left<0 else right-left+1

	# 方法2：向从左到右遍历，对升序序列不断入栈，如果当前元素大于栈顶元素，那说明当前元素的位置不对
	# 不断出栈，直到栈顶元素小于当前元素为止，当前栈顶元素的下标为k，这当前的左边界为k+1.
	# 如此遍历找到无序序列的左边界，同理可找到无序序列的右边界
	# left = len(nums)
	# right = 0
	# stack = []
	# for i in range(len(nums)):
	# 	while len(stack) and nums[i] < nums[stack[-1]]:
	# 		left = min(left, stack.pop())
	# 	stack.append(i)
	# stack = []
	# for j in range(len(nums)-1, -1, -1):
	# 	while len(stack) and nums[j] > nums[stack[-1]]:
	# 		right = max(right, stack.pop())
	# 	stack.append(j)
	# return 0 if right - left < 0 else right - left + 1


	# 方法3：方法2的改进，不用栈
	if len(nums) < 2:
		return 0
	left = len(nums)
	right = 0
	unsortMin = float('inf')
	unsortMax = float('-inf')
	flag = False
	for i in range(1, len(nums)):
		if nums[i] < nums[i - 1]:
			flag = True
		if flag:
			unsortMin = min(unsortMin, nums[i])
	flag = False
	for i in range(len(nums) - 2, -1, -1):
		if nums[i] > nums[i + 1]:
			flag = True
		if flag:
			unsortMax = max(unsortMax, nums[i])
	for i in range(len(nums)):
		if nums[i] > unsortMin:
			left = i
			break
	for i in range(len(nums) - 1, -1, -1):
		if nums[i] < unsortMax:
			right = i
			break
	return 0 if right - left < 0 else right - left + 1

nums = [2,1,3,4,5] #[2, 6, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(nums))