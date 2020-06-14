#!/usr/bin/env python

import math
n=4
dp = [0]
for i in range(1,n+1):
    t = int(math.sqrt(i))
    cur = float('inf')
    for j in range(1,t+1):
        cur = min(cur, dp[i-j*j]+1)
    dp.append(cur)
print(dp)