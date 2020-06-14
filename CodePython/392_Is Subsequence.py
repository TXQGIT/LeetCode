def isSubsequence(s, t):
    p_s = 0
    p_t = 0
    while p_s < len(s) and p_t < len(t):
        if s[p_s] == t[p_t]:
            p_s += 1
            p_t += 1
        else:
            p_t += 1
    if p_s == len(s):
        return True
    else:
        return False

s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))