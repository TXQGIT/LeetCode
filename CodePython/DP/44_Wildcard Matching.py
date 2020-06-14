class Solution:
    def isMatch(self, s, p):
        #方法1.递归——超时
        #如果p[0]='?', 则调用isMatch(s[1:], p[1:])
        #如果p[0]='*', 则当*匹配0个字符时调用isMatch(s[0:],p[1:])
        #               当*匹配1个字符时调用isMatch(s[0+1:],p[1:])
        #               当*匹配2个字符时调用isMatch(s[0+2:],p[1:])
        #               当*匹配j个字符时调用isMatch(s[0+j:],p[1:])
        #如果p[0]不属于'*?',则返回s[0]==p[0] and isMatch(s[1:], p[1:])
        # if len(p)==0:
        #     return len(s)==0
        # if len(s)==0:
        #     return len(p)==0 or (p[0]=='*' and self.isMatch(s, p[1:]))
        # if p[0]=='?':
        #     return self.isMatch(s[1:], p[1:])
        # elif p[0]=='*':
        #     for i in range(len(s)+1):
        #         if self.isMatch(s[i:], p[1:]):
        #             return True
        #     return False
        # else:
        #     return s[0]==p[0] and self.isMatch(s[1:], p[1:])

        #方法2.类似动态规划.方法1递归中存在子问题重叠, 因此可以有动态规划求解
        #令dp[i][j]表示s[i:]与p[j:]是否匹配
        #当p[j]='?'时, dp[i][j] = dp[i+1][j+1]
        #当p[j]='*'时, dp[i][j] = dp[i][j] or dp[i+k][j+1], where i<=i+k<=len(s)
        #otherwise, dp[i][j] = s[i]==p[j] and dp[i+1][j+1]
        if len(p)==0:
            return len(s)==0
        if len(s)==0:
            return len(p)==0 or (p=='*' * len(p))
        #优化匹配模板p:连续出现的*合并为1个
        p1 = ''
        for j in range(len(p)):
            if j>0 and p[j]=='*':
                if p[j-1]!='*':
                    p1 += p[j]
            else:
                p1 += p[j]
        p = p1
        n = len(s)
        m = len(p)
        dp = [[False]*(m+1) for i in range(n+1)]
        dp[n][m] = True
        for i in range(m-1,-1,-1): #''与p[i:]是否匹配
            dp[n][i] = p[i:]==('*' * len(p[i:]))
        for i in range(n-1,-1,-1): #s[i:]与''是否匹配
            dp[i][m] = False
        for j in range(m-1, -1, -1):
            for i in range(n-1, -1, -1):
                if p[j]=='?':
                    dp[i][j] = dp[i+1][j+1]
                elif p[j]=='*':
                    dp[i][j] = dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i][j] = s[i]==p[j] and dp[i+1][j+1]
        return dp[0][0]


s = Solution()
# a = 'aa'
# b = 'a'
a = "adceb"
b = "**a**b"
# a = "aabababbaabbbbbaab"
# b = "******a"
#a = "aaabaabbbbaaaaabaabbababbaaabbabaabaaabaaaaaabbabaabaaababbbabbaaaaaaaaaabaaaabbabaabbbbaabaaabaabaabbbbabaabbbaababaaaaabbabaabbbababaaaaaabbabaaababbbaabaaababbbbabbbabbbabbabbbaabbbbabaaaababaaabbaaa"
#b = "a**bbb****baab****b**bab**abb*abb***aab*********bab*bba*abbbab*baaababaa*a****b*****a**aaabab*bb*b*a*"
print(s.isMatch(a,b))