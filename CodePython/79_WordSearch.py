def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    
    def hasPath(board, word, flag, rows, cols, r, c):           
        if len(word)==0:
            return True
        if not (0<=r<rows and 0<=c<cols):
            return False
        
        if flag[r][c]==False:
            if board[r][c]==word[0]:
                flag[r][c] = True
                left  = hasPath(board, word[1:], flag, rows, cols, r, c-1)
                right = hasPath(board, word[1:], flag, rows, cols, r, c+1)
                up    = hasPath(board, word[1:], flag, rows, cols, r-1, c)
                down  = hasPath(board, word[1:], flag, rows, cols, r+1, c)
                if left or right or up or down:
                    return True
                else:
                    flag[r][c]=False
        return False
                    
    rows = len(board)
    cols = len(board[0])
    # flag = [[False] * cols] * rows #这样定义会导致flag[0][0]=True出现整个flag的第一列都变为True.
    flag = [[False] * cols for i in range(rows)] # this is fine
    for r in range(rows):
            for c in range(cols):
                if hasPath(board, word, flag, rows, cols, r, c):
                    return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
# word = "aaaaaaaaaaaaa"
print(exist(board, word))