def guess(num):
    if num==pick:
        return 0
    return -1 if num<pick else  1

def guessNumber(n):
    right = n
    left = 1
    while left <= right:
        mid = left + (right - left) // 2
        if guess(mid) == 0:
            return mid
        if guess(mid) == 1:
            right = mid - 1
        else:
            left = mid + 1
    return -1

pick = 9
print(guessNumber(10))