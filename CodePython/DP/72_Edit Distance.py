class Solution:
    def minDistance(self, word1, word2) -> int:
        #动态规划
        #dp[i][j]表示word1[:i]与word2[:j]的编辑距离
        m = len(word1)
        n = len(word2)
        if m==0:
            return n
        if n==0:
            return m
        dp = [[0]*n for _ in range(m)]
        choice = [['']*n for _ in range(m)]
        if word1[0]==word2[0]:
            dp[0][0] = 0
            choice[0][0] = 'skip'
        else:
            dp[0][0] = 1
            choice[0][0] = 'replace'
        for j in range(1,n):
            if word1[0] in word2[:j+1]:
                dp[0][j] = j
                choice = 'insert'
            else:
                dp[0][j] = j+1
                choice[0][j] = 'insert'
        for i in range(1,m):
            dp[i][0] = i if word2[0] in word1[:i+1] else i+1
        for i in range(1,m):
            for j in range(1,n):
                if word1[i] == word2[j]:
                    #dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]-1)
                    dp[i][j] = dp[i-1][j-1]
                    choice[i][j] = 'skip'
                else:
                    dp[i][j] = dp[i-1][j]
                    choice[i][j] = 'insert'
                    if dp[i][j-1]<dp[i][j]:
                        dp[i][j] = dp[i][j-1]
                        choice[i][j] = 'delete'
                    if dp[i-1][j-1]<dp[i][j]:
                        dp[i][j] = dp[i-1][j-1]
                        choice[i][j] = 'replace'
                    dp[i][j] += 1
                    #dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]

solution = Solution()
word1 = "horse"
word2 = "ros"
solution.minDistance(word1, word2)