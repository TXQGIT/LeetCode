def subsets(nums):
    def backtrace(curPath, nums, begin, end):
        if len(curPath) == len(nums):
            return
        for i in range(begin, end):
            curPath.append(nums[i])
            ans.append(curPath[:])
            backtrace(curPath, nums, i + 1, end)
            curPath.pop()

    ans = []
    backtrace([], nums, 0, len(nums))
    return ans
nums = [1,2,3]
print(subsets(nums))