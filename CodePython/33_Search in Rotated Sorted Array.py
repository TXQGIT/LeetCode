def search(nums, targe):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # 判断什么条件下left右移：
        # left右移条件1：当左半序列有序，且target不在左边序列中间时
        if nums[left] < nums[mid] and (nums[left] > target or nums[mid] < target):
            left = mid + 1
        # left右移条件2：当左半序列存在旋转，且target不在左边序列中间时，left右移
        elif nums[left] >= nums[mid] and (nums[left] > target and nums[mid] < target):
            left = mid + 1
        else:
            right = mid
    return left if nums[left] == target else -1