class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        def matRow(i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')

        def matCol(j):
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matRow(i)
                    matCol(j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0