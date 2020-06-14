#!/usr/bin/env python

import numpy as np

nums = [5,11,5,1]

n = len(nums)
sum_nums = sum(nums)
if sum_nums%2:
    print(False)
target = int(sum_nums/2)

m = np.zeros((n+1, target+1))
for i in range(1, n+1):
    for j in range(nums[i-1], target+1):
        if j-nums[i-1]>=0:
            m[i,j] = max(m[i-1,j], m[i-1, j-nums[i-1]]+nums[i-1])
        else:
            m[i,j] = m[i-1,j]
print(m)
print(int(m[n, target])==target)
                