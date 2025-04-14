class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posSet = set()  # (r + c)
        negSet = set()  # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posSet or (r - c) in negSet:
                    continue

                col.add(c)
                posSet.add(r + c)
                negSet.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                posSet.remove(r + c)
                negSet.remove(r - c)
                board[r][c] = '.'

        backtrack(0)
        return res