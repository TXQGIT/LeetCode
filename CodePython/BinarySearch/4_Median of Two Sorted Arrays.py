class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        def getKth(nums1, s1, e1, nums2, s2, e2, k):
            len1 = e1 - s1 + 1
            len2 = e2 - s2 + 1
            if len1 > len2:  # 确保nums1的长度小于nums2
                tmp = getKth(nums2, s2, e2, nums1, s1, e1, k)
                return tmp
            if len1 == 0:  # 当更短的nums1,长度为0时，直接从nums2中取数
                tmp =  nums2[s2 + k - 1]
                return tmp
            if k == 1:  # 当k为1时，取两数组起始的小值
                tmp = min(nums1[s1], nums2[s2])
                return tmp
            idx_1 = s1 + min(len1, k // 2) - 1  # 每次只取k的一半
            idx_2 = s2 + min(len2, k // 2) - 1  #
            if nums1[idx_1] > nums2[idx_2]:
                tmp = getKth(nums1, s1, e1, nums2, idx_2 + 1, e2, k - (idx_2 - s2 + 1))
                return tmp
            else:
                tmp = getKth(nums1, idx_1 + 1, e1, nums2, s2, e2, k - (idx_1 - s1 + 1))
                return tmp

        len1 = len(nums1)
        len2 = len(nums2)
        left = (len1 + len2 + 1) // 2
        right = (len1 + len2 + 2) // 2
        return (getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, left) +
                getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, right)) / 2

solution = Solution()
nums1 = [1,3]
nums2 = [2,4]
print(solution.findMedianSortedArrays(nums1, nums2))