#!/usr/bin/env python

def countAndSay(n):
        pre = '1'
        ans = pre
        for i in range(1,n):
            idx = 1
            count = 1
            cur = [str(count), pre[0]]
            for idx in range(1,len(pre)):
                if pre[idx]==pre[idx-1]:
                    count += 1
                    cur[-2] = str(count)
                else:
                    count = 1
                    cur.append(str(count))
                    cur.append(pre[idx])
            pre = cur
            ans = cur
        return ''.join(ans)

if __name__=='__main__':
	print(countAndSay(7))	
