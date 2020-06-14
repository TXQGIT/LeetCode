#!/usr/bin/env python

s = "babad"
A = '@#'+'#'.join(s)+'#$'
n = len(A)
P = [0]*n
center = right =0
for i in range(1,n-1):
    if i<right:
        P[i] = min(P[2*center-i], right-i)
    while A[i+P[i]+1]==A[i-P[i]-1]:
        P[i] +=1
    if i+P[i]>right:
        center, right = i, i+P[i]
print(A)
print(P)

result = 0
for v in P:
    result += int((v+1)/2)
print(result)

max_r = max(P)
max_center = P.index(max_r)
result = ''
for i in range(0, max_r+1):
    if i==0 and A[max_center]!='#':
        result = result + A[max_center]
        continue
    if A[max_center-i]!='#':
        result = A[max_center-i]+result
        result = result +A[max_center+i]
print(result)