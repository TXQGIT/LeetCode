def combinationSum(candidates, target):
    # #回溯法框架
    # result = []
    # def backtrack(路径, 选择列表):
    #     if 满足结束条件:
    #         result.add(路径)
    #         return
    #     for 选择 in 选择列表:
    #         做选择
    #         backtrack(路径, 选择列表)
    #         撤销选择
    def combReverse(candidates, target, begin, end, cur, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(cur[:])
            return
        for idx in range(begin, end):
            if idx>begin and candidates[idx-1]==candidates[idx]:
                continue
            cur.append(candidates[idx])
            combReverse(candidates, target - candidates[idx], idx + 1, end, cur, ans)
            cur.pop()

    cur = []
    ans = []
    # 有重复数字
    candidates.sort()
    combReverse(candidates, target, 0, len(candidates), cur, ans)
    return ans

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))