def generateParenthesis(n):
    #方法1：递归生成所有可能的组合，对每个组合判断是不是有效的括号
    def generate(a=[]):
        if len(a)==2*n:
            if isvalid(a):
                ans.append("".join(a))
        else:
            a.append('(')
            generate(a)
            a.pop()
            a.append(')')
            generate(a)
            a.pop()
    def isvalid(string):
        cur_pos = 0
        for e in string:
            if e=='(':
                cur_pos += 1
            elif e==')':
                cur_pos -= 1
            if cur_pos<0:
                return False
        return cur_pos==0

    #方法2
    def backtrack(a='',left=0,right=0):
        if len(a)==2*n:
            ans.append(''.join(a))
        else:
            if left<n:
                backtrack(a+'(', left+1, right)
            if right<left:
                backtrack(a+')', left, right+1)

    ans = []
    # generate()
    backtrack()
    return ans

n=3
# print('%d pairs with %d Parenthesis' % (n, len(generateParenthesis(n))))
print('%d pairs with %d Parenthesis' % (n, len(generateParenthesis(n))))