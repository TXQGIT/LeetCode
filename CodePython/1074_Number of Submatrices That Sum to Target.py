class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        from collections import defaultdict
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0
        # 存放每行的前缀和
        row_sum = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            row_sum[r][0] = matrix[r][0]
            for c in range(1, cols):
                row_sum[r][c] = row_sum[r][c-1] + matrix[r][c]
        for i in range(cols):
            for j in range(i, cols):
                d = defaultdict(int)
                tmp = 0
                for k in range(rows):
                    tmp += row_sum[k][j]-row_sum[k][i]+matrix[k][i]
                    if tmp==target:
                        ans += 1
                    if tmp-target in d:
                        ans += d[tmp-target]
                    d[tmp] += 1
        return ans

s = Solution()
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(s.numSubmatrixSumTarget(matrix, target))