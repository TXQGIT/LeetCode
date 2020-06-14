class Tire:
    def __init__(self):
        self.children = {}
class Solution:
    def findMaximumXOR(self, nums):
        tire = Tire() #前缀树
        for num in nums:  #对每个数，都在深度为32的前缀树种找到其位置
            curNode = tire
            for i in range(6,-1,-1):
                cur_bit = (num>>i) & 1
                if curNode.children.get(cur_bit, None) is None:
                    curNode.children[cur_bit] = Tire()
                curNode = curNode.children[cur_bit]
        ans = 0
        for num in nums:
            print(num)
            curNode = tire
            cur_xor = 0
            for i in range(6,-1, -1):
                cur_bit = (num>>i) & 1 #从高位开始遍历
                if curNode.children.get(cur_bit^1) is not None:  #性质a^b=c => a^c=b. 如果和1异或的结果存在
                    cur_xor += (1<<i)
                    curNode = curNode.children[cur_bit^1]
                else:
                    curNode = curNode.children[cur_bit]
            ans = max(ans, cur_xor)
        return ans

nums = [3,10,5,25,2,8]
solution = Solution()
print(solution.findMaximumXOR(nums))