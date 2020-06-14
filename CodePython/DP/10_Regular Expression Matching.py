class Solution:
    def isMatch(self, s, p):
        # #递归
        # if len(p)==0:
        #     return len(s)==0
        # first_match = len(s)>0 and p[0] in (s[0], '.')
        # if len(p)>=2 and p[1]=='*':
        #     match0 = self.isMatch(s, p[2:])  #用*匹配0个
        #     match1 = first_match and self.isMatch(s[1:], p) #用*号匹配至少1个
        #     return match0 or match1
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])

        #动态规划
        #dp[i][j]表示s[:i]与p[:j]是否匹配
        #当p[j]!='*'时, dp[i][j] = p[j] in (s[i], '.') and dp[i-1][j-1]
        #当p[j]='*'时，dp[i][j] = (p[j-1] in (s[i], '.') and dp[i-1][j])
        #                        or dp[i][j-2]
        ls = len(s)
        lp = len(p)
        dp = [[False]*(lp+1) for _ in range(ls+1)]
        dp[0][0] = True
        for j in range(1, lp+1):
            if p[j-1]=='*':
                dp[0][j] = dp[0][j-2]
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if p[j-1]!='*':
                    dp[i][j] = p[j-1] in (s[i-1], '.') and dp[i-1][j-1]
                else:
                    match0 = j>1 and dp[i][j-2]
                    match1 = p[j-2] in (s[i-1], '.') and dp[i-1][j]
                    dp[i][j] = match0 or match1
        return dp[-1][-1]

solution = Solution()
s = 'aa'
p = 'a*'
# s = ''
# p = '.*'
print(solution.isMatch(s, p))