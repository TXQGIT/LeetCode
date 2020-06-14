class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        hashMap = dict()
        sIdx = 0
        for eIdx in range(len(s)):
            if s[eIdx] in hashMap:
                sIdx = max(hashMap[s[eIdx]]+1, sIdx)
            ans = max(ans, eIdx- sIdx +1)
            hashMap[s[eIdx]] = eIdx
        return ans

if __name__ == '__main__':
    su = Solution()
    s = 'abcabcdef'
    res = su.lengthOfLongestSubstring(s)
    print(res)