class Solution:
    def wordBreak(self, s, wordDict):
        #递归
        def helper(s):
            res = []
            if not s:
                res.append('')
                return res
            for i in range(len(s)):
                if i<max_len and s[:i+1] in wordDict:
                    for t in helper(s[i+1:]):
                        if not t:
                            res.append(s[:i+1])
                        else:
                            res.append(s[:i+1]+' '+t)
            return res
        wordDict = set(wordDict)
        max_len = max(map(len, wordDict))
        return helper(s)

s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
so = Solution()
print(so.wordBreak(s,wordDict))