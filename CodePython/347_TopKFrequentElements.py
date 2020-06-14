#!/usr/bin/env python

import heapq

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = {}
    freq_list=[]  
    for num in nums:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
            
    for key in freq.keys():
        freq_list.append((-freq[key], key))
    heapq.heapify(freq_list)
    topk = []
    for i in range(0,k):
        topk.append(heapq.heappop(freq_list)[1])
    return topk

nums = [1,2,3,1,1,2,3,3,3]
print(topKFrequent(nums,2))