def sortColors(nums):
    #设立2个指针：p0表示0元素的右边界(初始为-1)，p2表示2元素的左边界(初始为n)，cur表示当前遍历元素
    #如果当前元素为0：p0+=1, 然后交换 p0和cur所指的元素
    #如果当前元素为1：cur+=1
    #如果当前元素为2：p2-=1, 然后交换 p2和cur所指的元素
    p0 = -1
    cur = 0
    p2 = len(nums)
    while cur<p2:
        if nums[cur]==0:
            p0 += 1
            nums[p0], nums[cur] = nums[cur], nums[p0]
            cur += 1
        elif nums[cur]==1:
            cur += 1
        else:
            p2 -= 1
            nums[p2], nums[cur] = nums[cur], nums[p2]

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)