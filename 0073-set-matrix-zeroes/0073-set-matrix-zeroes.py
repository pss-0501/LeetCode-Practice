class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Better Solution        
        n = len(matrix)
        m = len(matrix[0])

        row = [0] * n
        col = [0] * m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(n):
            for j in range(m):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j] = 0





        # Brute Force
        # n = len(matrix)
        # m = len(matrix[0])

        # def matRow(i):
        #     for j in range(m):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = float('inf')

        # def matCol(j):
        #     for i in range(n):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = float('inf')

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             matRow(i)
        #             matCol(j)

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == float('inf'):
        #             matrix[i][j] = 0