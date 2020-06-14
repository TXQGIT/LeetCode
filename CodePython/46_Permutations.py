def permute(nums):
    # #回溯法框架
    # result = []
    # def backtrack(路径, 选择列表):
    #     if 满足结束条件:
    #         result.add(路径)
    #         return
    #     for 选择 in 选择列表:
    #         做选择
    #         backtrack(路径, 选择列表)
    #         撤销选择
    def backtrace(curPath, nums, flags):
        if len(curPath) == len(nums):
            ans.append(curPath[:])
            return
        for i in range(len(nums)):
            if flags[i]:
                continue
            else:
                flags[i] = True
                curPath.append(nums[i])
                backtrace(curPath, nums, flags)
                curPath.pop()
                flags[i] = False

    flags = [False] * len(nums)
    curPath = []
    ans = []
    backtrace(curPath, nums, flags)
    return ans

nums =[1,2,3]
print(permute(nums))