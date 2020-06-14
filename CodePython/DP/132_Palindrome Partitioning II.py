class Solution:
    def minCut(self, s):
        def is_palindrome(s):
            if len(s)==0:
                return True
            if s[0]==s[-1]:
                return is_palindrome(s[1:-1])
            else:
                return False
        # dp[i,j]表示s[i:j]的最小分割次数
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if is_palindrome(s[i:j+1]):
                    continue
                min_count = float('inf')
                for k in range(i,j):
                    min_count = min(min_count, dp[i][k]+dp[k+1][j])
                dp[i][j] = min_count+1
        return dp[0][n-1]

s = Solution()
a = "leet"
print(s.minCut(a))