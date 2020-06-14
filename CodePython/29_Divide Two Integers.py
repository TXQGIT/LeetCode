class Solution:
    def divide(self, dividend, divisor):
        # res = 0
        # sign = 1 if dividend ^ divisor >= 0 else -1
        # divd = abs(dividend)
        # dior = abs(divisor)
        # while divd >= dior:
        #     res += 1
        #     divd -= dior
        # res = res * sign
        # return min(max(-2 ** 31, res), 2 ** 31 - 1)

        sign = 1 if dividend^divisor>=0 else -1
        divd = abs(dividend)
        dior = abs(divisor)
        res = 0
        if dior<=divd:
            count = 1
            while dior<<1 <= divd:
                count = count<<1
                dior = dior<<1
            res = count+self.divide(divd-dior, divisor)
        if sign==-1:
            res = -res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


solution = Solution()
print(solution.divide(10, 3))