class Solution:
    def stringAdd(self, s1, s2):
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        l1, l2 = len(s1), len(s2)
        s1 = s1[::-1]
        s2 = s2[::-1]
        carry = 0
        res = []
        for i in range(l2):
            v1 = int(s1[i])
            v2 = int(s2[i])
            v = v1 + v2 + carry
            res.append(str(v % 10))
            carry = v // 10
        for i in range(l2, l1):
            v1 = int(s1[i])
            v = v1 + carry
            res.append(str(v % 10))
            carry = v // 10
        if carry:
            res.append(str(carry))
        res = ''.join(res)
        return res[::-1]

    def stringMultiChar(self, s, c):
        res = []
        c = int(c)
        s = s[::-1]
        carry = 0
        for i in range(len(s)):
            v = int(s[i])
            m = v * c + carry
            res.append(str(m % 10))
            carry = m // 10
        if carry:
            res.append(str(carry))
        res = ''.join(res)
        return res[::-1]

    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        num2 = num2[::-1]
        res = '0'
        for i in range(len(num2)):
            c = num2[i]
            m = self.stringMultiChar(num1, c) + '0' * i
            res = self.stringAdd(res, m)
        return res

s = Solution()
num1 = "1312"
num2 = "1"
print(s.multiply(num1, num2))
print(int(num1)*int(num2))