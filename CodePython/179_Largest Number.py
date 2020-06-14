import functools

def cmp_str(x,y):
	a = x+y
	b = y+x
	if a>b:
		return 1
	elif a<b:
		return -1
	else:
		return 0

def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    #python3中取消了list.sort()中cmp参数，而改用key参数
    #同时通过functool.cmp_to_key()实现cmp的功能
    nums_str = [str(e) for e in nums]
    nums_str.sort(key=functools.cmp_to_key(cmp_str), reverse=True)
    ans = ''.join(nums_str)
    return str(int(ans))

if __name__ == '__main__':
	nums = [3,30,34,5,9]
	print(largestNumber(nums))

	nums = [1,20]
	print(largestNumber(nums))

	nums = [0,0]
	print(largestNumber(nums))