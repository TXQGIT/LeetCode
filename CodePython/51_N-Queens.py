class Solution:
    def solveNQueens(self, n):
        import copy

        def is_vaild(board, r, c):
            # 检查列是否冲突
            for i in range(n):
                if board[r][i] == 'Q':
                    return False
            # 检查行是否冲突
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
            # 检查右上方
            for (i, j) in zip(range(r - 1, -1, -1), range(c + 1, n)):
                if board[i][j] == 'Q':
                    return False
            # 检查左上方
            for (i, j) in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            return True

        def DFS(board, r):
            if r >= n:
                tmp = []
                for i in range(n):
                    tmp.append(''.join(board[i]))
                ans.append(tmp)
                return
            for i in range(n):
                if is_vaild(board, r, i):
                    board[r][i] = 'Q'
                    DFS(board, r + 1)
                    board[r][i] = '.'

        board = [['.'] * n for _ in range(n)]
        ans = []
        DFS(board, 0)
        return ans

s = Solution()
print(s.solveNQueens(4))