class Solution:
    def nthUglyNumber(self, n):
        # 三指针
        p2 = p3 = p5 = 0
        nums = [1]
        while n>len(nums):
            tmp = [nums[p2]*2, nums[p3]*3, nums[p5]*5]
            idx = tmp.index(min(tmp))
            if nums[-1]!=tmp[idx]:
                nums.append(tmp[idx])
            if idx==0:
                p2 += 1
            elif idx==1:
                p3 += 1
            else:
                p5 += 1
        return nums[-1]

s = Solution()
print(s.nthUglyNumber(10))
