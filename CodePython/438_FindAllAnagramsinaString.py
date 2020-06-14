#!/usr/bin/env python

from collections import Counter

s = "dcbaebabacd"
p = "abc"

result = []

# left = right = 0
# count = len_p = len(p)

# hash_p = {}
# for e in p:
# 	hash_p[e] = hash_p.get(e,0)+1

# while right<len_p:
# 	if hash_p.get(s[right],0)>0:
# 		count -=1
# 		hash_p[s[right]] -=1
# 	right +=1
# 	if count==0:
# 		result.append(left)
# 	if right-left==len_p:
# 		if hash_p.get(s[left],-1)

p_counter = Counter(p)
s_counter = Counter(s[:len(p)-1])

for i in range(len(p)-1, len(s)):
	s_counter[s[i]] +=1
	if s_counter==p_counter:
		result.append(i-(len(p)-1))
	s_counter[s[i-(len(p)-1)]] -=1
	if s_counter[s[i-(len(p)-1)]]==0:
		del s_counter[s[i-(len(p)-1)]]

print(result)