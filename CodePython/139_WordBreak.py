def wordBreak(s, wordDict):
    # def word_break_recurse(s,wordDict):
    #     if len(s)==0:
    #         return True
    #     for e in wordDict:
    #         if e in s:
    #             e_start = s.find(e)
    #             len_n = len(e)
    #             if word_break_recurse(s[0:e_start], wordDict) and word_break_recurse(s[e_start+len_n:], wordDict):
    #                 return True
    #     return False
    # return word_break_recurse(s, wordDict)

    # 动态规划
    # dp[i]表示s[:i]是否满足题意
    dp = [False]*(len(s)+1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
    return dp[-1]


s = "leetcode"; wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))

s = "applepenapple"; wordDict = ["apple", "pen"]
print(wordBreak(s, wordDict))

s= "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))

s = "ccbb"; wordDict = ["cb","bc"]  #should be Fasle
print(wordBreak(s, wordDict))
