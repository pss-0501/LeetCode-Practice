class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #  Brute Force
        # found = False
        # row = len(matrix)
        # col = len(matrix[0])
        # for i in range(row):
        #     for j in range(col):
        #         if matrix[i][j] == target:
        #             found = True
        #             break
        # return found

        # Better
        def BS(arr, k):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    return True
                elif arr[mid] < k:
                    low = mid + 1
                else:
                    high = mid - 1
            return False


        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] <= target and target <= matrix[i][col - 1]:
                return BS(matrix[i], target)
        return False