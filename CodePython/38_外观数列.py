class Solution:

    seq = ['1']

    def parse(self, s):
        ans = ''
        pre = s[0]
        count = 1
        for i in range(1, len(s)):
            cur = s[i]
            if cur==pre:
                count += 1
            else:
                ans += str(count)
                ans += pre
                pre = cur
                count = 1
        ans += str(count)
        ans += pre
        return ans

    def countAndSay(self, n):
        cur_n = len(self.seq)
        if n<=cur_n:
            return self.seq[n-1]
        for i in range(cur_n-1, n-1 ):
            s = self.seq[i]
            self.seq.append(self.parse(s))
        return self.seq[-1]

so = Solution()
print(so.countAndSay(4))