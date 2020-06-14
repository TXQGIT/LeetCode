from collections import Counter

def isAnagram(s, t):
	if len(s)!=len(t):
		return False
	dic = Counter(s)
	for e in t:
	    dic[e] = dic.get(e,0)-1
	    if dic[e]<0:
	        return False
	return True

print(isAnagram('ab','a'))

for i in range(20):
	print(i)
	i += 1
