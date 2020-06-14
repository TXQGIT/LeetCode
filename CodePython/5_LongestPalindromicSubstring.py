#!/usr/bin/env python

import numpy as np

# s = "babad"
s = "abcba"

# -----动态规划-----
# # dp[i][j] indicates whether substring s starting at index i and ending at j is palindrome
len_s = len(s)
dp = np.zeros((len_s, len_s), dtype=int)
maxPal = ''

# 解法1
# for i in range(len_s):  #错误：这个循环不能保证先求所有子序列长为1和2的，然后子序列长为3和4，依次...
# 	for j in range(i,len_s):
# 		if j<=i+1:
# 			dp[i,j] = (s[i]==s[j])
# 		else:
# 			dp[i,j] = (s[i]==s[j] and dp[i+1,j-1]) #此时dp[i+1][j-1]还未计算
#         if dp[i, j] and j - i + 1 > len(maxPal):
#             maxPal = s[i:j + 1]
# print(maxPal)

# 解法1修正: 递推公式中我们可以看到，我们首先知道了 i +1i+1 才会知道 ii ，所以我们只需要倒着遍历就行了。
# for i in range(len_s - 1, -1, -1):
#     for j in range(i, len_s):
#         dp[i, j] = (s[i] == s[j]) and (j - i < 2 or dp[i + 1][j - 1])
#         if dp[i, j] and j - i + 1 > len(maxPal):
#             maxPal = s[i:j + 1]
# print(maxPal)

# 解法2: 先判断所有长度为1的子序列，然后判断长为2的子序列，依次类推
# for length in range(1, len_s+1):
#     for startIdx in range(len_s):
#         endIdx = startIdx + length - 1
#         if endIdx > len_s - 1:
#             break
#         #对长度为1和2的子序列特殊判断
#         dp[startIdx][endIdx] = (s[startIdx]==s[endIdx]) and (endIdx-startIdx<2 or (dp[startIdx+1][endIdx-1]))
#         if dp[startIdx, endIdx] and length > len(maxPal):
#             maxPal = s[startIdx:endIdx + 1]
# print(maxPal)

# 解法3：扩展中心法, 时间复杂度O(n^2)， 空间复杂度O(1)
def expandAroundCenter(s, left, right):
    while left>=0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right-left-1

startIdx = endIdx = 0
for i in range(len(s)):
    len1 = expandAroundCenter(s, i, i)
    len2 = expandAroundCenter(s, i, i+1)
    maxLen = max(len1, len2)
    if maxLen > endIdx - startIdx:
        startIdx = i - int((maxLen-1)/2)
        endIdx = i + int(maxLen/2)
maxPal = s[startIdx:endIdx+1]
print(maxPal)


# -----Manacher Algorithm-----
# A = '@#'+'#'.join(s)+'#$'
# n = len(A)
# P = [0]*n
# center = right =0
# for i in range(1,n-1):
#     if i<right:
#         P[i] = min(P[2*center-i], right-i)
#     while A[i+P[i]+1]==A[i-P[i]-1]:
#         P[i] +=1
#     if i+P[i]>right:
#         center, right = i, i+P[i]
# print(A)
# print(P)
#
# max_r = max(P)
# max_center = P.index(max_r)
# result = ''
# for i in range(0, max_r+1):
#     if i==0 and A[max_center]!='#':
#         result = result + A[max_center]
#         continue
#     if A[max_center-i]!='#':
#         result = A[max_center-i]+result
#         result = result +A[max_center+i]
# print(result)
