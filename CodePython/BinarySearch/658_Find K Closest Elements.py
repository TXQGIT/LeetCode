class Solution:
    def findClosestElements(self, arr, k, x):
        #二分查找x在arr中的位置，如果不存在，则返回如果插入x应该插入的位置
        #即查找idx,使得arr[i]<x, where 0<=i<idx; arr[i]>=x, where idx<=i
        #然后从idx开始往左右扩张，每次选x差值绝对值最小的元素加入集合
        #Part1-二次查找
        #step1:确定左右边界
        left, right = 0, len(arr)
        while left<right:
            mid = (left+right)>>1
            if arr[mid]<x:
                left = mid+1
            else:
                right = mid
        idx = left

        ans = []
        left, right = idx-1, idx
        while k:
            if left<0:
                ans.append(arr[right])
                right += 1
            if right>=len(arr):
                ans.append(arr[left])
                left -= 1
            if left>=0 and right<len(arr):
                if x-arr[left]<=arr[right]-x:
                    ans.append(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            k -= 1
        ans.sort()
        return ans

arr = [1]
k,x = 1,1
s=Solution()
print(s.findClosestElements(arr, k, x))