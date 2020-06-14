def merge(intervals):
    # #方法1：时间复杂度O(n^2), 空间复杂度O(n)
    # def isIntersect(space1, space2):
    #     lowSpace = []
    #     highSpace = []
    #     if space1[0] <= space2[0]:
    #         lowSpace, highSpace = space1, space2
    #     else:
    #         lowSpace, highSpace = space2, space1
    #     if lowSpace[0] <= highSpace[0] <= lowSpace[1]:
    #         return True
    #     else:
    #         return False
    # ans = []
    # for cur in intervals:
    #     idx = 0
    #     while idx < len(ans):
    #         candidate = ans[idx]
    #         if isIntersect(candidate, cur):
    #             ans.pop(idx)
    #             cur = [min(candidate[0], cur[0]), max(candidate[1], cur[1])]
    #         else:
    #             idx += 1
    #     ans.append(cur)
    # return ans

    #方法2：先根据每个区间左边界进行排序
    intervals.sort(key=lambda x: x[0], reverse=False)
    merge = []
    for cur in intervals:
        if len(merge)==0 or cur[0]>merge[-1][1]:
            merge.append(cur)
        else:
            merge[-1][1] = max(cur[1], merge[-1][1])
    return merge


l = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(l))