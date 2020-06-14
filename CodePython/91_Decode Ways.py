

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    #dp[i]:以s[i]结尾的子串有多少种解码方式
    #case1. s[i]独立解码: dp[i] = 0 if s[i]=0 else dp[i-1] 
    #case2. s[i-1]s[i]合在一起解码: 如果s[i-1]s[i]<=27，那么s[i-1]s[i]可以合在一起解码，此时的解码方案等于取决于dp[i-2],即dp[i] += dp[i-2].
    n = len(s)
    if n<2:
        return 1 if int(s[0])>0 else 0

    dp = [0]*n
    if int(s[0]):
        dp[0] = 1 
    else:
        dp[0] = 0
    if int(s[0]) and int(s[1]):
        dp[1] += 1
    if int(s[0]) and 0<int(s[0]+s[1])<27:
        dp[1] += 1


    for i in range(2,n):
        dp[i] = dp[i-1] if int(s[i])>0 else 0
        tmp = int(s[i-1]+s[i])
        if int(s[i-1]) and 0<tmp<27:
            dp[i] += dp[i-2]
    return dp[-1]

if __name__ == '__main__':
    print(numDecodings('0'))
    print(numDecodings('00'))
    print(numDecodings('01'))
    print(numDecodings('10203'))
    print(numDecodings('102003'))
    print(numDecodings('112625'))