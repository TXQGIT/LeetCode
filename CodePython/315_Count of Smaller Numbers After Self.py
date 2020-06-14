
def countSmaller(nums):

    def mergeSmaller(nums):
        if len(nums)<2:
            return (nums,[0])
        elif len(nums)==2:
            if nums[0]<=nums[1]:
                return (nums,[0,0])
            else:
                return (nums[::-1],[0,1])
        else:
            mid = int(len(nums)/2)
            part1,part1ans = mergeSmaller(nums[:mid])
            part2,part2ans = mergeSmaller(nums[mid:])
            data = []
            data_ans = []
            idx1 = idx2 = 0
            while idx1<len(part1) and idx2<len(part2):
                if part1[idx1]<=part2[idx2]:
                    data.append(part1[idx1])
                    data_ans.append(part1ans[idx1]+idx2)
                    idx1 += 1
                else:
                    data.append(part2[idx2])
                    data_ans.append(part2ans[idx2])
                    idx2 += 1
            if idx1<len(part1):
                for i in range(idx1,len(part1)):
                    data.append(part1[i])
                    data_ans.append(part1ans[i]+idx2)
            if idx2<len(part2):
                data += part2[idx2:]
                data_ans += part2ans[idx2:]
            return (data, data_ans)
                      
    sorted_data,sorted_data_ans = mergeSmaller(nums)
    tmp = []
    for i in range(len(nums)):
        tmp.append((nums[i],i))
    tmp.sort()
    ans = [0]*len(nums)
    for i in range(len(nums)):
        ans[tmp[i][1]] = sorted_data_ans[i]
    return ans



nums = [5,2,6,1]  
nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(countSmaller(nums))