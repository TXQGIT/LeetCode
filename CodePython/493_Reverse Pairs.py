class Solution:
    def reversePairs(self, nums):
        # 树状数组

        def low_bit(x):
            # 令返回x二进制表示下末尾0的个数为k
            # low_bit(x) = 2**k
            return x & (-x)

        def query(tree_arr, i):
            # 返回序列nums中1~i项的和
            v_sum = 0
            while i:
                v_sum += tree_arr[i]
                i -= low_bit(i)
            return v_sum

        def update(tree_arr, i, delta):
            # nums[i]的值有delta的变动
            # 更新树状数组的值
            while i <= n:
                tree_arr[i] += delta
                i += low_bit(i)

        # 离散初始化
        nums_set = list(set([2 * v for v in nums]))
        nums_set.sort()
        n = len(nums_set)
        tree_arr = [0] * (n + 1)
        rank_map = {}
        rank = 1
        for v in nums_set:
            rank_map[v] = rank
            rank += 1
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            if rank>=rank_map[2*v]:
            update(tree_arr, r, 1)
            ans += query(tree_arr, r - 1)
        return ans

s = Solution()
nums = [1,3,2,3,1]
print(s.reversePairs(nums))