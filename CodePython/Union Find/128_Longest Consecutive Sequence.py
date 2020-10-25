class Solution:
    def longestConsecutive(self, nums):
        # 并查集
        def find(x):
            while pa[x] != x:
                x = pa[x]
            return pa[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                pa[px] = py

        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        pa = list(range(len(nums)))
        for i in range(len(nums)):
            ni_plus_one = nums[i] + 1
            if ni_plus_one in d:
                union(i, d[ni_plus_one])
        count = {}
        ans = 0
        for i in range(len(nums)):
            pi = find(i)
            count[pi] = count.get(pi, 0)+1
            if count[pi] > ans:
                ans = count[pi]
        return ans

nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))