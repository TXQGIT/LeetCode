def findDisappearedNumbers(nums):
    idx = 0
    while idx < len(nums):
        if nums[idx] == idx + 1 or nums[idx] == nums[nums[idx] - 1]:
            idx += 1
        else:
            temp = nums[idx]
            nums[idx] = nums[temp - 1]
            nums[temp - 1] = temp
    idx = 0
    ans = []
    while idx < len(nums):
        if nums[idx] != idx + 1:
            ans.append(idx + 1)
        idx += 1
    return ans

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))