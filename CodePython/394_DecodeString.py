def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    def DFS(s, k):
        ans = ''
        cnt = 0
        while k<len(s):
            if '0'<=s[k]<='9':
                cnt = 10*cnt+int(s[k])
                k += 1
            elif s[k]=='[':
                tmp,k = DFS(s, k+1)
                ans += tmp*cnt
                cnt = 0

            elif s[k]==']':
                k += 1
                return ans,k 
            else:
                ans += s[k]
                k += 1
        return ans
    
    return DFS(s, 0)

# s = '3[a]2[bc]'
s = '3[a2[bc]]'
print(decodeString(s))