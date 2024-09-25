class Solution:
    def getMaxElement(self, matrix, mid):
        index = -1
        maxi = float('-inf')

        for row in range(len(matrix)):
            elm = matrix[row][mid]

            if elm > maxi:
                maxi = max(maxi, elm)
                index = row

        return index

    def findPeakGrid(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        start = 0
        end = m - 1

        while start <= end:
            mid = start + (end - start) // 2

            # find maximum because we have to check top, bottom, left, right
            # if we use maximum, then our element is definitely greater than top and bottom
            # so we need to check only left and right, i.e., our problem is reduced to finding a peak in 1D

            row = self.getMaxElement(matrix, mid)
            left = -1
            right = -1

            # handling edge cases
            if mid - 1 >= 0:
                left = matrix[row][mid - 1]

            if mid + 1 < m:
                right = matrix[row][mid + 1]

            # we find the peak element
            if matrix[row][mid] > left and matrix[row][mid] > right:
                return [row, mid]

            # our peak is on the left side of mid, so eliminate the right part
            elif matrix[row][mid] > right:
                end = mid - 1

            # our peak is on the right side of mid, so eliminate the left part
            else:
                start = mid + 1

        return [-1, -1]