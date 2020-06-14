class Solution:
    def findRightInterval(self, intervals):
        import bisect
        n = len(intervals)
        ans = []
        intervals_wiht_idx = []
        for i, v in enumerate(intervals):
            intervals_wiht_idx.append(v+[i])
        intervals_wiht_idx.sort(key=lambda x: x[0])
        start_list = [x[0] for x in intervals_wiht_idx]
        for i, v in enumerate(intervals):
            idx = bisect.bisect_left(start_list, v[1])
            if idx<n:
                ans.append(intervals_wiht_idx[idx][2])
            else:
                ans.append(-1)
        return ans

s = Solution()
# intervals = [[3,4],[2,3],[1,2]]
intervals = [ [1,4], [2,3], [3,4] ]
print(s.findRightInterval(intervals))