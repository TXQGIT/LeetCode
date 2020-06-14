class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, r, c):
            if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or board[r][c] == 'X' or board[r][c] == '#':
                return
            board[r][c] = '#'
            dfs(board, r - 1, c)
            dfs(board, r + 1, c)
            dfs(board, r, c - 1)
            dfs(board, r, c + 1)

        if len(board) == 0:
            return;
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and board[i][j] == 'O':
                    dfs(board, i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
         ["O", "X", "O", "X", "O", "X"]]
solution = Solution()
solution.solve(board)
