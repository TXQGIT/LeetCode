def findRadius(houses, heaters):
    houses.sort()
    heaters.sort()
    ans_radius = 0
    for v in houses:  # 对每个house，查找与其最近的heater
        left = 0
        right = len(heaters) - 1
        while left < right:  # 二分查找，保证结束后的索引是大于等于v的第一个元素
            mid = (left + right) >> 1
            if heaters[mid] < v:
                left = mid + 1
            else:
                right = mid
        cur_radius = float('inf')
        if left > 0:
            cur_radius = min(heaters[left] - v, v - heaters[left-1])
        else:
            cur_radius = heaters[left] - v
        ans_radius = max(ans_radius, cur_radius)
    return ans_radius

houses = [1,2,3,4]
heaters = [1,4]
print(findRadius(houses,heaters))