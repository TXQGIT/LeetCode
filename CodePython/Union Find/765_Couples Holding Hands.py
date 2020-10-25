class Solution:
    def minSwapsCouples(self, row):
        # 假设k对情侣形成一个环状的错误链，我们只需要交换k - 1次就可以将这k对情侣的位置排好。
        # 并查集
        # def find(x):
        #     if x!=parent[x]:
        #         parent[x] = find(parent[x])
        #     return parent[x]

        # def union(x,y):
        #     root_x, root_y = find(x), find(y)
        #     if root_x!=root_y:
        #         parent[root_x]=root_y

        # n = len(row)
        # m = n//2
        # parent = [i for i in range(m)]
        # for i in range(0,n,2):
        #     union(row[i]//2, row[i+1]//2)
        # cicle = 0
        # for i in range(m):
        #     if i==parent[i]:
        #         cicle += 1
        # return m-cicle

        # 贪心算法
        # 对每个偶数位的人,如果右边奇数为不是其情侣,需要找到其情侣并换到当前位置
        ans = 0
        n = len(row)
        idx_arr = [0] * n
        for i in range(n):
            # 存放每个人的位置信息
            idx_arr[row[i]] = i
        for i in range(0, n, 2):
            # 情侣的标号
            couple = row[i] ^ 1
            if couple == row[i + 1]:
                continue
            # 找到其情侣的位置
            couple_idx = idx_arr[couple]
            idx_arr[row[i + 1]], idx_arr[couple] = idx_arr[couple], idx_arr[row[i + 1]]
            row[i + 1], row[couple_idx] = row[couple_idx], row[i + 1]
            ans += 1
        return ans

s = Solution()
row = [0,2,4,6,7,1,3,5]
print(s.minSwapsCouples(row))