class Solution:
    def maxCoins(self, nums):
        #自底向上
        n = len(nums)
        if n==0:
            return 0
        import itertools
        hashMap= {}
        hashMap[()] = 0
        for k in range(1,n+1):
            for item in itertools.combinations(nums, k):
                cur_item = 0
                for i in range(k):
                    tmp = list(item)
                    tmp.pop(i)
                    left = hashMap[tuple(tmp)]
                    split = item[i]
                    if k>1:
                        if i==0:
                            split *= item[1]
                        elif i==k-1:
                            split *= item[k-2]
                        else:
                            split *= item[i-1]*item[i+1]
                    cur_item = max(cur_item, left+split)
                hashMap[tuple(item)] = cur_item
        return hashMap[tuple(nums)]

s = Solution()
nums = [3,1,5,8]
print(s.maxCoins(nums))