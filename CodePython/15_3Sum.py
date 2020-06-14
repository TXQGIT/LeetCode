# def threeSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     nums.sort()
#     result = []
#     prior = None
#     for i in range(len(nums)):
#         if nums[i]==prior:
#             continue
#         prior = nums[i]
#
#         target = 0-nums[i]
#         left = i+1
#         right = len(nums)-1
#         while left<right:
#             if nums[left]+nums[right]==target:
#                 result.append([nums[i],nums[left],nums[right]])
#                 left += 1  #不保留重复解
#                 right -= 1
#                 while 0<=left<len(nums) and 0<=left<len(nums) and nums[left-1]==nums[left] and nums[right+1]==nums[right]:
#                     left += 1  #不保留重复解
#                     right -= 1
#             elif nums[left]+nums[right]<target:
#                 left += 1
#             else:
#                 right -= 1
#     return result

def threeSum(nums):
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        if v>0 and v == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        while left<right:
            if v+nums[left]+nums[right] == 0:
                res.add((v,nums[left],nums[right]))
                left += 1
                right -= 1
            elif v+nums[left]+nums[right] > 0:
                right -= 1
            else:
                left += 1
    return list(map(list, res))

# nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0]
print(threeSum(nums))