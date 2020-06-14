class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = num[0]
        count = 1
        for i in range(1,len(nums)):
        	if count>0:
        		if nums[i]==major:
        			count+=1
    			else:
    				count-=1
			else:
				major = nums[i]
				count = 1
		return major

if __name__ == '__main__':
	a = Solution()
	nums = [1,2,3,2,4,2,2]
	major = a.majorityElement(nums)
	print(major)