class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Optimise
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()





        # Brute Force - Not Acceptable

        # n = len(matrix)
        # m = len(matrix[0])

        # ans = [[0] * n for _ in range(m)]
        # for i in range(n):
        #     for j in range(m):
        #         ans[j][n - 1 - i] = matrix[i][j]

        # return ans