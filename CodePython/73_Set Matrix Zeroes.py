 
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    col0 = 1 #用于判断原始matrix第一列中是否有0出现
    for r in range(rows):
        if matrix[r][0]==0:
            col0 = 0
        for c in range(1,cols):
            if matrix[r][c]==0:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(rows-1,-1,-1): #必须从后往前
        for c in range(cols-1,0,-1):
            if matrix[r][0]==0 or matrix[0][c]==0:
                matrix[r][c]=0
        if col0==0:
            matrix[r][0]=0
    return matrix

if __name__=='__main__':
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(matrix)
    print(setZeroes(matrix))