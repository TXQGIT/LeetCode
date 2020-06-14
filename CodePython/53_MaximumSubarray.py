#!/usr/bin /env python

nums = [1,2,-1,-2,2,1,-2,1,4,-5,4]
max_ending_here = []
for i in list(range(len(nums))):
    if i==0:
        max_ending_here.append(nums[0])
        continue
    max_ending_here.append(max(0, max_ending_here[-1])+nums[i])
print(max_ending_here)