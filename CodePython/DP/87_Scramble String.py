class Solution:
    def isScramble(self, s1, s2):
        # 令dp[i,j]表示s1[i:j]与s2[i:j]是否满足题意
        n = len(s1)
        if n==0:
            return True
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True if s1[i]==s2[i] else False
        for l in range(1,n):
            for i in range(n-l):
                j = i+l
                for k in range(i,j):
                    if dp[i][k] and dp[k+1][j]:
                        dp[i][j] = True
                        break
        return dp[0][n-1]

s1 = "great"
s2 = "rgeat"
s = Solution()
print(s.isScramble(s1,s2))