class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []

        row_min = set()
        for i in range(rows):
            row_min.add(min(matrix[i]))
        
        col_max = set()
        for i in range(cols):
            curr_max = matrix[0][i]
            for j in range(rows):
                curr_max = max(curr_max, matrix[j][i])
            col_max.add(curr_max)
        
        for i in row_min:
            if i in col_max:
                res.append(i)

        return res