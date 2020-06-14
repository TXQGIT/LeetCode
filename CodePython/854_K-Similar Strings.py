class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        def do_search(A, B, cur_cnt, cur_idx, cnt):
            if cur_idx==n-1:
                if cur_cnt<cnt[0]:
                    cnt[0] = cur_cnt
                return
            idx = cur_idx
            while idx<n:
                if A[idx]!=B[idx]:
                    for i in range(idx+1, n):
                        if B[i] == A[idx]:
                            B[idx], B[i] = B[i], B[idx]
                            do_search(A, B, cur_cnt+1, idx+1, cnt)
                            B[idx], B[i] = B[i], B[idx]
                    return
                else:
                    idx += 1
            if idx == n and cur_cnt < cnt[0]:
                cnt[0] = cur_cnt

        list_a = list(A)
        list_b = list(B)
        n = len(A)
        cnt = [float('inf')]
        do_search(list_a, list_b, 0, 0, cnt)
        return cnt[0]

s = Solution()
A = "bccaba"
B = "abacbc"
print(s.kSimilarity(A,B))