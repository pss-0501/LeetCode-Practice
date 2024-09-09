class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Optimise
        col0 = 1
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    # check for col & row:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0







        # Better Solution        
        # n = len(matrix)
        # m = len(matrix[0])

        # row = [0] * n
        # col = [0] * m

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             row[i] = 1
        #             col[j] = 1

        # for i in range(n):
        #     for j in range(m):
        #         if row[i] == 1 or col[j] == 1:
        #             matrix[i][j] = 0


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