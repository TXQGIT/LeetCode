def left_edge(nums, target):
    # step1: 确定左右边界
    # 由于可能存在target大于max(nums)，所以right取len(nums)
    left, right = 0, len(nums)
    while left < right:  # 二分查找的固定语句
        # step3:根据分支逻辑确定mid取左中位数还是右中位数
        # 由于进入右边界时没有排除中位数，因此mid必须取左中位数
        mid = (left + right) >> 1
        # step2:只写两个查找分支，并且先写容易识别的分支
        # 由于是求左边界，因此当nums[mid]<target时，中位数一定不是答案
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
            # step4:退出循环后，做后处理
    # 当target比max(nums)大时，left=len(nums); 当target不存在于nums中时
    print(left, right)
    if left == len(nums) or nums[left] != target:
        return -1
    else:
        return left

def right_edge(nums, target):
    # step1: 确定左右边界
    # 由于可能存在target大于max(nums)，所以right取len(nums)
    left, right = 0, len(nums)
    while left < right:  # 二分查找的固定语句
        # step3:根据分支逻辑确定mid取左中位数还是右中位数
        # 由于进入左边界时没有排除中位数，因此mid必须取右中位数
        mid = (left + right + 1) >> 1
        # step2:只写两个查找分支，并且先写容易识别的分支
        # 由于是求右边界，因此当nums[mid]>target时，中位数一定不是答案
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
            # step4:退出循环后，做后处理
    # 当target比max(nums)大时，left=len(nums); 当target不存在于nums中时
    print(left, right)
    if left == len(nums) or nums[left] != target:
        return -1
    else:
        return left

if __name__=="__main__":
    nums = [1,3,3,3,5,7]
    target = 5
    print(left_edge(nums, target))
    print(right_edge(nums, target))